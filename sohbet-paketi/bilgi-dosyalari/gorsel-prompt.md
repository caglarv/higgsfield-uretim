# Durağan görsel prompt'u nasıl yazılır

Okuyucu: bir kullanıcı için görsel üretim ya da görsel düzenleme prompt'u yazacak yapay zekâ.
Prompt'un kendisi İngilizce yazılır; bu rehber Türkçedir. Tırnak içindeki İngilizce parçalar prompt'a olduğu gibi girebilir.

## İçindekiler
1. Temel ilke
2. Bölüm sırası (yeni görsel)
3. Kişi / varlık kartı
4. Mekân
5. Düzenleme kalıbı ("yalnız X'i değiştir")
6. Kamera, objektif, ışık, renk, yerleşim
7. Uzunluk ve dil
8. Sık hatalar ve çareleri
9. Ön kontrol listesi

---

## 1. Temel ilke
- **Görüntünün mantığını, içeriğini ve kamerasını sen belirle; ışığı yönlendir; render motorunu taklit etme.** Neden: modeller doku, pozlama ve renk inceliğini kendileri iyi yapar; senin işin karede NE olduğunu, NEREDE durduğunu ve nereden bakıldığını kesinleştirmek.
- **Ruh hâli kelimesi yerine görünür koşul yaz.** "dramatic, moody, cinematic" yerine ışığın kaynağını, yönünü ve hangi tarafın gölgede kaldığını söyle. Neden: model sıfatı kendi ortalamasıyla doldurur; somut koşulu ise uygular.
- **Kalite kelimesi yığma** ("beautiful, ultra-detailed, 8K, masterpiece"). Neden: hiçbir karar taşımazlar, yer kaplarlar; kare yanlışsa sıfat ekleme, yanlış talimatı düzelt.
- **Her cümle ya görüntüyü değiştirmeli ya da olası bir hatayı önlemeli.** Neden: gereksiz cümle önemli talimatın ağırlığını azaltır.
- **Tek görev, tek görsel.** Kişi, mekân ve eşya ayrı ayrı referans görsel olarak üretilir; sonra sahnede birleştirilir. Neden: tek görsele çok iş yüklemek her birinin sadakatini düşürür ve düzeltmeyi zorlaştırır.

