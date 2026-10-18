"""Собирает онлайн-версию в docs/ для GitHub Pages.

Копирует Python-движок, базу знаний, шаблоны и демо-данные в docs/ и пишет список файлов
docs/files.json — страница загружает их в Python, который работает в браузере (Pyodide).
Запуск: python3 tools/build_site.py
"""

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
FONTS = {
    "Inter-Bold.otf": "/usr/share/fonts/opentype/inter/Inter-Bold.otf",
    "Inter-Regular.otf": "/usr/share/fonts/opentype/inter/Inter-Regular.otf",
}

SOURCES = {
    "moneyball": "*.py",
    "knowledge": "*.json",
    "knowledge/cases": "*.json",
    "templates": "*.json",
    "templates/data": "*.csv",
    "examples/demo": "*.*",
}


def main():
    files = []
    for folder, pattern in SOURCES.items():
        for src in sorted((ROOT / folder).glob(pattern)):
            if src.name == "__main__.py":
                continue
            dst = DOCS / "app" / folder / src.name
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(src, dst)
            files.append(f"app/{folder}/{src.name}")
    shutil.copy(ROOT / "knowledge" / "principles.md", DOCS / "app" / "knowledge" / "principles.md")
    files.append("app/knowledge/principles.md")

    fonts_dir = DOCS / "app" / "fonts"
    fonts_dir.mkdir(parents=True, exist_ok=True)
    for name, path in FONTS.items():
        src = Path(path)
        if src.exists():
            shutil.copy(src, fonts_dir / name)
        if (fonts_dir / name).exists():
            files.append(f"app/fonts/{name}")
    license_src = Path("/usr/share/doc/fonts-inter/copyright")
    if license_src.exists():
        shutil.copy(license_src, fonts_dir / "LICENSE-Inter.txt")

    (DOCS / "files.json").write_text(json.dumps(sorted(set(files)), ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"docs/: {len(files)} файлов")


if __name__ == "__main__":
    main()
