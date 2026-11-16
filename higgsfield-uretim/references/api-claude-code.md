# API ile üretim (yalnız komut çalıştırabilen ortamda — ör. Claude Code)

Bu dosya yalnız şu ikisi de doğruysa geçerlidir: (1) komut çalıştırabiliyorsun, (2) Higgsfield API anahtarı tanımlı.
Biri eksikse bu dosyayı bırak; kullanıcıya prompt + ayar paketini ver, üretimi o sitede yapsın.

## İçindekiler
1. Güvenlik ve para kuralları
2. Akış (adım adım)
3. Yardımcı araç: `scripts/hf.py`
4. Denenmiş istek gövdeleri
5. Kayıt düzeni
6. Bilinen tuzaklar

## 1. Güvenlik ve para kuralları
- **Onaysız `gonder` yok.** Her ücretli çağrıdan önce kullanıcıya tek satır: model + ayar + ≈ maliyet; "evet" gelmeden gönderme. Düzeltme turu da ayrı onay ister — beğenilmeyen ama tamamlanan iş de ücretlidir.
- **Fiyatı tahmin etme, oku.** (Sayfayı açamıyorsan `modeller-ve-maliyet.md` içindeki tarihli rakamı kullan ve "bugün doğrulanmadı" de.) Liste sayfasındaki "from" fiyatı yalnız en ucuz ayarın fiyatıdır. Seçtiğin mod + çözünürlük + kalite + süre için modelin kendi sayfasındaki ("Price" bölümü) rakamı kullan. Okuyamadıysan "≈ tahmin, doğrulanmadı" de ve kullanıcıyı uyar. (Gerçek vaka: düzenleme için liste fiyatından ≈ $0.02 dendi, kesilen net tutar $0.13 oldu.)
- **Anahtarı gösterme.** Anahtarı ekrana, sohbete, kayıt dosyasına yazma; `.env` dosyasını `cat` ile dökme. `hf.py` anahtarı kendisi okur.
- **İstek numarası para demektir.** Gönderim döner dönmez numara diske yazılır; bağlantı koparsa aynı numaradan `devam` et. Zaman aşımında yeni `gonder` yapmadan önce kayıt dosyasına ve konsoldaki Requests sayfasına bak — aksi hâlde aynı iş iki kez ücretlenir.
- **Gerçek ücreti sonradan doğrula.** API yanıtında ücret alanı yok. İş bitince kullanıcıdan panelin işlem geçmişine bakmasını iste; farkı kayda yaz.

## 2. Akış
1. Prompt'u ve ayarları bir kayıt klasörüne yaz (aşağıda §5).
2. Referans görsel/video varsa yükle: `hf.py yukle <dosya>` → dönen adresi gövdeye koy.
3. Gövdeyi (`govde.json`) hazırla; alan adlarını modelin API sayfasından ya da §4'ten al. Bilmediğin alanı uydurma — yanlış alan sessizce yok sayılıp pahalı varsayılanla çalışabilir.
4. Kullanıcı onayı (model + ayar + ≈ maliyet).
5. `hf.py gonder <model-yolu> govde.json <klasör> --ad v1` → bekler, sonucu indirir.
6. Çıktıya KENDİN bak: görseli aç; videoda `hf.py kareler` ile ızgara çıkar ve ızgaraya bak. Videoyu izleyemediğini, karelere baktığını kullanıcıya söyle.
7. Değerlendirmeyi yaz, dosyayı kullanıcıya göster, gerçek ücreti sor.

## 3. Yardımcı araç: `scripts/hf.py`
Yalnız Python standart kütüphanesi; `kareler` için ffmpeg gerekir.
- `hf.py yukle <dosya>` — imzalı yükleme; herkese açık adresi yazar. Ücret kesilmez ama dosya dışarı gider ve adresi bilen herkes görebilir: kişisel fotoğrafı ancak kullanıcı o üretimi onayladıktan sonra yükle. Adres kayda yazılmaz; her yeni gönderimde (v2 dahil) referansı yeniden yükle.
- `hf.py gonder <model-yolu> <govde.json> <klasör> --ad v1` — **ücretli.** POST'tan önce "bekliyor" kaydı ve tekrar-gönderim anahtarı yazılır; aynı `--ad` ile ikinci `gonder` reddedilir. Bağlantı koparsa "BAĞLANTI KOPTU" der: yeni `gonder` yapma, panelin Requests sayfasına bak, sonra `devam` çalıştır.
- `hf.py devam <klasör> --ad v1` — kayıtlı istekten sürdürür, sonucu indirir. İstek numarası kayıtlıysa yalnız sorgular (ücretsiz). Gönderim yarım kaldıysa aynı tekrar-gönderim anahtarıyla yeniden gönderir; sunucunun bu anahtarla çift ücreti gerçekten engellediği DOĞRULANMADI — bu yüzden önce Requests sayfasına bak.
- `hf.py bagla <klasör> <istek-no> --ad v1` — bağlantı koptuktan sonra iş panelin Requests sayfasında GÖRÜNÜYORSA: o numarayı kayda yazar, yalnız sorgular ve indirir; asla yeniden göndermez. İş panelde yoksa `devam` kullanılır.
- `hf.py kareler <video.mp4> <klasör>` — süre/çözünürlük, olası kesme sayısı ve videonun TAMAMINI kapsayan ızgaralar (saniyede 2 kare, ızgara başına 8 saniye; uzun videoda birden çok dosya — hepsine bak). Kritik anı tam boy görmek için verdiği ffmpeg satırını kullan.
- Kimlik: `HF_API_BASE_URL` + `HF_CREDENTIALS` ortam değişkeni ya da `--env <dosya>`; yoksa yukarı doğru `studio/.env.local` / `.env.local` aranır. Yetki başlığı `Authorization: Key <anahtar>` biçimindedir.
- Durum (2026-11-16): `kareler`, `devam` ve kopuk bağlantı koruması (sahte adresle benzetim) denendi. `yukle` ve gerçek `gonder` aynı mantığın elle yazılmış hâliyle çalıştı; bu araçla gerçek ücretli gönderim henüz DENENMEDİ — ilk kullanımda çıktıyı dikkatle izle.

