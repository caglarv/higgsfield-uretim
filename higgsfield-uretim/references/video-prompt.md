# Video prompt'u nasıl yazılır

Okuyucu: bir kullanıcı için video üretim prompt'u yazacak yapay zekâ.
Prompt'un kendisi İngilizce yazılır; bu rehber Türkçedir. Bölüm başlıkları ve tırnak içindeki İngilizce parçalar prompt'a olduğu gibi girebilir.

## İçindekiler
1. Temel ilkeler
2. Bölüm iskeleti (FORMAT → HARD RULE)
3. Çekim boyutu, açı, kamera hareketi sözlüğü
4. Zamanlama ve vuruşlar
5. Referans rolleri
6. Konuşma ve ses
7. Süreklilik kilitleri, yön ve sayıyla kilitleme
8. UGC (telefonla çekilmiş) tarzı
9. Üretilen videoyu karelerden kontrol
10. Düzeltme ve ön kontrol listesi

---

## 1. Temel ilkeler
- **Önce varlıklar, sonra sahne.** Kişi, mekân ve eşya için ayrı, düzeltilmiş referans görseller hazırlanır; video bunları kullanır. Neden: video modeli kimliği referanstan alır; referans zayıfsa prompt bunu kurtaramaz.
- **Görsel görünüşü verir; prompt sahipliği, konumu ve eylemi verir.** Kimin ne yaptığını, eşyanın kimin elinde ve hangi yönde durduğunu her zaman yaz.
- **Somut ve sayılı yaz.** "Biraz", "hafif", "yakın" gibi gevşek kelimeler yerine metre, saniye, sayı, kadraj sınırı ver. Neden: gevşek ifadeyi model kendi yorumuyla doldurur (bkz. §7'deki deneme dersi).
- **Az kadro, az olay.** Kısa videoda bir ana eylem, bir duygu değişimi ve okunur bir son. Neden: çok vuruş acele ve birbirine karışmış hareket üretir.
- **Aynı prompt her seferinde farklı video verir.** Tek denemenin kusursuz olmasını bekleme; farklı denemelerin en iyi parçaları kurguda birleştirilebilir.
- **Önce ucuz taslak, beğenilirse büyük boy.** Neden: yanlış yön ucuzken yakalanır.
- **İlk karede olmayanı video zor uydurur.** Görselden videoda ışık, kıyafet ve mekân ilk kareden gelir; ilk karede yüzde güneş yoksa "yüzüne güneş vursun" isteği tutmayabilir. Böyle bir istekte önce ilk kareyi düzeltmeyi (görsel düzenleme) öner. (≈ çıkarım; denenmedi.)

## 2. Bölüm iskeleti
Her bölüm ayrı satır/başlık; İngilizce. Kullanılmayan bölümü sil, boş bırakma.
1. **FORMAT** — toplam süre, en-boy, kaç çekim, kesmeler saniyesiyle ("Shot 1: 0–3s, hard cut, Shot 2: 3–6s"), gerçek zamanlı mı. Tek çekimse "one continuous shot, zero cuts". Neden: "tek kesme" ile "sıfır kesme" karışabilir; sayı belirsizliği kaldırır.
2. **START FRAME** (görselden videoda) — "the input image is the exact first frame" + ilk karede kim, ne giyiyor, nerede.
3. **REFERENCE ROLES** — her referansa TEK görev (§5).
4. **LOCATION / SETTING** — mekân, kim karenin neresinde (sol/orta/sağ, yaklaşık yüzde), kameraya uzaklık.
5. **CAMERA + OPTICS** — çekim boyutu, yükseklik, açı, hareket (dört satır, §3), objektif; açık yasaklar ("does not pan, does not zoom, never crosses to the other side").
6. **ACTION TIMING** — "Beat 1 (0–2s): …" sırayla; her vuruşta kim, ne, hangi yöne (§4).
7. **DIALOGUE** — tam replikler tırnak içinde, kim söylüyor, dil, "no other speech" (§6).
8. **PHYSICS / SECONDARY MOTION** — saç, kumaş, eşya gecikmeli sallanır; nesne ışınlanmaz, yerinde kalır.
9. **LIGHTING** — tek ana kaynak, yönü çekim boyunca sabit; ışığın nereye düştüğü.
10. **COMPOSITION** — konu tam ortada değil; tek doygun renk vurgusu; çizgiler bakışı ana eyleme götürür.
11. **VISUAL STYLE** — üslup referanstan gelir; kelimeyle yalnız görünür özellik ekle. Animasyon üslubunda gerekirse "animate on twos".
12. **AUDIO** — yalnız sahnedeki sesler / sessiz; müzik sonradan eklenecekse "no music".
13. **CONTINUITY LOCKS** — kişi sayısı, kimlik, uzuv sayısı, eşyanın eli ve yeri, kameranın ekseni, kadraj sınırı; olumlu cümleyle (§7).
14. **HARD RULE (HIGHEST PRIORITY)** — en sık bozulan ya da en önemli TEK kural, büyük harfle, en sonda. Neden: modelin öncelik vereceği tek şeyi açıkça işaretler; birden fazla "en önemli" kural önceliği sulandırır.
- Kısa ve basit işlerde 5 parçalık sade iskelet de yeter: özne → mekân → olaylar (sırayla, sonu dahil) → kamera → ışık + ses.

## 3. Çekim boyutu, açı, kamera hareketi sözlüğü (kısa)
Üç ayrı karar, karıştırma: **BOYUT** (ne kadarı görünür) · **AÇI** (nereden bakılır) · **HAREKET** (kamera değişir mi).
- **Boyut (kadraj sınırıyla yaz):** extreme wide · wide · full shot (baş ve ayak kadrajda) · medium wide (baştan dize) · cowboy (uyluk ortası, eller görünür) · medium (bel üstü; diyalog için başlangıç) · medium close-up (göğüs üstü) · close-up (yüz baskın) · extreme close-up (göz, parmak).
- **Açı:** eye level (tarafsız) · high angle (kişi küçük, korunmasız) · low angle (heybetli) · top-down (harita gibi) · Dutch (eğik ufuk, huzursuzluk).
- **Hareket:**
  - locked-off / static (kilitli, tripod gibi) · pan (yerinde yatay dönüş) · tilt (yerinde yukarı/aşağı bakış; kamera yükselmez)
  - pedestal / crane (kamera yükselir/alçalır) · dolly in/out (kamera fiziksel olarak ilerler/geri çekilir) · zoom (kamera yerinde, kadraj daralır)
  - truck / slider (yana kayma, paralaks) · tracking (yürüyenin yanında aynı hızda) · follow (arkasından) · reverse tracking (önünde geri geri)
  - arc / orbit (konunun etrafında kavis) · handheld (hafif doğal kayma) · whip pan (hızlı savrulma, bulanıklık, sonra net kare) · push past (ön plandaki nesnenin yanından geçip içeri)
- **Hareketi dört satırla yaz, önce hareket sonra sahne:** "Movement: … Speed: … Framing: … End: …". Neden: hareketin NEREDE BİTECEĞİ ve ne sabit kalacağı yazılmazsa model durmaz ya da başka yöne kayar.
  - Kendi örneğin: "Slow dolly in. Movement: the camera moves straight toward the grandfather on the bench. Speed: gentle and steady. Framing: height and direction stay the same; he stays centred-left. End: a medium close-up of his face."
- **İlk denemede tek kamera değişikliği.** Neden: istenmeyen pan/zoom çıkarsa nedeni ancak böyle anlaşılır.
- **Arc/orbit'te ilk denemede konu yerinde dursun**, kendisi dönmesin. Neden: iki dönüş birden kimlik ve yön hatası üretir.
- **Yakın çekim**, öncesinde neye tepki verildiğini gösteren geniş çekim varsa daha etkilidir.
- **Eksen kuralı:** çok çekimli sahnede kamera hep aksiyon çizgisinin aynı tarafında kalır; ekran yönü (kim solda, kim sağda, hangi yöne gidiyor) sabit. Neden: taraf değişirse izleyici yönü kaybeder.

## 4. Zamanlama ve vuruşlar
- **Sıra:** başlangıç durumu → görünür değişiklikler sırayla → son kare. Son karede ne olacağını mutlaka yaz ("the clip ends while she is mid-spin, still smiling"). Neden: sonu yazılmayan video rastgele bir hareketle kapanır.
- **Her vuruş = saniye aralığı + kim + görünür eylem + (varsa) kamera + (varsa) replik.** Her vuruşun başında eylemi yapanı adıyla an. Neden: birden fazla kişide model eylemi yanlış kişiye verir.
- **Son vuruşun bitiş saniyesi = seçilen süre.** Süre değişirse TÜM vuruşları yeniden böl; yalnız sonuncuyu kırpma. Önce konuşmayı kısalt, sonra vuruş çıkar.
- **Küçük oyunculuk büyük tepkiden önce gelir** (önce bakış, sonra gülümseme, sonra kahkaha). Neden: ani büyük tepki yapay görünür.
- **Zaman damgaları hedeftir, garanti değil.** Kritik anın etrafına pay bırak; eylem, konuşma ve son bekleme için süre ayır.
- **Hız:** 5 saniyeye 2–3 vuruş, 15 saniyeye en fazla 5–6 vuruş makul (≈ tahmin). Vuruşlar acele çıkarsa vuruş sayısını azalt.
- **Çok çekimde** her kesmeye yeni çekim numarası, her çekime boyut + açı + başlangıç-bitiş saniyesi; "hard cut" açıkça yazılır.
- **Ara eylemi yazılı tut.** Yardımcı yapay zekâlar sahneyi sadeleştirirken ara adımları atabilir (ör. "ışıkları tek tek söndürür" → "son ışığı söndürür"); göndermeden önce fikirle karşılaştır.

## 5. Referans rolleri
- **Her referansa TEK görev:**
  - KİŞİ referansı = kimlik + kıyafet. "Use Image 1 only for her face, hair and clothes; do not copy its background or pose."
  - MEKÂN referansı = alan, ışık, renk. Kadrajı ayrıca yaz.
  - EŞYA referansı = şekil, renk, ayrıntı. Kimin taşıdığını, nerede durduğunu, yönünü yaz.
  - Hareket referansı (video) = yalnız hareket; "copy only the movement, not the person or the background".
- **Kişiyi, mekânı ve eşyayı videoya AYRI referans olarak ver;** önce kişiyi mekâna yapıştırıp tek görsel yapma. Neden: birleşik görselde hata varsa video onu kilitler; ayrı referansla model kişiyi mekânın ışığına doğal yerleştirir. (Görselden videoda ilk kare zaten birleşik sahnedir; bu durumda START FRAME bölümü yeterli.)
- **Numara o prompt'a özeldir.** "Image 1" her prompt'ta yeniden tanımlanır (yükleme sırasıyla); yazılan etiket tek başına referans eklemez, dosya ayrıca verilmelidir. `@` etiketi yalnız aracın desteklediği yerde işe yarar.
- **Çelişkide öncelik:** kullanıcı kısıtı > kişi kimliği > eşya > kompozisyon > mekân > üslup.
- **Video karakter kartı** (kısa konuşma + kişinin etrafında 360° kamera turu) sonraki sahnelerde yüz, ses ve tavır referansı olabilir. DOĞRULANMADI: bizde denenmedi.

## 6. Konuşma ve ses
- **Replikler tam metin, tırnak içinde, kimin söylediği ve dili ile:** "Grandmother (Turkish): "…"". Sonuna "no other speech". Neden: model eksik repliği kendi uydurur.
- **15 saniyeye ≈ 4–6 KISA replik.** Kısaltma gerekiyorsa kelime değil cümle çıkar.
- **Her replik ekrandaki bir harekete denk gelsin** (replik söylenirken eşyayı kaldırır, gösterir). Neden: hareketsiz konuşma donuk görünür.
- **Konuşmanın tonunu replik yanına yaz** (gülerek, fısıldayarak); vurgulu tek kelimeyi büyük harfle yazmak bir yöntemdir (UGC becerisi); etkisi ölçülmedi.
- **Son replik kesmeden ya da videonun sonundan önce bitsin;** sonda kısa bir sessiz bekleme bırak.
- **AUDIO:** yalnız sahnedeki sesleri say (ayak sesi, kuş, çaydanlık). Müzik kurguda eklenecekse "no music"; altyazı istenmiyorsa "no subtitles". Neden: model kendiliğinden müzik ve yazı ekleyebilir.
- **Konuşan kişi videosu:** modelin ürettiği ses kişinin kendi sesi değildir (kullanıcıya baştan söyle); dudak uyumu ve Türkçe telaffuz DOĞRULANMADI — kısa bir taslakla dene. Kişinin gerçek sesi gerekiyorsa sesi ayrı kaydedip kurguda eklemek daha güvenilir.
- Müzikli işlerde müzik önce gelir, kurgu vuruşlara göre yapılır; müzik prompt'una saniyeli bölüm listesi yazma (bir örnekte istenen sürenin neredeyse iki katı döndü). Dönen sesin süresini ölç.

## 7. Süreklilik kilitleri, yön ve sayıyla kilitleme
**Genel kilitler:** tek kişi / tam N kişi; aynı yüz ve kimlik baştan sona; iki kol, iki bacak, her elde beş parmak; eşya hangi elde; mobilyalar yerinde; yeni kişi, yazı, logo yok. Önce olumlu cümleyle yaz ("the cat stays inside the basket"); hata sürerse adı konmuş açık yasak ekle. Hangisinin daha iyi uygulandığı kaynaklarda çelişkili — DOĞRULANMADI.

**Ders A — yön (sağ/sol, dönüş) yazıyla güvenilir verilemez; ekrana + nesneye göre yaz, kesin olacaksa resimle göster (iki gerçek deneme + araştırma, 2026-11-16).**
- Ne oldu: v1'de "half turn toward the window on the left" → kameraya sırtını döndü. v2'de "turns 90 degrees to HER RIGHT (camera-left), toward the window" → yine ters tarafa (kameranın sağına) döndü, başını omzunun üstünden pencereye çevirdi. Aynı v2'de sayıyla yazılan konum kilidi TUTTU.
- Neden: video modelleri sağ/sol kelimesini neredeyse ayırt edemiyor (araştırmalarda belgeli; hareket yönü testlerinde en iyi modeller ≈%42–47 doğru). Görüntü modelleri "onun sağı"nı çoğunlukla izleyicinin sağı diye okuyor; "HER RIGHT" ile "camera-left" aynı cümlede çelişen iki işaret oldu. Konum tuttu, çünkü onu başlangıç karesi zaten gösteriyordu; dönüş yalnız yazıyla anlatılan şeydi.
- Yazıyla yapılacaksa (denenmemiş, kaynakların ortak önerisi):
  - Kişinin sağı/solu YAZMA; tek bir çerçeve kullan: ekran ("the left side of the frame") ve görünen bir nesne ("toward the bright window on the left side of the frame"). Derece ve büyük harfli RIGHT/LEFT yok.
  - Hareketi değil SONU yaz: "ends in profile facing the window, sunlight on her face; her back is never toward the camera".
  - Yön cümlesi prompt'un başına yakın ve bir kez; uzun kural listesi yön cümlesini boğar. Klip başına tek ana hareket.
- Yön işin özüyse yazıya güvenme, GÖSTER:
  1. Bitiş karesi: başlangıç karesini düzenleme modeliyle istenen son poza getir (yalnız pozu değiştir, yüz/kıyafet/oda/kadraj aynı), yönü gözle onayla, sonra bitiş karesi destekleyen moda ver (`api-modeller.md` §2). Gidip dönen hareket için iki kısa klip zinciri: A önden→profil, B profilden→öne.
  2. Hareket kopyalama: gerçek bir kişinin aynı hareketi yaptığı kısa video + Kling 3.0 Motion Control (`character_orientation: video`). Video ters yöndeyse yatay aynala.
  - Başarı oranları ölçülmedi; ucuz ayarda dene. Aynalama hilesi (başlangıç karesini çevir, üret, sonucu geri çevir) yalnız modelin sabit bir yön eğilimi varsa işe yarar — denenmedi.
- Işık yönü de aynı kurala uyar: "the window light comes from the left side of the frame".

**Ders B — gevşek ifade yetmez, SAYIYLA kilitle; en önemlisini HARD RULE'a koy (gerçek deneme, 2026-11-16).**
- Ne oldu: "stays in the same spot, at most one small step" yazıldı; kadın dans ederken kameraya ≈1 m yaklaştı, son karelerde ayakları alt kenarda kesildi, tam boy kadraj bozuldu.
- Neden: "yerinde", "küçük adım" ölçü değildir; dans gibi canlı eylemde model kişiyi serbestçe hareket ettirir.
- Çare: konumu ölçülebilir şeylere bağla:
  - "the distance between her and the camera stays 3.5 m for the entire shot"
  - "her feet stay on the rug / within the same two floorboards"
  - "her head and both feet are fully visible in EVERY frame, with floor visible below her feet"
  - kamera kilitliyse "camera locked, does not move or zoom" ile birlikte yaz.
- En kritik kilit HARD RULE'a girer, büyük harfle: ör. "HARD RULE (HIGHEST PRIORITY): HER FULL BODY, HEAD TO FEET, STAYS INSIDE THE FRAME IN EVERY FRAME; SHE NEVER MOVES CLOSER TO THE CAMERA." Denemede HARD RULE yüz kimliğine ayrılmıştı ve yüz tuttu; konum kuralı yalnız sıradan satırdaydı ve bozuldu.
- Denendi (v2, 2026-11-16): sayıyla yazılıp HARD RULE'a konan konum/kadraj kilidi tuttu — kameraya yaklaşmadı, baş ve ayaklar her karede göründü. Tek deneme.

**Sorunu adlandıran bölüm:** bir hata her denemede tekrarlıyorsa prompt'a ona özel kısa bir bölüm ekle ("CRITICAL — this keeps going wrong: …") ve hatayı kare kare, sayıyla tarif et.

## 8. UGC (telefonla çekilmiş) tarzı
- **Kamera görünmezliği en üste:** "The recording phone IS the camera and is never visible in the frame." Hook vuruşunda tekrar et. Neden: modeller kişinin eline ikinci bir telefon koymayı sever.
- **Tek fiziksel kamera düzeni seç ve elleri ona göre dağıt:**
  - selfie: bir el kadraj dışındaki telefonda, diğer el eşyada;
  - arkadaş çekiyor: iki el serbest, kamera hareketi küçük ve eyleme bağlı;
  - telefon bir yere dayalı: kamera sabit, iki el serbest.
  - Her kamera değişikliğinin fiziksel nedeni olsun (telefonu rafa dayar, kare sallanır, sonra sabitlenir). Kendi çeken birinde görünmez dolly/vinç hareketi yazma.
- **İskelet:** teknik + dünya kuralları (kamera tarzı, en-boy, görünmezlik, mekân + ışık) → karakter bloğu (referansa kilitli görünüş + göz kırpma cümlesi) → zaman damgalı vuruşlar ("HOOK (0–2s): …", "(2–5s): …") → isteğe bağlı kapanış çağrısı → stil satırı (konuşma enerjisi, duygu yayı, ışık özeti, cilt, telefon kalitesi).
- **Hook = selamlama değil, görsel olay + duygu sıçraması** (eşyayı lense yaklaştırıp sonra tepkiyi göstermek gibi).
- **Göz kırpma:** "blinks naturally throughout" + bir vuruşa açık bir göz kırpma. Neden: aksi halde sabit, yapay bir bakış çıkar.
- **Cilt ve görüntü:** doğal rötuşsuz cilt, mekânın ışığına uygun; güzellik filtresi yok; abartılı kumlanma ya da sürekli odak kayması efekti ekleme.
- **Duygu yayını adlandır** (ör. merak → sevinç) ve her duyguya bir beden hareketi eşle. Neden: tek donuk ifade yerine bir gelişim oynanır.
- **Olmayan özellik ya da kanıtsız iddia yazma** (dayanıklılık, popülerlik, "link bio'da"); çağrı yalnız kullanıcı hedefi verdiyse.
- **Kol mesafesinden profil dönüşü** selfie'de sık bozulur; arkadaş çekiyor ya da sabit telefon düzenine geç.

## 9. Üretilen videoyu karelerden kontrol
Video izlenemiyorsa karelere bakılır; bunu kullanıcıya açıkça söyle. Ses karelerden kontrol edilemez.
- **Teknik ölçüm:** gerçek süre, çözünürlük, kare hızı; kesme taraması (tek çekim istendiyse kesme sayısı 0 olmalı); siyah ya da donmuş kare var mı.
- **Kare çıkarma:** yalnız ilk ve son kareye bakma; zamanlama ancak videonun tamamından sık aralıkla (≈ saniyede 2 kare) çıkarılan ızgarayla anlaşılır. Kritik anlarda (vuruş geçişleri, son kare) tam boy kare de al.
- **Dört kontrol:**
  - MEKÂN: tarif edilen gibi mi, eşyalar yerinde mi, yeni kişi/eşya çıktı mı?
  - KİŞİ: ilk karedeki ya da referanstaki kişiye benziyor mu; beden, eller, uzuv sayısı her karede doğru mu?
  - EYLEM: doğru kişi, doğru eylemi, doğru sırada ve yönde yaptı mı (dönüş kameraya göre doğru tarafa mı)?
  - KAMERA + SON: kadraj kuralı her karede tuttu mu (baş/ayak kesilmesi), kamera istenmeden kaydı mı, son kare istenen anda mı?
- **Raporu iki listeyle yaz:** TUTTU / TUTMADI, her madde için saniye ve kare. Neden: düzeltmede neyin korunacağı da bilinmeli.
- **Yeni deneme, düzeltmediğin ayrıntıları da değiştirebilir;** her denemede kişi, kıyafet, mekân, eylem, kamerayı yeniden kontrol et.

## 10. Düzeltme ve ön kontrol listesi
**Karar:** aynı hata her denemede tekrar ediyor mu?
- EVET → istenmeyen görünüş referans görselde zaten varsa GÖRSELİ düzelt; yanlış kişi eylem yapıyorsa, eşya yanlış yerdeyse ya da kamera talimatları çelişiyorsa PROMPT'u düzelt.
- HAYIR → tek seferlik olabilir; yeni deneme yap, eskisini sakla, karşılaştır. "Daha dinamik yap" ya da "tekrar üret" daha iyisini garanti etmez.
- **Düzeltme notu = SORUN + İSTENEN + KORUNACAKLAR.** Çalışan cümlelere dokunma: yalnız ilgili bölümü değiştir ya da hatayı adlandıran yeni bir bölüm ekle, etkilenen satırları uyumlu güncelle. Çıktı olarak yine TAM prompt'u ver (fark listesi değil), çünkü gönderilecek olan tam metindir. Birden çok hata varsa: en ağırı HARD RULE'a, diğerleri ayrı "CRITICAL — …" bölümlerine; HARD RULE tek kalır. Yeni sürüm eski kısıtları bozmuş mu kontrol et. Aynı çıktı için en fazla 2 taslak (2 ücretli istek); çalışan bir taslak yeterlidir.

**Göndermeden önce:**
- [ ] FORMAT: süre, en-boy, çekim sayısı, kesmeler saniyeyle; tek çekimse "zero cuts" var mı?
- [ ] Her referansın tek görevi yazılı mı; ilk kare tanımlı mı?
- [ ] Kamera: boyut + açı + hareket; hareketin bitişi ve sabit kalacaklar yazılı mı?
- [ ] Vuruşlar saniyeli, eylemi yapan adıyla, son vuruş = toplam süre, son kare tarif edilmiş mi?
- [ ] Yön ekrana ve görünen bir nesneye göre, bitiş pozuyla mı yazıldı (kişinin sağı/solu yok)? Yön işin özüyse bitiş karesi ya da hareket kopyalama seçildi mi?
- [ ] Konum ve kadraj sayıyla mı kilitli (kameraya uzaklık, ayak/baş her karede görünür)?
- [ ] Replikler tam, tırnak içinde, "no other speech"; ses/müzik talimatı açık mı?
- [ ] CONTINUITY LOCKS olumlu cümleyle mi?
- [ ] HARD RULE tek ve en kritik kural mı, büyük harfle en sonda mı?
- [ ] UGC ise: kamera görünmezliği en üstte, el dağılımı, göz kırpma, kanıtsız iddia yok mu?
