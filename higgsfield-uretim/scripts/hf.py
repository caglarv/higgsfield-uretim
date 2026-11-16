#!/usr/bin/env python3
"""Higgsfield API yardımcı aracı (yalnız standart kütüphane).

Kullanım:
  hf.py yukle  <dosya>                          -> herkese açık URL'yi yazar (dosya dışarı gider)
  hf.py gonder <model-yolu> <govde.json> <cikti-klasoru> [--ad ONEK]   -> ÜCRETLİ
  hf.py devam  <cikti-klasoru> [--ad ONEK]      -> kayıtlı istekten sürdürür (yeni ücret yok)
  hf.py bagla  <cikti-klasoru> <istek-no> [--ad ONEK] -> panelde görülen istek numarasını kayda yazar,
                                                   yalnız sorgular ve indirir (ASLA yeniden göndermez)
  hf.py kareler <video.mp4> <klasor>            -> kontrol için kare ızgaraları (ffmpeg gerekir)
  hf.py sema    <model-yolu>                    -> modelin resmi alanları, seçenekleri, fiyatı (ücretsiz)
  hf.py kontrol <model-yolu> <govde.json>       -> gövdeyi resmi şemayla denetler (ücretsiz)
                                                   `gonder` bu kontrolü kendiliğinden yapar; hata varsa göndermez.

Kimlik: --env <dosya> verilirse o dosya; yoksa HF_API_BASE_URL ve HF_CREDENTIALS ortam
değişkenleri; o da yoksa çalışma klasöründen yukarı doğru studio/.env.local ya da .env.local.
Anahtar hiçbir zaman ekrana ya da dosyaya yazılmaz.

Çift ücret koruması: `gonder`, POST'tan ÖNCE <ONEK>_istek.json dosyasına "bekliyor" kaydı ve
tekrar-gönderim anahtarını (Idempotency-Key) yazar. Bağlantı koparsa kayıt yerinde kalır:
aynı --ad ile yeni `gonder` reddedilir; `devam` aynı anahtarla güvenli biçimde sürdürür.
"""
import argparse
import json
import mimetypes
import os
import pathlib
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
import uuid

BITTI = ("completed", "failed", "nsfw", "canceled")
AG_HATASI = -1


def env_oku(p, hedef):
    for satir in pathlib.Path(p).read_text().splitlines():
        if "=" in satir and not satir.strip().startswith("#"):
            k, v = satir.split("=", 1)
            hedef[k.strip()] = v.strip().strip("'\"")


def kimlik(env_yolu):
    env = {}
    if env_yolu:
        env_oku(env_yolu, env)
    else:
        for k in ("HF_API_BASE_URL", "HF_CREDENTIALS"):
            if os.environ.get(k):
                env[k] = os.environ[k]
        if not (env.get("HF_API_BASE_URL") and env.get("HF_CREDENTIALS")):
            d = pathlib.Path.cwd()
            for kok in [d, *d.parents]:
                for p in (kok / "studio/.env.local", kok / ".env.local"):
                    if p.is_file():
                        bulunan = {}
                        env_oku(p, bulunan)
                        for k in ("HF_API_BASE_URL", "HF_CREDENTIALS"):
                            if bulunan.get(k):
                                env.setdefault(k, bulunan[k])
                if env.get("HF_API_BASE_URL") and env.get("HF_CREDENTIALS"):
                    break
    taban = env.get("HF_API_BASE_URL", "").rstrip("/")
    ham = env.get("HF_CREDENTIALS", "")
    if not taban or not ham:
        sys.exit("HATA: HF_API_BASE_URL / HF_CREDENTIALS bulunamadı (ortam değişkeni ya da --env).")
    anahtar = (json.loads(ham)["apiKey"] if ham.startswith("{") else ham).strip()
    return taban, anahtar


def adres_gizle(metin):
    return re.sub(r"https?://\S+", "<adres>", str(metin))[:800]


