# Modeller ve maliyet — seçim rehberi

Bilgi tarihi: 2026-11-16. Model listeleri ve fiyatlar değişir; her işte modelin kendi sayfasından doğrula.
Okuyucu: kullanıcının ne istediğine bakıp model ve ayarı SEN seçersin; kullanıcıya model seçtirme (o "ne istediğini" bilir, model adlarını bilmek zorunda değil).

## İçindekiler
1. Önce ortamı belirle: web mi, API mi
2. İki para sistemi
3. Hangi iş → hangi model (WEB / API)
4. Model kartları: güçlü yanı / dikkat
5. Ucuzdan pahalıya çalışma sırası
6. Maliyet kuralları
7. Bilinen API dolar fiyatları (2026-11-16)
8. Gerçek kişi ve çocuk fotoğrafı
9. Açık / doğrulanmamış konular

---

## 1. Önce ortamı belirle
- **API'siz (web):** sen prompt ve ayar önerisi yazarsın, kullanıcı higgsfield.ai sitesinde kendisi üretir. Yalnız WEB sütunundaki modelleri öner (API'deki bazı adlar sitede farklı ya da yok olabilir). Model değil de hazır bir ARAÇ (ışık değiştirme, oran değiştirme, storyboard, kısa film stüdyosu, seslendirme) gerekiyorsa `site-ozellikleri.md`. Sitenin 2026-11-16 menüsünde güncel adlar: Seedream 5.5, GPT Image 2.6 Sunburst / Flare, Nano Banana 2.1 / Pro, Soul 2.0, Soul Cinema; aşağıdaki tabloda eski sürüm adı geçiyorsa sitedekini kullan.
- **API'li (Claude Code):** sen Higgsfield API'ye gönderirsin. Yalnız API sütunundaki modelleri kullan, çünkü örnek filmlerin ve derslerin kullandığı birçok model API'de YOK (aşağıda).
- Emin değilsen WEB'i varsay: komut çalıştıramıyorsan ya da API anahtarı yoksa gönderen sen olamazsın; olmayan bir aracı varmış gibi "ben göndereyim" deme. Yanlış listeden model önermek işi baştan bozar.

**API'de OLMAYAN (yalnız web) modeller:** Seedream (5.5; eski adı 5.0 Pro), Nano Banana (2 / Pro), GPT Image 2, Topaz (video büyütme), Soul Cast — API fiyat listesinde ve explore aramasında yok (2026-11-16). Web özelliklerinin (tek fotoğraf canlandırma, Soul ID → Elements, kayıtlı öğeler) API'de çalıştığını varsayma, çünkü API sayfalarında görülmedi.

## 2. İki para sistemi — birbirine çevrilmez
| | Web (higgsfield.ai) | API (open.higgsfield.ai) |
|---|---|---|
| Birim | Kredi + abonelik | Dolar bakiyesi |
| Fiyatı nereden okursun | Sitedeki üretim ekranının teklifi | Modelin API sayfasındaki $/adet ya da $/saniye |
| Not | Üretim için yeterli kredi/abonelik gerekir; ücretsiz planda bazı araçlar kapalı olabilir | API yanıtında ücret alanı yok; gerçek ücret panelin işlem geçmişinde görünür |

- Kredi rakamını dolara, dolar rakamını krediye ÇEVİRME, çünkü iki ayrı hesap ve ayrı fiyat tablosudur; "10 kredi" ile "10 dolar" aynı şey değildir.
- Web kredi fiyatı bu rehberde YOK; "sitedeki teklifi kontrol et" de. Kullanıcı kredinin dolar karşılığını sorarsa: bunu abonelik planı belirler (aylık ödeme ÷ ayda gelen kredi = bir kredinin fiyatı); API dolar fiyatını web işine fiyat diye verme. Tek kayıtlı örnek: Ders 2'de Seedance 2.5 · 15 sn · 16:9 · 480p = 38 kredi — o hesabın teklifi, bizimki farklı olabilir.

## 3. Hangi iş → hangi model

