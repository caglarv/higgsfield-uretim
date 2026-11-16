# Üretilen görsel ve videoyu denetlemek, kötü sonucu düzeltmek

Bu rehber, üretilen bir görsel ya da videonun nasıl denetleneceğini ve sonuç kötüyse ne yapılacağını anlatır. Okuyucu: aile fotoğraflarından görsel, tanıtım videosu ya da kısa film planlayan bir yapay zekâ. Prompt'lar İngilizce yazılır; aşağıdaki İngilizce parçalar prompt'a olduğu gibi konabilir.

**İçindekiler**
1. Temel ilkeler
2. Görseli denetlemek
3. Videoyu denetlemek
4. Düzeltme notu: SORUN + DEĞİŞİKLİK + KORUNACAKLAR
5. Karar ağacı: görseli mi, prompt'u mu düzelt, yoksa yeniden mi üret?
6. Prompt'u düzeltme teknikleri (hatayı adlandır, sayıya çevir, kilitler)
7. Kaç deneme? Ne zaman durmalı?
8. Kurguda kurtarma
9. Sürüm saklama
10. Gerçek denemeden iki vaka (2026-11-16)

---

## 1. Temel ilkeler

- **Ucuz taslak → onay → büyük boy.** Her kontrol kapısı bir sonrakinden ucuzdur, çünkü yanlış yön ucuzken yakalanırsa pahalı üretim boşa gitmez.
- **Üretmeden önce prompt'u okuyun** ve fikirle karşılaştırın, çünkü yardımcı/model ara adımları sessizce atlayabilir (ör. "ışıkları tek tek söndürür" yalnız "son ışığı söndürür" olabilir).
- **Aynı prompt her seferinde farklı sonuç verir.** Bu yüzden onaylanan prompt sonuçla birlikte saklanır ve "bir kez daha üret" daha iyisini garanti etmez.
- **Yeni üretim, düzeltmediğiniz ayrıntıları da değiştirebilir.** Her yeni sürümde her şey (kişi, kıyafet, mekân, eylem, kadraj, ışık, ses) baştan kontrol edilir, yalnız düzeltilen yer değil.
- **Bakmadığınızı "tamam" saymayın.** Küçük önizlemede bakıldıysa bunu söyleyin; video izlenemiyorsa karelere bakıldığını söyleyin, çünkü küçük boyda görünmeyen kusur büyük boyda çıkar.
- **Seçim ölçütü:** en gösterişli sonuç değil, sahnenin ve kullanıcının ihtiyacına en uygun olan.

## 2. Görseli denetlemek

Önce tam boyda genel bakış, sonra **büyütüp** bölge bölge bakın.

- **İsteğe uygunluk:** kadraj sınırı (tam boy istendiyse baş VE ayaklar içeride mi, kenara yapışık mı), kişi sayısı, kıyafet rengi ve parçaları, mekân, günün saati, ışık yönü — prompt'u satır satır görselle eşleyin, çünkü "genel olarak benziyor" hissi tek tek maddeleri gizler.
- **Kimlik:** yüz referansa benziyor mu; yaş doğru görünüyor mu; gerçek kişi kaynaksa kaynak fotoğrafla yan yana.
- **İstenmeyen eklemeler:** dövme, takı, gözlük, yazı, logo, filigran, giysideki küçük yazılar, fazladan kişi, yansımadaki insan şekli.
- **Anatomi:** eller ve parmak sayısı, kulaklar, dişler, boyun-omuz bağlantısı, birbirine karışan uzuvlar.
- **Düşük kalite ("yapay görünüm") işaretleri — büyütünce:**
  - Aşırı keskin, plastik ya da "render" gibi yüzeyler; rötuşlanmış, gözeneksiz cilt.
  - İstenmeyen kumlanma ya da gürültü.
  - Tekdüze tekrar: aynı şekil, ölçek ve aralıkta yinelenen nesneler (tuğla, yaprak, kalabalık yüzleri).
  - Dikkati dağıtan parlak yansımalar.
  - Bükülmüş düz çizgiler (kapı kasası, raf, ufuk).