def cagir(taban, anahtar, yontem, yol, veri=None, ek=None):
    """(durum, yanıt) döner. Ağ hatası / zaman aşımında durum = AG_HATASI."""
    bas = {"Authorization": f"Key {anahtar}"}
    if veri is not None:
        bas["Content-Type"] = "application/json"
    bas.update(ek or {})
    istek = urllib.request.Request(
        taban + yol, method=yontem, headers=bas,
        data=json.dumps(veri).encode() if veri is not None else None)
    try:
        with urllib.request.urlopen(istek, timeout=90) as r:
            return r.status, json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode(errors="replace")
    except Exception as e:  # zaman aşımı, bağlantı kopması, bozuk yanıt
        return AG_HATASI, f"{type(e).__name__}: {e}"


def yukle(taban, anahtar, dosya):
    p = pathlib.Path(dosya)
    tur = mimetypes.guess_type(p.name)[0] or "application/octet-stream"
    if tur == "image/jpg":
        tur = "image/jpeg"
    durum, bilet = cagir(taban, anahtar, "POST", "/files/generate-upload-url", {"content_type": tur})
    if durum != 200 or not isinstance(bilet, dict):
        sys.exit(f"HATA: yükleme bileti alınamadı ({durum}): {adres_gizle(bilet)}")
    # İmzalı adrese API anahtarı GÖNDERİLMEZ; yalnız biletin verdiği başlıklar.
    istek = urllib.request.Request(bilet["upload_url"], method="PUT",
                                   headers=bilet["upload_headers"], data=p.read_bytes())
    with urllib.request.urlopen(istek, timeout=300) as r:
        if r.status >= 300:
            sys.exit(f"HATA: yükleme başarısız ({r.status})")
    return bilet["public_url"]


def indir(url, hedef):
    with urllib.request.urlopen(url, timeout=300) as r:
        hedef.write_bytes(r.read())
    print("indirildi", hedef.name, hedef.stat().st_size, "bayt")


SEMA_ADRES = "https://dash.higgsfield.ai/models/{}/llms.txt"
# Varsayılanı açıkken modelin prompt'umuzu kendi kafasına göre yeniden yazdığı ayarlar.
YENIDEN_YAZAN = ("enhance_prompt", "prompt_optimizer", "prompt_extend", "enable_thinking")


