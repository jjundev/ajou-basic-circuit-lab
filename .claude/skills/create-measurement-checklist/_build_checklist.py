"""Build measurement checklist HTML from a SCHEMA v5 cache."""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime
from html import escape
from pathlib import Path


class BuildError(RuntimeError):
    """Raised when the cache cannot be built safely."""


@dataclass
class InputSpec:
    symbol: str
    unit: str = ""
    tool: str = ""
    expected: str = ""
    confidence: str = ""


@dataclass
class Column:
    name: str
    unit: str
    kind: str  # independent | measured | derived | computed | fixed
    tool: str = ""
    expected: list[str] = field(default_factory=list)
    confidence: str = ""
    formula: str = ""
    value: str = ""
    measured_flag: bool = False
    inputs: str = ""
    inputs_by_row: list[InputSpec | None] = field(default_factory=list)
    kind_by_row: list[str] = field(default_factory=list)


@dataclass
class Table:
    ac: str
    part: str
    code: str
    model: str
    shape: str = "column-major"
    fixed_conds: list[str] = field(default_factory=list)
    indep_name: str = ""
    indep_values: list[str] = field(default_factory=list)
    columns: list[Column] = field(default_factory=list)
    formula_map: dict[str, str] = field(default_factory=dict)
    shared_inputs: list[InputSpec] = field(default_factory=list)


KNOWN_KEYS = (
    "kind",
    "tool",
    "expected",
    "confidence",
    "formula",
    "value",
    "measured",
    "inputs",
    "inputs-by-row",
    "kind-by-row",
)
FIELD_SPLIT_RE = re.compile(r"\s\|\s(?=(?:" + "|".join(KNOWN_KEYS) + r")\s*:)", re.I)


def schema_version(text: str) -> int:
    first = text.splitlines()[0].strip() if text.splitlines() else ""
    m = re.match(r"<!--\s*SCHEMA:\s*v(\d+)\s*-->", first, re.I)
    return int(m.group(1)) if m else 0


def require_schema_v5(text: str) -> None:
    version = schema_version(text)
    if version < 5:
        raise BuildError("requires SCHEMA v5; run with refresh to regenerate")


def split_field_spec(spec: str) -> tuple[str, dict[str, str]]:
    matches = list(FIELD_SPLIT_RE.finditer(spec))
    if not matches:
        return spec.strip(), {}
    head = spec[: matches[0].start()].strip()
    fields: dict[str, str] = {}
    for idx, match in enumerate(matches):
        start = match.start() + 3
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(spec)
        segment = spec[start:end].strip()
        if ":" not in segment:
            continue
        key, value = segment.split(":", 1)
        fields[key.strip().lower()] = value.strip()
    return head, fields


def parse_cache(text: str, *, require_v5: bool = True) -> list[Table]:
    if require_v5:
        require_schema_v5(text)

    lines = text.splitlines()
    tables: list[Table] = []
    cur_ac = cur_part = ""
    cur_table: Table | None = None
    section = ""
    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            continue
        if line.startswith("## AC "):
            cur_ac = line[3:].strip()
            continue
        if line.startswith("### Part ") or line.startswith("### "):
            cur_part = line[4:].strip()
            continue
        if line.startswith("#### "):
            code = line[5:].strip()
            cur_table = Table(ac=cur_ac, part=cur_part, code=code, model="")
            tables.append(cur_table)
            section = ""
            continue
        if cur_table is None:
            continue

        stripped = line.lstrip()
        if line.startswith("- 표 양식:"):
            cur_table.shape = line.split(":", 1)[1].strip()
            section = ""
            continue
        if line.startswith("- 회로 모형:"):
            cur_table.model = line.split(":", 1)[1].strip()
            section = ""
            continue
        if line.startswith("- 고정조건:"):
            section = "fixed"
            continue
        if line.startswith("- 측정 입력 (공통):"):
            section = "shared_inputs"
            continue
        if line.startswith("- 독립변수:"):
            body = line.split(":", 1)[1].strip()
            m = re.match(r"(\S+)\s*=\s*\[(.*?)\]", body)
            if m:
                cur_table.indep_name = m.group(1).strip()
                cur_table.indep_values = [v.strip() for v in m.group(2).split(",")]
            section = ""
            continue
        if line.startswith("- 컬럼:"):
            section = "columns"
            continue
        if line.startswith("- 식 정의:"):
            section = "formulas"
            continue

        if section == "fixed":
            if stripped.startswith("- "):
                cur_table.fixed_conds.append(stripped[2:].strip())
            continue
        if section == "shared_inputs":
            if stripped.startswith("- "):
                cur_table.shared_inputs.append(parse_input_spec(stripped[2:].strip()))
            continue
        if section == "columns":
            if stripped.startswith("- "):
                cur_table.columns.append(parse_column(stripped[2:].strip()))
            continue
        if section == "formulas":
            if stripped.startswith("- "):
                body = stripped[2:].strip()
                if ":" in body:
                    label, expr = body.split(":", 1)
                    cur_table.formula_map[label.strip()] = expr.strip()
            continue
    return tables


