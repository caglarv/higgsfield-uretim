# Karakter, mekân ve eşyayı tutarlı tutmak

Bu rehber, birden çok görselde ya da çekimde AYNI kişinin, AYNI mekânın ve AYNI eşyanın görünmesini sağlayan yöntemi anlatır. Okuyucu: aile fotoğraflarından görsel, tanıtım videosu ya da kısa film planlayan bir yapay zekâ. Prompt'lar İngilizce yazılır; aşağıdaki İngilizce parçalar prompt'a olduğu gibi konabilir.

**İçindekiler**
1. Temel ilke ve iş sırası
2. Kişi: yüz kilidi
3. Kişi: karakter kartı (panel düzenleri; gerçekçi ve animasyon farkı)
4. Kişi: kıyafet, yaş ve durum değişimi
5. Mekân: boş kur, aynı kameradan düzenle, ters açı
6. Eşya referansı
7. Figüranlar ve kalabalık
8. Referansları sahnede kullanmak: her referansa tek görev
9. Aile fotoğrafına uyarlama: gerçek kişinin benzerliği
10. Kısa kontrol listesi

---

## 1. Temel ilke ve iş sırası

- **Önce varlıklar, sonra sahneler.** Tekrar eden her kişi, mekân ve eşya için önce tek bir referans görsel üretilir, düzeltilir, onaylanır; sonra her sahnede AYNI onaylı referans kullanılır, çünkü model her sahnede sıfırdan tarif okursa her seferinde biraz farklı bir kişi/oda uydurur.
- Çok çekimli işte önerilen sıra:
  1. Kişiler: yüz kilidi → karakter kartı → gerekiyorsa kıyafet/yaş/durum varyasyonları.
  2. Mekânlar: boş temel görsel → aynı kameradan varyasyonlar → gereken diğer açılar.
  3. Eşyalar: tek tek eşya kartları.
  4. Ancak bundan sonra sahne görselleri ve videolar — çünkü sahne aşamasında bir varlık değişirse önceki bütün sahneler tutarsız kalır.
- Varlıkları ucuz ve küçük üretip onaylatın, büyük boyu sonra alın, çünkü yanlış yön en ucuz aşamada yakalanır.
- Önce az seçenek (2–3), çok değil, çünkü her seçenek para ve karar yükü demektir; büyük "döküm" (aynı rol için çok sayıda deneme) yalnız kişi uydurulacaksa ve bütçe izin veriyorsa.
- Kişiyi, mekânı ve eşyayı **ayrı referanslar** olarak tutun; kişiyi önceden mekâna yapıştırıp tek görsel yapmayın, çünkü sonra kişiyi ya da odayı ayrı ayrı düzeltemezsiniz.
- Her varlığı **hikâyedeki hâliyle** kartlamak (yorgun, bayramlık, ıslak saçlı) nötr kart + sonradan değişiklikten daha tutarlı sonuç verir, çünkü model en çok referansta gördüğünü taşır.

## 2. Kişi: yüz kilidi

Yüz kilidi = kimliği taşıyan tek, temiz portre. Diğer bütün kartlar ona bağlanır.

- **Kadraj:** baş-omuz, yüz kareyi doldurur; dikey oran (3:4 ya da 9:16), çünkü yüz ayrıntısı ne kadar büyükse model kimliği o kadar iyi taşır.
- **Fon:** tek düz nötr gri, köşeden köşeye aynı ton; zemin, duvar, ufuk, degrade, vinyet yok — çünkü fondaki her şey sonra sahneye sızar.
  - Örnek parça: `one flat neutral 18% grey background, same value edge to edge, no floor, no wall, no horizon, no gradient, no vignette`
- **Işık:** referans fotoğrafın ışığını yok sayıp sıfırdan, eşit ve yumuşak; dışarıdan düşen sert gölge yok, çünkü referans ışıksız olursa kişi her sahnenin ışığını doğal biçimde alır.
- **Kıyafet sade** (düz tişört gibi), çünkü bu kart yüz içindir; kıyafet ayrı kartta kilitlenir.
- **Kimliği yapan 3–5 özelliği adlandırın** (yüz şekli, göz aralığı, kaş biçimi, burun, ağız köşesi, ben, saç çizgisi) ve bunları **her prompt'ta aynı kelimelerle**, başta ve sonda tekrar edin, çünkü eş anlamlı sözcük model için farklı bir tarif demektir.
- **İfade ayrı satırda** yazılır (ör. `calm, mouth closed, eyes just past the lens`); gerekirse aynı yüzle ifade varyasyonları üretilir, çünkü ifadeyi kimlikten ayırmak yüzün kaymasını önler.
- **Olmayanları listeleyin:** gözlük, takı, makyaj, dövme, oje — yoksa açıkça "yok" deyin, çünkü model bunları kendiliğinden ekler.
  - Örnek parça: `no jewellery (no rings, bracelets, watch, necklace, earrings), no makeup, no tattoos`

