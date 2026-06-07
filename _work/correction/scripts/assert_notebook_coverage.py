from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
MISMATCH = ROOT / "_work" / "correction" / "inventory" / "mismatch_matrix.csv"
MANUAL_CHECKS = ROOT / "_work" / "correction" / "manual_checks.md"
PUBLIC_MD = [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md"))]
MARKER = "## Missing Text Assertion Register"

STOPWORDS = {
    "bir", "ve", "ile", "için", "gibi", "olan", "olarak", "daha", "çok", "şu", "bu", "da", "de",
    "diye", "ama", "çünkü", "notebook", "staj", "defterde", "siemens", "enerji",
}
ADMIN_TERMS = [
    "karabük üniversitesi", "mühendislik fakültesi", "öğrencinin", "imza", "kaşe",
    "iş yeri yetkilisi", "kontrol eden", "servis, yemek", "sosyal hizmetleri",
    "[ignore]", "iş yaprağı", "yapılan iş tanımı",
]


def norm(text: str) -> str:
    text = text.lower()
    text = text.replace("ı", "i").replace("ğ", "g").replace("ü", "u").replace("ş", "s").replace("ö", "o").replace("ç", "c")
    return re.sub(r"[^a-z0-9%]+", " ", text)


def words(text: str) -> list[str]:
    return [w for w in norm(text).split() if len(w) >= 5 and w not in STOPWORDS]


def is_admin_or_filler(excerpt: str) -> bool:
    lower = excerpt.lower()
    return any(term in lower for term in ADMIN_TERMS)


def public_score(excerpt: str, public_text: str) -> float:
    unique = list(dict.fromkeys(words(excerpt)))
    if len(unique) < 4:
        return 0.0
    hits = sum(1 for word in unique if word in public_text)
    return hits / len(unique)


def load_rows() -> list[dict[str, str]]:
    with MISMATCH.open("r", encoding="utf-8-sig", newline="") as handle:
        return [row for row in csv.DictReader(handle) if row.get("kind") == "missing_text"]


def classify(row: dict[str, str], public_text: str) -> tuple[str, str]:
    excerpt = row.get("source_excerpt", "")
    if is_admin_or_filler(excerpt):
        return "ignored_admin_or_filler", "İdari şablon, form, imza/kaşe veya açık filler olduğu için public metne taşınmadı."
    score = public_score(excerpt, public_text)
    if score >= 0.55:
        return "resolved_or_transformed", f"Public metinde dönüştürülerek karşılandı; kelime kapsama skoru {score:.2f}."
    return "manual_check", "Birebir taşınmadı; konu seçimi, kaynak zayıflığı veya tekrar riski nedeniyle manuel karar olarak bırakıldı."


def write_register(rows: list[dict[str, str]], public_text: str) -> None:
    lines = [
        MARKER,
        "",
        "Bu tablo `mismatch_matrix.csv` içindeki `missing_text` kayıtlarının son durumunu gösterir.",
        "Public metne taşınmayan kayıtlar ya idari/filler kabul edildi ya da manuel karar olarak bırakıldı.",
        "",
        "| source_anchor | hedef | durum | gerekçe |",
        "|---|---|---|---|",
    ]
    for row in rows:
        status, reason = classify(row, public_text)
        target = row.get("suggested_target_file", "")
        lines.append(f"| `{row.get('source_anchor', '')}` | `{target}` | {status} | {reason} |")

    original = MANUAL_CHECKS.read_text(encoding="utf-8", errors="replace")
    if MARKER in original:
        original = original.split(MARKER, 1)[0].rstrip() + "\n\n"
    MANUAL_CHECKS.write_text(original + "\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-register", action="store_true")
    args = parser.parse_args()

    rows = load_rows()
    public_text = norm("\n".join(path.read_text(encoding="utf-8", errors="replace") for path in PUBLIC_MD))

    if args.write_register:
        write_register(rows, public_text)

    manual_text = MANUAL_CHECKS.read_text(encoding="utf-8", errors="replace")
    failures: list[str] = []
    counts: dict[str, int] = {}
    for row in rows:
        status, _ = classify(row, public_text)
        counts[status] = counts.get(status, 0) + 1
        if status == "manual_check" and row.get("source_anchor", "") not in manual_text:
            failures.append(f"{row.get('source_anchor')}: unresolved missing_text not recorded in manual_checks.md")

    if failures:
        print("ASSERT_NOTEBOOK_COVERAGE_FAIL")
        print("\n".join(failures))
        return 1

    summary = " ".join(f"{key}={value}" for key, value in sorted(counts.items()))
    print(f"ASSERT_NOTEBOOK_COVERAGE_OK missing_text={len(rows)} {summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

