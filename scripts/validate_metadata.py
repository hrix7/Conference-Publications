"""Validate publication metadata before generating public citations."""
from __future__ import annotations
import sys
from pathlib import Path
import yaml

PLACEHOLDER = "PENDING_VERIFICATION"

def validate(path: Path) -> list[str]:
    with path.open(encoding="utf-8") as handle:
        item = yaml.safe_load(handle)
    errors = []
    for field in ("status", "title", "authors", "venue", "conference_date", "materials_cleared"):
        if field not in item:
            errors.append(f"missing {field}")
    if item.get("title") == PLACEHOLDER or item.get("venue") == PLACEHOLDER:
        errors.append("citation metadata still contains placeholders")
    if not item.get("authors"):
        errors.append("author list is empty")
    return errors

if __name__ == "__main__":
    paths = [Path(p) for p in sys.argv[1:]] or sorted(Path("publications").glob("*.yaml"))
    failed = False
    for path in paths:
        issues = validate(path)
        print(f"{path}: " + ("; ".join(issues) if issues else "valid"))
        failed = failed or bool(issues)
    raise SystemExit(failed)
