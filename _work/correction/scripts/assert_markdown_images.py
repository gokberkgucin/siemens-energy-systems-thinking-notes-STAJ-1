from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PUBLIC_MD = [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md"))]
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def normalize_asset_ref(ref: str, md_file: Path) -> str:
    ref = ref.split("#", 1)[0].strip()
    if ref.startswith("../"):
        return ref[3:]
    if ref.startswith("./"):
        return ref[2:]
    return ref


def figure_table_paths() -> set[str]:
    source = ROOT / "docs" / "kaynakca-ve-sekil-notlari.md"
    text = source.read_text(encoding="utf-8", errors="replace")
    return set(re.findall(r"`(assets/figures/[^`]+)`", text))


def main() -> int:
    failures: list[str] = []
    image_refs: set[str] = set()
    image_count = 0
    link_count = 0

    for md_file in PUBLIC_MD:
        text = md_file.read_text(encoding="utf-8", errors="replace")
        rel = md_file.relative_to(ROOT).as_posix()

        for alt, target in IMAGE_RE.findall(text):
            image_count += 1
            if not alt.strip():
                failures.append(f"{rel}: empty image alt -> {target}")
            if md_file.name == "README.md" and not (
                target.startswith("./assets/") or target.startswith("http://") or target.startswith("https://")
            ):
                failures.append(f"{rel}: README image path must start with ./assets/ -> {target}")
            if md_file.parent.name == "docs" and not (
                target.startswith("../assets/") or target.startswith("http://") or target.startswith("https://")
            ):
                failures.append(f"{rel}: docs image path must start with ../assets/ -> {target}")

            if re.match(r"^(https?|mailto):", target):
                continue
            resolved = (md_file.parent / target.split("#", 1)[0]).resolve()
            if not resolved.exists():
                failures.append(f"{rel}: broken image -> {target}")
            image_refs.add(normalize_asset_ref(target, md_file))

        for target in LINK_RE.findall(text):
            link_count += 1
            if re.match(r"^(https?|mailto):", target):
                continue
            target_path = target.split("#", 1)[0].strip()
            if not target_path:
                continue
            resolved = (md_file.parent / target_path).resolve()
            if not resolved.exists():
                failures.append(f"{rel}: broken markdown link -> {target}")

    table_paths = figure_table_paths()
    public_figure_refs = {ref for ref in image_refs if ref.startswith("assets/figures/")}
    if public_figure_refs != table_paths:
        missing_in_table = sorted(public_figure_refs - table_paths)
        stale_in_table = sorted(table_paths - public_figure_refs)
        for item in missing_in_table:
            failures.append(f"figure table missing public ref -> {item}")
        for item in stale_in_table:
            failures.append(f"figure table has stale ref -> {item}")

    if failures:
        print("ASSERT_MARKDOWN_IMAGES_FAIL")
        print("\n".join(failures))
        return 1

    print(f"ASSERT_MARKDOWN_IMAGES_OK images={image_count} links={link_count} figure_refs={len(public_figure_refs)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

