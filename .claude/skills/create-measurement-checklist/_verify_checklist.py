"""Programmatic verification of a generated measurement checklist.

Replaces visually re-reading the rendered PDF (which costs ~2k tokens per page).
Reuses _build_checklist.parse_cache so the parser is never duplicated.

Run:
    python _verify_checklist.py "<WEEK_DIR>"
    # or, from inside <WEEK_DIR>\\측정체크리스트 with no arg.

Checks (exit code 1 on any FAIL; WARN never fails the run):
  1. Cache parses + validates under SCHEMA v5.
  2. Length — every measured/derived column's `expected` length == row count (or 1).
     Catches a dropped frequency/value that the builder would silently render as a
     shaded cell (_build_checklist._row_value returns "" on overflow, no error).
  3. Values — cache `expected` arrays == _expected.json (the compute script's output,
     the source of truth). Catches hand-copy/paste errors and post-hoc edits.
  4. Anchors — _expected.json["_anchors"][code][sym] string appears in that table's
     고정조건. Cross-checks resonance/cutoff frequencies against the swept data.
  5. HTML smoke — #cards == #tables and count("예상 <span") == measured+derived totals,
     i.e. the builder rendered every value-bearing cell. Replaces a page read.

_expected.json schema (emitted by each week's _compute_expected.py):
    {
      "<table.code>": { "<column.name>": ["v0", "v1", ...], ... },
      ...,
      "_anchors": { "<table.code>": { "f_p": "5033", ... }, ... }   # optional
    }
column.name is the unit-stripped header (e.g. "V_C(p-p)", "θ (V_o lead)").
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from _build_checklist import (  # noqa: E402
    BuildError,
    _effective_kind,
    parse_cache,
    render_table_card,
    validate_tables,
)


def find_week_dir(argv: list[str]) -> Path:
    if len(argv) > 1:
        return Path(argv[1]).resolve()
    cwd = Path.cwd()
    return cwd.parent if cwd.name == "측정체크리스트" else cwd


def main(argv: list[str]) -> int:
    week = find_week_dir(argv)
    cdir = week / "측정체크리스트"
    cache = cdir / "요구목록.md"
    html = cdir / f"{week.name} 측정체크리스트.html"
    expjson = cdir / "_expected.json"

    oks: list[str] = []
    warns: list[str] = []
    fails: list[str] = []

    if not cache.exists():
        print(f"FAIL: cache not found: {cache}")
        return 1
    text = cache.read_text(encoding="utf-8")

    # 1) parse + validate
    try:
        tables = parse_cache(text)
        validate_tables(tables)
        oks.append(f"cache parses + validates ({len(tables)} tables)")
    except BuildError as exc:
        print(f"FAIL: cache invalid under SCHEMA v5: {exc}")
        return 1

    by_code = {t.code: t for t in tables}

    # 2) expected-length per measured/derived column
    bad_len = False
    for t in tables:
        n_rows = max(len(t.indep_values), 1)
        for col in t.columns:
            kinds = [_effective_kind(col, i) for i in range(n_rows)]
            if not any(k in ("measured", "derived") for k in kinds):
                continue
            n = len(col.expected)
            if n not in (1, n_rows):
                bad_len = True
                fails.append(
                    f"[length] {t.code} · {col.name}: expected has {n} values but table has {n_rows} rows"
                )
    if not bad_len:
        oks.append("all measured/derived columns have full-length expected arrays")

    # 3) + 4) values + anchors vs _expected.json
    if expjson.exists():
        data = json.loads(expjson.read_text(encoding="utf-8"))
        anchors = data.pop("_anchors", {})
        val_bad = False
        for code, cols in data.items():
            t = by_code.get(code)
            if t is None:
                val_bad = True
                fails.append(f"[values] _expected.json table {code!r} not found in cache")
                continue
            colmap = {c.name: c for c in t.columns}
            for cname, vals in cols.items():
                c = colmap.get(cname)
                if c is None:
                    val_bad = True
                    fails.append(f"[values] {code}: column {cname!r} not found in cache")
                    continue
                jvals = [str(v) for v in vals]
                if jvals != list(c.expected):
                    val_bad = True
                    diff = next(
                        (
                            (i, a, b)
                            for i, (a, b) in enumerate(zip(jvals, c.expected))
                            if a != b
                        ),
                        None,
                    )
                    where = (
                        f" idx {diff[0]}: json={diff[1]!r} cache={diff[2]!r}"
                        if diff
                        else f" length json={len(jvals)} cache={len(c.expected)}"
                    )
                    fails.append(f"[values] {code} · {cname}: cache != _expected.json,{where}")
        if not val_bad:
            oks.append("cache expected arrays == _expected.json (computed values)")

        anc_bad = False
        for code, syms in anchors.items():
            t = by_code.get(code)
            if t is None:
                anc_bad = True
                warns.append(f"[anchor] table {code!r} not in cache")
                continue
            joined = " · ".join(t.fixed_conds)
            for sym, val in syms.items():
                if str(val) not in joined:
                    anc_bad = True
                    warns.append(f"[anchor] {code}: {sym}≈{val} not found in 고정조건")
        if anchors and not anc_bad:
            oks.append("anchor frequencies consistent with 고정조건")
    else:
        warns.append("_expected.json absent — value/anchor checks skipped (compute script should emit it)")

    # 5) HTML smoke
    if not html.exists():
        fails.append(f"[html] generated HTML not found: {html.name}")
    else:
        h = html.read_text(encoding="utf-8")
        ncards = h.count('<div class="card">')
        if ncards != len(tables):
            fails.append(f"[html] card count {ncards} != table count {len(tables)}")
        total = 0
        for t in tables:
            _, counts = render_table_card(t)
            total += counts["measure"] + counts["derived"]
        nyes = h.count("예상 <span")
        if nyes != total:
            fails.append(f"[html] rendered '예상' cells {nyes} != measured+derived total {total}")
        if ncards == len(tables) and nyes == total:
            oks.append(f"HTML smoke OK ({ncards} cards, {nyes} 예상 cells == {total} value cells)")

    # report
    print(f"== verify {week.name} ==")
    for o in oks:
        print(f"  OK   {o}")
    for w in warns:
        print(f"  WARN {w}")
    for f in fails:
        print(f"  FAIL {f}")
    status = "FAIL" if fails else "PASS"
    print(f"-- {status}: {len(oks)} ok, {len(warns)} warn, {len(fails)} fail --")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
