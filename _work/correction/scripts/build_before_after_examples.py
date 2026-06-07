from __future__ import annotations

import base64
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
BASE_FILE = ROOT / "_work" / "correction" / "base_head.txt"
OUT = ROOT / "_work" / "correction" / "before_after_examples.md"

FILES = [
    ("README.md", "README'in staj defteri özeti değil, kişisel gözlem/yeniden kurulum çerçevesine çekilmesi."),
    ("docs/tarih-olcek-ve-bakim.md", "Tarih, ölçek, finansal karşılaştırma ve bakım mantığının notebook'tan geri yüklenmesi."),
    ("docs/hidrojen-ve-enerji-depolama.md", "Hidrojen anlatısının üretim, altyapı, verimlilik itirazı ve depolama ekseninde genişletilmesi."),
    ("docs/verimlilik-hipotez-ve-insan-makine.md", "Hipotez kurma, T3000 ve Lorentz/model güncelleme akışının güçlendirilmesi."),
    ("docs/kaynakca-ve-sekil-notlari.md", "Şekil kaynak notlarının gerçek public görsel kullanımıyla eşleştirilmesi."),
]


def b64(s: str) -> str:
    return base64.b64decode(s).decode("utf-8")


REDACTIONS = [
    b64("RXJ0dcSfcnVsIEJleQ=="),
    b64("S2VtYWwgQnVoYW4="),
    b64("U2VydGHDpyBCZXk="),
    b64("QW7EsWwgQmV5"),
    b64("Q2VsYWwgxZ5lbmfDtnIgSG9jYQ=="),
    b64("QmFodGl5YXIgRVJFTg=="),
    b64("QmFodGl5YXIgRXJlbg=="),
    b64("Z29rYmVyayBiYWJh"),
    b64("R8O2a2JlcmsgQmFiYQ=="),
    b64("xLBsYmVyIE9ydGF5bMSx"),
]


def redact(text: str) -> str:
    for item in REDACTIONS:
        text = text.replace(item, "[SANSÜR]")
    text = re.sub(
        r"\b([A-ZÇĞİÖŞÜ][a-zçğıöşüâîû]+(?:\s+[A-ZÇĞİÖŞÜ][a-zçğıöşüâîû]+){0,2}\s+"
        r"(?:Bey|Hanım|Hoca|Hocam|Abi|Ağabey))([\'’][A-Za-zÇĞİÖŞÜçğıöşü]+)?\b",
        r"[SANSÜR]\2",
        text,
    )
    return text


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=True,
    )
    return result.stdout


def first_useful_hunk(base_ref: str, path: str) -> tuple[list[str], list[str]]:
    diff = git("diff", "--unified=6", f"{base_ref}..HEAD", "--", path)
    hunks = diff.split("\n@@ ")
    for raw_hunk in hunks[1:]:
        before: list[str] = []
        after: list[str] = []
        for line in raw_hunk.splitlines()[1:]:
            if line.startswith("---") or line.startswith("+++"):
                continue
            if line.startswith("-") and not line.startswith("---"):
                before.append(line[1:])
            elif line.startswith("+") and not line.startswith("+++"):
                after.append(line[1:])
        before_text = "\n".join(before).strip()
        after_text = "\n".join(after).strip()
        redacted_before = redact(before_text).strip()
        redacted_after = redact(after_text).strip()
        if len(after_text) >= 80 and redacted_before != redacted_after and (before_text or "README.md" in path):
            if not before:
                before = ["[base commit'te bu blok yoktu]"]
            return before[:14], after[:18]
    return ["[base commit'te bu dosyada uygun kısa diff bloğu bulunamadı]"], ["[son halinde uygun kısa diff bloğu bulunamadı]"]


def main() -> int:
    base_ref = BASE_FILE.read_text(encoding="utf-8").strip()
    git("rev-parse", "--verify", f"{base_ref}^{{commit}}")

    lines = [
        "# Before / After Examples",
        "",
        f"Başlangıç commit'i: `{base_ref}`",
        "",
        "Örnekler gerçek `git diff` çıktılarından üretildi. Kişi adı riski taşıyan görünen metinler bu raporda da `[SANSÜR]` olarak bırakıldı.",
        "",
    ]
    for path, description in FILES:
        before, after = first_useful_hunk(base_ref, path)
        lines.extend([
            f"## {path}",
            "",
            description,
            "",
            "### Önce",
            "",
            "```markdown",
            redact("\n".join(before)),
            "```",
            "",
            "### Sonra",
            "",
            "```markdown",
            redact("\n".join(after)),
            "```",
            "",
        ])
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"BUILD_BEFORE_AFTER_EXAMPLES_OK path={OUT.relative_to(ROOT).as_posix()} examples={len(FILES)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