## 3. Kişi: karakter kartı

Kart = aynı kişinin birkaç görünümü, tek geniş görselde (genellikle 16:9), aynı ölçek ve aynı ışıkta.

**Kaynaklarda görülen panel düzenleri:**
- **A) Üç panel, yüz iki yerde:** sol önden tam boy · orta arkadan tam boy · sağ (en büyük) baş-göğüs üç çeyrek portre. Yaygın ve basit.
- **B) Üç panel, yüz tek yerde (önerilen, gerçekçi işte):** sol büyük yakın portre · orta önden tam boy BAŞSIZ (köprücük kemiğinden kesik) · sağ arkadan tam boy başsız. Yüz yalnız bir panelde olduğu için model iki farklı yüz üretip karıştırmaz.
  - Örnek parça: `centre panel: full-body front view cropped at the collarbone, head out of frame`
- **C) İki panel:** solda tam boy, sağda yüz. Kısa reklam/tek sahne işlerinde yeterli.
- Düzen A'da tam boydaki küçük yüz büyük portreyle yarışıyorsa kapatılabilir ya da kadraj dışı bırakılabilir, çünkü küçük ve bulanık ikinci yüz kimliği bulandırır.

**Her kartta ortak kurallar:**
- `three separate full views side by side, equal spacing, grey between them, no overlap; same scale, same outfit, same light in all panels`
- Nötr duruş, kollar yanda, eller boş, ağız kapalı, çünkü abartılı poz beden oranını gizler.
- Kıyafeti baştan ayağa, parça parça yazın; görünmeyen parçayı (sırt, ayakkabı) da tamamlayın, çünkü model boş bırakılanı her sahnede farklı doldurur.
- Kumaşa malzeme ve geçmiş verin (yıkanmış, solmuş, dizi torbalanmış), çünkü gerçek kumaş kişiyi inandırıcı kılar ve kıyafeti tanınır yapar.
- Yazı, etiket, numara yok — en başta söyleyin, çünkü kart düzeni modele "afiş" çağrışımı yapıp yazı ekletebilir.
- Gerekirse önce kıyafetsiz beden oranı için sade bir tam boy (ör. düz tişört-tayt), sonra kıyafet; çünkü beden oranı kıyafetten bağımsız kilitlenir. (Kaynaklarda bir yapımda görüldü; zorunlu değil.)

**Gerçekçi (fotoğraf gibi) ile animasyon farkı** — yöntem aynı, değişenler:
- *Üslup cümlesi:* gerçekçide `photoreal, real person, unretouched skin, visible pores, a small catchlight in each eye`; animasyonda üslubu başta VE sonda kesin söyleyin (`stylised 3D animated film character, not photoreal, not 2D, not anime, not plastic`), çünkü model iki uç arasında kayar.
- *Abartı:* animasyonda her karaktere **tek belirgin, abartılı özellik** verin (iri kulak, uzun ince boyun) — modeller pürüzsüz, simetrik, "emoji yüzü"ne kayar ve bu karakteri jenerik yapar. Gerçekçide abartma yok; kişinin GERÇEK ayırt edici özelliklerini adlandırıp koruyun.
- *Işık:* animasyonda tamamen düz ve gölgesiz (kişinin kendi hacim gölgesi kalır); gerçekçide önden hafif yukarıdan yumuşak eşit gün ışığı, az hacim kalır — çünkü gerçek yüz tamamen düz ışıkta yassı ve yapay görünür.
- *Ayrıntı:* animasyonda yüz sade, en yüksek ayrıntı kumaşta; gerçekçide cilt dokusu (gözenek, ince çizgiler) da korunur.
- *Fon rengi:* kaynaklarda beyaz, açık gri, orta gri ve kırık beyaz hepsi kullanılmış — **DOĞRULANMADI** hangisinin daha iyi olduğu. Varsayılan: düz nötr gri (beyaz, açık tenli yüzde ve beyaz giyside kontur kaybettirebilir; bu da bir çıkarım).

