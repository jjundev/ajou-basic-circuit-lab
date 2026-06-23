# -*- coding: utf-8 -*-
"""Build a landscape exam sheet (시험지) from all problems that have a 풀이
in 기말고사 대비/풀이/, matching the layout of 6월11일/문제_6월11일.pdf.

One landscape page per problem: problem image on the left half, blank
풀이 space on the right half. Cover page lists concepts + index.
Images and font are base64-embedded so Korean paths never break file URIs.
"""
from __future__ import annotations
import base64
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent  # 기말고사 대비/
FONT = BASE.parent / ".claude" / "skills" / "explain-lab-preview" / "fonts" / "PretendardVariable.woff2"
OUT_HTML = BASE / "풀이" / "시험지_전체.html"

# (seq, problem, chapter, topic, image-relative-to-BASE)
PROBLEMS = [
    ("9.1",  "Ch9",  "정현파 파라미터",          "6월8일/01_new_09-01.png"),
    ("9.3",  "Ch9",  "정현파 파라미터",          "6월8일/03_new_09-03.png"),
    ("9.5",  "Ch9",  "정현파 식 구성",           "6월9일/01_new_09-05.png"),
    ("9.43", "Ch9",  "phasor 테브난 등가",       "6월9일/04_new_09-43.png"),
    ("9.91", "Ch9",  "직렬 RLC 임피던스",        "6월10일/01_new_09-91.png"),
    ("9.92", "Ch9",  "직 · 병렬 임피던스",       "6월10일/02_new_09-92.png"),
    ("9.93", "Ch9",  "임피던스 전압분배",        "6월10일/03_new_09-93.png"),
    ("10.42","Ch10", "최대전력전달",             "6월11일/04_new_10-42.png"),
    ("10.44","Ch10", "최대전력전달",             "6월11일/06_new_10-44.png"),
    ("10.46","Ch10", "최대전력전달",             "6월11일/08_new_10-46.png"),
    ("14.1", "Ch14", "RL 저역통과 필터",         "6월12일/01_new_14-01.png"),
    ("14.11","Ch14", "RC 고역통과 필터",         "6월12일/07_new_14-11.png"),
    ("14.21","Ch14", "대역통과 필터 · 직렬공진 설계", "6월13일/04_new_14-21.png"),
    ("14.35","Ch14", "대역저지 필터 · 직렬공진",  "6월13일/08_new_14-35.png"),
    ("14.38","Ch14", "대역저지 필터 · 병렬공진",  "6월13일/11_new_14-38.png"),
]

N = len(PROBLEMS)

# Optional supplementary reference figures (inline SVG), keyed by problem id.
# Used when a problem's text references a figure that is NOT inside its own image
# (e.g. 14.21 says "see Fig. 14.19[a]" but the prototype circuit is not shown).
SVG_14_19A = """<svg viewBox="0 0 440 250" xmlns="http://www.w3.org/2000/svg" class="ckt">
  <g fill="none" stroke="#1a1a1a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <line x1="50" y1="50" x2="50" y2="101"/>
    <circle cx="50" cy="125" r="24"/>
    <line x1="50" y1="149" x2="50" y2="200"/>
    <line x1="50" y1="50" x2="130" y2="50"/>
    <path d="M130,50 a10,10 0 0 1 20,0 a10,10 0 0 1 20,0 a10,10 0 0 1 20,0 a10,10 0 0 1 20,0"/>
    <line x1="210" y1="50" x2="283" y2="50"/>
    <line x1="283" y1="36" x2="283" y2="64"/>
    <line x1="297" y1="36" x2="297" y2="64"/>
    <line x1="297" y1="50" x2="390" y2="50"/>
    <line x1="390" y1="50" x2="390" y2="90"/>
    <path d="M390,90 L380,100 L400,112 L380,124 L400,136 L380,148 L390,160"/>
    <line x1="390" y1="160" x2="390" y2="200"/>
    <line x1="50" y1="200" x2="390" y2="200"/>
  </g>
  <g fill="#1a1a1a" font-family="'Pretendard',sans-serif" font-size="16">
    <text x="50" y="117" text-anchor="middle">+</text>
    <text x="50" y="147" text-anchor="middle">&#8722;</text>
    <text x="6" y="130" font-style="italic">v</text><text x="17" y="134" font-size="11">i</text>
    <text x="162" y="28" font-style="italic">L</text>
    <text x="284" y="26" font-style="italic">C</text>
    <text x="360" y="132" font-style="italic">R</text>
    <text x="406" y="98">+</text>
    <text x="406" y="170">&#8722;</text>
    <text x="418" y="131" font-style="italic">v</text><text x="429" y="135" font-size="11">o</text>
  </g>
</svg>"""