## 2. Bölüm sırası (yeni görsel)
Düz İngilizce paragraflar halinde yaz; aşağıdaki sıra modelin önce neyin önemli olduğunu anlamasını sağlar.
1. **Görselin işlevi + ana konu** — tek cümle: ne tür fotoğraf, kim/ne, ne yapıyor. Neden: ilk cümle tüm kararın çerçevesidir.
2. **Konunun ayrıntısı** — kişi kartı (§3) ya da nesne tarifi: tür, boyut, siluet, renk, malzeme, durum.
3. **Kadraj + kamera + objektif** — çekim boyutu, kamera konumu/yüksekliği/uzaklığı, mm, görüş açısı, "distortion off" (§6).
4. **Mekân, soldan sağa** — kare solu → ortası → sağı; her birinde ön → orta → arka plan (§4).
5. **Eylem / duruş** — ellerin, ayakların, bakışın nerede olduğu.
6. **Işık** — kaynak, yön, nereye düştüğü, nerede söndüğü.
7. **Renk ve doku** — nötr temel, renk kaynağın yakınında (§6).
8. **Üslup** — tek ana üslup, görünür özellikleriyle.
9. **Varlık ve yazı kontrolü** — kişi sayısı, "No people…" (boş mekânda), yazı varsa harfi harfine.
10. **Yalnız olası hatalara karşı kısa kısıtlar** — ör. "both hands visible, five fingers each".
11. **Tek satırlık özet** — "Short summary: …". Neden: uzun tarifin sonunda ana fikri tekrar etmek modelin önceliği kaybetmesini önler (Higgsfield'in örnek film kalıbı; etkisi ayrıca ölçülmedi).
- Bölüm etiketi ("Setting:", "Light:") kullanmak serbesttir ama zorunlu değildir; Higgsfield'in kendi görsel becerisi etiketsiz düz yazı öneriyor. İkisinin farkı ölçülmedi — DOĞRULANMADI.

## 3. Kişi / varlık kartı
Burada yalnız kartın prompt'u anlatılır; yüz kilidi, panel düzenleri, kıyafet/yaş değişimi ve aile fotoğrafı yöntemi için `karakter-mekan-esya.md` dosyasına bak — ikisi çelişirse o dosya geçerlidir.
Tekrar eden her kişi, eşya ya da hayvan için önce bir "kart" görseli üretilir, düzeltilir, sonra her sahnede AYNI kart kullanılır. Neden: her sahnede kişiyi yeniden tarif etmek yüzü ve kıyafeti kaydırır; sabit referans tutarlılığın tek güvenilir yoludur.
- **Fon ve ışık:** dikişsiz düz nötr fon (kaynaklarda beyaz da nötr gri de kullanılmış; varsayılan nötr gri — ayrıntı ve gerekçe `karakter-mekan-esya.md` içinde), yumuşak eşit ışık, başka hiçbir şey ("nothing else in the image"). Neden: fon ve sert ışık sonraki sahneye taşınır; temiz kart yalnız kimliği taşır.
- **Duruş:** tam boy, önden, nötr duruş, kollar yanda, eller boş, ağız kapalı, yüz net görünür. Neden: el ya da ağızdaki hareket karta "kalıcı özellik" olarak yapışır.
- **Tarif sırası:** kim (yaş aralığı, beden, boy) → yüz (yüz şekli, ten, saç rengi-boyu-dokusu, belirgin işaret) → kıyafet PARÇA PARÇA (üst, alt, ayakkabı, aksesuar; renk + kumaş + kalıp) → duruş → fon/ışık → özet satırı.
- **Görünmeyen parçayı tamamla:** ayakkabı ya da pantolon kadraj dışında kalacak olsa bile yaz. Neden: yazmazsan sonraki sahnede model uydurur ve her sahnede farklı uydurur.
- **Kart düzenleri** (kaynaklarda üç farklı öneri var; ihtiyaca göre seç):
  - 2 panel, 16:9: solda tam boy, sağda büyük yüz.
  - 3 panel: önden tam boy · arkadan tam boy · göğüsten yukarı üç çeyrek portre.
  - Gerçekçi işler için: büyük yüz paneli + başsız önden/arkadan kıyafet panelleri. Neden: küçük yüz kopyaları büyük yüzle "yarışıp" kimliği bulandırabiliyor.
- **Kalabalık / aile:** tek grup fotoğrafı düzeni (uzunlar arkada, çocuklar önde), her kişi ayrı cümleyle ve soldan sağa sırayla. Neden: toplu tarifte özellikler kişiler arasında karışır.
- **Gerçek kişi fotoğrafından kart:** kimliği fotoğraf taşır; prompt kıyafeti, duruşu ve fonu tarif eder. Yüzü kafandan yeniden tarif etme; yalnız fotoğrafta gerçekten görünen ve kullanıcının doğruladığı ayırt edici özellikleri (ben, gözlük, saç çizgisi) her prompt'ta aynı kelimelerle an. Neden: uydurulmuş tarif fotoğrafla çelişirse model ikisinin ortasını üretir; doğrulanmış özellik ise kimliği pekiştirir.
- **Nesne kartı:** düz fon, nesnenin tamamı görünür, net ışık; kontur, sap, köprü, renk gibi ayırt edici ayrıntıları say. Fon temizlemek nesneyi yeniden tasarlama izni değildir; sonucu orijinalle karşılaştır.

## 4. Mekân
- **Önce BOŞ mekân üret**, kişiyi sonra düzenlemeyle ekle. Neden: boş mekânda mimari ve kullanılabilir alan net görülür; kişi baştan konursa mekân onun etrafında bozulur.
- **Kişi istenmediyse kişi YASAK, açıkça yaz:** "No people, silhouettes, faces, human figures, human-shaped reflections, or figures visible through windows, mirrors or screens." Neden: modeller mutfağa aşçı, sokağa yaya ekleme eğilimindedir; insan izini eşyayla anlat (yarım içilmiş çay, açık kitap).
- **Soldan sağa harita:** önce kafanda kur, sonra prompt'u bu sırayla yaz:
  - kare solu (ön / orta / arka) → kare ortası (ön / orta / arka) → kare sağı (ön / orta / arka).
  - Prompt'ta etiket değil düz ifade kullan: "on frame left…", "across the centre…", "on frame right…".
  - Neden: model tek ve tutarlı bir yerleşim alır; bir nesnenin iki farklı konumda anılması ya da kopyalanması önlenir.
- **Boş bırakılan bölgenin amacını söyle** ("open floor in the centre for a person to walk through"). Neden: amacı söylenmeyen boşluğu model eşyayla doldurur.
- **Mekânın NE İÇİN olduğunu yaz** (sonra kişi oturacak, kamera dönecek). Neden: model alanı o kullanıma göre açar.
- **Etiket yerine yapı:** "rustik, endüstriyel, lüks" deme; malzeme, oran, tavan, zemin, açıklıklar ve yıpranma durumunu yaz ("faded green shutters, worn stone threshold").
- **Nesne tarifi:** tür, boyut, siluet, renk, malzeme, durum (tozlu, yıpranmış), konum, yön, komşusuyla ilişkisi. Küçük tekrar eden eşyaları grup olarak an; sayıyı yalnız kompozisyonu etkiliyorsa ver.
- **Işık düzeltmesi:** yanlış ışıkta "şu an ne yanlış / ne olmalı" diye iki cümle yaz. Neden: model farkı görünce yalnız ışığı değiştirir.

## 5. Düzenleme kalıbı ("yalnız X'i değiştir, gerisini koru")
Hedefli düzeltme için yeniden üretme; düzenleme (edit) modeli kullan. Neden: yeniden üretim beğenilen her şeyi de değiştirir.
- **Kalıp (sırası önemli):**
  1. Neyin düzenlendiği: "Edit the input image. Keep the same photo."
  2. Korunacakların kısa listesi.
  3. Değişiklik(ler), numaralı, fiil büyük harfle: "1. REMOVE …", "2. ADD …", "3. CHANGE … to …".
  4. "Change NOTHING else:" + korunacakları TEK TEK say (kişi, yüz, ifade, saç, kıyafet parçaları, poz, eşyalar, ışık yönü, renkler).
  5. "Do not add any people, text or logos."
  6. Tek satır özet.
- **Kendi kısa örneğin:** "Edit the input image. 1. REMOVE the red cap from the boy's head; show his short black hair. Change NOTHING else: same boy, same face and smile, same blue raincoat, same pose, same garden, same afternoon light."
- **Neden saymak gerekiyor:** "gerisi aynı" demek yetmez; model saymadığın şeyi değiştirilebilir sayar.
- **Bir seferde en fazla 2–3 değişiklik.** Neden: çok değişiklik, korunacakların bozulma ihtimalini artırır.
- **Varsayılan olarak hep korunur:** kişi kimliği ve sayısı, kompozisyon, kamera ve perspektif, kırpma, poz, ana yerleşim. Işık, gölge, fon, alan derinliği yalnız değişiklik mantıken gerektiriyorsa değişir.
- **Kadrajı genişletme** de bir düzenlemedir: "ZOOM OUT slightly so both feet are fully inside the frame with floor visible below them." Neden: denemede tam boy kuralı bozuk çıkan görsel bu kalıpla düzeldi.
- **Bedeli kontrol et:** denemede dövme silinip kadraj açılınca yüzdeki sıcak gün batımı ışığı zayıfladı. Korunacak ışığı adıyla ve yeriyle yaz ("the same warm orange sunset light on her face and left arm").
- **İki referanslı düzenleme:** "Use Image 1 only for identity. Use Image 2 only for the outfit; do not transfer its face." Her referansa tek görev ver; kaynağın en-boy oranını koru. (Referansları "Image 1, Image 2" diye yükleme sırasıyla an; `@` etiketi yalnız kullanılan aracın desteklediği yerde işe yarar.)
- **Öncelik sırası** (çelişkide): kullanıcının açık kısıtı > düzenlenen görselin kimliği > kişi/nesne referansı > kompozisyon > mekân > üslup > ruh hâli.
- **Ters açı:** "Show the same room from the opposite end; change only the camera view." Yeni açıda model ayrıntı uydurur; orijinalde olmayan eşyayı kontrol et.
- **Not:** her görsel modeli düzenleme yapmaz (bazıları tek görsel girdiyi baştan yorumlar). Hangi modelin düzenleme yaptığını model seçimi rehberinden kontrol et.

## 6. Kamera, objektif, ışık, renk, yerleşim
**Kadraj (önce bu):** çekim boyutunu kadraj sınırıyla yaz — "full-body shot: head and both feet fully inside the frame". Neden: "full body" etiketini model gevşek yorumlar. Uyarı: denemede bu sınır yazılı olduğu halde 4 seçeneğin 2'sinde baş ya da ayak kenara dayandı; sınıra ek olarak kamera uzaklığı ver, baş üstünde ve ayak altında boşluk iste, sonucu kontrol et.
- Boyutlar: extreme wide · wide · full shot (baş + ayak) · medium wide (baştan dize) · cowboy (uyluk ortası, eller görünür) · medium (bel üstü) · medium close-up (göğüs üstü) · close-up (yüz) · extreme close-up (tek ayrıntı).
- "Close-up" bir kadrajdır, objektif değil; önce kadraj, sonra objektif.

**Kamera konumu:** yükseklik (ör. "chest height", "1.4 m"), konuya uzaklık ("about 3.5 m away"), bakış yönü, açı (eye level · high angle · low angle · top-down · Dutch). Neden: konum yazılmazsa model her denemede farklı bakış seçer.

**Objektif:** her yeni görselde mm + yaklaşık yatay görüş açısı + "distortion off". Belirtilmemişse:
- dengeli iç mekân 32–35 mm (~54–59°) · dar iç mekân 24–28 mm (~65–74°) · mekânda kişi/nesne 35 mm (~54°) · büyük dış mekân 28–35 mm · portre daha uzun objektif.
- Neden: geniş objektif yüzü ve mimariyi bozar; değer yazınca oranlar doğal kalır.

**Işık:** zaman/hava + kaynak + yön + nereye düştüğü + nerede söndüğü.
- Kendi örneğin: "Morning light enters from a window on frame right, falls across the table and the grandmother's hands, and fades toward the dark cupboard on the left."
- Mekân ve sahne prompt'unda Kelvin, pozlama, ışık oranı yazma. Neden: render motorunu taklit etmek modelin doğal ışık zekâsını bozar.
- İstisna: stüdyo tipi işler (kart, portre, ürün) — burada "key light … camera-left, raised above head height, soft quality; fill …, roughly 2:1" gibi stüdyo dili işe yarar.

**Renk:** nötr orta ton temeli; her malzeme kendi rengini korur (beton gri, ahşap bal rengi); sıcak/soğuk ışık rengi kaynağının yakınında kalır. Tüm kareye turuncu ya da camgöbeği sürme. Neden: tek renk sürmek malzemeleri ayırt edilmez yapar ve yapay görünür.
- Sahnede tek doygun renk vurgusu bakışı yönlendirir.

**Yerleşim:** konuyu yüzdeyle ya da bölgeyle yerleştir ("slightly left of centre, about 40% of the frame height"). Ön-orta-arka plan katmanları ayrı olsun; ana eylem kolay bulunsun. Üçte bir kuralı rehberdir, zorunluluk değil.

**Üslup:** tek ana üslup; etiketle değil görünür özelliklerle (ışık davranışı, doku, kompozisyon). Sanatçı, yönetmen, marka adıyla üslup isteme. Neden: iki üslup çakışınca model ikisinin bulanık ortalamasını üretir.

**Yazı:** yazı taşıyan nesnede yazıyı harfi harfine ver (metin, dil, büyük/küçük harf, yer). Yazı taşımayan yüzeyler için ayrıca "blank" deme; yalnız genel "No text, no logos, no watermark" yeter. Neden: belirtilmeyen yazıyı model sahte harflerle doldurur.

## 7. Uzunluk ve dil
- Prompt İngilizce, düz ve somut cümlelerle.
- Kaynaklar farklı uzunluk öneriyor — DOĞRULANMADI, hangisinin daha iyi olduğu ölçülmedi:
  - Higgsfield görsel becerisi: basit konu 250–400 kelime, kontrollü mekân 500–750 kelime.
  - Akademi mekân dersi (düzenleme modeli için): ≈60–90 kelime.
  - İlk gerçek deneme (2026-11-16) ≈300 kelimeydi: tarif büyük ölçüde tuttu, ama 4 seçeneğin 2'sinde kadraj kuralı bozuldu, birinde istenmeyen dövme çıktı.
- Pratik kural: kısaltırken kamera, objektif, konum, kişi sayısı, yazı ve düzenleme kilitlerini ASLA atma; tekrar eden sonuçları, eşanlamlı yığınlarını ve kalite kelimelerini at.
- Önce olumlu cümle ("both feet stay on the rug"); hata sürerse adı konmuş açık yasak ekle. Boş mekândaki "No people…" ve "no jewellery, no tattoos" gibi listeler baştan açık yasak olarak yazılır. Hangisinin daha iyi uygulandığı kaynaklarda çelişkili — DOĞRULANMADI.

## 8. Sık hatalar ve çareleri
- **Baş ya da ayak kadrajdan taşıyor** → kadraj sınırını yaz ("head and both feet fully inside the frame, clear space above the head and below the feet") + uzaklık ver.
- **İstenmeyen ayrıntı (dövme, yazı, ek eşya)** → düzenlemeyle sil (§5); ayrıntı referans görselde varsa kelimeyle silmeye çalışma, önce görseli düzelt.
- **Kıyafet rengi kaydı (gri istendi, bej geldi)** → rengi ve kumaşı tek kelimeyle sabitle, özet satırında tekrar et.
- **Yaş farklı görünüyor** → yaş aralığını somut işaretle destekle (cilt, saç, yüz hatları); seçeneklerden en yakını seç.
- **Bozuk el / fazla parmak** → ellerin ne yaptığını ve görünür olduğunu yaz ("both hands relaxed and visible, five fingers each"); karmaşık el hareketinden kaçın.
- **Plastik, aşırı pürüzsüz yüz** → "natural skin with visible texture, small asymmetries"; stüdyo ışığı ekleme, mekânın ışığına uydur.
- **Mekâna davetsiz kişi** → "No people…" cümlesi (§4).
- **Aşırı keskin, render gibi yüzey; tekdüze tekrar eden nesneler; dikkat dağıtan parlamalar** → büyütüp bak; tarifi sadeleştir, nesnelere durum ve kusur ekle ("slightly uneven", "worn at the edges").
- **Tüm kare tek renge boyanmış** → renk kaynağını yerine bağla (§6).
- **Kompozisyon yorumlanmış** → konumu yüzdeyle ve soldan sağa haritayla ver; birkaç seçenek üretip en uygununu seç.
- **"Tekrar üret" daha iyisini garanti etmez.** Aynı hata her denemede tekrar ediyorsa prompt'u ya da referans görseli düzelt; tek seferlik ise yeni deneme yap ve karşılaştır.
- **Seçim ölçütü:** en gösterişli görsel değil, sahnenin ihtiyacına en uygun olan.

## 9. Ön kontrol listesi (göndermeden önce)
- [ ] İlk cümle görselin işlevini ve ana konusunu söylüyor mu?
- [ ] Kadraj sınırı, kamera konumu/yüksekliği/uzaklığı, mm, görüş açısı, "distortion off" var mı?
- [ ] Mekân soldan sağa, ön → arka sırasıyla mı anlatıldı; boş bölgelerin amacı yazıldı mı?
- [ ] Kişi sayısı açık mı? Boş mekânda "No people…" cümlesi var mı?
- [ ] Kıyafet parça parça, renk + kumaşla mı yazıldı; görünmeyen parçalar tamamlandı mı?
- [ ] Işığın kaynağı ve yönü var mı; Kelvin/pozlama gibi render dili yok mu (stüdyo hariç)?
- [ ] Renk kaynağına bağlı mı, tüm kareye tek renk sürülmemiş mi?
- [ ] Tek ana üslup mu; sanatçı/marka adı yok mu?
- [ ] Yazı varsa harfi harfine mi verildi?
- [ ] Düzenlemede değişiklikler numaralı mı, "Change NOTHING else:" listesi tek tek sayılmış mı, korunacak ışık adıyla yazılmış mı?
- [ ] Her referansa tek görev verilmiş mi?
- [ ] Kalite kelimesi yığını, tekrar ve gereksiz cümle temizlendi mi?
- [ ] Sonda tek satır özet var mı?
