#!/usr/bin/env python3
"""Validate logos.json (plain JSON) and check every referenced art file
exists on disk."""
import json
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    index_path = root / "logos.json"
    if not index_path.exists():
        print(f"INVALID: {index_path} missing")
        return 1
    data = json.loads(index_path.read_text(encoding="utf-8"))
    required = {"schema_version", "defaults", "categories", "families", "logos"}
    missing_keys = required - set(data)
    if missing_keys:
        print(f"INVALID logos.json: missing keys {sorted(missing_keys)}")
        return 1
    ok = True
    files = 0
    for entry in data["logos"]:
        ref = Path(str(entry.get("file", "")))
        if not ref.is_absolute() and ".." not in ref.parts:
            path = root / ref
            files += 1
            if not path.is_file():
                ok = False
                print(f"INVALID: referenced file missing: {ref} ({entry.get('id')})")
    for category in data.get("defaults", {}).values():
        if isinstance(category, dict):
            for key, value in category.items():
                if isinstance(value, str) and value.endswith(".txt"):
                    path = root / value
                    files += 1
                    if not path.is_file():
                        ok = False
                        print(f"INVALID: default logo missing: {value}")
    if ok:
        print(f"OK: logos.json valid, {files} referenced files present.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