def parse_head_unit(head: str) -> tuple[str, str]:
    unit = ""
    name = head.strip()
    m = re.match(r"^(.+?)\s*\[(.*?)\]\s*$", name)
    if m:
        name = m.group(1).strip()
        unit = m.group(2).strip()
    return name, unit


def parse_column(spec: str) -> Column:
    head, fields = split_field_spec(spec)
    name, unit = parse_head_unit(head)
    col = Column(name=name, unit=unit, kind="")
    for key, value in fields.items():
        if key == "kind":
            col.kind = value
        elif key == "tool":
            col.tool = value
        elif key == "expected":
            col.expected = [x.strip() for x in value.split(",")]
        elif key == "confidence":
            col.confidence = value
        elif key == "formula":
            col.formula = value
        elif key == "value":
            col.value = value
        elif key == "measured":
            col.measured_flag = value.lower() in ("true", "yes", "1")
        elif key == "inputs":
            col.inputs = value
        elif key == "inputs-by-row":
            col.inputs_by_row = parse_inputs_by_row(value)
        elif key == "kind-by-row":
            col.kind_by_row = [x.strip() for x in strip_brackets(value).split(";")]
    return col


def strip_brackets(value: str) -> str:
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        return value[1:-1].strip()
    return value


def parse_inputs_by_row(value: str) -> list[InputSpec | None]:
    out: list[InputSpec | None] = []
    for item in strip_brackets(value).split(";"):
        item = item.strip()
        if item in ("", "-", "—"):
            out.append(None)
        else:
            out.append(parse_input_spec(item))
    return out


def parse_input_spec(spec: str) -> InputSpec:
    spec = spec.strip()
    if spec in ("", "-", "—"):
        raise BuildError("empty input spec cannot be parsed")

    if " | " in spec:
        head, fields = split_field_spec(spec)
        symbol, unit = parse_head_unit(head)
        return InputSpec(
            symbol=symbol,
            unit=unit,
            tool=fields.get("tool", ""),
            expected=fields.get("expected", ""),
            confidence=fields.get("confidence", ""),
        )

    m = re.match(r"^(.+?)\s*\[(.*?)\]\s*@\s*(.*?)\s*(?:→|->)\s*(.*?)\s*(?:\[(.*?)\])?$", spec)
    if m:
        expected = m.group(4).strip()
        confidence = (m.group(5) or "").strip()
        if not confidence:
            cm = re.match(r"^(.*?)\s*\[(.*?)\]\s*$", expected)
            if cm:
                expected = cm.group(1).strip()
                confidence = cm.group(2).strip()
        return InputSpec(
            symbol=m.group(1).strip(),
            unit=m.group(2).strip(),
            tool=m.group(3).strip(),
            expected=expected,
            confidence=confidence,
        )

    symbol, unit = parse_head_unit(spec)
    return InputSpec(symbol=symbol, unit=unit)


SHADED_CELL = '<td class="cell-independent" style="background:#e8e8e8;color:#999;">—</td>'


def _row_value(values: list[str], idx: int, fallback: str = "") -> str:
    if not values:
        return fallback
    if idx < len(values):
        return values[idx]
    if len(values) == 1:
        return values[0]
    return fallback


def _effective_kind(col: Column, row_idx: int) -> str:
    if row_idx < len(col.kind_by_row):
        kind = col.kind_by_row[row_idx].strip()
        if kind and kind not in ("-", "—"):
            return kind
    return col.kind


def _input_for_row(col: Column, row_idx: int) -> InputSpec | None:
    if row_idx < len(col.inputs_by_row):
        return col.inputs_by_row[row_idx]
    return None