- **Eşya sadakati:** gerçek bir eşya/ürün kaynaksa kontur, desen, renk ve küçük ayrıntılar orijinalle karşılaştırılır; fonun dokusu nesnenin içine sızmış mı (ör. masa deseni camın içinde).
- **Yeni açı/düzenlemede süreklilik:** orijinalde olmayan, yeni icat edilmiş ayrıntı var mı; korunması istenen her şey yerinde mi.
- **Teknik:** çıkan boyut ve en-boy oranı istenenle aynı mı, çünkü bazı üretimler farklı boyutta döner ve kurguya oturmaz.

## 3. Videoyu denetlemek

İlk ve son kare yetmez, çünkü zamanlama hataları ortada olur. **Videonun tamamından sık aralıkla kare çıkarın** (ör. saniyede 2 kare bir ızgara + kritik anlarda tam boy kareler) ve sırayla bakın; mümkünse ayrıca normal hızda izleyin.

**Dört ana kontrol:**
- **MEKÂN:** tarif edilen yer mi; eşyalar yerinde mi, kaybolan/beliren nesne var mı; yeni kişi girdi mi.
- **KİŞİ:** baştan sona aynı kişi mi (yüz ortada kayabilir); kıyafet sabit mi; beden ve eller düzgün mü; oyunculuk istenen gibi mi.
- **EYLEM:** doğru kişi doğru eylemi doğru sırayla yaptı mı; yön doğru mu (kameraya göre sol/sağ); kişi istenen yerde kaldı mı, kameraya yaklaştı/uzaklaştı mı.
- **SON:** son kare, sürpriz ya da son replik istenen anda mı; video eylem bitmeden kesiliyor mu.

**Ek kontroller:**
- **Kamera:** istenmeyen pan, zoom, kayma var mı; kadraj önemli eylemi gösteriyor mu; tam boy istendiyse ayaklar her karede içeride mi.
- **Kesme sayısı:** "tek kesintisiz çekim" istendiyse sıfır kesme olmalı; çok çekim istendiyse kesmeler doğru saniyede mi. Ani görüntü değişimlerini otomatik bir sahne-değişimi taramasıyla da sayın, çünkü hızlı kesme gözle kaçabilir.
- **Süre:** dönen dosyanın süresini her zaman ölçün; istenen süreden farklı dönebilir.
- **Hız:** istenmeyen ağır çekim ya da "süzülen, rüya gibi" hareket, ya da tersine aceleye gelmiş vuruşlar.
- **Süreklilik izleri:** boya, ıslaklık, leke gibi izler kendiliğinden kayboluyor ya da sırasız beliriyor mu.
- **Ses (açıksa):** istenmeyen müzik sızdı mı; ses eyleme uyuyor mu; replik kesmeden önce bitiyor mu; siyah kare ya da ses seviyesi sorunu var mı.
- Bulguları **TUTTU / TUTMADI** diye iki listeye yazın, çünkü düzeltmede korunacaklar TUTTU listesinden çıkar.

## 4. Düzeltme notu: SORUN + DEĞİŞİKLİK + KORUNACAKLAR

Para harcamadan önce önce metni düzeltin. Not üç parçadan oluşur:

- **SORUN:** gözlenen hata, somut ve ölçülebilir ("2.–4. saniyede kameraya sırtını dönüyor", "ayaklar son 1 saniyede alt kenarda kesiliyor").
- **DEĞİŞİKLİK:** tek, dar bir talimat ("yalnız kadrajı geri çek"), çünkü geniş talimat ("daha iyi yap", "daha dinamik") modelin fazlasını değiştirmesine yol açar.
- **KORUNACAKLAR:** TUTTU listesinin tamamı, tek tek ("aynı kadın, yüz, kıyafet, oda, eşyalar, pencere, ışık").

Görsel düzenlemede kalıp:
- `Edit this image. Keep everything exactly the same: [list]. Change ONLY: [one change]. Nothing else is added, removed or redesigned.`

