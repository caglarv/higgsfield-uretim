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
- **API'siz (web):** sen prompt ve ayar önerisi yazarsın, kullanıcı higgsfield.ai sitesinde kendisi üretir. Yalnız WEB sütunundaki modelleri öner (API'deki bazı adlar sitede farklı ya da yok olabilir).
- **API'li (Claude Code):** sen Higgsfield API'ye gönderirsin. Yalnız API sütunundaki modelleri kullan, çünkü örnek filmlerin ve derslerin kullandığı birçok model API'de YOK (aşağıda).
- Emin değilsen WEB'i varsay: komut çalıştıramıyorsan ya da API anahtarı yoksa gönderen sen olamazsın; olmayan bir aracı varmış gibi "ben göndereyim" deme. Yanlış listeden model önermek işi baştan bozar.

**API'de OLMAYAN (yalnız web) modeller:** Seedream 5.0 Pro, Nano Banana (2 / Pro), GPT Image 2, Topaz (video büyütme), Soul Cast — API fiyat listesinde ve explore aramasında yok (2026-11-16). Web özelliklerinin (tek fotoğraf canlandırma, Soul ID → Elements, kayıtlı öğeler) API'de çalıştığını varsayma, çünkü API sayfalarında görülmedi.

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
| Gerçek kişinin fotoğrafından görsel | Seedream 5.0 Pro (kişiyi koruyarak kıyafet/fon değiştirir); Nano Banana Pro alternatif | Soul ID'li Soul 2 (kişi başı bir kerelik eğitim) ya da fotoğrafı `image_urls` ile Marketing Studio Image'a vererek düzenleme |
| Hedefli düzenleme ("her şeyi koru, yalnız ___") | Seedream 5.0 Pro (asıl gücü bu) | Marketing Studio Image (`marketing-studio/image`) — denendi, çalıştı; alternatif Grok Imagine 2.0 (`xai/grok-imagine-image-2.0`) |
| Mekân | Seedream 5.0 Pro (mimari, büyük mekân); Soul Cinema (ışık, doku keşfi) | Soul 2; Soul Cinema API'de olabilir (DOĞRULANMADI) |
| Yazı içeren görsel | GPT 2.5 Sunburst (talimata en sadık, yazı/infografik) | Marketing Studio Image 2.5 Sunburst sürümü (aynı model olduğu DOĞRULANMADI; sürüm seçme alanı API sayfasında yazmıyor); Ideogram 4.0 adayı (yazı gücü DOĞRULANMADI) |
| Tutarlı karakter | Soul ID → Elements (web özelliği) | Soul 2 + `custom_reference_id` (Soul ID) |
| Yüz kilidi portresi (kartın ilk adımı) | Hayali kişi: Soul 2.0; fotoğraftan: Seedream 5.0 Pro ile fotoğrafı düz fonlu portreye düzenle | Hayali kişi: Soul 2; fotoğraftan: Marketing Studio Image düzenleme |
| Basit hareketli video (manzara, hafif hareket) | Seedance 2.5, 480p taslak | Wan 3.0 (`alibaba/wan-3.0/text-to-video`) adayı; Seedance 2.5 480p taslak |
| Karmaşık hareket / dans / aksiyon | Seedance 2.5 | Seedance 2.5 (`bytedance/seedance-2.5/image-to-video` denendi; `/text-to-video` ve `/reference-to-video` da var); dans için Kling 3.0 Motion Control adayı (aşağıda) |
| Ürün / kamera kontrollü çekim | Cinema Studio (Ders 3 sinematik reklam örneği) | Kling 4.0 ya da MiniMax H3 adayı; Kling 3.0 (`kling-video/v3.0/...`) |
| Konuşmalı / sesli video | Seedance 2.5 (sesli üretim desteği web'de DOĞRULANMADI) | Seedance 2.5 (`generate_audio` alanı var); Kling 3.0 (`sound` ayarı var) |

Video adayları (Wan / Kling 4.0 / MiniMax H3 / Seedance sıralaması) bağımsız sıralamalardan gelen bir öneridir, kendi denememiz yok — ilk işte küçük test yap, çünkü kalite karşılaştırması ancak gerçek çıktıyla yapılabilir.

## 4. Model kartları — güçlü yanı / dikkat

### WEB (kredi)
- **Soul 2.0** — oyuncu seçimi portreleri, yüzlerde çeşitlilik. / Dikkat: kesin yerleşim ve yazı için ilk tercih değil (kaynakta yalnız portre gücü yazıyor).
- **Soul Cinema** — fotoğraf gibi ışık, doğal cilt/kumaş, film havası; mekân ve görsel yön keşfi. / Dikkat: kesin kompozisyonu yorumlar (birkaç deneme gerekir), küçük nesneler bozulabilir, gecede gölge ayrıntısı kaybolur; metinle yerel düzenleme YAPMAZ.
- **Seedream 5.0 Pro** — düzenleme (kişi, eşya, kıyafet, fon) ve cilt/kumaş dokusunu koruma; büyük mekân, mimari, renk; karakter kartı. / Dikkat: çok yoğun tarif "fazla kusursuz CGI" görünümü verir; tekrarlanan nesneler aynı şekil/aralıkta çıkar.
- **GPT 2.5 Sunburst** — talimata en sadık; yazı, infografik, storyboard, kesin yerleşim. / Dikkat: mekân aşırı keskin/ayrıntılı olabilir; yazıyı harf harf kontrol et.
- **Nano Banana Pro** — genel amaçlı, talimata sadık. / Dikkat: bitiş yapay görünebilir, yüzler idealize ve birbirine benzer.
- **Seedance 2.5** — animasyon ve video; 480p taslak → beğenilirse büyük boy. / Dikkat: büyük boy ayrı ücret.
- **Cinema Studio** — sinematik reklam (Ders 3: 12 sn, 9:16 örnek). / Dikkat: kısa istekte süre belirtilmemişti, süre ayarını kontrol et.
- **Topaz** — video büyütme (THREAD filmi: 720p üret + Topaz büyüt). / Dikkat: yalnız web.
- **Soul Cast** — kaynakta yalnız adı geçiyor; ne yaptığı okunmadı.

### API (dolar)
- **Soul 2** (`higgsfield-ai/soul/v2/standard`) — en ucuz görsel ($0.0032/adet 720p), 4'lü batch, Soul ID ile kimlik. / Dikkat: `enhance_prompt` API sayfasında varsayılan AÇIK, kendi prompt'unu korumak için kapat; 720p istenip 1696×960 geldi (boyut beklenenden büyük olabilir).
- **Soul 2 Image to Image** — var, Soul 2 ile aynı fiyat. / Dikkat: uç noktası ve alanları okunmadı.
- **Marketing Studio Image** (`marketing-studio/image`) — üretir ve DÜZENLER, 4K'ya kadar, 16'ya kadar referans görsel; düzenleme denemesinde kişi/oda korundu. / Dikkat: gerçek ücret liste tahmininin ≈7 katı çıktı (net $0.13); kaliteyi/fiyatı belirleyen alanın adı ve değerleri DOĞRULANMADI — göndermeden önce model sayfasından oku, bilmediğin alanı uydurma; yan etki olarak ışık zayıflayabilir; `enhance_prompt` açılırsa `preset_id` gerekir ve +%10 ücret.
- **Grok Imagine 2.0** (`xai/grok-imagine-image-2.0`) — kaynak görselleri dönüştürür/iyileştirir (`image_urls`, `quality` low/medium). / Dikkat: düzenleme sadakati denenmedi.
- **Qwen Image 3** — yalnız metinden görsel. / Dikkat: düzenleme YOK.
- **Z-Image Turbo, Ideogram 4.0, Recraft 4.1, AI Influencer, Ads Studio, Soul Standard** — fiyat listesinde var. / Dikkat: ne için iyi oldukları okunmadı; seçmeden önce model sayfasına bak.
- **Seedance 2.5** (`bytedance/seedance-2.5`) — 4–30 sn; başlangıç/bitiş karesi, 30'a kadar referans görsel, video ve ses referansı; ayrıca edit ve extend modları. / Dikkat: gerçek yüzü reddedebilir (§8); ilk denemede yön ve mesafe talimatları tutmadı (kameraya yaklaştı, yanlış yöne döndü).
- **Wan 3.0 / Wan 3.0 Prime** — ucuz video ($0.038 / $0.051/sn'den). / Dikkat: katalogda yalnız metinden video yolu var; deneme yok.
- **Kling 3.0** (Turbo / Standard / Pro / 4K) — 3–15 sn, başlangıç+bitiş karesi, `sound`, çoklu çekim seçeneği. / Dikkat: deneme yok.
- **Kling 3.0 Motion Control** (`kling-video/v3/motion-control/std|pro`) — katalogda bir görsel + bir video alıyor; bir videodaki hareketi görseldeki kişiye aktarma aracı gibi görünüyor (DOĞRULANMADI, yalnız ayarlardan çıkarım). / Dikkat: dans işinde denenmeye değer, önce sayfasını oku.
- **Kling 2.5 / 2.6 / O1 / O3 / 4.0 / 4.0 Flash, MiniMax Hailuo 2.3 / H3, LTX 2.5 Fast / Pro, PixVerse 6, Grok Video 1.5, Happy Horse, Cinema Studio 4.0** — fiyat listesinde var. / Dikkat: güçlü yanları okunmadı.
- **Genjutsu Object Swap / Light Object Swap** — videoda nesne değiştirme olabilir (DOĞRULANMADI).

## 5. Ucuzdan pahalıya çalışma sırası
**Tanım:** "taslak" = bir ücretli istek. Tek istekte birden çok seçenek gelebilir (ör. 4'lü); bu yine tek taslaktır. "En fazla 2 taslak" kuralı istek sayısını sınırlar, seçenek sayısını değil.

**WEB'de (kredi):** görselde ucuz bir modelle tek istekte birkaç seçenek → en uygununu seç → yalnız seçileni düzenleme modeliyle düzelt. Videoda kısa (4–5 sn) ve en düşük çözünürlükte taslak → kullanıcı sonucu getirir, birlikte kontrol → beğenilirse büyük boy ayrı üretim. Maliyeti dolarla SÖYLEME: "sitenin üretmeden önce gösterdiği kredi tutarına bak" de; kredi tutarını bilmiyorsan bilmediğini söyle.

**API'de (dolar) — Görsel:** ucuz modelle 4'lü tek taslak (Soul 2 batch 4 ≈ $0.01) → en uygununu seç → yalnız seçileni düzenle (Marketing Studio: gerçek net $0.13). Neden: tek düzenleme 4'lü taslağın ≈13 katı; yanlış görseli düzenlemek parayı boşa harcar.

**Görselde "büyük boy" nasıl alınır:** aynı prompt'u büyük boyda yeniden üretme — beğenilen seçenek kaybolur, yerine başka bir görsel gelir. İki yol: (1) seçilen görseli düzenleme modeline verip yalnız çözünürlüğü yükselt ("keep the image identical, only increase resolution"); kişi ve ayrıntı yine de biraz değişebilir, sonucu orijinalle karşılaştır. (2) Model aynı tohum (seed) değeriyle yeniden üretmeye izin veriyorsa aynı tohumla büyük boy. Hangisinin daha sadık olduğu ve fiyatı DOĞRULANMADI; ikisi de ayrı ücretli adım, ayrı onay.
**API'de (dolar) — Video:** kısa (4–5 sn) + düşük çözünürlük taslak (Seedance 480p) → karelerden kontrol (baştan sona sık aralıklı kareler, hareket, istenmeyen kesme) → beğenilirse büyük boy AYRI istek, ayrı ücret ve AYRI onay. Neden: Seedance'te 1080p saniyesi 480p'nin ≈5,5 katı; yanlış yön ucuzken yakalanır.
- Aynı çıktı için en fazla 2 taslak (2 ücretli istek); çalışan bir taslak yeterli, çünkü "tekrar üret" daha iyisini garanti etmez.
- Başı temiz sonu bozuk çekim kurguda kesilebilir; yalnız sorunlu planı yeniden üret, çünkü tüm sahneyi yeniden üretmek düzgün kısımları da değiştirebilir.
- Yazı ve logo: üretime yazdırma, sonradan yerleştir — modeller harfi bozar, düzeltmesi ek ücret.

## 6. Maliyet kuralları
1. **"from" liste fiyatını başka ayara uygulama.** Neden: liste fiyatı en ucuz modun fiyatı. Vaka (2026-11-16): Marketing Studio düzenlemesine "1k düşük $0.0162" ile ≈$0.02 dendi; gerçek −$0.15 + $0.02 iade = net ≈ $0.13 (≈7 kat). Olası neden: `quality` gönderilmedi, varsayılan yüksek olabilir (DOĞRULANMADI).
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
| Seedance 2.5 (i2v / t2v) | 480p $0.1177 · 720p $0.2647 · 1080p $0.6518 (1080p'nin doğrudan mı yoksa yalnız Finalize Draft ile mi alındığı DOĞRULANMADI; ses açıkken fiyat değişiyor mu bilinmiyor) |
| Seedance 2.5 Finalize Draft (taslak → 1080p) | $0.6518/sn, ayrı istek |
| Seedance 2.5 referanslı / edit / extend | $0.1387–$0.7858/sn (model sayfasındaki karşılaştırma tablosu, 2026-11-16) |
| Kling 2.5 | from $0.032 |
| Wan 3.0 | from $0.038 |
| MiniMax Hailuo 2.3 | from $0.047 |
| Wan 3.0 Prime | from $0.051 |
| Kling 2.6 | from $0.052 |
| Kling 4.0 Flash | from $0.063 (720p) |
| Kling O1 / O3 / 3.0 | from $0.063 / $0.068 / $0.071 |
| Genjutsu Light (Object Swap) | from $0.074 (Object Swap $0.074–0.294, 4 sn) |
| Wan 2.6 / 2.7 | from $0.075 |
| Seedance 2.0 · Grok Video 1.5 | from $0.080 |
| LTX 2.5 Fast / Pro | from $0.090 / $0.120 |
| PixVerse 6 | from $0.115 |
| Cinema Studio 4.0 | from $0.123 (720p'ye kadar) |
| Kling 4.0 | from $0.126 |
| MiniMax H3 | from $0.130 |
| Happy Horse | from $0.140 |
| Genjutsu (Object Swap) | $0.154–0.835 |

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
- **Soul ID en az fotoğraf sayısı:** Soul 2 API notumuz 1–100 diyor; başka bir kaynak en az 20 diyor. ÇELİŞKİ — Soul ID işinden önce resmi sayfadan doğrula.
- **Marketing Studio `quality` alanı:** değerleri ve varsayılanı bilinmiyor; varsayılan yüksek olabilir (≈7 kat ücretin olası nedeni). Sürüm (2.0 Alpha / 2.5 Flare / 2.5 Sunburst) seçme alanı API sayfasında yazmıyor.
- **Marketing Studio 2.5 Sunburst = web'deki GPT 2.5 Sunburst mü?** Aynı ad; aynı model olduğu DOĞRULANMADI.
- **Soul Cinema API'de var mı?** Fiyat listesinde yok; Studio kataloğu `higgsfield-ai/soul/cinema` yolunu kullanıyor. DOĞRULANMADI.
- **Seedance 2.5 çözünürlükleri:** model sayfası 480p/720p/1080p fiyatı veriyor; Studio kataloğu yalnız 480p/720p seçeneği içeriyor. 1080p'nin doğrudan mı yoksa yalnız Finalize Draft ile mi alındığı DOĞRULANMADI. Ses (`generate_audio`, katalogda varsayılan açık) fiyatı etkiliyor mu, bilinmiyor.
- **Kling 3.0 Motion Control** hareket aktarımı mı yapıyor — yalnız katalog ayarlarından çıkarım.
- **Soul 2 Image to Image** alanları, **Grok Imagine 2.0** ve **Genjutsu** düzenleme gücü denenmedi.
- **Web'de** sesli/konuşmalı videoyu hangi modelin en iyi yaptığı kaynaklarda yok; Soul Cast'in ne yaptığı okunmadı; web kredi fiyatları bilinmiyor.
- **Kayıtlı öğeler (elements)** API'de var mı: görülmedi; API'de referanslar görsel olarak gönderiliyor.
- **Video model sıralaması** (Wan / Kling 4.0 / MiniMax H3 / Seedance) bağımsız kaynaklardan; kendi denememiz yalnız Seedance 2.5.
- **API üretimleri web hesabına (Akademi ödevlerine) sayılıyor mu** bilinmiyor.
- **Tarih farkı:** ilk Soul 2 ücreti panelde "Nov 15" görünüyor, iş 16 Kasım'da yapıldı (saat dilimi olabilir).
