"""Build my public citation list only from verified publication metadata."""
from __future__ import annotations
import argparse
from pathlib import Path
import yaml

PLACEHOLDER = "PENDING_VERIFICATION"

def load_verified(path: Path) -> dict:
    item = yaml.safe_load(path.read_text(encoding="utf-8"))
    required = ("title", "authors", "venue", "conference_date", "status", "materials_cleared")
    missing = [field for field in required if field not in item]
    if missing:
        raise ValueError(f"{path}: missing {', '.join(missing)}")
    if any(item[field] == PLACEHOLDER for field in ("title", "venue", "conference_date")):
        raise ValueError(f"{path}: citation metadata is not verified")
    if not item["authors"]:
        raise ValueError(f"{path}: author list is empty")
    return item

def citation(item: dict) -> str:
    authors = ", ".join(item["authors"])
    return f"- {authors}. **{item['title']}**. {item['venue']}, {item['conference_date']}. Status: {item['status']}."

def build(folder: Path) -> str:
    records = [load_verified(path) for path in sorted(folder.glob("*.yaml"))]
    return "# Publications\n\n" + "\n".join(citation(item) for item in records) + "\n"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", default="publications")
    parser.add_argument("--output")
    args = parser.parse_args()
    text = build(Path(args.folder))
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
    else:
        print(text, end="")