FIGURES = {
    "14.21": ("Fig. 14.19[a] — 직렬 RLC 대역통과 필터 (출력 v_o 는 R 양단)", SVG_14_19A),
}


def b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("ascii")


def font_face() -> str:
    if not FONT.exists():
        return ""
    data = b64(FONT)
    return (
        "@font-face{font-family:'Pretendard';font-weight:45 920;font-style:normal;"
        "font-display:block;src:url(data:font/woff2;base64,%s) format('woff2-variations');}"
        % data
    )


CONCEPTS = [
    ("Ch9 · 정현파 · phasor", [
        "v = V_m cos(ωt+φ),  ω = 2πf,  T = 1/f",
        "Z_R = R,  Z_L = jωL,  Z_C = 1/(jωC)",
        "페이저 V = Z·I — 전압분배 · 테브난 그대로 적용",
    ]),
    ("Ch10 · 최대전력전달", [
        "Z_L = Z_Th*  (켤레 정합)",
        "P_max = |V_Th,rms|² / (4·R_Th)",
        "순저항 부하 제약: R = |Z_Th|",
    ]),
    ("Ch14 · 필터 · 공진", [
        "ω_c : -3dB,  |H| = 1/√2",
        "RL LPF ω_c = R/L,  RC HPF ω_c = 1/RC",
        "공진 ω₀ = 1/√(LC),  Q = ω₀L/R,  β = ω₀/Q",
    ]),
]


def cover() -> str:
    # left: concepts grouped by chapter
    concept_html = []
    for head, items in CONCEPTS:
        lis = "".join(f"<li>{it}</li>" for it in items)
        concept_html.append(f'<div class="cgroup"><div class="ch">{head}</div><ul>{lis}</ul></div>')
    concept_block = "".join(concept_html)

    # right: index
    idx_rows = []
    for i, (prob, ch, topic, _) in enumerate(PROBLEMS, 1):
        idx_rows.append(
            f'<div class="irow"><span class="inum">[{i}]</span>'
            f'<span class="iprob">{prob}</span>'
            f'<span class="itopic">— {ch} · {topic}</span></div>'
        )
    idx_block = "".join(idx_rows)

    return f"""
  <section class="page cover">
    <div class="titlebar">
      <span class="t-main">기초전기실험 기말대비</span>
      <span class="t-dot">·</span>
      <span class="t-sub">풀이 보유 {N}문항 모음 시험지 — Ch9 · 10 · 14</span>
    </div>
    <div class="instrbar">
      <span><b>①</b> 문제만 보고 가로 빈칸에 직접 풀이</span>
      <span><b>②</b> 막히면 풀이 폴더의 같은 번호 .md 로 대조</span>
      <span><b>③</b> 채점: solve-exam-prep · 정리노트 1순위</span>
    </div>
    <div class="coverbody">
      <div class="ccol">
        <div class="colhead">떠올릴 개념</div>
        {concept_block}
      </div>
      <div class="ccol">
        <div class="colhead">문항 목차 (총 {N}문항)</div>
        <div class="index">{idx_block}</div>
      </div>
    </div>
    <div class="coverfoot">
      한 문제당 1페이지 · 가로모드 · 풀이공간 포함
      <span class="sep">|</span>
      풀이 폴더 {N}문항 일괄 시험지 · 2026-06-14
    </div>
  </section>
"""


def problem_page(i: int, prob: str, ch: str, topic: str, img_rel: str) -> str:
    img_path = BASE / img_rel
    src = f"data:image/png;base64,{b64(img_path)}"
    fig = FIGURES.get(prob)
    if fig:
        cap, svg = fig
        left = (
            f'<div class="pleft haspfig">'
            f'<div class="pimg"><img src="{src}" alt="{prob}"></div>'
            f'<div class="pfig"><div class="figcap">{cap}</div>{svg}</div>'
            f'</div>'
        )
    else:
        left = f'<div class="pleft"><img src="{src}" alt="{prob}"></div>'
    return f"""
  <section class="page prob">
    <div class="phead">
      <span class="ptag">[{i}/{N}]</span>
      <span class="pch">{ch} · {prob}</span>
      <span class="pdash">—</span>
      <span class="ptopic">{topic}</span>
      <span class="ppage">{i} / {N}</span>
    </div>
    <div class="pbody">
      {left}
      <div class="pright">
        <div class="solvelabel">— 풀이 —</div>
      </div>
    </div>
  </section>
"""