## 4. Kişi: kıyafet, yaş ve durum değişimi

- **Kıyafet değişimi:** kişiyi yeniden üretmeyin; düzenleme (edit) modeliyle kartı düzenleyin ve referanslara tek görev verin:
  - `Image 1 is for identity only. Image 2 is for the outfit only — do not transfer that person's face, hair or body.`
  - Değişiklik kartın TÜM panellerinde aynı olsun; kaynağın en-boy oranı ve çözünürlüğü korunsun, çünkü oran değişirse model kadrajı yeniden kurar.
  - Kıyafet varyasyonlarını kişiden ayrı saklayın (kıyafet = ayrı varlık), çünkü aynı kişi birden çok kıyafetle farklı sahnelerde dolaşır.
- **Yaş değişimi** (ör. dedenin gençliği): her yaş **ayrı bir yüz kilidi**; prompt'ta ne KALIR ne DEĞİŞİR açıkça yazılır, çünkü model "aynı kişi" dendiğinde neyin değişebileceğini bilmez.
  - KALIR: yüz şekli, göz yeri ve aralığı, kulaklar, ağız asimetrisi, ben.
  - DEĞİŞİR: cilt, yanak-çene tanımı, saç rengi/çizgisi, boyun, beden oranı.
  - Videoda her yaşın doğru referansı çağrılır.
- **Durum değişimi** (ıslak, çamurlu, dağınık saç, boyalı eller): mevcut kartı düzenleyin, yalnız değişeni yazın:
  - `Edit this image. Same person, face, hair, pose, outfit, background and light. Change ONLY the hands and sleeves: …` + her izin nerede, ne renk, ne kadar kuru olduğu.
- **Video hilesiyle durum değişimi:** kişi kıpırdamadan yalnız rüzgâr/olay saçı ve kıyafeti etkilesin, son kare yeni durum referansı olarak alınsın. Bir kaynak bunun görsel düzenlemeden daha sadık sonuç verdiğini söylüyor — **DOĞRULANMADI** (bizde denenmedi).
- **Video karakter kartı:** kısa bir konuşma + kişinin etrafında yavaş kamera turu; sonraki sahnelerde yüz, tavır ve ses referansı olur. Kaynakta önerildi, bizde denenmedi — **DOĞRULANMADI**.
- **Küçük düzeltmeler** hep aynı kalıpla: `Keep everything exactly the same, change only ___.` Büyük prompt'u yeniden yazmak yerine tek değişiklik, çünkü yeniden yazım düzeltilmemiş ayrıntıları da değiştirir.

## 5. Mekân: boş kur, aynı kameradan düzenle, ters açı

- **Önce boş mekân.** İnsansız, mimari ve kullanılabilir alan görünsün, çünkü kişili mekânda oda kişinin arkasında kaybolur ve sonra temiz düzenlenemez.
  - Kişi yasak cümlesi şart: `No people, silhouettes, faces, human figures or human-shaped reflections.` — yoksa model aşçı, garson, yoldan geçen uydurur.
  - Mekânın NE İÇİN olduğunu söyleyin (`open floor space in the centre for a dancer`), çünkü model alanı ona göre boşaltır.
  - Kamera cümlesiyle başlayın: konum, yükseklik (ör. 1,4 m), yön, objektif (24–35 mm). Odayı bölge bölge yazın: kare SOLU → ORTA → SAĞI, her birinde ön → arka.
  - Olmayan şeyleri açıkça yasaklayın (`no second door, no stairs, no corridor`), çünkü boş bırakılan alanı model doldurur.
  - Ruh hâli kelimesi yerine görünür ışık koşulu (`low sun from the left window, warm patch on the floor`).
  - Yazı istemiyorsanız: çerçeveli resimler soyut, kitap sırtları okunmaz.
- **Aynı kameradan düzenleme:** varyasyonların hepsi (gece, sabah, süslenmiş, dağınık) temel görselin düzenlenmesiyle yapılır:
  - `Edit the attached image. Camera position, framing, angle, lens and composition stay IDENTICAL — no reframing, no crop, no zoom.` + korunacakların listesi + TEK değişiklik ayrıntılı.
  - Böylece sahneler arası kesmede oda "aynı yer" olarak okunur.
