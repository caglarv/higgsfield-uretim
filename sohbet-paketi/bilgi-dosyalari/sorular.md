# 15 soru — nasıl seçilir, nasıl sorulur

Üretimden önce 15 çoktan seçmeli soru sorulur. Neden: soru bedava, hatalı üretim paralı; her cevap ya prompt'a girecek bir ayrıntıyı ya da bir plan kararını (model, sıra, taslak/büyük boy) besler. İkisine de yaramayan soru sorulmaz.

## Kurallar
- **Ne istediğini sor, nasıl yapılacağını değil.** "Nerede izleyeceksin?" sorulur; "16:9 mu 9:16 mı?", "hangi model?", "kaç piksel?" sorulmaz. Model, çözünürlük ve ayarı cevaplardan sen seçersin.
- **Günlük dil.** Şıklarda terim yok; "kamera sabit dursun / yavaşça yaklaşsın" gibi.
- **Kullanıcının zaten söylediğini sorma.** O konunun yerini daha derin bir soruyla doldur (ör. mekân belliyse: mekânın saati, dağınıklığı, penceresi). Sayı 15 kalır.
- **Her soruda 2–4 şık + serbest cevap hakkı.** Uygun yerde "Sen seç" şıkkı koy; bu bir cevaptır, sonra karar senindir.
- **İlk soru çoğu zaman başlangıç malzemesidir:** elde fotoğraf/önceki görsel var mı, sıfırdan mı.
- **Önceki cevaba göre sonraki soruları uyarlat.** "İnsan yok" dendiyse kişi soruları yerine mekân/nesne ayrıntısı sor.
- **Sunum:** çoktan seçmeli soru aracı varsa onu kullan (4'erli gruplar, "(3/15)" sayacıyla). Yoksa numaralı liste yaz, şıkları a/b/c/d diye ver ve "1a 2c 3b…" gibi kısa cevap iste; 15'i tek mesajda ya da iki mesajda sor.
- **Bitince** cevapları tek satırlık özetle kayda geçir; prompt'un her bölümü bir cevaba dayansın.

## Görsel için konu havuzu
Amaç (deneme / hatıra / tanıtım / paylaşım) · konu (hayali kişi / fotoğraftaki kişi / mekân / eşya) · üslup (gerçek fotoğraf / film karesi / animasyon / resim) · nerede görülecek (telefon / ekran / kare / baskı) · kişi: yaş, cinsiyet, görünüş, kıyafet, hâl (temiz/dağınık) · kaç kişi · mekân · saat ve ışık · duygu · eylem (ne yapıyor) · kadraj (yüz / belden yukarı / tam boy / geniş) · renk havası · yazı olacak mı (varsa tam metni) · kaç seçenek görmek ister · asla olmaması gereken şey (HARD RULE adayı).
Fotoğraftan yola çıkılıyorsa ekle: fotoğraftaki kim, benzerlik ne kadar önemli, neler aynen korunacak, fotoğrafı kullanma izni var mı (başkası/çocuk ise). Fotoğraf siyah-beyaz ya da soluksa saç, göz ve ten rengini de sor. Fotoğraf henüz eklenmediyse sorularla birlikte yüklenmesini iste.

## Video için konu havuzu
Başlangıç (hangi görselden / sıfırdan) · bu sürede ne olsun (olay sırası: önce ne, sonra ne) · nasıl bitsin (son kare) · süre · tek çekim mi birkaç çekim mi · kamera hissi (sabit / yaklaşan / takip / elde) · hareketin türü ve hızı · kişi yerinde mi kalır, gezinir mi · konuşma var mı, hangi dilde, tam replik · ses (sessiz / ortam / müzik; müzik sonradan mı) · nerede izlenecek · amaç (öğrenme denemesi / paylaşılacak kalite) · gerçekçilik düzeyi · ışık video boyunca değişir mi · saç-kumaş hareketi · kaç deneme · asla olmaması gerekenler (yüz değişmesi, bozuk beden, kesme, odada değişiklik…).

## Çok parçalı iş (tanıtım filmi, kısa film) için ek konular
İzleyici kim · tek cümlelik ana fikir · toplam süre ve bölüm sayısı · tekrar eden kişiler/mekânlar/eşyalar (her biri için referans var mı) · müzik önce mi seçilecek · bütçe yolu (önce kaç ucuz taslak) · teslim biçimi.
Bu işlerde 15 soru işin bütünü için sorulur; çekime özel eksik ayrıntı kalırsa yalnız o sorulur.

## Düzeltme turu
Var olan bir çıktı düzeltilirken ("şunu değiştir, gerisi aynı") 15 soru sorulmaz; yalnız eksik kalan sorulur. Eksik olmaya aday konular: tam olarak ne değişecek (belirsizse) · neler aynen korunacak (kullanıcı söylemediyse önceki "tuttu" listesini say ve onaylat) · değişikliğin ölçüsü ya da yönü (ör. dönüş hangi tarafa, ne kadar). Hiçbiri eksik değilse soru sormadan sahne tarifine geç. Zorlama soru sorma: 15'i doldurmak için sorulan soru kullanıcıyı yorar ve cevabı prompt'a girmez.