def _formula_for_row(col: Column, row_idx: int, row_label: str, table: Table) -> str:
    effective = _effective_kind(col, row_idx)
    if effective == "computed":
        if row_label and row_label in table.formula_map:
            return table.formula_map[row_label]
        return col.formula
    if col.formula:
        return col.formula
    if row_label and row_label in table.formula_map:
        return table.formula_map[row_label]
    return ""


def sibling_matches(table: Table, col: Column, row_idx: int, formula: str) -> list[str]:
    if not formula:
        return []
    matches: list[str] = []
    for other in table.columns:
        if other is col:
            continue
        other_kind = _effective_kind(other, row_idx)
        if other_kind == "measured" or (other_kind == "independent" and other.measured_flag):
            if other.name and other.name in formula:
                matches.append(other.name)
    return matches


def validate_table(table: Table) -> None:
    n_rows = max(len(table.indep_values), 1)
    for col in table.columns:
        for row_idx in range(n_rows):
            if _effective_kind(col, row_idx) != "derived":
                continue
            row_label = table.indep_values[row_idx] if row_idx < len(table.indep_values) else ""
            formula = _formula_for_row(col, row_idx, row_label, table)
            has_source = (
                bool(table.shared_inputs)
                or _input_for_row(col, row_idx) is not None
                or col.inputs in ("same-row", "graph-lookup", "measured-rows")
                or bool(sibling_matches(table, col, row_idx, formula))
            )
            if not has_source:
                raise BuildError(
                    f"derived column '{col.name}' in {table.code}: no raw input source "
                    "(add 측정 입력 / inputs-by-row / sibling match / inputs: graph-lookup)"
                )


def validate_tables(tables: list[Table]) -> None:
    for table in tables:
        validate_table(table)


def input_label(spec: InputSpec) -> str:
    unit = f" [{escape(spec.unit)}]" if spec.unit else ""
    return f"{escape(spec.symbol)}{unit}"


def render_input_chip(spec: InputSpec) -> str:
    tool_html = f'<span>{escape(spec.tool)}</span>' if spec.tool else ""
    conf_html = f'<span class="conf">[{escape(spec.confidence)}]</span>' if spec.confidence else ""
    expected = escape(spec.expected) if spec.expected else "—"
    return (
        '<div class="cell-input">'
        f'<div class="top"><span class="badge badge-input">입력</span>{tool_html}</div>'
        f'<div class="expected">{input_label(spec)} · 예상 <span class="v">{expected}</span>{conf_html}</div>'
        '<span class="blank"></span>'
        "</div>"
    )


def render_shared_inputs_panel(table: Table) -> str:
    if not table.shared_inputs:
        return ""
    chips = "".join(render_input_chip(spec) for spec in table.shared_inputs)
    return (
        '<div class="card-inputs">'
        '<div class="inputs-title">직접 측정 입력 (모든 환산 행 공통)</div>'
        f'<div class="inputs-grid">{chips}</div>'
        "</div>"
    )


