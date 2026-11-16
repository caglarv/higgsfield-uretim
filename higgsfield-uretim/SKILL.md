---
name: higgsfield-uretim
description: Yapay zekâ ile görsel ve video ÜRETİMİNİ (Higgsfield ve içindeki modeller) baştan sona yönetir — 15 soruyla isteği netleştirir, İngilizce prompt yazar, model/ayar seçer, maliyeti söyleyip onay alır, sonucu kare kare denetler ve düzeltir. Kullanıcı yapay zekâyla fotoğraf/görsel üretmek ya da düzenlemek, aile fotoğrafından görsel, karakter, tanıtım videosu, reklam, Reels, kısa film istediğinde ya da "şunu videoya çevir / şöyle bir sahne üret / Seedance için prompt yaz" dediğinde MUTLAKA kullan; Higgsfield, Seedance, Soul, Soul ID, Kling, Wan, Nano Banana, Seedream, Marketing Studio, Cinema Studio adları geçtiğinde ve üretilmiş bir görsel/videonun neden kötü çıktığı sorulduğunda da kullan. API olmadan da çalışır (kopyala-yapıştır prompt paketi verir). Kodla yapılan grafik, animasyon ya da sunum işleri için değildir.
---

# Higgsfield üretim

Kullanıcıyla Türkçe, kısa ve günlük dille konuş; programcı değil. Üretim prompt'larını İngilizce yaz. Görselde görünecek ya da videoda söylenecek metni kullanıcının verdiği dilde ve yazımla aynen koru.

## Önce: hangi biçimde çalışıyorsun?
- **Üretim biçimi** — komut çalıştırabiliyorsan VE Higgsfield API anahtarı tanımlıysa: prompt'u kendin gönderir, sonucu indirir, denetlersin. `references/api-claude-code.md` dosyasını oku.
- **Prompt biçimi** — diğer her yerde (ChatGPT, Claude sohbet, başka yapay zekâ): üretimi kullanıcı higgsfield.ai sitesinde yapar. Sen teslim paketi verirsin, kullanıcı sonucu geri getirir, sen denetlersin.

Emin değilsen prompt biçimini varsay; olmayan bir aracı varmış gibi anlatma. Site KREDİ, API DOLAR kullanır ve model listeleri farklıdır; hangi biçimdeysen o listeden seç.

## Akış
1. **İsteği ve eldekileri oku:** mesaj, fotoğraflar, önceki kararlar, önceki denemelerin notları. Gereken fotoğraf eklenmemişse iste. Fotoğraftaki kişi kullanıcının kendisi değilse izin sorusu 15 sorudan ÖNCE ve ayrı sorulur (aşağıda "Gerçek kişiler"); izin yoksa plan yapılmaz.
2. **15 soru sor** (`references/sorular.md`). Ne istediğini sor; modeli, çözünürlüğü, ayarı kullanıcıya seçtirme — cevaplardan sen seç. Soru ucuz, hatalı üretim pahalı. Yeni her üretim isteğinde 15 soru sorulur. Var olan bir çıktıyı düzeltirken 15'e tamamlama: yalnız eksik kalanı sor (çoğu zaman 0–3 soru), çünkü gerisi önceki cevaplarda ve kayıtta zaten var.
3. **Sahneyi düz Türkçeyle anlat** (3–5 cümle: kim, nerede, ne oluyor, kamera, ışık). Yanlış anlaşılan burada, para harcanmadan yakalanır.
4. **Prompt'u yaz.** Görsel: `references/gorsel-prompt.md`. Video: `references/video-prompt.md`. Aynı kişi/mekân/eşya birden çok çıktıda geçecekse ya da gerçek kişi fotoğrafı kaynaksa önce `references/karakter-mekan-esya.md`.
5. **Model ve ayarı seç, maliyeti hesapla** (`references/modeller-ve-maliyet.md`; üretim biçiminde ayrıca `references/api-modeller.md`). Tek modele alışkanlıkla atlama: işe uyan 2–3 adayı fiyatıyla karşılaştır, birini gerekçeyle seç. Yön ya da son poz işin özüyse yazıya güvenme; bitiş karesi ya da hareket kopyalama destekleyen yolu seç (`references/video-prompt.md` §7). Önce ucuz taslak, beğenilirse büyük boy.
6. **Onay iste — tek satır:** model + ayar + ≈ maliyet. Onay gelmeden ücretli hiçbir şey başlatma. Büyük boy ayrı ücretli adımdır: taslak beğenildikten sonra ayrıca maliyet + onay.
7. **Üret** (üretim biçimi) ya da **teslim paketini ver** (prompt biçimi).
8. **Sonucu denetle** (`references/kontrol-ve-duzeltme.md`). Görsele kendin bak; videoda baştan sona sık aralıklı karelere bak. Videoyu izleyemiyorsan söyle. Bakmadığın şeye "iyi" deme.
9. **Tutanı ve tutmayanı ayrı söyle,** tek bir sonraki adım öner: kabul / hedefli düzeltme / yeniden üretim. Her düzeltme yeni ücretli iştir: yine maliyet + onay.
10. **Kaydet:** cevap özeti, tam prompt, model + ayar, sonuç, değerlendirme, tahmini ve gerçek ücret. Eski sürümün üzerine yazma (v1, v2…). Dosya yazamıyorsan aynı kaydı kullanıcının saklayacağı tek bir "kayıt" bloğu olarak ver.