def sema_metni(model, dosya=None):
    """Modelin resmi kullanım kâğıdını (Copy agent prompt metni) döner; ücretsiz, anahtarsız."""
    if dosya:
        return pathlib.Path(dosya).read_text(encoding="utf-8")
    istek = urllib.request.Request(SEMA_ADRES.format(model.strip("/")),
                                   headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(istek, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def sema_coz(metin):
    m = re.search(r"### Input JSON Schema\s*```json\s*(\{.*?\})\s*```", metin, re.S)
    if not m:
        raise ValueError("kâğıtta 'Input JSON Schema' bulunamadı")
    s = json.loads(m.group(1))
    fiyat = re.search(r"## Pricing\s*\n+(.*?)\n\n", metin, re.S)
    return s, (fiyat.group(1).replace("\n", " ") if fiyat else "")


TURLER = {"string": str, "boolean": bool, "integer": int, "number": (int, float),
          "array": list, "object": dict}


def denetle(model, govde, sema):
    """(hatalar, uyarılar) döner. Hata = sunucu reddeder ya da yanlış iş olur; gönderme."""
    hatalar, uyarilar = [], []
    alanlar = sema.get("properties", {})
    for z in sema.get("required", []):
        if z not in govde:
            hatalar.append(f"zorunlu alan eksik: {z}")
    for k, v in govde.items():
        t = alanlar.get(k)
        if t is None:
            if sema.get("additionalProperties") is False:
                hatalar.append(f"modelde böyle bir alan yok: {k} (geçerliler: {', '.join(alanlar)})")
            continue
        beklenen = TURLER.get(t.get("type"))
        if beklenen and (not isinstance(v, beklenen) or (t.get("type") in ("integer", "number") and isinstance(v, bool))):
            hatalar.append(f"{k}: tür {t.get('type')} olmalı, gelen {type(v).__name__}")
            continue
        if "enum" in t and v not in t["enum"]:
            hatalar.append(f"{k}: '{v}' geçersiz; seçenekler {t['enum']}")
        if isinstance(v, (int, float)) and not isinstance(v, bool):
            if "minimum" in t and v < t["minimum"]:
                hatalar.append(f"{k}: {v} < en az {t['minimum']}")
            if "maximum" in t and v > t["maximum"]:
                hatalar.append(f"{k}: {v} > en çok {t['maximum']}")
        if isinstance(v, str) and t.get("minLength") and len(v) < t["minLength"]:
            hatalar.append(f"{k}: boş olamaz")
        if isinstance(v, list) and t.get("maxItems") and len(v) > t["maxItems"]:
            hatalar.append(f"{k}: en çok {t['maxItems']} öğe")
    for k in YENIDEN_YAZAN:
        if k in alanlar:
            acik = govde.get(k, alanlar[k].get("default"))
            if acik is True:
                uyarilar.append(f"{k} AÇIK: model prompt'u kendi kafasına göre yeniden yazar; "
                                f"kendi prompt'unu koruyacaksan {k}: false ver")
    if "quality" in alanlar and "quality" not in govde:
        uyarilar.append(f"quality verilmedi; varsayılan '{alanlar['quality'].get('default')}' kullanılır "
                        "(fiyatı etkiler — açıkça yaz)")
    for k, t in alanlar.items():
        if k not in govde and "default" in t and k in ("resolution", "duration", "generate_audio", "sound"):
            uyarilar.append(f"{k} verilmedi; varsayılan {t['default']!r} kullanılır (fiyatı etkileyebilir)")
    return hatalar, uyarilar


def kontrol_et(model, govde, sema_dosya=None, sessiz=False):
    """Şemayı indirip gövdeyi denetler. Hata varsa False döner."""
    try:
        sema, fiyat = sema_coz(sema_metni(model, sema_dosya))
    except Exception as e:
        print(f"ŞEMA OKUNAMADI ({type(e).__name__}: {e}). Gövde doğrulanamadı.")
        return None
    hatalar, uyarilar = denetle(model, govde, sema)
    if not sessiz and fiyat:
        print("fiyat (kâğıttan):", fiyat[:300])
    for u in uyarilar:
        print("UYARI:", u)
    for h in hatalar:
        print("HATA:", h)
    print("kontrol:", "GEÇTİ" if not hatalar else f"{len(hatalar)} HATA — gönderilmez")
    return not hatalar


def sema_goster(model, sema_dosya=None):
    sema, fiyat = sema_coz(sema_metni(model, sema_dosya))
    zorunlu = set(sema.get("required", []))
    print(f"model: {model}")
    print("fiyat:", fiyat or "kâğıtta yok — fiyat sayfasından oku")
    for k, t in sema.get("properties", {}).items():
        ek = []
        if "enum" in t: ek.append("seçenek " + "/".join(map(str, t["enum"])))
        if "default" in t: ek.append(f"varsayılan {t['default']!r}")
        if "minimum" in t or "maximum" in t: ek.append(f"aralık {t.get('minimum', '')}–{t.get('maximum', '')}")
        print(f"  {'*' if k in zorunlu else ' '} {k} ({t.get('type', '?')}) {'; '.join(ek)}")
    print("(* = zorunlu; listede olmayan alan gönderilirse sunucu reddeder)"
          if sema.get("additionalProperties") is False else "(* = zorunlu)")


def uzanti(url, varsayilan):
    u = pathlib.PurePosixPath(url.split("?", 1)[0]).suffix.lower()
    return u if u in (".png", ".jpg", ".jpeg", ".webp", ".gif", ".mp4", ".mov", ".webm") else varsayilan


def bekle_indir(taban, anahtar, rid, klasor, onek, azami_sn=1500):
    klasor = pathlib.Path(klasor)
    basla = time.time()
    son = None
    ag_hata = 0
    while True:
        durum, s = cagir(taban, anahtar, "GET", f"/requests/{rid}/status")
        if durum == AG_HATASI:
            ag_hata += 1
            if ag_hata >= 6:
                print("Ağ hatası sürüyor; iş arka planda devam ediyor olabilir. "
                      "Sonra `devam` ile yeniden sorgula (yeni ücret yok).")
                return 2
            time.sleep(10)
            continue
        if 400 <= durum < 500:
            print(f"SORGU REDDEDİLDİ (HTTP {durum}): {adres_gizle(s)}")
            return 1
        hal = s.get("status") if isinstance(s, dict) else f"HTTP {durum}"
        if hal != son:
            print(f"[{int(time.time() - basla)} sn] {hal}", flush=True)
            son = hal
        if hal in BITTI:
            break
        if time.time() - basla > azami_sn:
            print("Süre doldu; iş sürüyor olabilir. `devam` ile yeniden sorgula (yeni ücret yok).")
            return 2
        time.sleep(5)
    (klasor / f"{onek}_sonuc.json").write_text(json.dumps(s, indent=2, ensure_ascii=False))
    if hal != "completed":
        print(f"İŞ TAMAMLANMADI: {hal}. Ayrıntı: {onek}_sonuc.json")
        return 1
    n = 0
    for i, g in enumerate(s.get("images") or [], 1):
        if isinstance(g, dict) and g.get("url"):
            indir(g["url"], klasor / f"{onek}_{i}{uzanti(g['url'], '.png')}")
            n += 1
    v = s.get("video")
    if isinstance(v, dict) and v.get("url"):
        indir(v["url"], klasor / f"{onek}{uzanti(v['url'], '.mp4')}")
        n += 1
    if n == 0:
        print(f"UYARI: yanıtta indirilecek dosya bulunamadı; {onek}_sonuc.json dosyasına bak.")
    return 0


def kareler(video, klasor):
    k = pathlib.Path(klasor)
    k.mkdir(parents=True, exist_ok=True)
    olc = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries",
         "format=duration:stream=width,height,r_frame_rate,codec_type", "-of", "compact", video],
        capture_output=True, text=True)
    print(olc.stdout.strip() or olc.stderr.strip())
    ham = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", video], capture_output=True, text=True).stdout.strip()
    try:
        sure = float(ham)
    except ValueError:
        sys.exit("HATA: video süresi okunamadı.")
    # Saniyede 2 kare; her ızgara 16 kare = 8 saniye. Videonun TAMAMI kapsanır:
    # zamanlama hatası ortada olur, ilk/son kare yetmez.
    parca = 8.0
    adet = max(1, int(-(-sure // parca)))
    for i in range(adet):
        bas = i * parca
        uz = min(parca, sure - bas)
        kare = max(1, round(uz * 2))
        satir = -(-kare // 4)
        hedef = k / (f"izgara_{i + 1}.png" if adet > 1 else "izgara.png")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{bas:.3f}", "-t", f"{uz:.3f}",
                        "-i", video, "-vf", f"fps=2,scale=480:-1,tile=4x{satir}",
                        "-frames:v", "1", str(hedef)], check=True)
        print(f"{hedef.name}: {bas:.1f}–{bas + uz:.1f}. saniyeler, {kare} kare "
              f"(soldan sağa, yukarıdan aşağı; kareler arası 0,5 sn)")
    kes = subprocess.run(["ffmpeg", "-v", "error", "-i", video, "-vf",
                          "select='gt(scene,0.3)',showinfo", "-f", "null", "-"],
                         capture_output=True, text=True)
    print("olası kesme sayısı:", kes.stderr.count("pts_time"))
    print(f"toplam {adet} ızgara, video süresi {sure:.2f} sn; klasör: {k}")
    print("Kritik anı tam boy görmek için: "
          f"ffmpeg -ss <saniye> -i {video} -frames:v 1 {k}/an.png")


def gonder(taban, anahtar, arg):
    klasor = pathlib.Path(arg.klasor)
    klasor.mkdir(parents=True, exist_ok=True)
    kayit = klasor / f"{arg.ad}_istek.json"
    if kayit.exists():
        sys.exit(f"DUR: {kayit.name} zaten var. Aynı işi ikinci kez ücretlendirmemek için "
                 f"`devam` kullan; gerçekten YENİ bir üretimse yeni bir --ad ver (v2 gibi).")
    govde = json.loads(pathlib.Path(arg.govde).read_text())
    sonuc = kontrol_et(arg.model, govde, sessiz=True)
    if sonuc is False:
        sys.exit("DUR: gövde resmi şemaya uymuyor; hiçbir şey gönderilmedi, ücret yok.")
    if sonuc is None and not arg.semasiz:
        sys.exit("DUR: şema okunamadı. Ağ sorunu olabilir; tekrar dene. "
                 "Gövdeden eminsen bilerek geçmek için --semasiz ekle.")
    # Medya adresleri kalıcı kayda yazılmaz (kişisel fotoğraf adresi sızmasın);
    # tam gövde yalnız yarım kalan gönderimi sürdürmek için ayrı dosyada tutulur ve iş alınınca silinir.
    temiz = {k: v for k, v in govde.items() if not k.endswith(("_url", "_urls"))}
    anahtar_tekrar = str(uuid.uuid4())
    bekleyen = klasor / f"{arg.ad}_bekleyen_govde.json"
    bekleyen.write_text(json.dumps(govde, ensure_ascii=False))
    kayit.write_text(json.dumps({"durum": "bekliyor", "request_id": None, "model": arg.model,
                                 "idempotency_key": anahtar_tekrar, "govde": temiz},
                                indent=2, ensure_ascii=False))
    return post_ve_bekle(taban, anahtar, klasor, arg.ad)


def post_ve_bekle(taban, anahtar, klasor, onek):
    kayit = klasor / f"{onek}_istek.json"
    bekleyen = klasor / f"{onek}_bekleyen_govde.json"
    k = json.loads(kayit.read_text())
    govde = json.loads(bekleyen.read_text())
    durum, yanit = cagir(taban, anahtar, "POST", "/" + k["model"].strip("/"), govde,
                         {"Idempotency-Key": k["idempotency_key"]})
    if durum == AG_HATASI:
        print("BAĞLANTI KOPTU — isteğin sunucuya ulaşıp ulaşmadığı BELLİ DEĞİL.")
        print("Yeni `gonder` YAPMA. Önce paneldeki Requests sayfasına bak:")
        print(f"  - iş orada GÖRÜNÜYORSA: `bagla {klasor} <panel-istek-no> --ad {onek}` (yalnız indirir, yeniden göndermez)")
        print(f"  - iş orada YOKSA: `devam {klasor} --ad {onek}` (aynı tekrar-gönderim anahtarıyla yeniden dener)")
        return 3
    if durum >= 300 or not isinstance(yanit, dict) or "request_id" not in yanit:
        # Sunucu isteği reddetti: iş başlamadı, kayıt temizlenir ki düzeltilmiş gövdeyle yeniden gönderilebilsin.
        kayit.unlink(missing_ok=True)
        bekleyen.unlink(missing_ok=True)
        sys.exit(f"HATA: gönderim reddedildi ({durum}): {adres_gizle(yanit)}")
    k["durum"] = "gonderildi"
    k["request_id"] = yanit["request_id"]
    kayit.write_text(json.dumps(k, indent=2, ensure_ascii=False))
    bekleyen.unlink(missing_ok=True)
    print("istek:", yanit["request_id"])
    return bekle_indir(taban, anahtar, yanit["request_id"], klasor, onek)


def main():
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    a.add_argument("--env")
    alt = a.add_subparsers(dest="komut", required=True)
    y = alt.add_parser("yukle"); y.add_argument("dosya")
    g = alt.add_parser("gonder"); g.add_argument("model"); g.add_argument("govde"); g.add_argument("klasor")
    g.add_argument("--ad", default="cikti")
    g.add_argument("--semasiz", action="store_true", help="şema okunamazsa bile gönder (önerilmez)")
    s = alt.add_parser("sema"); s.add_argument("model"); s.add_argument("--dosya")
    kt = alt.add_parser("kontrol"); kt.add_argument("model"); kt.add_argument("govde"); kt.add_argument("--dosya")
    d = alt.add_parser("devam"); d.add_argument("klasor"); d.add_argument("--ad", default="cikti")
    b = alt.add_parser("bagla"); b.add_argument("klasor"); b.add_argument("istek"); b.add_argument("--ad", default="cikti")
    k = alt.add_parser("kareler"); k.add_argument("video"); k.add_argument("klasor")
    arg = a.parse_args()

    if arg.komut == "kareler":
        return kareler(arg.video, arg.klasor)
    if arg.komut == "sema":
        return sema_goster(arg.model, arg.dosya)
    if arg.komut == "kontrol":
        sonuc = kontrol_et(arg.model, json.loads(pathlib.Path(arg.govde).read_text()), arg.dosya)
        return 0 if sonuc else 2

    taban, anahtar = kimlik(arg.env)
    if arg.komut == "yukle":
        print(yukle(taban, anahtar, arg.dosya))
        return 0
    if arg.komut == "gonder":
        return gonder(taban, anahtar, arg)

    klasor = pathlib.Path(arg.klasor)
    kayit = klasor / f"{arg.ad}_istek.json"
    if arg.komut == "bagla":
        # Bağlantı koptuktan sonra iş panelde görünüyorsa: numarayı kayda yaz, yarım gövdeyi sil,
        # yalnız sorgula. Böylece `devam` bir daha yeniden gönderemez.
        klasor.mkdir(parents=True, exist_ok=True)
        k = json.loads(kayit.read_text()) if kayit.is_file() else {"model": None, "govde": {}}
        if k.get("request_id") and k["request_id"] != arg.istek:
            sys.exit(f"DUR: kayıtta başka bir istek numarası var ({k['request_id']}). Yeni --ad kullan.")
        k["durum"] = "gonderildi"
        k["request_id"] = arg.istek
        k["not"] = "numara panelden elle bağlandı"
        kayit.write_text(json.dumps(k, indent=2, ensure_ascii=False))
        (klasor / f"{arg.ad}_bekleyen_govde.json").unlink(missing_ok=True)
        print("istek numarası kayda yazıldı; yalnız sorgulanıyor:", arg.istek)
        return bekle_indir(taban, anahtar, arg.istek, klasor, arg.ad)
    if not kayit.is_file():
        sys.exit(f"HATA: {kayit} yok; sürdürülecek istek bulunamadı.")
    k = json.loads(kayit.read_text())
    if k.get("request_id"):
        return bekle_indir(taban, anahtar, k["request_id"], klasor, arg.ad)
    if (klasor / f"{arg.ad}_bekleyen_govde.json").is_file() and k.get("idempotency_key"):
        print("Yarım kalmış gönderim bulundu; AYNI tekrar-gönderim anahtarıyla sürdürülüyor.")
        return post_ve_bekle(taban, anahtar, klasor, arg.ad)
    sys.exit("HATA: kayıtta istek numarası yok ve sürdürülecek gövde bulunamadı. "
             "Paneldeki Requests sayfasına bak.")


if __name__ == "__main__":
    sys.exit(main() or 0)
