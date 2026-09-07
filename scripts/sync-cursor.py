#!/usr/bin/env python3
"""Regenerate the existing Cursor skill distribution from its canonical package."""
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--check", action="store_true")
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
source = root / "skills" / "learn-codebase"
target = root / ".cursor" / "skills" / "learn-codebase"
files = {p.relative_to(source): p.read_bytes() for p in source.rglob("*") if p.is_file()}
actual = {p.relative_to(target): p for p in target.rglob("*") if p.is_file()}
if args.check:
    stale = sorted(str(p) for p in files if p not in actual or actual[p].read_bytes() != files[p])
    extra = sorted(str(p) for p in actual if p not in files)
    if stale or extra:
        raise SystemExit(f"Cursor distribution differs: stale={stale}, extra={extra}")
    print("Cursor distribution matches canonical package")
else:
    for relative, data in files.items():
        path = target / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    # Do not delete unexpected files silently; --check reports them for review.
    print(f"Wrote {len(files)} distribution files; run --check")