def render_cell(col: Column, row_idx: int, row_label: str, table: Table) -> str:
    kind = _effective_kind(col, row_idx)
    if kind == "independent":
        label = row_label if row_label else (col.value or col.name or "—")
        if col.measured_flag:
            nominal = _row_value(col.expected, row_idx)
            if not nominal and row_label:
                nominal = row_label
            return (
                '<td class="cell-independent measured-hint">'
                '<div class="top"><span class="badge badge-measure">측정</span>'
                '<span>DMM</span></div>'
                f'<div class="nominal">{escape(label)}</div>'
                '<div class="expected">예상 <span style="font-weight:600;color:#111;">'
                f'{escape(nominal or label)}</span><span class="conf">[상]</span></div>'
                "</td>"
            )
        return f'<td class="cell-independent">{escape(label)}</td>'

    if kind == "measured":
        exp = _row_value(col.expected, row_idx)
        if exp in ("—", "-", ""):
            return SHADED_CELL
        conf_html = f'<span class="conf">[{escape(col.confidence)}]</span>' if col.confidence else ""
        tool_html = f'<span>{escape(col.tool)}</span>' if col.tool else ""
        return (
            '<td class="cell-measure">'
            f'<div class="top"><span class="badge badge-measure">측정</span>{tool_html}</div>'
            f'<div class="expected">예상 <span class="v">{escape(exp)}</span>{conf_html}</div>'
            '<span class="blank"></span>'
            "</td>"
        )

    if kind == "derived":
        exp = _row_value(col.expected, row_idx)
        if exp in ("—", "-", ""):
            return SHADED_CELL
        conf_html = f'<span class="conf">[{escape(col.confidence)}]</span>' if col.confidence else ""
        formula = _formula_for_row(col, row_idx, row_label, table)
        formula_html = f'<div class="formula">{escape(formula)}</div>' if formula else ""
        row_input = _input_for_row(col, row_idx)
        input_html = f'<div class="input-strip">{render_input_chip(row_input)}</div>' if row_input else ""
        ref_html = ""
        if not row_input:
            if table.shared_inputs:
                ref_html = '<div class="ref">↑ 공통 입력 참조</div>'
            elif col.inputs == "graph-lookup":
                ref_html = '<div class="ref">그래프 읽기</div>'
            elif col.inputs == "measured-rows":
                ref_html = '<div class="ref">↑ 같은 표의 측정 행 참조</div>'
            else:
                matches = sibling_matches(table, col, row_idx, formula)
                if col.inputs == "same-row":
                    ref_html = '<div class="ref">↑ 같은 행 측정 셀</div>'
                elif matches:
                    ref_html = f'<div class="ref">↑ {escape(", ".join(matches))} 셀</div>'
        return (
            '<td class="cell-derived">'
            f'<div class="top"><span class="badge badge-derived">환산</span></div>'
            f'{input_html}{ref_html}{formula_html}'
            f'<div class="expected">예상 <span class="v">{escape(exp)}</span>{conf_html}</div>'
            '<span class="blank"></span>'
            "</td>"
        )

    if kind == "computed":
        formula_text = _formula_for_row(col, row_idx, row_label, table)
        if formula_text in ("—", "-", ""):
            return SHADED_CELL
        return (
            '<td class="cell-compute">'
            f'<div class="top"><span class="badge badge-compute">계산</span></div>'
            f'<div class="formula">{escape(formula_text)}</div>'
            "</td>"
        )

    if kind == "fixed":
        val = _row_value(col.expected, row_idx) or col.value
        return (
            '<td class="cell-fixed">'
            '<div class="top">고정</div>'
            f"{escape(val)}"
            "</td>"
        )

    return f'<td>{escape(col.name)}</td>'


def render_table_card(table: Table) -> tuple[str, dict[str, int]]:
    counts = {"measure": len(table.shared_inputs), "compute": 0, "derived": 0, "fixed": 0}
    title = f"{table.ac} · {table.part} · {table.code}"
    head = (
        '<div class="card-head">'
        f'<div class="title">{escape(title)}</div>'
        f'<div class="model">{escape(table.model)}</div>'
        "</div>"
    )
    fixed_str = " · ".join(table.fixed_conds) if table.fixed_conds else "—"
    indep_str = (
        f"{table.indep_name} = [{', '.join(table.indep_values)}]"
        if table.indep_name else "(단일 행)"
    )
    meta = (
        '<div class="card-meta">'
        f'<div class="row"><span class="k">표 양식</span><span class="v">{escape(table.shape)}</span></div>'
        f'<div class="row" style="margin-top:1mm;"><span class="k">고정조건</span><span class="v">{escape(fixed_str)}</span></div>'
        f'<div class="row" style="margin-top:1mm;"><span class="k">독립변수</span><span class="v">{escape(indep_str)}</span></div>'
        "</div>"
    )
    inputs_panel = render_shared_inputs_panel(table)

    th_cells = []
    for col in table.columns:
        unit_html = f'<span class="unit">{escape(col.unit)}</span>' if col.unit else ""
        th_cells.append(f"<th>{escape(col.name)}{unit_html}</th>")
    thead = "<thead><tr>" + "".join(th_cells) + "</tr></thead>"

    body_rows = []
    n_rows = max(len(table.indep_values), 1)
    for i in range(n_rows):
        row_label = table.indep_values[i] if i < len(table.indep_values) else ""
        cells = []
        for col in table.columns:
            kind = _effective_kind(col, i)
            cell = render_cell(col, i, row_label, table)
            if kind == "measured":
                exp = _row_value(col.expected, i)
                if exp not in ("—", "-", ""):
                    counts["measure"] += 1
            elif kind == "derived":
                exp = _row_value(col.expected, i)
                if exp not in ("—", "-", ""):
                    counts["derived"] += 1
                    if _input_for_row(col, i) is not None:
                        counts["measure"] += 1
            elif kind == "computed":
                formula = _formula_for_row(col, i, row_label, table)
                if formula not in ("—", "-", ""):
                    counts["compute"] += 1
            elif kind == "fixed":
                counts["fixed"] += 1
            elif kind == "independent" and col.measured_flag:
                counts["measure"] += 1
            cells.append(cell)
        body_rows.append("<tr>" + "".join(cells) + "</tr>")
    tbody = "<tbody>" + "".join(body_rows) + "</tbody>"
    table_html = f'<table class="data">{thead}{tbody}</table>'

    foot = (
        '<div class="card-foot">'
        f'<span>측정 {counts["measure"]}</span>'
        f'<span>계산 {counts["compute"]}</span>'
        f'<span>환산 {counts["derived"]}</span>'
        f'<span>고정 {counts["fixed"]}</span>'
        "</div>"
    )
    return '<div class="card">' + head + meta + inputs_panel + table_html + foot + "</div>", counts


