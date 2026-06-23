"""Week-local wrapper for the canonical measurement checklist builder."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
WEEK_DIR = HERE.parent
PROJECT = WEEK_DIR.parent
BUILDER = PROJECT / ".claude" / "skills" / "prep-measurement-checklist" / "_build_checklist.py"


def _load_builder():
    spec = importlib.util.spec_from_file_location("prep_measurement_checklist_builder", BUILDER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load builder: {BUILDER}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    _load_builder().main(WEEK_DIR)