def build() -> str:
    pages = [cover()] + [
        problem_page(i, prob, ch, topic, img)
        for i, (prob, ch, topic, img) in enumerate(PROBLEMS, 1)
    ]
    css = """
  @page { size: A4 landscape; margin: 0; }
  * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  html, body { margin:0; padding:0; background:#fff; color:#1a1a1a;
    font-family:'Pretendard','Malgun Gothic',sans-serif; }
  .page { width:297mm; height:210mm; page-break-after:always; position:relative;
    overflow:hidden; padding:0; }
  .page:last-child { page-break-after:auto; }

  /* ---------- cover ---------- */
  .titlebar { background:#20284a; color:#fff; padding:7mm 12mm; display:flex;
    align-items:baseline; gap:5mm; }
  .titlebar .t-main { font-size:17pt; font-weight:600; letter-spacing:-0.01em; }
  .titlebar .t-dot { color:#8a93c0; font-size:13pt; }
  .titlebar .t-sub { font-size:13pt; font-weight:500; color:#dfe3f2; }

  .instrbar { background:#efe9da; color:#5a5240; padding:4mm 12mm; display:flex;
    gap:9mm; font-size:9.5pt; }
  .instrbar b { color:#20284a; margin-right:1.5mm; }

  .coverbody { display:flex; gap:14mm; padding:9mm 12mm 0; }
  .ccol { flex:1; }
  .colhead { font-size:12.5pt; font-weight:600; color:#20284a; margin-bottom:4mm;
    padding-bottom:1.5mm; border-bottom:1.5px solid #20284a; }
  .cgroup { margin-bottom:4.5mm; }
  .cgroup .ch { font-size:10pt; font-weight:600; color:#33384f; margin-bottom:1mm; }
  .cgroup ul { margin:0; padding-left:5mm; }
  .cgroup li { font-size:10pt; line-height:1.75; color:#2a2a2a; }

  .index { }
  .irow { font-size:10pt; line-height:1.95; display:flex; gap:2.5mm; align-items:baseline; }
  .inum { color:#8a8a8a; min-width:9mm; }
  .iprob { font-weight:600; color:#20284a; min-width:13mm; }
  .itopic { color:#444; }

  .coverfoot { position:absolute; left:12mm; right:12mm; bottom:8mm; font-size:8.5pt;
    color:#9a9a9a; border-top:1px solid #e6e6e6; padding-top:2mm; }
  .coverfoot .sep { margin:0 3mm; color:#cfcfcf; }

  /* ---------- problem pages ---------- */
  .phead { display:flex; align-items:baseline; gap:3mm; padding:6mm 12mm 3mm;
    border-bottom:1.5px solid #20284a; }
  .phead .ptag { font-size:9pt; font-weight:700; color:#20284a; }
  .phead .pch { font-size:11pt; font-weight:600; color:#1a1a1a; }
  .phead .pdash { color:#bbb; }
  .phead .ptopic { font-size:10.5pt; font-weight:500; color:#555; }
  .phead .ppage { margin-left:auto; font-size:9pt; color:#999; }

  .pbody { display:flex; height:calc(210mm - 22mm); }
  .pleft { width:50%; padding:7mm 6mm 7mm 12mm; }
  .pleft img { max-width:100%; max-height:100%; object-fit:contain; object-position:top left; }
  .pleft.haspfig { display:flex; flex-direction:column; }
  .pleft.haspfig .pimg img { max-width:100%; max-height:70mm; object-fit:contain; object-position:top left; }
  .pfig { margin-top:7mm; padding-top:5mm; border-top:1px dashed #d0d0d0; }
  .figcap { font-size:9.5pt; font-weight:600; color:#444; margin-bottom:3mm; }
  .pfig svg { width:100%; max-width:135mm; height:auto; }
  .pright { width:50%; padding:7mm 12mm 7mm 8mm; border-left:1px solid #ececec; }
  .solvelabel { text-align:center; font-size:9pt; color:#aaa; letter-spacing:0.2em; }
"""
    return (
        "<!DOCTYPE html><html lang='ko'><head><meta charset='UTF-8'>"
        f"<title>풀이 {N}문항 모음 시험지</title>"
        f"<style>{font_face()}{css}</style></head><body>"
        + "".join(pages)
        + "</body></html>"
    )


def main() -> None:
    OUT_HTML.write_text(build(), encoding="utf-8")
    print(f"OK wrote {OUT_HTML}  ({OUT_HTML.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