Kullanıcı yalnız "prompt yaz" ya da "planla" dediyse 15 soru yine sorulur (iyi prompt onlara dayanır; kullanıcı "soru sorma" derse sorma), ama ücretli onayı ve üretimi atla; prompt'u (prompt biçiminde teslim paketinin tamamını) ve tahmini maliyeti ver, hiçbir şey gönderme. Yalnız fiyat sorulduysa soru sormadan seçilen ayarın fiyatını hesapla.

**Prompt biçiminde** parayı kullanıcı kendi tıklamasıyla harcar; bu yüzden 3, 6 ve 7. adımlar tek cevapta verilebilir. Kredi tutarını bilmiyorsan uydurma: "sitenin gösterdiği tutara bak" de.

**Taslak** = bir ücretli istek (içinde birden çok seçenek olabilir). Aynı çıktı için en fazla 2 taslak; sonra dur ve konuş. Aynı hata iki denemede de çıkıyorsa sorun şans değil prompt ya da kaynak görseldir.

## Teslim paketi (prompt biçimi)
1. **Nerede:** sitede hangi araç ve model. Menü adı ekranda farklıysa kullanıcı gördüğünü söylesin.
2. **Ayarlar:** en-boy, çözünürlük, süre, ses, kaç çıktı; prompt iyileştirme (enhance) seçeneği varsa kapalı — her biri tek satır.
3. **Yüklenecek dosyalar:** hangi fotoğraf hangi kutuya, her birinin görevi.
4. **Prompt:** tek kod bloğu, kopyalanmaya hazır.
5. **Üretmeden önce:** "sitenin gösterdiği kredi tutarına bak; yüksek gelirse üretme, bana yaz."
6. **Sonra:** "çıkanı buraya yükle, birlikte kontrol edelim." Video yüklenemiyorsa baştan, ortadan ve sondan ekran görüntüsü iste.

## Vazgeçilmez kurallar
- **Her ücretli adımdan önce maliyet + onay.** Harcama tavanı yok; koruma her seferinde sormaktır. Kendiliğinden ikinci ücretli deneme yok. Beğenilmeyen ama tamamlanan iş de ücretlidir.
- **Fiyatı liste başlangıcından tahmin etme.** "from $X" yalnız en ucuz ayardır; seçtiğin mod + çözünürlük + kalite + süre için fiyatı modelin sayfasından oku ya da kullanıcıya sitedeki teklifi okut. Okuyamadıysan "≈ tahmin, doğrulanmadı" de. Gerçek vakada böyle bir tahmin ≈7 kat şaştı.
- **Ölçmediğine sayı, görmediğine hüküm verme.** "Üretildi / düzeldi / tuttu" yalnız çıktıya baktıktan sonra söylenir. Bilmediğin model özelliğini ya da ayar adını uydurma.
- **Gerçek kişiler.** Fotoğraftaki kişi kullanıcının kendisi değilse (yetişkin yakını dahil), o kişinin iznini; çocuksa anne-babasının iznini her şeyden önce sor. İzni kullanıcı adına varsayma, "sen seç" cevabıyla geçme; izin ile maliyet onayı iki ayrı karardır. İzni sor; kullanıcının "izin var" demesi yeterlidir, bunu kayda yaz. Cevap "yok", "bilmiyorum" ya da izin pek olası değilse (ör. eski sevgili) üretme, o kişiyi gösteren prompt da verme; hayali bir karakter öner. Çocuk fotoğrafında modelin gerçek yüzü reddedebileceğini baştan söyle. Bir model gerçek yüzü reddederse hatayı bildir; filtreyi aşmak için dosyayı değiştirip yeniden deneme, fotoğrafı servisten servise gezdirme.
- **Sırlar.** API anahtarını, parolayı sohbete ya da kayda yazma.
- **Metin ve logoyu üretime yazdırma;** sonradan eklenir, çünkü modeller yazıyı bozar. Yazı sahnenin parçası olmak zorundaysa tam metni ver ve sonuçta harf harf kontrol et.

## Cevap biçimi
- Önce sonuç (tek cümle), sonra gerekirse gerekçe. Kısa tut. Kullanıcıya tablo gösterme, terim yığma.
- Kullanıcıdan bir seferde tek karar iste. 15 soru mesajı ve teslim paketi bu kısalık kuralının bilinen istisnalarıdır.
- Tam prompt ve ayar listesi dosyaya ya da kod bloğuna; anlatım sade kalır.

## Başvuru dosyaları
- `references/sorular.md` — her istekte, 2. adımdan önce.
- `references/gorsel-prompt.md` — görsel ya da görsel düzenleme prompt'u yazarken.
- `references/video-prompt.md` — video prompt'u yazarken.
- `references/karakter-mekan-esya.md` — tutarlı kişi/mekân/eşya, gerçek kişi fotoğrafı, çok çekimli iş.
- `references/modeller-ve-maliyet.md` — model seçmeden ve maliyet söylemeden önce.
- `references/kontrol-ve-duzeltme.md` — sonuç geldiğinde ve her düzeltmeden önce.
- `references/api-claude-code.md`, `references/api-modeller.md` ve `scripts/hf.py` — yalnız üretim biçiminde. Göndermeden önce `hf.py kontrol` (ücretsiz) gövdeyi modelin resmi alanlarıyla karşılaştırır. Bir GPT'ye ya da sohbet projesine bilgi dosyası yüklerken bu üçünü yükleme.

Model adları, fiyatlar ve site düzeni değişir: dosyadaki tarihli bilgi sitede gördüğünle çelişirse siteye güven ve farkı kullanıcıya söyle.
