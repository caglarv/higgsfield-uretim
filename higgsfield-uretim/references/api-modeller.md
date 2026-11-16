# API model haritası (yalnız üretim biçiminde)

Bilgi tarihi: 2026-11-16 — 103 mod, resmi kullanım kâğıtlarından ("Copy agent prompt" = `https://dash.higgsfield.ai/models/<yol>/llms.txt`). Liste ve fiyat değişir: seçtiğin modun güncel alanlarını ve fiyatını `hf.py sema <yol>` ile oku.

Okuma notu: bu kâğıtlar TEKNİK kullanım belgesidir (alanlar, zorunlular, fiyat, çağırma). Nasıl iyi prompt yazılacağını söylemezler; yazım için `video-prompt.md` / `gorsel-prompt.md`.

## İçindekiler
1. Nasıl seçilir
2. Video aileleri
3. Videodan video (hareketi koru, kişi/stil değiştir)
4. Görsel aileleri
5. Prompt'u kendiliğinden değiştiren ayarlar
6. Eksikler

## 1. Nasıl seçilir
- Bir işe tek modelle atlama. İşin ihtiyacını çıkar (bitiş karesi mi, referans video mu, ses mi, uzunluk, çözünürlük), bu dosyadan buna uyan 2–3 adayı bul, her birinin 5 sn (ya da istenen süre) fiyatını hesapla, birini gerekçesiyle seç ve kullanıcıya tek satırda söyle. Neden: model başına fiyat 10 kat oynuyor ve hiçbir model her işte en iyisi değil; kendi denememiz şimdilik yalnız Seedance 2.5.
- Kalite karşılaştırması ancak gerçek çıktıyla yapılır. Önemli bir işte 2 adayı en ucuz ayarda birer taslakla denemek (iki ayrı ücret, iki onay) tek pahalı denemeden çoğu zaman ucuzdur.
- Yön, poz ya da hareket şekli işin özüyse yazıya güvenme: bitiş karesi ya da hareket kopyalama destekleyen modu seç (bkz. `video-prompt.md` §7).

## 2. Video aileleri (liste fiyatı, saniye başı)
- **Seedance 2.5** (`bytedance/seedance-2.5/...`): `text-to-video`, `image-to-video` (`image_url` zorunlu, `end_image_url` = bitiş karesi), `reference-to-video` (`image_urls`/`video_urls`/`audio_urls`), `video-edit`, `video-extend`, `finalize-draft` (`draft_id`). 4–30 sn. 480p $0.1177 · 720p $0.2647 · 1080p $0.6518; edit/extend 480p $0.1387. `draft: true` = 480p taslak, 7 gün içinde 1080p'ye çevrilir (ayrı ücret). Denendi: dans, konum tuttu, yön tutmadı.
- **Seedance 2.0**: t2v, i2v (`end_image_url`), reference. 480p $0.0804 · 720p $0.1735 · 1080p $0.4293 · 4K $0.8907.
- **Kling 3.0** (`kling-video/v3.0/std|pro|4k/text-to-video|image-to-video`): std 720p $0.0714 · pro 1080p $0.0962 · 4K $0.3151. i2v'de `last_image_url` (bitiş karesi), `multi_prompt` (6 çekime kadar, her biri kendi süresiyle), `cfg_scale` 0–1 (prompt'a bağlılık, varsayılan 0.5), `sound`, `elements`. **Turbo** (`v3.0-turbo`) 720p $0.0839.
- **Kling O3 / Omni** (`kling-video/o3|omni/...`): `first-last-frame` (ilk + son kare), `image-reference`, `video-reference`, `video-edit`. O3 720p $0.0683 · Omni 720p $0.0632; video modları $0.0945.
- **Kling 4.0** (`kling-video/v4.0/...`): t2v, i2v (`end_image_url`, ek `image_urls`), reference, video-edit; 30 sn'ye kadar. 720p $0.1257 · 1080p $0.1879. **4.0 Flash**: 720p; reference $0.094.
- **Kling 2.6 pro** 1080p $0.0666 (`sound`) · **Kling 2.5 turbo** std 720p $0.0315 / pro 1080p $0.0525 (`negative_prompt`).
- **Wan 3.0** (`alibaba/wan-3.0/...`): t2v, i2v (`end_image_url`), reference. 480p **$0.0375** · 720p $0.075 · 1080p $0.15. **Wan 3.0 Prime** 480p $0.051. Ses: `generate_audio`.
- **Wan 2.6 / 2.7** (`wan/v2.6|v2.7/...`): 720p ≈ $0.075; `negative_prompt`; 2.7 i2v'de `end_image_url`; 2.6'da `multi_shots`.
- **MiniMax H3** (`minimax/h3/...`): t2v, i2v (`end_image_url`), reference (2K $0.13/sn, 5 referanstan sonrası $0.08/adet). **Hailuo 2.3** (`minimax/hailuo-2.3/standard/...`): t2v, i2v; fiyat kâğıtta yok.
- **PixVerse 6** (i2v `end_image_url`, `negative_prompt`), **LTX 2.5** fast/pro (i2v `end_image_url`, `camera_movement`: static, dolly_in/out/left/right, jib_up/down, focus_shift), **Happy Horse** (1.0 / 1.1), **Grok Imagine Video 1.5** (reference) — fiyat kâğıtta yok; fiyat sayfasından oku.
- **Cinema Studio 4.0** (`higgsfield/cinema-studio/4.0`): 30 sn'ye kadar, otomatik sahne yönetimi; kamera/lens/ışık/dönem/renk alanları; token ile ücretlenir (hesap kâğıtta).