- **Işık düzeltmesi ayrı iş:** `This is ONLY a light and colour correction; nothing is added, removed or redesigned.` + **ŞU AN NE YANLIŞ** + **NE OLMALI** (ör. "duvarlar gün ışığı beyazı; 2 stop karanlık, gece yarısı evi"). Işıkla nesneyi aynı düzenlemede değiştirmeyin, çünkü hangisinin neyi bozduğu anlaşılmaz.
- **Kişiyi mekâna koymak:** boş mekânı düzenleme modeliyle düzenleyip kişiyi ekleyin; kişinin nereye geleceğini bir **mekânsal çapa** ile gösterin (ör. masanın ortasında tek çay bardağı → kişi onun yanına oturur), çünkü çapa olmadan model kişiyi rastgele yere koyar.
- **Ters açı ve diğer açılar:** `Show the same room from the opposite end. Change only the camera direction; architecture, materials, furniture and light stay the same.` Her yeni açıda yeni icat edilen ayrıntıları orijinalle karşılaştırın, çünkü model görmediği duvarı uydurur ve bazen görünen ayrıntıyı da değiştirir.
- Komşu mekânlar arasında tutarlılığı adıyla yazın (`same mint-green paint and same floor as the kitchen`).
- Havada asılı şey istemiyorsanız: `air completely clear; light is visible only where it lands, no beams, no haze, no dust`.

## 6. Eşya referansı

- Tek nesne, nesne yüksekliğinden düz karşıdan, ortalanmış, üstte ve yanlarda boşluk; düz nötr gri fon; gölgesiz düz ışık, çünkü ışıksız eşya sahneye konunca sahnenin ışığını alır.
- Gerekirse 3 panel (önden, yandan, arkadan): aynı ölçek, aynı ışık, renk/yıpranma/işarette fark yok.
- **Durum ayrıntısı** ve **olmayan durum** birlikte yazılır (`dry cracked soil, brown leaf edges — no rot, no yellowing`), çünkü "eski" gibi tek kelime modelde her seferinde farklı bir eskime üretir.
- Tür, boyut, siluet, renk, malzeme, durum ayrı ayrı; yazı taşıyorsa yazının tam metni, dili, harf büyüklüğü ve yeri.
- Gerçek bir eşyanın fotoğrafı kaynaksa (aile yadigârı, ürün): düz fonda, tamamı görünen, net ışıklı fotoğraf kullanın; fon temizlemek nesneyi yeniden tasarlama izni DEĞİLDİR — kontur, sap, desen, renk orijinalle yan yana karşılaştırılır. Bozulursa orijinal fotoğrafı kullanın.
- Sahnede eşyanın **kimin elinde, nerede, hangi yöne dönük** olduğu prompt'ta yazılır, çünkü referans görünüşü verir, sahipliği ve konumu vermez.

## 7. Figüranlar ve kalabalık

- Kalabalık önce tek bir grup görseliyle kurulabilir: baştan ayakkabıya kadrajda, sıra değil doğal grup, her kişi tek tek tarif — çünkü tek görselde kurulan grup birbirine benzemeyen yüzler üretir.
- **Her figürana adı konmuş TEK yüz özelliği** (kalkık burun, dolgun yanak, uzun oval yüz), ama "ön plan karakteri gibi dikkat çekmeyecek kadar yumuşak", çünkü özelliksiz figüranlar aynı yüzün kopyası olur.
- Gerekli figüranlar sonra tek tek kart olarak çıkarılır.
- Sahnede kimliği kısa etiketle sabitleyin ve **tam sayıyı** yazın: `exactly four people: one girl in a red sweater, one grandfather in a blue shirt, …`, çünkü model kişileri çoğaltır ya da birleştirir.

## 8. Referansları sahnede kullanmak: her referansa tek görev

- Her referansa prompt'ta adıyla TEK görev verin ve neyi ALMAYACAĞINI söyleyin:
  - `Image 1 = identity and outfit of the grandmother only.`
  - `Image 2 = the living room: architecture, furniture positions, palette, light only. Nothing else exists.`
  - `Image 3 = camera angle and composition only; do not copy its people.`
  - Çünkü görevi yazılmamış referanstan model her şeyi (açı, poz, fon) birden kopyalar.
- Videoda referans genellikle **bilgi**dir, kadraj değil: `References are knowledge only, not shots — the camera never jumps to a reference's angle.` (Bir referansı bilerek kadraj için veriyorsanız bunu açıkça yazın.)
- Her eylemden önce eylemi yapan kişiyi adıyla anın, çünkü model eylemi yanlış kişiye verebilir.
- Yazılan etiket tek başına referans eklemez; görsel ayrıca eklenmelidir.
- Öncelik sırası çatışmada: kullanıcının kısıtı > düzenlenen görselin kimliği > kişi/eşya referansı > kompozisyon > mekân > üslup > ruh hâli.

