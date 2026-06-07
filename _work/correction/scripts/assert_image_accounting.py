from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
IMAGE_MANIFEST = ROOT / "_work" / "correction" / "inventory" / "image_manifest.csv"
FINAL_MAPPING = ROOT / "_work" / "correction" / "inventory" / "final_figure_mapping.csv"
UNUSED = ROOT / "_work" / "correction" / "inventory" / "unused_notebook_images.csv"
SOURCE_NOTES = ROOT / "docs" / "kaynakca-ve-sekil-notlari.md"
PUBLIC_MD = [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md"))]


REASON_BY_ID = {
    "nb_img_001": "Kapak/üniversite görseli; public argümana hizmet etmiyor.",
    "nb_img_002": "İdari fotoğraf/yer tutucu; public argümana hizmet etmiyor.",
    "nb_img_004": "Tarihsel atmosfer görseli; Silahtarağa ve bakım görselleri aynı işlevi daha güçlü taşıyor.",
    "nb_img_006": "Modern santral atmosferi; operasyon argümanını daha doğrudan taşıyan bakım görseli seçildi.",
    "nb_img_009": "Modern santral atmosferi; argümana katkısı dekoratif kaldı.",
    "nb_img_010": "T3000 panel detayı; kontrol odası görseli insan-makine ilişkisini daha iyi taşıyor.",
    "nb_img_013": "Tarihsel türbin/jeneratör görseli; seçilen şeker fabrikası ve bakım görselleri yeterli bağlam veriyor.",
    "nb_img_015": "2. Dünya Savaşı kalite sapması metin olarak korundu; askeri görsel public akışı sertleştireceği için alınmadı.",
    "nb_img_016": "2. Dünya Savaşı kalite sapması metin olarak korundu; askeri görsel public akışı sertleştireceği için alınmadı.",
    "nb_img_017": "2. Dünya Savaşı kalite sapması metin olarak korundu; askeri görsel public akışı sertleştireceği için alınmadı.",
    "nb_img_018": "2. Dünya Savaşı kalite sapması metin olarak korundu; askeri görsel public akışı sertleştireceği için alınmadı.",
    "nb_img_019": "2. Dünya Savaşı kalite sapması metin olarak korundu; askeri görsel public akışı sertleştireceği için alınmadı.",
    "nb_img_020": "Finansal gösterge ekranı; public metinde finansal ölçek fikri görsel/yorumla sadeleştirildi.",
    "nb_img_023": "Logo/kurumsal görsel; şirket tanıtımı hissi verdiği için kullanılmadı.",
    "nb_img_025": "Global 500 ekranı; finansal ölçek fikri metin ve notebook denklemiyle taşındı.",
    "nb_img_026": "Global 500 karşılaştırma ekranı; finansal ölçek fikri metin ve notebook denklemiyle taşındı.",
    "nb_img_027": "Emisyon atmosfer görseli; hidrojen argümanını doğrudan taşımadığı için kullanılmadı.",
    "nb_img_028": "Hidrojen üretim payı/arka plan görseli; renk ve üretim yolu için daha açık görsel seçildi.",
    "nb_img_030": "Dizel jeneratör analojisi metinde korundu; görsel tekrar ve dağınıklık yaratıyordu.",
    "nb_img_031": "Dizel jeneratör analojisi metinde korundu; görsel tekrar ve dağınıklık yaratıyordu.",
    "nb_img_032": "Hidrojen üretim yolları tekrar görseli; seçilen üretim şeması yeterli oldu.",
    "nb_img_033": "Dizel jeneratör analojisi tekrar görseli; metin olarak taşındı.",
    "nb_img_035": "Hidrojen renkleri teknik tekrar; seçilen üretim şeması yeterli oldu.",
    "nb_img_036": "Elektroliz bağlamı var ama ana argümanı taşıyan üretim/depolama görselleri seçildi.",
    "nb_img_037": "Ülke/kurum teşvikleri için haber örneği; AB ve NREL örnekleri yeterli görüldü.",
    "nb_img_038": "Ülke/kurum teşvikleri için haber örneği; AB ve NREL örnekleri yeterli görüldü.",
    "nb_img_042": "Hidrojen lojistiği görseli; altyapı/depolama argümanı başka görsellerle daha net taşındı.",
    "nb_img_043": "Hidrojen lojistiği tekrar görseli; altyapı/depolama argümanı başka görsellerle daha net taşındı.",
    "nb_img_051": "İnsan/çeki hayvanı metin ekranı; public yazıda Markdown/LaTeX ile yeniden kuruldu.",
    "nb_img_052": "İnsan gücü dramatizasyonu; düşünce deneyini fazla teatral yaptığı için kullanılmadı.",
    "nb_img_053": "İnsan gücü dramatizasyonu; düşünce deneyini fazla teatral yaptığı için kullanılmadı.",
    "nb_img_054": "Gaz türbini parça detayı; operasyon/bakım ekonomisini doğrudan taşımıyor.",
    "nb_img_055": "Lorentz için alternatif görsel; yük devresi görseli model güncelleme fikrini daha net taşıyor.",
    "nb_img_056": "At fotoğrafı dekoratif kaldı; kalori kaynağı görseli düşünce deneyine daha doğrudan bağlı.",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def used_source_ids() -> set[str]:
    ids: set[str] = set()
    for row in read_csv(FINAL_MAPPING):
        for item in re.split(r"[;,]", row.get("source_image_id", "")):
            item = item.strip()
            if item:
                ids.add(item)
    return ids


def public_refs() -> set[str]:
    refs: set[str] = set()
    for md in PUBLIC_MD:
        text = md.read_text(encoding="utf-8", errors="replace")
        for target in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text):
            target = target.split("#", 1)[0].strip()
            if target.startswith("../"):
                target = target[3:]
            elif target.startswith("./"):
                target = target[2:]
            if target.startswith("assets/figures/"):
                refs.add(target)
    return refs


def source_table_paths() -> set[str]:
    text = SOURCE_NOTES.read_text(encoding="utf-8", errors="replace")
    return set(re.findall(r"`(assets/figures/[^`]+)`", text))


def refresh_unused() -> None:
    used = used_source_ids()
    rows = read_csv(IMAGE_MANIFEST)
    output: list[dict[str, str]] = []
    for row in rows:
        image_id = row["image_id"]
        if image_id in used:
            continue
        new_row = {
            "image_id": image_id,
            "sequence": row.get("sequence", ""),
            "sha256": row.get("sha256", ""),
            "width": row.get("width", ""),
            "height": row.get("height", ""),
            "original_name": row.get("original_name", ""),
            "nearest_heading": row.get("nearest_heading", ""),
            "previous_text": row.get("previous_text", ""),
            "next_text": row.get("next_text", ""),
            "suggested_target_file": "",
            "unused_reason": REASON_BY_ID.get(image_id, "Final public argümanına doğrudan katkısı zayıf veya tekrar niteliğinde."),
        }
        output.append(new_row)

    fieldnames = [
        "image_id", "sequence", "sha256", "width", "height", "original_name",
        "nearest_heading", "previous_text", "next_text", "suggested_target_file", "unused_reason",
    ]
    with UNUSED.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh-unused", action="store_true")
    args = parser.parse_args()

    if args.refresh_unused:
        refresh_unused()

    manifest = read_csv(IMAGE_MANIFEST)
    all_ids = {row["image_id"] for row in manifest}
    used = used_source_ids()
    unused_rows = read_csv(UNUSED)
    unused_ids = {row["image_id"] for row in unused_rows}
    failures: list[str] = []

    for image_id in sorted(used):
        if image_id not in all_ids:
            failures.append(f"used source image not in image_manifest -> {image_id}")

    expected_unused = all_ids - used
    missing_unused = sorted(expected_unused - unused_ids)
    stale_unused = sorted(unused_ids & used)
    for image_id in missing_unused:
        failures.append(f"unused image missing from unused_notebook_images.csv -> {image_id}")
    for image_id in stale_unused:
        failures.append(f"used image still listed as unused -> {image_id}")

    for row in unused_rows:
        if not row.get("unused_reason", "").strip():
            failures.append(f"unused row has empty reason -> {row.get('image_id')}")

    mapping_paths = {row["final_path"] for row in read_csv(FINAL_MAPPING)}
    refs = public_refs()
    table_paths = source_table_paths()
    if mapping_paths != refs:
        failures.append(f"final_figure_mapping/public refs mismatch mapping={len(mapping_paths)} refs={len(refs)}")
        for item in sorted(mapping_paths - refs):
            failures.append(f"mapped but not referenced -> {item}")
        for item in sorted(refs - mapping_paths):
            failures.append(f"referenced but not mapped -> {item}")
    if refs != table_paths:
        failures.append(f"source notes/public refs mismatch source_table={len(table_paths)} refs={len(refs)}")

    if failures:
        print("ASSERT_IMAGE_ACCOUNTING_FAIL")
        print("\n".join(failures))
        return 1

    print(f"ASSERT_IMAGE_ACCOUNTING_OK used_source_ids={len(used)} unused={len(unused_ids)} public_figures={len(refs)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