def collect_tools(tables: list[Table]) -> list[str]:
    seen: list[str] = []

    def add(tool: str) -> None:
        if tool and tool not in seen:
            seen.append(tool)

    for table in tables:
        for spec in table.shared_inputs:
            add(spec.tool)
        for col in table.columns:
            if col.tool and col.kind in ("measured", "derived"):
                add(col.tool)
            for spec in col.inputs_by_row:
                if spec:
                    add(spec.tool)
            if col.kind == "independent" and col.measured_flag:
                add("DMM (저항 모드)")
    return seen


def parse_sources(text: str) -> list[str]:
    m = re.search(r"<!-- SOURCES\s*\n(.*?)\n-->", text, re.DOTALL)
    if not m:
        return []
    out = []
    for line in m.group(1).splitlines():
        line = line.strip()
        if "|" in line:
            out.append(line.split("|", 1)[0].strip())
    return out


def build(week_dir: Path) -> Path:
    week_dir = week_dir.resolve()
    checklist_dir = week_dir / "측정체크리스트"
    project = week_dir.parent
    template_path = project / ".claude" / "skills" / "create-measurement-checklist" / "template.html"
    cache_path = checklist_dir / "요구목록.md"
    week = week_dir.name

    text = cache_path.read_text(encoding="utf-8")
    tables = parse_cache(text)
    validate_tables(tables)
    template = template_path.read_text(encoding="utf-8")

    cards = []
    total_m = total_c = total_d = total_f = 0
    for table in tables:
        card_html, counts = render_table_card(table)
        cards.append(card_html)
        total_m += counts["measure"]
        total_c += counts["compute"]
        total_d += counts["derived"]
        total_f += counts["fixed"]

    sources = parse_sources(text)
    sources_html = "<br>".join(escape(source) for source in sources) if sources else "(없음)"
    tools = collect_tools(tables)
    tools_str = " · ".join(tools) if tools else "—"
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    pre_md = next((p for p in (week_dir / "output").glob("*예비보고서*.md")), None)
    pre_pdf = next(week_dir.glob("*예비보고서*.pdf"), None)
    winner = pre_md.name if pre_md else (pre_pdf.name if pre_pdf else "(없음)")

    rendered = (
        template.replace("{{WEEK}}", week)
        .replace("{{GENERATED_AT}}", now)
        .replace("{{COUNT_TABLES}}", str(len(tables)))
        .replace("{{COUNT_MEASURE}}", str(total_m))
        .replace("{{COUNT_COMPUTE}}", str(total_c))
        .replace("{{COUNT_DERIVED}}", str(total_d))
        .replace("{{COUNT_FIXED}}", str(total_f))
        .replace("{{TOOLS}}", escape(tools_str))
        .replace("{{WINNER_PREREPORT}}", escape(winner))
        .replace("{{CACHE_STATUS}}", "v5 신선")
        .replace("{{TABLE_CARDS}}", "\n".join(cards))
        .replace("{{SOURCES_LIST}}", sources_html)
    )
    out = checklist_dir / f"{week} 측정체크리스트.html"
    out.write_text(rendered, encoding="utf-8")
    print(f"HTML written: {out}")
    print(f"  Tables: {len(tables)}, 측정: {total_m}, 계산: {total_c}, 환산: {total_d}, 고정: {total_f}")
    return out


def main(week_dir: str | Path | None = None) -> Path:
    if week_dir is None:
        week_dir = Path.cwd().parent if Path.cwd().name == "측정체크리스트" else Path.cwd()
    return build(Path(week_dir))


if __name__ == "__main__":
    main()
