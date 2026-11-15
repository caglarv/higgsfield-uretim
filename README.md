# Higgsfield üretim becerisi

Yapay zekâ yardımcına (Claude, ChatGPT ya da başkası) Higgsfield ile görsel ve video üretmeyi öğreten bir talimat paketi.
Sen ne istediğini düz Türkçeyle söylersin; yardımcı sana sorular sorar, prompt'u yazar, model ve ayarı seçer, maliyeti söyler, sonucu seninle birlikte kontrol eder.

Sürüm: v1 (2026-11-16). Model adları ve fiyatlar zamanla değişir; dosyalardaki tarihli bilgi ile sitede gördüğün çelişirse siteye güven.

## Ne yapar
1. İsteğini netleştirmek için 15 çoktan seçmeli soru sorar (düzeltme isteklerinde yalnız eksik kalanı sorar).
2. Sahneyi kısaca Türkçe anlatır; yanlış anlaşılan para harcanmadan yakalanır.
3. İngilizce prompt'u yazar, işe uygun modeli ve ayarı seçer.
4. Maliyeti söyler ve onayını ister.
5. Sonucu denetler: neyin tuttuğunu, neyin tutmadığını söyler ve nasıl düzeltileceğini önerir.

## İki kullanım biçimi
- **Sen üretirsin (API gerekmez):** Yardımcı sana kopyala-yapıştır bir paket verir (model, ayarlar, prompt). Sen higgsfield.ai sitesinde üretir, sonucu sohbete geri yüklersin. ChatGPT, Claude sohbet ve benzerlerinde böyle çalışır.
- **Yardımcı üretir (Claude Code + Higgsfield API anahtarı):** Yardımcı prompt'u kendisi gönderir, sonucu indirir ve denetler. Her ücretli adımdan önce senden onay ister.

## Kurulum

### Claude Code
`higgsfield-uretim` klasörünü şu iki yerden birine kopyala:
- her projede geçerli olsun: `~/.claude/skills/higgsfield-uretim`
- yalnız bir projede: `<proje>/.claude/skills/higgsfield-uretim`

Sonra Claude Code'u yeniden başlat ve isteğini yaz (ör. "bir görsel üretmek istiyorum"). Devreye girmezse `/higgsfield-uretim` yaz.

### Claude (claude.ai ya da masaüstü uygulaması)
`paket/higgsfield-uretim.skill` dosyasını ayarlardaki beceriler (Skills) bölümünden yükle. Menü adı sürüme göre değişebilir.

### ChatGPT ve diğer sohbet yardımcıları
`sohbet-paketi` klasörünü kullan:
- `talimat.txt` içeriğini bir Projenin (ya da özel talimat alanının) talimat kutusuna yapıştır,
- `bilgi-dosyalari` içindeki altı dosyayı aynı projeye dosya olarak yükle.

Not: ChatGPT özel GPT'leri kaldırıyor; Kasım 2026'da yeni GPT oluşturulamıyordu. Bu paket ChatGPT'de henüz denenmedi — menü adları farklı çıkabilir.

## API ile üretim (isteğe bağlı)
Yalnız Claude Code'da ve kendi Higgsfield API hesabınla çalışır.
1. open.higgsfield.ai üzerinden API anahtarı al ve bakiye yükle. (API dolar bakiyesi kullanır; sitedeki krediler API'de geçmez.)
2. Proje klasöründe `.env.local` adlı bir dosya aç ve iki satır yaz:
   ```
   HF_API_BASE_URL=<API adresi; anahtarı aldığın sayfada yazar>
   HF_CREDENTIALS=<anahtarın>
   ```
3. Bu dosyayı kimseyle paylaşma ve git'e ekleme. Anahtarını sohbete yapıştırma.

Gönderim, sürdürme ve kare çıkarma işlerini `higgsfield-uretim/scripts/hf.py` yapar (yalnız Python; video kareleri için ffmpeg gerekir).

## Para konusunda bilmen gerekenler
- Fiyat listelerindeki "from $X" yalnız en ucuz ayarın fiyatıdır. Gerçek bir denemede liste fiyatına göre ≈ $0.02 beklenen bir düzenleme net $0.13 tuttu.
- Beğenmediğin ama tamamlanan üretim de ücretlidir.
- Önce ucuz taslak (görselde birkaç seçenek, videoda kısa ve düşük çözünürlük), beğenirsen büyük boy.
- Higgsfield panelinde otomatik bakiye yükleme (auto top-up) açıksa kartından kendiliğinden para çekilebilir; ayarını kontrol et.

## Bu sürümde henüz doğrulanmayanlar
- `hf.py` ile gerçek ücretli gönderim (parçaları ayrı ayrı çalıştı; araç olarak ilk kullanımda dikkatle izle).
- Videoda yön ve uzaklık kilitlerinin gerçekten işe yaradığı.
- ChatGPT'de çalışması.
- Dosyalarda "DOĞRULANMADI" diye işaretli model ve ayar bilgileri.

## Klasörler
- `higgsfield-uretim/` — becerinin kendisi: `SKILL.md` (ana talimat), `references/` (rehberler), `scripts/hf.py`.
- `sohbet-paketi/` — API'siz sohbet yardımcıları için aynı içerik.
- `paket/` — Claude'a tek dosya olarak yüklenecek paket.

## Kaynak ve kullanım
İçerik, Higgsfield'in herkese açık blog ve eğitim materyallerinden çıkarılmış notlara ve kendi denemelerimize dayanır; örnek prompt'lar bize aittir. Higgsfield ile bir bağımız yoktur. Kişisel kullanım için paylaşılmıştır.