## 3. Videodan video — hareketi koru
- **Kling 3.0 Motion Control** (`kling-video/v3/motion-control/std|pro`): bir resmi (`image_url`) verilen videodaki (`video_url`) hareketle canlandırır. `character_orientation`: `video` (yön ve dönüş videodan; varsayılan) ya da `image`. std 720p $0.0920 · pro 1080p $0.1189; ücret referans videonun süresi kadar. Eski sürüm `kling-video/motion-control/std` 720p $0.0523. Yön kesin olsun isteniyorsa en sağlam yol (kendi çektiğin kısa bir video gerekir).
- **Genjutsu** (`higgsfield/genjutsu/...`): `motion-transfer` (kişi/mekân/stili değiştir, hareketi koru), `object-swap`, `restyle` (`preset_id` zorunlu, ≈ $0.318/sn 480p). motion-transfer/object-swap 480p $0.154. **Genjutsu Light** 480p $0.0739. Girdi: `video_url` + `image_urls`.

## 4. Görsel aileleri
- **Soul 2** (`higgsfield-ai/soul/v2/standard`, `.../image-to-image`): `custom_reference_id` (Soul ID), `enhance_prompt`, `batch_size`. **Soul ID** (`soul-id`): 1–100 fotoğraf (`input_images`), $2.50.
- **Marketing Studio Image** (`marketing-studio/image`, `/flare`, `/sunburst`): üretir ve düzenler (`image_urls`). `quality` low/medium/**high (varsayılan)**; ücret token ile — çekilen tutar tahmin, sonra düzeltilir. Her gönderimde `quality`yi açıkça yaz.
- **Grok Imagine 2.0** (`xai/grok-imagine-image-2.0`): `image_urls`, `quality`. **Qwen Image 3**: t2i + `edit` (`image_urls`, `negative_prompt`). **Ideogram 4.0**: yazılı afiş/ambalaj, düzenleme (`image_url`). **Z-Image Turbo**: hızlı, Çince/İngilizce yazı. **Recraft 4.1**: marka renkleri, illüstrasyon. **AI Influencer**: karakter sayfası $0.05. **Ads Studio**: brief'ten reklam (token ücreti).

## 5. Prompt'u kendiliğinden değiştiren ayarlar
Varsayılanı AÇIK: Hailuo `prompt_optimizer`, Soul `enhance_prompt`. Varsayılanı kapalı: Wan `prompt_extend`, Wan 3.0 `enable_thinking`, Qwen `prompt_extend`. Kendi prompt'unu gönderiyorsan açıkları `false` yap; `hf.py kontrol` açık kalanı uyarır. Neden: model yazdığın yön, konum ve kilitleri kendi cümlesiyle değiştirir.

## 6. Eksikler
- `workflows/*` (ads-studio, cinema-studio-4-0, genjutsu, graphic-ads, marketplace-design, product-shots) için kullanım kâğıdı yok (404).
- Fiyatı kâğıtta yazmayanlar: Hailuo 2.3, PixVerse 6, LTX 2.5, Happy Horse, Grok Video, Kling 4.0 Flash t2v/i2v, Soul 2, birçok görsel modeli. Fiyat sayfasından oku; okuyamazsan "≈ tahmin, doğrulanmadı".
- Kalite karşılaştırması yok; yalnız Seedance 2.5, Soul 2 ve Marketing Studio gerçekten denendi.
