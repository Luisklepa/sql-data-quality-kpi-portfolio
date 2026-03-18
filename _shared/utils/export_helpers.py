"""
Helpers para exportar resultados a CSV, Excel y Markdown.
Usado por: 02 Data Quality, 03 Tailoring (opcional), 04 Pipeline.
"""
import csv
from pathlib import Path
from typing import Any

def write_csv(path: Path, rows: list[dict], fieldnames: list[str] | None = None) -> None:
    if not rows:
        return
    fieldnames = fieldnames or list(rows[0].keys())
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

def write_md_section(path: Path, title: str, lines: list[str], mode: str = "a") -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, mode, encoding="utf-8") as f:
        f.write(f"## {title}\n\n")
        f.write("\n".join(lines) + "\n\n")

def table_to_md(rows: list[dict], fieldnames: list[str] | None = None) -> str:
    if not rows:
        return ""
    fieldnames = fieldnames or list(rows[0].keys())
    header = "| " + " | ".join(str(f) for f in fieldnames) + " |"
    sep = "| " + " | ".join("---" for _ in fieldnames) + " |"
    body = []
    for r in rows:
        body.append("| " + " | ".join(str(r.get(f, "")) for f in fieldnames) + " |")
    return "\n".join([header, sep] + body)
