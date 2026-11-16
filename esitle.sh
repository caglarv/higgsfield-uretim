#!/bin/sh
# Depodaki beceriyi bu bilgisayardaki kopyalara ve paketlere eşitler.
# Kullanım: sh esitle.sh   (beceri-repo klasöründen)
set -e
cd "$(dirname "$0")"
K=higgsfield-uretim
[ -d ../.claude/skills ] && rsync -a --delete --exclude __pycache__ "$K/" "../.claude/skills/$K/" && echo "proje kopyası eşitlendi"
[ -d "$HOME/.codex/skills" ] && rsync -a --delete --exclude __pycache__ "$K/" "$HOME/.codex/skills/$K/" && echo "Codex kopyası eşitlendi"
# sohbet paketi: ana talimatın gövdesi (API'ye özgü satırlar çıkarılır) + rehberler (API dosyası hariç)
python3 - <<'PY'
import pathlib, shutil
k = pathlib.Path("higgsfield-uretim")
s = (k/"SKILL.md").read_text(encoding="utf-8").split("---", 2)[2].strip() + "\n"
s = s.replace("`references/", "`")
s = s.replace("`api-claude-code.md` ve `scripts/hf.py` — yalnız üretim biçiminde. Bir GPT'ye ya da sohbet projesine bilgi dosyası yüklerken bu ikisini yükleme.", "(API dosyaları bu pakete dahil değildir; burada hep prompt biçiminde çalışırsın.)")
s = s.replace("`api-claude-code.md` dosyasını oku.", "(Bu ortamda geçerli değil.)")
pathlib.Path("sohbet-paketi/talimat.txt").write_text(s, encoding="utf-8")
for f in (k/"references").glob("*.md"):
    if f.name != "api-claude-code.md":
        shutil.copy(f, "sohbet-paketi/bilgi-dosyalari/")
print("sohbet paketi eşitlendi:", len(s), "karakter")
PY
rm -f paket/higgsfield-uretim.skill
(cd "$K/.." && zip -qr "paket/higgsfield-uretim.skill" "$K" -x "*/__pycache__/*" "*.DS_Store") && echo "Claude paketi yenilendi"
