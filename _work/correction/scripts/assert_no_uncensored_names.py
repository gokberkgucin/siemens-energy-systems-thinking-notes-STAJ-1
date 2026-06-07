from __future__ import annotations

import base64
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
TEXT_SUFFIXES = {".md", ".csv", ".txt", ".json", ".log"}


def b64(s: str) -> str:
    return base64.b64decode(s).decode("utf-8")


DENYLIST = [
    b64("RXJ0dcSfcnVsIEJleQ=="),
    b64("S2VtYWwgQnVoYW4="),
    b64("U2VydGHDpyBCZXk="),
    b64("QW7EsWwgQmV5"),
    b64("Q2VsYWwgxZ5lbmfDtnIgSG9jYQ=="),
    b64("QmFodGl5YXIgRVJFTg=="),
    b64("Z29rYmVyayBiYWJh"),
    b64("R8O2a2JlcmsgQmFiYQ=="),
    b64("xLBsYmVyIE9ydGF5bMSx"),
]

FIRST_NAME_HINTS = [
    b64("QW7EsWw="),
    b64("U2VydGHDpw=="),
    b64("RXJ0dcSfcnVs"),
    b64("S2VtYWw="),
    b64("QmFodGl5YXI="),
    b64("Q2VsYWw="),
    b64("xLBsYmVy"),
    b64("R8O2a2Jlcms="),
    b64("Z29rYmVyaw=="),
]

HONORIFIC_RE = re.compile(
    r"\b([A-ZÇĞİÖŞÜ][a-zçğıöşüâîû]+(?:\s+[A-ZÇĞİÖŞÜ][a-zçğıöşüâîû]+){0,2}\s+"
    r"(?:Bey|Hanım|Hoca|Hocam|Abi|Ağabey))([\'’][A-Za-zÇĞİÖŞÜçğıöşü]+)?\b"
)

FULL_NAME_RE = re.compile(
    r"\b([A-ZÇĞİÖŞÜ][a-zçğıöşüâîû]+(?:\s+[A-ZÇĞİÖŞÜ][a-zçğıöşüâîû]+){1,2})"
    r"([\'’][A-Za-zÇĞİÖŞÜçğıöşü]+)?\b"
)


def iter_scanned_files() -> list[Path]:
    files: list[Path] = [ROOT / "README.md"]
    files.extend(sorted((ROOT / "docs").glob("*.md")))
    correction = ROOT / "_work" / "correction"
    for path in sorted(correction.rglob("*")):
        if not path.is_file():
            continue
        if path.parent.name == "scripts":
            continue
        if path.suffix.lower() in TEXT_SUFFIXES:
            files.append(path)
    return files


def main() -> int:
    failures: list[str] = []
    for path in iter_scanned_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        rel = path.relative_to(ROOT).as_posix()

        for item in DENYLIST:
            if item in text:
                failures.append(f"{rel}: direct denylist match")

        for match in HONORIFIC_RE.finditer(text):
            failures.append(f"{rel}: honorific match -> {match.group(0)!r}")

        for match in FULL_NAME_RE.finditer(text):
            name = match.group(1)
            if any(hint in name for hint in FIRST_NAME_HINTS):
                failures.append(f"{rel}: hinted full-name match -> {match.group(0)!r}")

    if failures:
        print("ASSERT_NO_UNCENSORED_NAMES_FAIL")
        print("\n".join(failures))
        return 1

    print(f"ASSERT_NO_UNCENSORED_NAMES_OK files={len(iter_scanned_files())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

