#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Notebook ile mevcut repo arasındaki kaynak envanteri ve fark matrisi."""

from __future__ import annotations

import argparse
import csv
import difflib
import hashlib
import json
import os
import re
import struct
import zipfile
from collections import defaultdict
from pathlib import Path, PurePosixPath
from urllib.parse import unquote
import xml.etree.ElementTree as ET


IGNORE_LINE_RE = re.compile(
    r"^\s*(?:İŞ\s*YAPRAĞI|İş Yeri Yetkilisi|İmza,\s*Kaşe|Yapılan İş Tanımı|"
    r"İş Tarihi|Sayfa Numarası:.*|KARABÜK ÜNİVERSİTESİ|MÜHENDİSLİK FAKÜLTESİ|"
    r"Staj Genel Bilgileri|Staj Yapan Öğrenci|Staj Yapılan İş Yeri|Staj Komisyonu|"
    r"Defter Kontrolü|Onay|x|\.{1,}|…+)\s*$"
)

NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp", ".tif", ".tiff"}
EXPECTED_PUBLIC_MD = [
    "README.md",
    "docs/tarih-olcek-ve-bakim.md",
    "docs/hidrojen-ve-enerji-depolama.md",
    "docs/verimlilik-hipotez-ve-insan-makine.md",
    "docs/kaynakca-ve-sekil-notlari.md",
]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def rel_path(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def safe_excerpt(text: str, limit: int = 240) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def normalize_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\[[0-9]+\]", " ", text)
    text = re.sub(r"\([0-9]+\)", " ", text)
    text = re.sub(r"\b[0-9]{1,3}\b", lambda m: f" {m.group(0)} ", text)
    text = re.sub(r"[^\wçğıöşüâîû]+", " ", text, flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", text).strip()


def image_size_from_bytes(data: bytes) -> tuple[int | None, int | None]:
    if len(data) >= 24 and data[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", data[16:24])
    if len(data) >= 10 and data[:6] in (b"GIF87a", b"GIF89a"):
        return struct.unpack("<HH", data[6:10])
    if len(data) >= 26 and data[:2] == b"BM":
        return struct.unpack("<II", data[18:26])
    if len(data) >= 12 and data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        chunk = data[12:16]
        if chunk == b"VP8X" and len(data) >= 30:
            width = int.from_bytes(data[24:27], "little") + 1
            height = int.from_bytes(data[27:30], "little") + 1
            return width, height
        if chunk == b"VP8 " and len(data) >= 30:
            width = struct.unpack("<H", data[26:28])[0] & 0x3FFF
            height = struct.unpack("<H", data[28:30])[0] & 0x3FFF
            return width, height
    if len(data) >= 4 and data[:2] == b"\xff\xd8":
        i = 2
        while i + 9 < len(data):
            if data[i] != 0xFF:
                i += 1
                continue
            marker = data[i + 1]
            i += 2
            while marker == 0xFF and i < len(data):
                marker = data[i]
                i += 1
            if marker in (0xD8, 0xD9):
                continue
            if i + 2 > len(data):
                break
            seg_len = struct.unpack(">H", data[i : i + 2])[0]
            if seg_len < 2 or i + seg_len > len(data):
                break
            if marker in {
                0xC0,
                0xC1,
                0xC2,
                0xC3,
                0xC5,
                0xC6,
                0xC7,
                0xC9,
                0xCA,
                0xCB,
                0xCD,
                0xCE,
                0xCF,
            }:
                height = struct.unpack(">H", data[i + 3 : i + 5])[0]
                width = struct.unpack(">H", data[i + 5 : i + 7])[0]
                return width, height
            i += seg_len
    return None, None


def paragraph_text(p: ET.Element) -> str:
    parts: list[str] = []
    for node in p.iter():
        if node.tag == f"{{{NS['w']}}}t":
            parts.append(node.text or "")
        elif node.tag == f"{{{NS['w']}}}tab":
            parts.append("\t")
        elif node.tag == f"{{{NS['w']}}}br":
            parts.append("\n")
    return "".join(parts).strip()


def paragraph_style(p: ET.Element) -> str:
    style = p.find("./w:pPr/w:pStyle", NS)
    if style is None:
        return ""
    return style.attrib.get(f"{{{NS['w']}}}val", "")


def is_heading(style: str, text: str) -> bool:
    lowered = style.lower()
    if lowered.startswith("heading") or "başlık" in lowered or lowered.startswith("title"):
        return True
    stripped = text.strip()
    return bool(stripped and len(stripped) <= 80 and stripped.isupper() and not IGNORE_LINE_RE.match(stripped))


def blip_rel_ids(p: ET.Element) -> list[str]:
    ids: list[str] = []
    for blip in p.findall(".//a:blip", NS):
        rid = blip.attrib.get(f"{{{NS['r']}}}embed") or blip.attrib.get(f"{{{NS['r']}}}link")
        if rid:
            ids.append(rid)
    return ids


def iter_docx_paragraphs(body: ET.Element):
    for child in list(body):
        if child.tag == f"{{{NS['w']}}}p":
            yield child
        elif child.tag == f"{{{NS['w']}}}tbl":
            for p in child.findall(".//w:p", NS):
                yield p


def parse_relationships(zf: zipfile.ZipFile) -> dict[str, str]:
    rels: dict[str, str] = {}
    rel_xml = ET.fromstring(zf.read("word/_rels/document.xml.rels"))
    for rel in rel_xml.findall("rel:Relationship", NS):
        rid = rel.attrib.get("Id")
        target = rel.attrib.get("Target", "")
        if not rid or not target or target.startswith(("http://", "https://")):
            continue
        if target.startswith("/"):
            normalized = target.lstrip("/")
        else:
            normalized = str(PurePosixPath("word") / target)
        rels[rid] = normalized
    return rels


def extract_docx(docx_path: Path, extract_dir: Path) -> tuple[list[dict], list[dict], dict]:
    image_dir = extract_dir / "notebook_images"
    image_dir.mkdir(parents=True, exist_ok=True)

    text_blocks: list[dict] = []
    image_events: list[dict] = []
    blocks: list[dict] = []
    extracted_by_media: dict[str, dict] = {}

    with zipfile.ZipFile(docx_path) as zf:
        rels = parse_relationships(zf)
        document = ET.fromstring(zf.read("word/document.xml"))
        body = document.find("w:body", NS)
        if body is None:
            raise RuntimeError("DOCX içinde word/document.xml body bulunamadı.")

        nearest_heading = ""
        block_index = 0
        image_seq = 0

        for p in iter_docx_paragraphs(body):
            text = paragraph_text(p)
            style = paragraph_style(p)
            if text:
                block_index += 1
                ignore = bool(IGNORE_LINE_RE.match(text))
                if is_heading(style, text):
                    nearest_heading = text
                row = {
                    "block_index": block_index,
                    "text": text,
                    "style": style,
                    "nearest_heading": nearest_heading,
                    "ignore_line": ignore,
                    "normalized": normalize_text(text),
                }
                text_blocks.append(row)
                blocks.append({"type": "text", "text": text, "block_index": block_index})

            for rid in blip_rel_ids(p):
                media = rels.get(rid)
                if not media or media not in zf.namelist():
                    continue
                image_seq += 1
                data = zf.read(media)
                digest = sha256_bytes(data)
                width, height = image_size_from_bytes(data)
                original_name = Path(media).name
                if media not in extracted_by_media:
                    out_name = f"notebook_img_{image_seq:03d}_{original_name}"
                    out_path = image_dir / out_name
                    out_path.write_bytes(data)
                    extracted_by_media[media] = {
                        "extracted_path": out_path,
                        "first_sequence": image_seq,
                    }
                else:
                    out_path = extracted_by_media[media]["extracted_path"]

                event = {
                    "image_id": f"nb_img_{image_seq:03d}",
                    "sequence": image_seq,
                    "relationship_id": rid,
                    "original_name": original_name,
                    "docx_media_path": media,
                    "extracted_path": out_path,
                    "sha256": digest,
                    "width": width,
                    "height": height,
                    "nearest_heading": nearest_heading,
                    "previous_text": "",
                    "next_text": "",
                }
                image_events.append(event)
                blocks.append({"type": "image", "image_id": event["image_id"]})

    image_by_id = {event["image_id"]: event for event in image_events}
    for i, block in enumerate(blocks):
        if block["type"] != "image":
            continue
        event = image_by_id[block["image_id"]]
        for prev in reversed(blocks[:i]):
            if prev["type"] == "text" and prev["text"].strip():
                event["previous_text"] = prev["text"]
                break
        for nxt in blocks[i + 1 :]:
            if nxt["type"] == "text" and nxt["text"].strip():
                event["next_text"] = nxt["text"]
                break

    stats = {
        "text_block_count": len(text_blocks),
        "image_count": len(image_events),
        "unique_image_sha_count": len({event["sha256"] for event in image_events}),
    }
    return text_blocks, image_events, stats


def parse_markdown_file(path: Path, repo_root: Path) -> tuple[list[dict], list[dict]]:
    text = path.read_text(encoding="utf-8", errors="replace")
    rel = rel_path(path, repo_root)
    blocks: list[dict] = []
    images: list[dict] = []
    heading = ""
    paragraph: list[str] = []
    block_index = 0
    image_re = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")

    def flush_paragraph() -> None:
        nonlocal paragraph, block_index
        content = "\n".join(paragraph).strip()
        paragraph = []
        if not content:
            return
        block_index += 1
        blocks.append(
            {
                "file_path": rel,
                "block_index": block_index,
                "block_type": "text",
                "heading_context": heading,
                "text": content,
                "normalized_text": normalize_text(content),
                "ignore_line": bool(IGNORE_LINE_RE.match(content)),
                "image_alt": "",
                "image_target": "",
                "image_resolved": "",
                "image_exists": "",
            }
        )

    for line in text.splitlines():
        if line.startswith("#"):
            flush_paragraph()
            heading = line.lstrip("#").strip()
            block_index += 1
            blocks.append(
                {
                    "file_path": rel,
                    "block_index": block_index,
                    "block_type": "heading",
                    "heading_context": heading,
                    "text": line.strip(),
                    "normalized_text": normalize_text(line),
                    "ignore_line": False,
                    "image_alt": "",
                    "image_target": "",
                    "image_resolved": "",
                    "image_exists": "",
                }
            )
            continue
        for match in image_re.finditer(line):
            target = match.group(2).strip()
            clean = unquote(target.split("#", 1)[0])
            resolved = ""
            exists = ""
            if clean and not re.match(r"^(https?://|mailto:)", clean):
                resolved_path = (path.parent / clean).resolve()
                resolved = rel_path(resolved_path, repo_root)
                exists = str(resolved_path.exists())
            image_row = {
                "file_path": rel,
                "block_index": block_index + 1,
                "block_type": "image",
                "heading_context": heading,
                "text": "",
                "normalized_text": "",
                "ignore_line": False,
                "image_alt": match.group(1),
                "image_target": target,
                "image_resolved": resolved,
                "image_exists": exists,
            }
            images.append(image_row)
            blocks.append(image_row)
        if line.strip():
            paragraph.append(line)
        else:
            flush_paragraph()
    flush_paragraph()
    return blocks, images


def find_public_files(repo_root: Path) -> list[dict]:
    all_md = [p for p in repo_root.rglob("*.md") if ".git" not in p.parts]
    rows: list[dict] = []
    for expected in EXPECTED_PUBLIC_MD:
        expected_path = repo_root / expected
        if expected_path.exists():
            rows.append(
                {
                    "expected_path": expected,
                    "resolved_path": expected,
                    "resolution_reason": "birebir bulundu",
                }
            )
            continue
        best_path = ""
        best_score = 0.0
        for candidate in all_md:
            score = difflib.SequenceMatcher(None, expected.lower(), rel_path(candidate, repo_root).lower()).ratio()
            if score > best_score:
                best_score = score
                best_path = rel_path(candidate, repo_root)
        rows.append(
            {
                "expected_path": expected,
                "resolved_path": best_path,
                "resolution_reason": f"birebir yok; en yakın eşleşme skoru {best_score:.3f}",
            }
        )
    return rows


def suggested_target(text: str, heading: str) -> str:
    probe = f"{heading} {text}".lower()
    if any(k in probe for k in ["hidrojen", "elektroliz", "batarya", "depolama", "yenilenebilir"]):
        return "docs/hidrojen-ve-enerji-depolama.md"
    if any(k in probe for k in ["verimlilik", "etkililik", "etkinlik", "t3000", "lorentz", "jeneratör", "operatör", "çeki", "at "]):
        return "docs/verimlilik-hipotez-ve-insan-makine.md"
    if any(k in probe for k in ["silahtarağa", "telgraf", "siemens", "bakım", "türbin", "santral", "ölçek", "tarih"]):
        return "docs/tarih-olcek-ve-bakim.md"
    return "README.md"


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_notebook_full_text(path: Path, docx_path: Path, blocks: list[dict]) -> None:
    lines = [
        "# Notebook Full Text",
        "",
        f"Kaynak DOCX: `{docx_path}`",
        "",
        "Paragraf sırası korunmuştur. Gürültü satırları silinmedi; sadece envanter CSV'lerinde `ignore_line` olarak işaretlendi.",
        "",
    ]
    for block in blocks:
        prefix = f"[{block['block_index']:04d}]"
        if block["ignore_line"]:
            prefix += " [IGNORE]"
        lines.append(f"{prefix} {block['text']}")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", required=True)
    parser.add_argument("--workspace-root", required=True)
    parser.add_argument("--docx", default="")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    workspace_root = Path(args.workspace_root).resolve()
    correction_root = repo_root / "_work" / "correction"
    extract_root = correction_root / "extract"
    inventory_root = correction_root / "inventory"
    extract_root.mkdir(parents=True, exist_ok=True)
    inventory_root.mkdir(parents=True, exist_ok=True)

    docx_candidates = []
    if args.docx:
        docx_candidates.append(Path(args.docx))
    patterns = [
        "EK-09*Siemens*Staj*Genel*Gozlemler*.docx",
        "EK-09*Siemens*Staj*Genel*Gözlemler*.docx",
        "*Siemens*Staj*Genel*Gozlemler*.docx",
        "*Siemens*Staj*Genel*Gözlemler*.docx",
    ]
    for pattern in patterns:
        docx_candidates.extend(workspace_root.rglob(pattern))
    docx_candidates = [p.resolve() for p in docx_candidates if p.exists()]
    docx_path = docx_candidates[0] if docx_candidates else None

    prompt_patterns = [
        "İlk Siemens Stajı İçin Ardışık Codex Promptları.md",
        "*Ardışık*Codex*Promptları*.md",
    ]
    prompt_candidates: list[Path] = []
    for pattern in prompt_patterns:
        prompt_candidates.extend(workspace_root.rglob(pattern))

    public_resolved = find_public_files(repo_root)
    (inventory_root / "public_md_resolved.json").write_text(
        json.dumps(public_resolved, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    if docx_path is None:
        note = (
            "# Notebook Source Unspecified\n\n"
            "Aday DOCX dosyası mevcut proje kökü içinde bulunamadı.\n"
            "Repo içinde notebook'a giden açık bir referans ayrıca elle kontrol edilmelidir.\n"
        )
        (correction_root / "NOTEBOOK_SOURCE_UNSPECIFIED.md").write_text(note, encoding="utf-8")
        write_csv(
            inventory_root / "mismatch_matrix.csv",
            [
                "kind",
                "source_anchor",
                "source_excerpt",
                "source_image_id",
                "suggested_target_file",
                "confidence",
                "notes",
            ],
            [
                {
                    "kind": "source_unspecified",
                    "source_anchor": "",
                    "source_excerpt": "",
                    "source_image_id": "",
                    "suggested_target_file": "",
                    "confidence": "1.00",
                    "notes": "Notebook DOCX bulunamadı.",
                }
            ],
        )
        return 2

    notebook_blocks, notebook_images, stats = extract_docx(docx_path, extract_root)
    write_notebook_full_text(extract_root / "notebook_full_text.md", docx_path, notebook_blocks)

    image_rows = []
    for event in notebook_images:
        image_rows.append(
            {
                "image_id": event["image_id"],
                "sequence": event["sequence"],
                "sha256": event["sha256"],
                "width": event["width"],
                "height": event["height"],
                "original_name": event["original_name"],
                "docx_media_path": event["docx_media_path"],
                "extracted_path": rel_path(Path(event["extracted_path"]), repo_root),
                "previous_text": safe_excerpt(event["previous_text"]),
                "next_text": safe_excerpt(event["next_text"]),
                "nearest_heading": event["nearest_heading"],
            }
        )
    write_csv(
        inventory_root / "image_manifest.csv",
        [
            "image_id",
            "sequence",
            "sha256",
            "width",
            "height",
            "original_name",
            "docx_media_path",
            "extracted_path",
            "previous_text",
            "next_text",
            "nearest_heading",
        ],
        image_rows,
    )

    dup_rows = []
    by_sha = defaultdict(list)
    for event in notebook_images:
        by_sha[event["sha256"]].append(event)
    for digest, events in by_sha.items():
        if len(events) > 1:
            dup_rows.append(
                {
                    "sha256": digest,
                    "count": len(events),
                    "image_ids": ";".join(e["image_id"] for e in events),
                    "original_names": ";".join(sorted({e["original_name"] for e in events})),
                }
            )
    write_csv(inventory_root / "image_duplicates.csv", ["sha256", "count", "image_ids", "original_names"], dup_rows)

    md_files = [p for p in repo_root.rglob("*.md") if ".git" not in p.parts]
    markdown_rows: list[dict] = []
    markdown_images: list[dict] = []
    for md in md_files:
        blocks, images = parse_markdown_file(md, repo_root)
        markdown_rows.extend(blocks)
        markdown_images.extend(images)
    write_csv(
        inventory_root / "repo_markdown_inventory.csv",
        [
            "file_path",
            "block_index",
            "block_type",
            "heading_context",
            "text",
            "normalized_text",
            "ignore_line",
            "image_alt",
            "image_target",
            "image_resolved",
            "image_exists",
        ],
        markdown_rows,
    )

    public_paths = {row["resolved_path"] for row in public_resolved if row["resolved_path"]}
    public_text_blocks = [
        row
        for row in markdown_rows
        if row["file_path"] in public_paths
        and row["block_type"] in ("text", "heading")
        and row["normalized_text"]
        and not row["ignore_line"]
    ]
    mismatch_rows: list[dict] = []
    for block in notebook_blocks:
        normalized = block["normalized"]
        if block["ignore_line"] or len(normalized) < 30:
            continue
        best_score = 0.0
        best_file = ""
        best_excerpt = ""
        for candidate in public_text_blocks:
            score = difflib.SequenceMatcher(None, normalized, candidate["normalized_text"]).ratio()
            if score > best_score:
                best_score = score
                best_file = candidate["file_path"]
                best_excerpt = candidate["text"]
        if best_score < 0.80:
            mismatch_rows.append(
                {
                    "kind": "missing_text",
                    "source_anchor": f"notebook_block_{block['block_index']:04d}",
                    "source_excerpt": safe_excerpt(block["text"]),
                    "source_image_id": "",
                    "suggested_target_file": suggested_target(block["text"], block["nearest_heading"]),
                    "confidence": f"{1 - best_score:.3f}",
                    "notes": f"En yakın repo bloğu: {best_file}; skor={best_score:.3f}; repo_excerpt={safe_excerpt(best_excerpt, 120)}",
                }
            )

    repo_asset_images = []
    assets_root = repo_root / "assets"
    if assets_root.exists():
        for path in assets_root.rglob("*"):
            if path.is_file() and path.suffix.lower() in IMAGE_EXTS:
                repo_asset_images.append(
                    {
                        "path": path,
                        "rel": rel_path(path, repo_root),
                        "sha256": sha256_file(path),
                        "width": image_size_from_bytes(path.read_bytes())[0],
                        "height": image_size_from_bytes(path.read_bytes())[1],
                    }
                )

    referenced_paths = set()
    referenced_hashes = set()
    public_markdown_images = [img for img in markdown_images if img["file_path"] in public_paths]
    for img in public_markdown_images:
        if img["image_resolved"]:
            resolved = (repo_root / img["image_resolved"]).resolve()
            if not resolved.exists():
                mismatch_rows.append(
                    {
                        "kind": "broken_md_image",
                        "source_anchor": img["file_path"],
                        "source_excerpt": img["image_target"],
                        "source_image_id": "",
                        "suggested_target_file": img["file_path"],
                        "confidence": "1.000",
                        "notes": f"Markdown görsel referansı dosya bulamıyor: {img['image_target']}",
                    }
                )
            else:
                referenced_paths.add(resolved)
                referenced_hashes.add(sha256_file(resolved))

    unreferenced_rows = []
    for asset in repo_asset_images:
        if asset["path"].resolve() not in referenced_paths:
            row = {
                "asset_path": asset["rel"],
                "sha256": asset["sha256"],
                "width": asset["width"],
                "height": asset["height"],
                "notes": "Repo assets içinde var ama public markdown referansı yok.",
            }
            unreferenced_rows.append(row)
            mismatch_rows.append(
                {
                    "kind": "unreferenced_repo_image",
                    "source_anchor": asset["rel"],
                    "source_excerpt": "",
                    "source_image_id": "",
                    "suggested_target_file": "",
                    "confidence": "1.000",
                    "notes": row["notes"],
                }
            )
    write_csv(
        inventory_root / "unreferenced_repo_images.csv",
        ["asset_path", "sha256", "width", "height", "notes"],
        unreferenced_rows,
    )

    unused_rows = []
    for event in notebook_images:
        if event["sha256"] not in referenced_hashes:
            row = {
                "image_id": event["image_id"],
                "sequence": event["sequence"],
                "sha256": event["sha256"],
                "width": event["width"],
                "height": event["height"],
                "original_name": event["original_name"],
                "nearest_heading": event["nearest_heading"],
                "previous_text": safe_excerpt(event["previous_text"]),
                "next_text": safe_excerpt(event["next_text"]),
                "suggested_target_file": suggested_target(
                    f"{event['nearest_heading']} {event['previous_text']} {event['next_text']}",
                    event["nearest_heading"],
                ),
            }
            unused_rows.append(row)
            mismatch_rows.append(
                {
                    "kind": "unused_notebook_image",
                    "source_anchor": event["docx_media_path"],
                    "source_excerpt": safe_excerpt(f"{event['previous_text']} / {event['next_text']}"),
                    "source_image_id": event["image_id"],
                    "suggested_target_file": row["suggested_target_file"],
                    "confidence": "0.900",
                    "notes": "Notebook görselinin SHA değeri public markdown'da referanslanan repo görselleriyle eşleşmedi.",
                }
            )
    write_csv(
        inventory_root / "unused_notebook_images.csv",
        [
            "image_id",
            "sequence",
            "sha256",
            "width",
            "height",
            "original_name",
            "nearest_heading",
            "previous_text",
            "next_text",
            "suggested_target_file",
        ],
        unused_rows,
    )

    write_csv(
        inventory_root / "mismatch_matrix.csv",
        [
            "kind",
            "source_anchor",
            "source_excerpt",
            "source_image_id",
            "suggested_target_file",
            "confidence",
            "notes",
        ],
        mismatch_rows,
    )

    source_inventory = [
        "# Correction Source Inventory",
        "",
        f"- Repo kökü: `{repo_root}`",
        f"- Çalışma alanı kökü: `{workspace_root}`",
        f"- Kullanılan notebook DOCX: `{docx_path}`",
        f"- Ardışık Codex prompt dosyası bulundu mu: `{bool(prompt_candidates)}`",
        "",
        "## Sayımlar",
        "",
        f"- Notebook paragraf bloğu: {stats['text_block_count']}",
        f"- Notebook görsel olayı: {stats['image_count']}",
        f"- Benzersiz notebook görsel SHA sayısı: {stats['unique_image_sha_count']}",
        f"- Repo markdown dosyası: {len(md_files)}",
        f"- Repo assets görsel dosyası: {len(repo_asset_images)}",
        f"- Public markdown görsel referansı: {len(public_markdown_images)}",
        f"- Mismatch satırı: {len(mismatch_rows)}",
        "",
        "## Public Markdown Çözümlemesi",
        "",
    ]
    for row in public_resolved:
        source_inventory.append(
            f"- `{row['expected_path']}` -> `{row['resolved_path']}` ({row['resolution_reason']})"
        )
    source_inventory.extend(
        [
            "",
            "## Üretilen Dosyalar",
            "",
            "- `_work/correction/base_head.txt`",
            "- `_work/correction/extract/notebook_full_text.md`",
            "- `_work/correction/extract/notebook_images/`",
            "- `_work/correction/inventory/public_md_resolved.json`",
            "- `_work/correction/inventory/image_manifest.csv`",
            "- `_work/correction/inventory/image_duplicates.csv`",
            "- `_work/correction/inventory/repo_markdown_inventory.csv`",
            "- `_work/correction/inventory/mismatch_matrix.csv`",
            "- `_work/correction/inventory/unreferenced_repo_images.csv`",
            "- `_work/correction/inventory/unused_notebook_images.csv`",
        ]
    )
    (inventory_root / "source_inventory.md").write_text("\n".join(source_inventory) + "\n", encoding="utf-8")

    summary = {
        "repo_root": str(repo_root),
        "workspace_root": str(workspace_root),
        "docx_path": str(docx_path),
        "text_block_count": stats["text_block_count"],
        "notebook_image_count": stats["image_count"],
        "unique_notebook_image_sha_count": stats["unique_image_sha_count"],
        "repo_markdown_file_count": len(md_files),
        "repo_asset_image_count": len(repo_asset_images),
        "public_markdown_image_ref_count": len(public_markdown_images),
        "mismatch_count": len(mismatch_rows),
        "unused_notebook_image_count": len(unused_rows),
        "unreferenced_repo_image_count": len(unreferenced_rows),
        "prompt_candidates": [str(p) for p in prompt_candidates],
    }
    (inventory_root / "run_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