| İş | WEB'de (kredi) | API'de (dolar) |
|---|---|---|
| Hayali kişi / konsept görseli | Soul 2.0 (oyuncu seçimi, yüz çeşitliliği); film havası için Soul Cinema | Soul 2 (`higgsfield-ai/soul/v2/standard`), ucuz 4'lü taslak |
| Gerçek kişinin fotoğrafından görsel | Seedream (5.5; eski adı 5.0 Pro) (kişiyi koruyarak kıyafet/fon değiştirir); Nano Banana Pro alternatif | Soul ID'li Soul 2 (kişi başı bir kerelik eğitim) ya da fotoğrafı `image_urls` ile Marketing Studio Image'a vererek düzenleme |
| Hedefli düzenleme ("her şeyi koru, yalnız ___") | Seedream (5.5; eski adı 5.0 Pro) (asıl gücü bu) | Marketing Studio Image (`marketing-studio/image`) — denendi, çalıştı; alternatif Grok Imagine 2.0 (`xai/grok-imagine-image-2.0`) |
| Mekân | Seedream (5.5; eski adı 5.0 Pro) (mimari, büyük mekân); Soul Cinema (ışık, doku keşfi) | Soul 2; Soul Cinema API'de olabilir (DOĞRULANMADI) |
| Yazı içeren görsel | GPT Image 2.6 Sunburst (eski 2.5) (talimata en sadık, yazı/infografik) | Marketing Studio Image Sunburst (`marketing-studio/image/sunburst`; web'deki GPT Image 2.6 Sunburst ile aynı model olduğu DOĞRULANMADI); Ideogram 4.0 adayı (yazı gücü DOĞRULANMADI) |
| Tutarlı karakter | Soul ID → Elements (web özelliği) | Soul 2 + `custom_reference_id` (Soul ID) |
| Yüz kilidi portresi (kartın ilk adımı) | Hayali kişi: Soul 2.0; fotoğraftan: Seedream (5.5; eski adı 5.0 Pro) ile fotoğrafı düz fonlu portreye düzenle | Hayali kişi: Soul 2; fotoğraftan: Marketing Studio Image düzenleme |
| Basit hareketli video (manzara, hafif hareket) | Seedance 2.5, 480p taslak | Wan 3.0 i2v 480p ($0.0375/sn) · Kling 3.0 std · Seedance 2.5 480p taslak |
| Karmaşık hareket / dans / aksiyon | Seedance 2.5 | Seedance 2.5 i2v (denendi) · Kling 3.0 i2v · Kling 4.0; hareketin şekli kesin olacaksa Kling 3.0 Motion Control (referans videodan) |
| Yönü / son pozu kesin olan hareket (döner, oturur, bakar) | Bitiş karesi destekleyen araç | Bitiş karesi: Seedance 2.5/2.0 i2v, Kling 3.0 i2v (`last_image_url`), Kling O3/Omni first-last-frame, Wan 3.0, Kling 4.0 · hareket kopyalama: Kling 3.0 Motion Control |
| Ürün / kamera kontrollü çekim | Cinema Studio (Ders 3 sinematik reklam örneği) | Kling 4.0 ya da MiniMax H3; LTX 2.5 (`camera_movement` seçimi); Cinema Studio 4.0 |
| Konuşmalı / sesli video | Seedance 2.5 (sesli üretim desteği web'de DOĞRULANMADI) | Seedance 2.5 (`generate_audio`); Kling 3.0 / 2.6 (`sound`); Wan 3.0 (`generate_audio`) |

API'de tek modele atlama: işe uyan 2–3 adayı `api-modeller.md`'den bul, fiyatlarını hesapla, birini gerekçeyle seç. Kalite sıralaması için kendi denememiz yalnız Seedance 2.5; önemli işte iki adayı en ucuz ayarda birer taslakla dene (iki ücret, iki onay).

## 4. Model kartları — güçlü yanı / dikkat

### WEB (kredi)
- **Soul 2.0** — oyuncu seçimi portreleri, yüzlerde çeşitlilik. / Dikkat: kesin yerleşim ve yazı için ilk tercih değil (kaynakta yalnız portre gücü yazıyor).
- **Soul Cinema** — fotoğraf gibi ışık, doğal cilt/kumaş, film havası; mekân ve görsel yön keşfi. / Dikkat: kesin kompozisyonu yorumlar (birkaç deneme gerekir), küçük nesneler bozulabilir, gecede gölge ayrıntısı kaybolur; metinle yerel düzenleme YAPMAZ.
- **Seedream (5.5; eski adı 5.0 Pro)** — düzenleme (kişi, eşya, kıyafet, fon) ve cilt/kumaş dokusunu koruma; büyük mekân, mimari, renk; karakter kartı. / Dikkat: çok yoğun tarif "fazla kusursuz CGI" görünümü verir; tekrarlanan nesneler aynı şekil/aralıkta çıkar.
- **GPT Image 2.6 Sunburst (eski 2.5)** — talimata en sadık; yazı, infografik, storyboard, kesin yerleşim. / Dikkat: mekân aşırı keskin/ayrıntılı olabilir; yazıyı harf harf kontrol et.
- **Nano Banana Pro** — genel amaçlı, talimata sadık. / Dikkat: bitiş yapay görünebilir, yüzler idealize ve birbirine benzer.
- **Nano Banana 2.1** — temiz, cilalı 3B karakter görünümü; askılı tulum gibi kıyafet ayrıntısına sadık. / Dikkat (tek deneme, 2026-11-16): abartılı karakter özelliklerini "ortalama" bir yüze yumuşattı — sırık beden, uzun sivri burun, huysuz ifade, şapkanın uzun arka siperi kayboldu; portreyi üç çeyrek yerine tam önden çizdi. Bu modelde abartıyı sayıyla ve sert yaz (bkz. karakter-mekan-esya.md, "Abartı").
- **ChatGPT Görseller (GPT görsel üretimi)** — Higgsfield dışı; ChatGPT aboneliğinden düşer. / Aynı kart prompt'unda (2026-11-16) abartılı özellikleri ve küçük ayrıntıları en sadık uygulayan bu oldu; ama kendiliğinden ayrıntı ekler (kazak, kapüşon) — kartı okuyup tarife geri yaz.
- **Seedance 2.5** — animasyon ve video; 480p taslak → beğenilirse büyük boy. / Dikkat: büyük boy ayrı ücret.
- **Cinema Studio** — sinematik reklam (Ders 3: 12 sn, 9:16 örnek). / Dikkat: kısa istekte süre belirtilmemişti, süre ayarını kontrol et.
- **Topaz** — video büyütme (THREAD filmi: 720p üret + Topaz büyüt). / Dikkat: yalnız web.
- **Soul Cast** — kaynakta yalnız adı geçiyor; ne yaptığı okunmadı.

### API (dolar)
- **Soul 2** (`higgsfield-ai/soul/v2/standard`) — en ucuz görsel ($0.0032/adet 720p), 4'lü batch, Soul ID ile kimlik. / Dikkat: `enhance_prompt` API sayfasında varsayılan AÇIK, kendi prompt'unu korumak için kapat; 720p istenip 1696×960 geldi (boyut beklenenden büyük olabilir).
- **Soul 2 Image to Image** — var, Soul 2 ile aynı fiyat. / Dikkat: uç noktası ve alanları okunmadı.
- **Marketing Studio Image** (`marketing-studio/image`) — üretir ve DÜZENLER, 4K'ya kadar, 16'ya kadar referans görsel; düzenleme denemesinde kişi/oda korundu. / Dikkat: `quality` low/medium/high, **varsayılan high**; ücret token ile hesaplanır (önce tahmini çekim, sonra düzeltme). İlk düzenlemede `quality` gönderilmedi, net $0.13 çekildi (liste tahmininin ≈7 katı) — büyük olasılıkla neden bu, ücret etkisi DOĞRULANMADI. Her gönderimde `quality`yi açıkça yaz; yan etki olarak ışık zayıflayabilir; `enhance_prompt` açılırsa `preset_id` gerekir ve +%10 ücret.
- **Grok Imagine 2.0** (`xai/grok-imagine-image-2.0`) — kaynak görselleri dönüştürür/iyileştirir (`image_urls`, `quality` low/medium). / Dikkat: düzenleme sadakati denenmedi.
- **Qwen Image 3** — yalnız metinden görsel. / Dikkat: düzenleme YOK.
- **Z-Image Turbo, Ideogram 4.0, Recraft 4.1, AI Influencer, Ads Studio, Soul Standard** — fiyat listesinde var. / Dikkat: ne için iyi oldukları okunmadı; seçmeden önce model sayfasına bak.
- **Seedance 2.5** (`bytedance/seedance-2.5`) — 4–30 sn; i2v'de bitiş karesi (`end_image_url`), referans modunda 30'a kadar görsel + video + ses; edit, extend, 480p taslak → 1080p. / Dikkat: gerçek yüzü reddedebilir (§8); iki dans denemesinde konum kilidi tuttu ama dönüş yönü iki kez ters çıktı (yazıyla yön verilmişti).
- **Wan 3.0 / Wan 3.0 Prime** — en ucuz video (480p $0.0375 / $0.051/sn); t2v, i2v (bitiş karesi), reference. / Dikkat: deneme yok.
- **Kling 3.0** (Turbo / Standard / Pro / 4K) — 3–15 sn, bitiş karesi (`last_image_url`), `sound`, `multi_prompt` (çekim çekim), `cfg_scale`. / Dikkat: deneme yok.
- **Kling 3.0 Motion Control** (`kling-video/v3/motion-control/std|pro`) — resmi tanım: bir resmi verilen videodaki hareketle canlandırır; `character_orientation: video` yönü videodan alır. std 720p $0.092/sn (referans video süresi kadar). / Dikkat: bir referans video (kendi çekimin) gerekir; büyük baş dönüşlerinde yüz kayabilir (kaynak: kullanıcı yazıları, denemedik).
- **Kling O3 / Omni, Kling 4.0 / 4.0 Flash, Kling 2.5 / 2.6, MiniMax H3 / Hailuo 2.3, LTX 2.5, PixVerse 6, Grok Video 1.5, Happy Horse, Cinema Studio 4.0** — modları, alanları ve fiyatları `api-modeller.md`'de. / Dikkat: hiçbiri denenmedi; Hailuo'da `prompt_optimizer` varsayılan açık (prompt'u yeniden yazar).
- **Genjutsu** (motion-transfer, object-swap, restyle) ve **Genjutsu Light** — videonun hareketini koruyup kişi/nesne/stil değiştirir (resmi tanım). / Dikkat: denenmedi.

## 5. Ucuzdan pahalıya çalışma sırası
**Tanım:** "taslak" = bir ücretli istek. Tek istekte birden çok seçenek gelebilir (ör. 4'lü); bu yine tek taslaktır. "En fazla 2 taslak" kuralı istek sayısını sınırlar, seçenek sayısını değil.

**WEB'de (kredi):** görselde ucuz bir modelle tek istekte birkaç seçenek → en uygununu seç → yalnız seçileni düzenleme modeliyle düzelt. Videoda kısa (4–5 sn) ve en düşük çözünürlükte taslak → kullanıcı sonucu getirir, birlikte kontrol → beğenilirse büyük boy ayrı üretim. Maliyeti dolarla SÖYLEME: "sitenin üretmeden önce gösterdiği kredi tutarına bak" de; kredi tutarını bilmiyorsan bilmediğini söyle.

**API'de (dolar) — Görsel:** ucuz modelle 4'lü tek taslak (Soul 2 batch 4 ≈ $0.01) → en uygununu seç → yalnız seçileni düzenle (Marketing Studio: gerçek net $0.13). Neden: tek düzenleme 4'lü taslağın ≈13 katı; yanlış görseli düzenlemek parayı boşa harcar.

**Görselde "büyük boy" nasıl alınır:** aynı prompt'u büyük boyda yeniden üretme — beğenilen seçenek kaybolur, yerine başka bir görsel gelir. İki yol: (1) seçilen görseli düzenleme modeline verip yalnız çözünürlüğü yükselt ("keep the image identical, only increase resolution"); kişi ve ayrıntı yine de biraz değişebilir, sonucu orijinalle karşılaştır. (2) Model aynı tohum (seed) değeriyle yeniden üretmeye izin veriyorsa aynı tohumla büyük boy. Hangisinin daha sadık olduğu ve fiyatı DOĞRULANMADI; ikisi de ayrı ücretli adım, ayrı onay.
**API'de (dolar) — Video:** kısa (4–5 sn) + düşük çözünürlük taslak (Seedance 480p) → karelerden kontrol (baştan sona sık aralıklı kareler, hareket, istenmeyen kesme) → beğenilirse büyük boy AYRI istek, ayrı ücret ve AYRI onay. Neden: Seedance'te 1080p saniyesi 480p'nin ≈5,5 katı; yanlış yön ucuzken yakalanır.
- **Taslağı aynen büyüten yol yalnız Seedance 2.5'te var** (`draft` → `finalize-draft`). Wan, Kling ve diğerlerinde "büyük boy" aynı prompt'la YENİ bir üretimdir; hareket ve ayrıntı taslaktan farklı çıkabilir. Bunu onay isterken söyle; taslağın birebir büyümesi önemliyse Seedance 2.5 taslak yolunu seç ya da baştan istenen çözünürlükte üret.
- Aynı çıktı için en fazla 2 taslak (2 ücretli istek); çalışan bir taslak yeterli, çünkü "tekrar üret" daha iyisini garanti etmez.
- Başı temiz sonu bozuk çekim kurguda kesilebilir; yalnız sorunlu planı yeniden üret, çünkü tüm sahneyi yeniden üretmek düzgün kısımları da değiştirebilir.
- Yazı ve logo: üretime yazdırma, sonradan yerleştir — modeller harfi bozar, düzeltmesi ek ücret.

## 6. Maliyet kuralları
1. **"from" liste fiyatını başka ayara uygulama.** Neden: liste fiyatı en ucuz modun fiyatı. Vaka (2026-11-16): Marketing Studio düzenlemesine "1k düşük $0.0162" ile ≈$0.02 dendi; gerçek −$0.15 + $0.02 iade = net ≈ $0.13 (≈7 kat). Neden büyük olasılıkla: `quality` gönderilmedi ve varsayılanı high (kâğıtta yazıyor); ücret etkisi denenmedi. Varsayılanı fiyatı artıran her alanı (kalite, çözünürlük, süre, ses) açıkça yaz; `hf.py kontrol` verilmeyenleri uyarır.
2. **Fiyatı seçilen mod + çözünürlük + kalite + süre (+ referans/ses) için modelin kendi sayfasından oku.** Neden: aynı model içinde fiyat 5–50 kat oynuyor (Marketing Studio 1k düşük $0.0162 ↔ 4k yüksek $0.7219).
3. **Toplamı söyle: taslak + final + düzenleme + büyütme + varyasyon.** Neden: Seedance'te taslağı 1080p'ye çevirmek (Finalize Draft) ayrı istek, ayrı ücret; tek kalem söylemek gerçek maliyeti gizler.
4. **Beğenilmeyen ama tamamlanan iş de ücretlidir.** Neden: ücret çıktı kalitesine değil üretime göre alınır. Başarısız / NSFW / fikrî hak engeli genelde iade edilir, bazı modellerde istisna var (Ders 1).
5. **Kullanılabilir çıktı başına maliyet** = sahneye harcanan toplam ÷ kabul edilen çıktı sayısı. Neden: ucuz model çok deneme isterse pahalı modelden pahalıya gelebilir.
6. **Her ücretli adımdan önce tek satır: model + ayar + ≈ maliyet → onay.** Harcama tavanı yok; koruma her çağrıda ayrı onaydır — "bütçe içindeyse onaysız ilerle" kuralı uygulanmaz.
7. **Ölçülmemiş fiyata "≈ tahmin" yaz;** gerçek ücreti işlem geçmişinden (web'de kredi geçmişi, API'de Usage/Refund satırları) teyit et, çünkü API yanıtında ücret alanı yok.
8. **Teslimde:** model + ayar + gerçek ya da tahmini USD/kredi ayrı ayrı yazılır.

## 7. Bilinen API dolar fiyatları (2026-11-16)
DEĞİŞEBİLİR — her işte modelin sayfasından doğrula. "from" = listedeki en düşük mod; başka ayar daha pahalı.

**Görsel (adet başı):**
| Model | Fiyat | Not |
|---|---|---|
| Soul 2 | 720p $0.0032 · 1080p $0.0057 | Gerçek: 4 görsel 720p ≈ $0.01 (panel kuruşa yuvarlıyor) |
| Soul 2 Image to Image | Soul 2 ile aynı | |
| Soul ID eğitimi | $2.50 / istek | Kişi başı bir kerelik |
| Marketing Studio Image | 1k düşük $0.0162 · 2k düşük $0.0222 · 4k yüksek $0.7219; Sunburst/Flare $0.0126'dan | Gerçek: 1k, quality gönderilmeden net ≈ $0.13 |
| Z-Image Turbo | from $0.015 | |
| Ideogram 4.0 | from $0.030 | |
| Recraft 4.1 | from $0.035 | |
| Grok Imagine 2.0 | from $0.040 | |
| Qwen Image 3 | from $0.040 | |
| AI Influencer | from $0.050 | |
| Ads Studio | from $0.084 | |
| Soul Standard | from $0.094 | |

**Video (saniye başı):**
| Model | Fiyat |
|---|---|
| Seedance 2.5 (i2v / t2v) | 480p $0.1177 · 720p $0.2647 · 1080p $0.6518 (1080p doğrudan seçilebilir; ses açıkken fiyat değişiyor mu kâğıtta yazmıyor) |
| Seedance 2.5 Finalize Draft (taslak → 1080p) | $0.6518/sn, ayrı istek |
| Seedance 2.5 edit / extend (video girdili) | 480p $0.1387 · 720p $0.3264 · 1080p $0.7858 |
| Seedance 2.0 | 480p $0.0804 · 720p $0.1735 · 1080p $0.4293 · 4K $0.8907 |
| Wan 3.0 / Wan 3.0 Prime | 480p $0.0375 / $0.051 · 720p $0.075 / $0.105 · 1080p $0.15 / $0.21 |
| Wan 2.6 / 2.7 | 720p ≈ $0.075 · 1080p ≈ $0.113 |
| Kling 2.5 turbo | std 720p $0.0315 · pro 1080p $0.0525 |
| Kling 2.6 pro | 1080p $0.0666 |
| Kling 3.0 | std 720p $0.0714 · pro 1080p $0.0962 · 4K $0.3151 · turbo 720p $0.0839 |
| Kling 3.0 Motion Control | std 720p $0.0920 · pro 1080p $0.1189 (referans video süresi kadar); eski sürüm std $0.0523 |
| Kling O3 / Omni | 720p $0.0683 / $0.0632 (görsel modları); video modları $0.0945 |
| Kling 4.0 / 4.0 Flash | 720p $0.1257 · 1080p $0.1879 / Flash reference 720p $0.094 |
| MiniMax H3 | reference 2K $0.13 (+ 5'ten sonraki her referans görsel $0.08) |
| Genjutsu / Genjutsu Light | 480p $0.154 / $0.0739 (kaynak video süresi kadar); restyle ≈ $0.318 |
| Hailuo 2.3, LTX 2.5, PixVerse 6, Happy Horse, Grok Video 1.5 | kâğıtta yok; liste "from": Hailuo $0.047 · LTX $0.090/$0.120 · PixVerse $0.115 · Happy Horse $0.140 · Grok $0.080 |
| Cinema Studio 4.0 | token ile; liste "from" $0.123 |

Kaynak: modlerin kullanım kâğıtları (2026-11-16); ayrıntı `api-modeller.md`.

Örnek hesap: Seedance 2.5, 480p, 5 sn = 5 × $0.1177 ≈ $0.59 (ilk video denemesi; gerçek ücret DOĞRULANMADI). Aynı 5 sn 1080p'ye çevirmek ≈ +$3.26 daha.
Eşzamanlılık: yeni hesapta 2 eşzamanlı üretim; son 28 günde ≥ $25 yüklenince 10.

**Fiyat sayfasını okuyamıyorsan** (ağ yok, sayfa açılmıyor): bu tablodaki tarihli rakamı kullan, "≈ tahmin, bugün doğrulanmadı" de ve onay isterken bunu açıkça söyle.

**Baskı için boyut (≈ kural):** iyi baskı için uzun kenar ≈ santimetre × 118 piksel (300 dpi); ör. 30×40 cm ≈ 3540×4720 piksel. Modelin en yüksek çözünürlüğü buna yetmiyorsa ayrıca büyütme gerekir; hangi büyütme aracının görselde iyi sonuç verdiği DOĞRULANMADI — kullanıcıya bunu söyle, baskıdan önce küçük bir deneme baskısı öner.

## 8. Gerçek kişi ve çocuk fotoğrafı
- Fotoğraf başkasına ya da çocuğa aitse ve izin belirsizse ücretli çağrıdan ÖNCE sor, çünkü yüz başka bir servise yükleniyor ve geri alınamaz.
- Çocuk fotoğrafını servisler arasında otomatik deneme ("bu reddetti, şunu deneyeyim" yapma), çünkü her deneme fotoğrafı yeni bir yere gönderir.
- Video modeli gerçek yüzü reddedebilir (Seedance: `InputImageSensitiveContentDetected.PrivacyInformation`). Hatayı kullanıcıya bildir; aynı dosyayı ya da kırpılmış/değiştirilmiş kopyasını filtreyi aşmak için TEKRAR GÖNDERME, çünkü filtre bilinçli bir koruma.
- Reddedilirse dürüst seçenekler sun: hayali karakterle üretmek ya da kullanıcının izinli başka bir yol seçmesi.

## 9. Açık / doğrulanmamış konular
- **Soul ID fotoğraf sayısı:** API kâğıdı 1–100 fotoğraf kabul ediyor (`input_images`). Başka bir kaynağın "en az 20" demesi kalite önerisi olabilir; kaç fotoğrafın iyi sonuç verdiği DOĞRULANMADI.
- **Marketing Studio `quality`:** low/medium/high, varsayılan high (kâğıttan). Sürümler ayrı yollar: `marketing-studio/image/flare`, `/sunburst`. Ücretin ne kadar düştüğü denenmedi.
- **Marketing Studio 2.5 Sunburst = web'deki GPT Image 2.6 Sunburst (eski 2.5) mü?** Aynı ad; aynı model olduğu DOĞRULANMADI.
- **Soul Cinema API'de var mı?** Fiyat listesinde yok; Studio kataloğu `higgsfield-ai/soul/cinema` yolunu kullanıyor. DOĞRULANMADI.
- **Seedance 2.5 ses:** `generate_audio` varsayılan AÇIK; fiyatı etkiliyor mu kâğıtta yazmıyor. Sessiz istiyorsan `false` ver.
- **Soul 2 Image to Image** (alanları `api-modeller.md`'de), **Grok Imagine 2.0** ve **Genjutsu** düzenleme gücü denenmedi.
- **Web'de** sesli/konuşmalı videoyu hangi modelin en iyi yaptığı kaynaklarda yok; Soul Cast'in ne yaptığı okunmadı; web kredi fiyatları bilinmiyor.
- **Kayıtlı öğeler (elements)** API'de var mı: görülmedi; API'de referanslar görsel olarak gönderiliyor.
- **Video model kalitesi:** kendi denememiz yalnız Seedance 2.5; diğer modellerin dans/yön/kimlik başarısı bilinmiyor.
- **API üretimleri web hesabına (Akademi ödevlerine) sayılıyor mu** bilinmiyor.
- **Tarih farkı:** ilk Soul 2 ücreti panelde "Nov 15" görünüyor, iş 16 Kasım'da yapıldı (saat dilimi olabilir).