Bir yardımcı yapay zekâdan prompt düzelttirirken verilecek kalıp:
- Test edilen prompt'un **tamamı** + ne yanlış gitti + ne isteniyor + "işe yarayanları koru, etkilenen her satırı uyumlu güncelle, tam prompt'u ver, neyi neden değiştirdiğini listele".
- Dönen değişiklik listesini okuyun: istenmeyen eylem, kamera ya da sahne öğesi eklenmiş mi; eski bir kısıt gevşemiş mi (ör. "sıfır kesme" "tek kesme"ye dönmüş mü).

## 5. Karar ağacı: görseli mi, prompt'u mu düzelt, yoksa yeniden mi üret?

**Soru 1 — Aynı hata her denemede tekrar ediyor mu?**
- **HAYIR (tek seferlik):** büyük olasılıkla rastgele kusur.
  - Sorun küçük ve yerelse (dövme, bir eşya, kadraj) → **düzenleme (edit)** ile o noktayı düzelt.
  - Sorun bütüne yayılmışsa → aynı prompt'la **yeni deneme**; eskisini sil**me**, ikisini baştan sona karşılaştır.
- **EVET (tekrar ediyor):** sebebi girdide ara, yeniden üretmeye para harcama. **Soru 2'ye geç.**

**Soru 2 — İstenmeyen şey referans görselde zaten var mı?**
- **EVET** (referansta dövme, yanlış renk, yanlış saç) → **görseli düzelt** (referansı düzenle ya da değiştir), kelimeyle silmeye çalışma, çünkü model görseldekini prompt'taki yasaktan daha güçlü taşır.
- **HAYIR → Soru 3.**

**Soru 3 — Hata prompt'tan mı geliyor?** Şunlara bakın:
- Eylemi yanlış kişi yapıyor → eylemi yapanı adıyla yaz.
- Sıra yanlış → adımları numaralı ve saniyeli yaz.
- Yön yanlış → yönü **kameraya göre** yaz.
- Eşya yanlış yerde/yönde → sahibini, yüzeyini ve yönünü yaz.
- Kamera talimatları çelişiyor → çelişen satırları uyumlu hâle getir; ilk testte tek kamera hareketi bırak, çünkü istenmeyen hareketin hangi satırdan geldiği ancak böyle anlaşılır.
- Belirsiz ifade ("biraz", "yakın", "küçük bir adım") → **sayıya çevir** (bölüm 6).
- Bunlardan biri varsa → **prompt'u düzelt**, sonra tek yeni deneme.

**Soru 4 — Prompt ve referanslar doğru görünüyor ama hata sürüyor mu?**
- Hatayı **adlandıran** kilit bölümü ekle (bölüm 6).
- Eylemi sadeleştir: gösterişli/karmaşık hareketi daha basit, gündelik harekete çevir; süre ver ya da vuruş sayısını azalt.
- Yine olmuyorsa: bu çekimden vazgeçip kurguda kurtar (bölüm 8) ya da sahneyi başka bir çekimle anlat.

## 6. Prompt'u düzeltme teknikleri