## 9. Aile fotoğrafına uyarlama: gerçek kişinin benzerliği

- Kaynak gerçek bir kişinin fotoğrafıysa **yüz kilidi o fotoğraftan** yapılır; birden çok fotoğraf varsa farklı açılardan, net, yakın, filtresiz olanlar seçilir, çünkü bulanık ya da filtreli fotoğraftaki hata kilide taşınır.
- Kurgusal karakter üretirken kaynaklarda kullanılan "özgün karakter, bu yüzü kopyalama" cümlesinin TERSİ gerekir: `the SAME real person as the reference photo — keep bone structure, eye spacing, nose, mouth and hairline exactly`.
- Kişinin gerçek ayırt edici özelliklerini (ben, gülüş biçimi, kaş, gözlük) kullanıcıya sorup listeleyin, çünkü yabancı birinin "benziyor" dediği yüzü aile tanımayabilir.
- **Benzerlik kontrolü her aşamada:** yüz kilidi, kart, her sahne görseli ve videonun birkaç karesi kaynak fotoğrafla yan yana büyütülerek karşılaştırılır. Bakılacaklar: yüz şekli, göz aralığı, burun, ağız, yaş görünümü, ten rengi, saç çizgisi.
  - Modellerin bilinen eğilimi: yüzü güzelleştirme, gençleştirme ya da yaşlandırma, birbirine benzetme — bunları özellikle arayın.
  - Gerçek bir denemede (2026-11-16) kişi tarif edilen yaştan büyük göründü; yaşı her kontrolde ayrıca not edin.
- **Son onay aileden:** benzerlik hükmünü yapay zekâ değil kullanıcı verir, çünkü tanıdık bir yüzdeki küçük sapmayı yalnız onu tanıyan görür.
- İyi bir sahnede yalnız yüz kaydıysa yeniden üretmek yerine düzenleme ile kurtarın: `Edit the first image; the second image is the identity reference. Keep everything in the first image (framing, light, grain, hair, EXPRESSION). Change ONLY the facial bone structure to match the person in the second image — same expression, the referenced face.`
- Fotoğrafı yalnız kullanıcının izin verdiği iş için kullanın; aile fotoğrafları ve üretilen yüzler özeldir, başka yerde paylaşılmaz.
- **Siyah-beyaz ya da soluk fotoğraf:** saç, göz ve ten rengini fotoğraftan çıkaramazsınız; kullanıcıya sorun. Kullanıcı "sen seç" derse tahmininizi "tahmindir" diye işaretleyip onaylatın, çünkü yanlış göz ya da saç rengi benzerliği en hızlı bozan şeydir.
- **Tek karelik iş için kısa yol:** yalnız bir görsel istenmişse kart, boş mekân ve eşya kartı şart değildir. Benzerlik önemliyse yüz kilidi (temiz, renkli portre) + sahne iki adımı yeter; önemli değilse doğrudan sahne. Fazla adım fazla ücrettir; uzun yol tekrar eden varlıklar içindir.
- **Eldeki fotoğraf yüz kilidi kurallarına uymuyorsa** (fonlu, sert ışıklı, vesikalık): fotoğrafı yeniden kurmaya çalışmayın; olduğu gibi kimlik referansı yapın ve yalnız gerekeni düzeltin.

## 10. Kısa kontrol listesi

- [ ] Her tekrar eden kişi/mekân/eşya için onaylı tek referans var mı?
- [ ] Kimlik özellikleri her prompt'ta aynı kelimelerle, başta ve sonda mı?
- [ ] Olmayanlar (takı, dövme, gözlük, fazladan kişi, yazı) açıkça yasak mı?
- [ ] Her referansın tek görevi ve almayacağı şeyler yazıldı mı?
- [ ] Mekân varyasyonları aynı kameradan mı; yeni açıda uydurulan ayrıntı var mı?
- [ ] Eşyanın sahibi, yeri ve yönü yazılı mı?
- [ ] Kişi sayısı tam sayı olarak yazılı mı?
- [ ] Gerçek kişide: kaynak fotoğrafla yan yana büyütülmüş benzerlik kontrolü yapıldı mı, kullanıcı onayladı mı?