## 4. Denenmiş istek gövdeleri (2026-11-16)
Metinden görsel — Soul 2, yol `higgsfield-ai/soul/v2/standard`:
```json
{"prompt": "...", "batch_size": 4, "resolution": "720p", "aspect_ratio": "16:9", "enhance_prompt": false}
```
`enhance_prompt` kapalı tutulur; açıkken model yazdığın prompt'u kendi kafasına göre değiştirir. `batch_size` 1 ya da 4. 4 görsel ≈ 16 sn sürdü, panelde $0.01 göründü.

Görsel düzenleme — Marketing Studio Image, yol `marketing-studio/image`:
```json
{"prompt": "Edit the input image... Change NOTHING else: ...", "image_urls": ["<yüklenen adres>"], "resolution": "1k", "aspect_ratio": "16:9", "enhance_prompt": false}
```
≈ 50 sn. Kesilen net $0.13 (liste fiyatından beklenen ≈ $0.02 idi). Kalite alanı gönderilmedi; kaliteyi/fiyatı belirleyen alanı göndermeden önce model sayfasından oku — DOĞRULANMADI.

Görselden video — Seedance 2.5, yol `bytedance/seedance-2.5/image-to-video`:
```json
{"prompt": "...", "image_url": "<yüklenen adres>", "draft": true, "resolution": "480p", "duration": 5, "generate_audio": false}
```
≈ 100 sn. En-boy oranı ilk kareden gelir. Büyük boy için aynı taslağı çeviren ayrı, ayrı ücretli bir "Finalize Draft" isteği var — alanları DOĞRULANMADI.

Durum sorgusu: `GET /requests/{id}/status` → `queued` / `in_progress` / `completed` / `failed` / `nsfw` / `canceled`; sonuç `images[].url` ya da `video.url`.

## 5. Kayıt düzeni
Her iş için tek klasör (git dışında tutulan bir yerde, ör. `veri/uretimler/<tarih>_<kısa-ad>/`):
- `prompt_v1.md` — model, ayar, soru cevaplarının özeti, tam prompt
- `v1_istek.json`, `v1_sonuc.json`, çıktı dosyaları (`v1_1.png`, `v1.mp4`) — `hf.py --ad v1` bu adları kendisi verir. Eski işlerde adlar farklı olabilir; klasörü listeleyip oku
- `degerlendirme.md` — ne tuttu, ne tutmadı, ders, tahmini ve gerçek ücret
Düzeltme = yeni sürüm (`v2`); eski dosyanın üzerine yazma — karşılaştırma ve geri dönüş için eski sürüm gerekir.

## 6. Bilinen tuzaklar
- İstenen çözünürlük ile gelen dosyanın boyutu aynı olmayabilir (720p istendi, 1696×960 geldi); dosyayı ölç.
- Aynı anda en fazla 2 üretim (yeni hesap sınırı).
- Bir model yolunun API'de olup olmadığını öğrenmek için ücretli adrese "deneme" isteği atma (boş gövdeli POST dahil): zorunlu alanı olmayan bir model isteği kabul edip varsayılan ayarla ücretli iş başlatabilir. Önce modelin API sayfasına ya da fiyat listesine bak; yine de denemek gerekiyorsa bu ücretli bir adım sayılır — maliyet + onay.
- Video modeli gerçek kişi yüzü içeren görseli reddedebilir; hata kodunu ve hangi dosyanın tetiklediğini bildir, filtreyi aşmak için dosyayı değiştirip tekrar gönderme. Gönderim aşamasında reddedilen (`gonder` HATA veren) iş başlamamış sayılır; yine de panelin işlem geçmişinde ücret görünüp görünmediğini kullanıcıya kontrol ettir (DOĞRULANMADI). Yüklenen fotoğrafın açık adresini silmenin API yolu bilinmiyor; kullanıcıya bunu söyle.
- Web sitesindeki bir özelliğin (kayıtlı öğeler, tek fotoğraf canlandırma vb.) API'de de olduğunu varsayma; model sayfasından doğrula.