**Baştan yazmayın.** Usta örneklerde kötü denemeden sonra prompt baştan yazılmıyor; hatayı adlandıran tek bölüm ekleniyor, geri kalan cümlelere dokunulmuyor, çünkü her yeniden yazım çalışan kısımları da riske atar. (Gönderilen metin yine tam prompt'tur; "baştan yazma" = çalışan cümleleri değiştirme.) Birden çok hata varsa en ağırı HARD RULE'a, diğerleri ayrı adlandırılmış bölümlere gider.

- **Hatayı adlandıran bölüm, kural başlıkta.** Başlığın kendisi kuralı söyler; gerekirse "neden" de eklenir:
  - `TURNS TO HER RIGHT — FACE STAYS VISIBLE — CRITICAL:`
  - `NO TEARS — CHEEKS STAY DRY`
  - `ALREADY STANDING — SHE DOES NOT STAND UP`
  - `CRITICAL — BECAUSE THIS KEEPS GOING WRONG:` + hareketin fiziksel sırası (1)(2)(3), kameraya göre.
- **"Başarısız çekim" cümlesi:** en kritik kuralın sonuna `If X happens, the shot has failed.` — modele önceliği açıkça söyler.
- **Belirsizliği sayıya çevirin:**
  - "kameraya yaklaşmaz" → `distance to camera stays 3.5 m for the whole shot`
  - "yerinde dans eder" → `feet stay inside the rug; feet visible in every frame`
  - "başını kaldırır" → `raises her head over 1.5 seconds`
- **Yönü kameraya göre yazın:** "pencereye döner" değil, `turns to HER RIGHT, ending in profile to camera`; çünkü model "pencereye doğru"yu kendi bakış noktasına göre yorumlayabilir. Gerekirse referans görselin üzerine **ok çizerek** bakış/hareket yönü gösterilir.
- **Sık sızıntılar için hazır kilitler** (gerekeni baştan şablona koyun):
  - Hız: `real-time speed, no slow motion, no speed ramps; if it looks floaty or dreamlike, the speed is wrong.`
  - Fazladan kişi: `exactly N people; nobody else appears, not even as a shadow or reflection.`
  - Yoktan belirme: `Nothing appears out of thin air; everything enters from the frame edge.`
  - Sahne sınırı: `the room has exactly one door; no corridor, no stairs.`
  - Müzik: kısa "no music" yetmezse sayarak genişletin (`no score, no strings, no drums, no humming, no melody`), çünkü model tek kelimelik yasağı esnetir.
  - Durgun beden: `living head micro-movement; a rigid head reads as a photo and is wrong.`
  - Süreklilik izi: `the paint marks only accumulate; they never reset or disappear.`
- **Amacı söyleyin:** sahnenin asıl noktasını bir cümleyle (`THE POINT OF THIS SHOT: …`), çünkü niyeti bilen model ayrıntıyı ona göre seçer.
- **Gösterişi fizikle değiştirin:** kasıtlı, performanslı eylem yerine kazara, gündelik olanı yazın; model basit fiziği daha iyi yapar.
- **Karmaşıklaştırdıysanız geri alın:** eklenen öğe yeni sorun yaratırsa bir sonraki sürümde çıkarın.
- **En önemli kural başta VE sonda.** Uzun prompt'ta sondaki kısa özet (kilitler listesi) kuralı pekiştirir.
- **Olumlu mu olumsuz mu?** Bir kaynak "olumlu cümle daha iyi" (`the cat stays in the cage` > `the cat must not leave`) diyor; usta örnekler ise ayrıntılı yasak listeleri kullanıyor — **DOĞRULANMADI**, kaynaklar çelişiyor. Pratik yol: önce olumlu cümle, sızıntı sürerse adlandırılmış yasak.

## 7. Kaç deneme? Ne zaman durmalı?

- Aynı çekim için **en fazla 2 taslak**; çalışan bir taslak yeterlidir, çünkü her yeni deneme hem para hem yeni rastgele hata demektir.
- Usta yapımlarda bile bir prompt ortalama bir-iki kez denenmiş; sonra deneme değil **prompt** değişmiş — yani tekrar tekrar aynı prompt'u üretmek yöntem değildir.
- 2 taslaktan sonra hâlâ kusur varsa: işi "taslak" diye etiketleyin, **tek** bir sonraki düzeltmeyi not edin ve kullanıcıya sorun; maliyetli yeni denemeyi onaysız yapmayın.
- Her yeni denemeden önce ≈ maliyeti söyleyip onay alın.

## 8. Kurguda kurtarma

- **Tek üretimin kusursuz olmasını beklemeyin.** Aynı sahnenin farklı denemelerinden en iyi parçalar birleştirilebilir (açılış bir denemeden, devamı başka denemeden).
- Videonun iyi kısmı varsa **kesip kullanın**; yalnız bozuk planı (çekimi) yeniden üretin, çünkü bütün sahneyi yeniden üretmek iyi kısımları da riske atar.
- Örnek: 5 saniyelik videonun ilk 2 saniyesi kusursuz, sonrası bozuksa → ilk 2 saniyeyi alın; kalan an için kısa, tek amaçlı yeni bir çekim planlayın.
- Kesme noktası seçerken kişi, ışık ve kamera konumunun iki parçada uyuştuğunu kontrol edin, çünkü uyuşmayan kesme "sıçrama" gibi görünür.
- Görselde de aynı mantık: iyi bir kare yalnız yüz ya da tek bir ayrıntıda bozuksa yeniden üretmeyin, düzenleme ile yalnız o ayrıntıyı düzeltin.

## 9. Sürüm saklama

- **Asla üzerine yazmayın.** Her düzeltme yeni sürümdür (v1, v1_duzeltme, v2…) ve eskisinin yanında durur, çünkü yeni sürüm bazı şeyleri bozarsa eskisine dönebilmek gerekir — düzeltme her zaman iyileştirme değildir.
- Her sürümle birlikte saklayın: tam prompt, kullanılan referanslar, ayarlar, kısa TUTTU/TUTMADI notu ve hangi kilidin işe yaradığı.
- Bir prompt'u düzeltirken önceki sürümü silmeyin; fark (eklenen/çıkan cümleler) sonraki işlerde ders olur.
- Kullanıcıya teslim edilen dosya da üzerine yazılmaz; yeni teslim yeni sürüm adıyla.

## 10. Gerçek denemeden iki vaka (2026-11-16)

**Vaka 1 — Görsel düzenleme: dövme ve kadraj tuttu, yüz ışığı zayıfladı.**
- Durum: dört görsellik ilk denemede en doğal kare seçildi; ama kolda istenmeyen dövme vardı ve ayaklar alt kenara çok yakındı (tam boy kuralı zayıf).
- Yapılan: düzenleme modeliyle "dövmeyi kaldır, kadrajı geri çek; aynı kadın, yüz, kıyafet, oda, eşyalar, pencere korunsun".
- TUTTU: dövme kalktı; iki ayak ve altında zemin göründü; kişi, kıyafet, oda korundu.
- TUTMADI: yüzdeki sıcak gün batımı ışığı belirgin şekilde zayıfladı — korunacaklar listesinde ışık yoktu.
- Ders: **ışığı da korunacaklar listesine adıyla yazın** (`keep the warm orange sunset light on her face exactly as in the original`), çünkü model listede olmayanı "düzeltilebilir" sayar. Düzenlemeden sonra çıktı boyutu da değişmişti; boyutu da kontrol edin.

**Vaka 2 — Video: kişi kameraya yaklaştı ve yanlış yöne döndü.**
- Durum: aynı kareden 5 saniyelik taslak video; "yerinde dans et, pencereye yarım dön, yüzüne güneş vursun".
- TUTTU: tek kesintisiz çekim (otomatik taramada sıfır kesme); kamera sabit; oda ve eşyalar yerinde; yeni kişi yok; yüz baştan sona aynı kadına benziyor; hareket neşeli ve doğal.
- TUTMADI: (1) kişi kameraya yaklaşık 1 m yaklaştı, son karelerde ayaklar kesildi. (2) pencereye değil kameraya sırtını döndü; yüze sıcak ışık hiç düşmedi.
- Teşhis (karar ağacı): referans temiz → hata prompt'ta. "Pencereye doğru" yönü kameraya göre değildi; "en fazla küçük bir adım" ölçülebilir değildi.
- Düzeltme önerisi (henüz denenmedi): yönü kameraya göre yazmak (`turns to HER RIGHT, ending in profile to camera; face stays visible`), mesafeyi sayıya çevirmek (`feet stay inside the rug; distance to camera stays 3.5 m; feet visible in every frame`) ve bunu en öncelikli kural olarak başta ve sonda tekrarlamak; korunacaklar = TUTTU listesi.
