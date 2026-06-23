# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# ── 한글 폰트 등록 ──────────────────────────────────────────────
FONT_PATH = r"C:\Windows\Fonts\malgun.ttf"
FONT_BOLD_PATH = r"C:\Windows\Fonts\malgunbd.ttf"
pdfmetrics.registerFont(TTFont("Malgun", FONT_PATH))
pdfmetrics.registerFont(TTFont("MalgunBd", FONT_BOLD_PATH))

# ── 출력 경로 ────────────────────────────────────────────────────
OUTPUT = os.path.join(os.path.dirname(__file__), "10주차_실험_참고노트.pdf")

# ── 색상 ─────────────────────────────────────────────────────────
C_BLUE   = colors.HexColor("#1a3a6b")   # 제목
C_SKY    = colors.HexColor("#3a7fc1")   # 소제목 배경
C_LIGHT  = colors.HexColor("#dce8f5")   # 표 헤더
C_YELLOW = colors.HexColor("#fff8e1")   # 주의사항 배경
C_GREEN  = colors.HexColor("#e8f5e9")   # 공통 준비 배경
C_GRAY   = colors.HexColor("#f5f5f5")   # 교대 행

W, H = A4

# ── 스타일 ────────────────────────────────────────────────────────
def S(name, **kw):
    kw.pop("parent", None)
    kw.setdefault("fontName", "Malgun")
    kw.setdefault("fontSize", 10)
    kw.setdefault("leading", 16)
    kw.setdefault("spaceAfter", 4)
    return ParagraphStyle(name, **kw)

sTitle   = S("Title",   fontName="MalgunBd", fontSize=22, leading=28,
             alignment=1, textColor=C_BLUE, spaceAfter=6)
sSubtitle= S("Subtitle",fontName="Malgun",  fontSize=13, leading=20,
             alignment=1, textColor=colors.HexColor("#555555"), spaceAfter=2)
sDate    = S("Date",    fontName="Malgun",  fontSize=10, leading=14,
             alignment=1, textColor=colors.gray, spaceAfter=0)
sH1      = S("H1",      fontName="MalgunBd",fontSize=13, leading=18,
             textColor=colors.white, spaceAfter=0)
sH2      = S("H2",      fontName="MalgunBd",fontSize=11, leading=16,
             textColor=C_BLUE, spaceAfter=2)
sBody    = S("Body",    fontSize=10, leading=15)
sBullet  = S("Bullet",  fontSize=10, leading=15, leftIndent=12,
             bulletIndent=0)
sSmall   = S("Small",   fontSize=9,  leading=13, textColor=colors.HexColor("#444444"))
sFormula = S("Formula", fontName="MalgunBd", fontSize=10, leading=16,
             textColor=colors.HexColor("#1a3a6b"), leftIndent=20)
sWarn    = S("Warn",    fontSize=9,  leading=14, textColor=colors.HexColor("#333333"))
sTH      = S("TH",      fontName="MalgunBd", fontSize=9, leading=13,
             alignment=1, textColor=C_BLUE)
sTD      = S("TD",      fontSize=9, leading=13)
sTDc     = S("TDc",     fontSize=9, leading=13, alignment=1)

def h1_block(text):
    tbl = Table([[Paragraph(text, sH1)]], colWidths=[W - 40*mm])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), C_SKY),
        ("TOPPADDING",  (0,0), (-1,-1), 6),
        ("BOTTOMPADDING",(0,0),(-1,-1), 6),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("ROUNDEDCORNERS", [4]),
    ]))
    return tbl

def bullet(text):
    return Paragraph("• " + text, sBullet)

def subbullet(text):
    return Paragraph("  – " + text, sSmall)

# ── 문서 빌드 ─────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=20*mm, rightMargin=20*mm,
    topMargin=18*mm, bottomMargin=18*mm,
)
story = []
add = story.append

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 헤더 박스 (표지)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
cover_rows = [
    [Paragraph("10주차 실험 참고 노트", sTitle)],
    [Paragraph("AC 주파수 응답 — R, L, C 소자 및 직렬 R-L / R-C 네트워크", sSubtitle)],
    [Paragraph("기초전기전자실험 | Ch. 4 · 5 · 6  |  2026. 04. 28", sDate)],
]
cover_tbl = Table(cover_rows, colWidths=[W - 40*mm])
cover_tbl.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,-1), colors.HexColor("#eef4fb")),
    ("TOPPADDING",    (0,0), (-1,-1), 12),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ("LEFTPADDING",   (0,0), (-1,-1), 16),
    ("RIGHTPADDING",  (0,0), (-1,-1), 16),
    ("BOX", (0,0), (-1,-1), 1.5, C_BLUE),
    ("LINEBELOW", (0,1), (-1,1), 0.5, colors.HexColor("#aaccee")),
]))
add(cover_tbl)
add(Spacer(1, 8*mm))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1. 실험 목적
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
add(h1_block("1.  이 실험에서 무엇을 알아보는가?"))
add(Spacer(1, 3*mm))

purpose_data = [
    [Paragraph("챕터", sTH), Paragraph("실험 목적", sTH)],
    [
        Paragraph("Ch 4\nPart 1", sTDc),
        Paragraph(
            "저항(R)의 저항값이 주파수와 무관하게 <b>일정</b>한지 확인한다.\n"
            "→ 이상적인 탄소 저항은 f에 따른 임피던스 변화가 없다.", sTD),
    ],
    [
        Paragraph("Ch 4\nPart 2", sTDc),
        Paragraph(
            "인덕터의 유도 리액턴스 <b>X<sub>L</sub> = 2πfL</b>이 주파수에 "
            "<b>정비례</b>하여 선형 증가하는지 확인한다.\n"
            "→ f ↑  ⇒  X<sub>L</sub> ↑  (그래프: 원점 통과 직선)", sTD),
    ],
    [
        Paragraph("Ch 4\nPart 3", sTDc),
        Paragraph(
            "커패시터의 용량 리액턴스 <b>X<sub>C</sub> = 1/(2πfC)</b>가 주파수에 "
            "<b>반비례</b>하여 비선형 감소하는지 확인한다.\n"
            "→ f ↑  ⇒  X<sub>C</sub> ↓  (그래프: 반비례 곡선)", sTD),
    ],
    [
        Paragraph("Ch 5", sTDc),
        Paragraph(
            "직렬 R-L 회로에서 주파수 증가 시 V<sub>L</sub> 증가·V<sub>R</sub> 감소, "
            "전류 감소, 위상각 θ 증가를 확인한다.\n"
            "→ AC KVL (벡터 합산) E = √(V<sub>R</sub><super>2</super> + V<sub>L</sub><super>2</super>) 검증", sTD),
    ],
    [
        Paragraph("Ch 6", sTDc),
        Paragraph(
            "직렬 R-C 회로에서 주파수 증가 시 V<sub>C</sub> 감소·V<sub>R</sub> 증가, "
            "전류 증가, 위상각 |θ| 감소를 확인한다.\n"
            "→ AC KVL (벡터 합산) E = √(V<sub>R</sub><super>2</super> + V<sub>C</sub><super>2</super>) 검증", sTD),
    ],
]

cw = [22*mm, W - 40*mm - 22*mm]
purpose_tbl = Table(purpose_data, colWidths=cw, repeatRows=1)
purpose_tbl.setStyle(TableStyle([
    ("BACKGROUND",    (0, 0), (-1, 0), C_LIGHT),
    ("BACKGROUND",    (0, 1), (-1, 1), colors.white),
    ("BACKGROUND",    (0, 2), (-1, 2), C_GRAY),
    ("BACKGROUND",    (0, 3), (-1, 3), colors.white),
    ("BACKGROUND",    (0, 4), (-1, 4), C_GRAY),
    ("BACKGROUND",    (0, 5), (-1, 5), colors.white),
    ("BOX",           (0, 0), (-1,-1), 0.8, C_BLUE),
    ("INNERGRID",     (0, 0), (-1,-1), 0.4, colors.lightgrey),
    ("VALIGN",        (0, 0), (-1,-1), "MIDDLE"),
    ("TOPPADDING",    (0, 0), (-1,-1), 5),
    ("BOTTOMPADDING", (0, 0), (-1,-1), 5),
    ("LEFTPADDING",   (0, 0), (-1,-1), 6),
    ("RIGHTPADDING",  (0, 0), (-1,-1), 6),
]))
add(purpose_tbl)
add(Spacer(1, 6*mm))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2. 핵심 이론 요약
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
add(h1_block("2.  핵심 이론 요약"))
add(Spacer(1, 3*mm))

theory_data = [
    [
        Paragraph("소자\n주파수 응답", sTH),
        Paragraph("R — 저항", sTH),
        Paragraph("L — 인덕터", sTH),
        Paragraph("C — 커패시터", sTH),
    ],
    [
        Paragraph("임피던스 식", sTDc),
        Paragraph("Z = R  (일정)", sTDc),
        Paragraph("X<sub>L</sub> = 2πfL", sTDc),
        Paragraph("X<sub>C</sub> = 1/(2πfC)", sTDc),
    ],
    [
        Paragraph("f 증가 시", sTDc),
        Paragraph("변화 없음", sTDc),
        Paragraph("X<sub>L</sub> ↑  (비례)", sTDc),
        Paragraph("X<sub>C</sub> ↓  (반비례)", sTDc),
    ],
    [
        Paragraph("저주파 극한", sTDc),
        Paragraph("— ", sTDc),
        Paragraph("단락 (Short)", sTDc),
        Paragraph("개방 (Open)", sTDc),
    ],
    [
        Paragraph("고주파 극한", sTDc),
        Paragraph("—", sTDc),
        Paragraph("개방 (Open)", sTDc),
        Paragraph("단락 (Short)", sTDc),
    ],
]
cw2 = [28*mm, (W-40*mm-28*mm)/3] * 1
cw2 = [28*mm] + [(W-40*mm-28*mm)/3]*3
theory_tbl = Table(theory_data, colWidths=cw2, repeatRows=1)
theory_tbl.setStyle(TableStyle([
    ("BACKGROUND",    (0, 0), (-1, 0), C_LIGHT),
    ("BACKGROUND",    (0, 1), (-1, 1), colors.white),
    ("BACKGROUND",    (0, 2), (-1, 2), C_GRAY),
    ("BACKGROUND",    (0, 3), (-1, 3), colors.white),
    ("BACKGROUND",    (0, 4), (-1, 4), C_GRAY),
    ("BOX",           (0, 0), (-1,-1), 0.8, C_BLUE),
    ("INNERGRID",     (0, 0), (-1,-1), 0.4, colors.lightgrey),
    ("VALIGN",        (0, 0), (-1,-1), "MIDDLE"),
    ("TOPPADDING",    (0, 0), (-1,-1), 5),
    ("BOTTOMPADDING", (0, 0), (-1,-1), 5),
    ("LEFTPADDING",   (0, 0), (-1,-1), 6),
    ("RIGHTPADDING",  (0, 0), (-1,-1), 6),
    ("FONTNAME",      (0, 1), (0,-1), "MalgunBd"),
]))
add(theory_tbl)
add(Spacer(1, 4*mm))

# 수식 박스
formula_items = [
    Paragraph("<b>직렬 회로 AC KVL (벡터 합산)</b>", sH2),
    Paragraph(
        "E = sqrt( V<sub>R</sub><super>2</super> + V<sub>X</sub><super>2</super> )", sFormula),
    Spacer(1, 2*mm),
    Paragraph("<b>위상각 (Phase Angle)</b>", sH2),
    Paragraph(
        "θ = tan<super>-1</super>(X / R)  "
        "  →  R-L: θ &gt; 0 (lagging),   R-C: θ &lt; 0 (leading)", sFormula),
    Spacer(1, 2*mm),
    Paragraph("<b>RMS ↔ Peak-to-Peak 변환</b>", sH2),
    Paragraph(
        "V<sub>rms</sub> = V<sub>pp</sub> / (2√2)   "
        "  →   V<sub>pp</sub> = V<sub>rms</sub> × 2√2  ≈  V<sub>rms</sub> × 2.828", sFormula),
    Spacer(1, 2*mm),
    Paragraph("<b>전류 간접 측정 (감지 저항 R<sub>s</sub> 이용)</b>", sH2),
    Paragraph(
        "I = V<sub>Rs</sub> / R<sub>s</sub>   "
        "  →   X = V<sub>소자</sub> / I   (R<sub>s</sub> &lt;&lt; X 조건 필수)", sFormula),
]
formula_box_data = [[formula_items]]

# 수식 항목들을 세로 쌓기
formula_content = []
for item in formula_items:
    formula_content.append(item)

add(Spacer(1, 1*mm))
for item in formula_items:
    add(item)
add(Spacer(1, 5*mm))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3. 실험 진행 방법
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
add(h1_block("3.  실험 진행 방법"))
add(Spacer(1, 3*mm))

# 공통 준비
prep_rows = [
    [Paragraph("공통 준비 사항", S("PrepH", fontName="MalgunBd", fontSize=10,
                                   textColor=C_BLUE, leading=14))],
    [bullet("오실로스코프(KEYSIGHT MSO X 3022A)와 내장 Wave Gen 함수 발생기를 켠다.")],
    [bullet("브레드보드에 회로를 구성하고, 오실로스코프 채널로 peak-to-peak 전압을 측정한다.")],
    [bullet("주파수를 변경할 때마다 전원 전압(E 또는 지정 소자 전압)이 설정값을 유지하는지 반드시 재확인한다.")],
    [bullet("DMM은 RMS 값을 표시하므로, 필요 시 V_pp = V_rms × 2√2 로 환산한다.")],
]
prep_tbl = Table(prep_rows, colWidths=[W - 40*mm])
prep_tbl.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,-1), C_GREEN),
    ("BOX",           (0,0), (-1,-1), 0.8, colors.HexColor("#388e3c")),
    ("TOPPADDING",    (0,0), (-1,-1), 4),
    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ("LEFTPADDING",   (0,0), (-1,-1), 8),
    ("RIGHTPADDING",  (0,0), (-1,-1), 8),
]))
add(prep_tbl)
add(Spacer(1, 4*mm))

# 각 챕터 절차 표
proc_header = [
    Paragraph("챕터", sTH),
    Paragraph("회로 구성", sTH),
    Paragraph("전원 / 주파수 설정", sTH),
    Paragraph("측정 항목 및 계산", sTH),
]

proc_data = [proc_header]

rows = [
    (
        "Ch 4\nPart 1\n저항",
        "E (정현파) — R (1 kΩ) 직렬\n오실로스코프로 V_R 측정",
        "V_R = 4 V(p-p) 고정\n주파수: 1k / 3k / 5k / 7k / 10k Hz",
        "각 f 에서 V_R 측정\nR = V_R / I 계산\n→ 이론: R 일정 (주파수 무관)",
    ),
    (
        "Ch 4\nPart 2\n인덕터",
        "E — L (10 mH) + R_s (100 Ω) 직렬\nR_s 양단 전압으로 전류 측정",
        "V_L = 2 V(p-p) 고정\n주파수: 1k / 3k / 5k / 7k / 10k Hz",
        "V_Rs 측정 → I = V_Rs / 100\nX_L = V_L / I\n→ 그래프: X_L vs f (직선 확인)",
    ),
    (
        "Ch 4\nPart 3\n커패시터",
        "E — C (0.1 uF) + R_s (1.2 k / 3.3 kΩ) 직렬\nR_s 양단으로 전류 측정",
        "V_C 고정 (약 2 V(p-p))\n100 / 200 / 300 / 500 / 800 / 1k / 2k Hz",
        "V_Rs 측정 → I = V_Rs / R_s\nX_C = V_C / I\n→ 그래프: X_C vs f (반비례 곡선)",
    ),
    (
        "Ch 5\n직렬\nR-L",
        "E (2 V p-p) — R (100 Ω) + L (10 mH) 직렬",
        "E = 2 V(p-p) 고정\n1k ~ 10k Hz (1k 단위, 총 10점)",
        "V_R, V_L 측정\nZ_T = E/I, X_L, theta = tan-1(X_L/R)\nAC KVL 검증: E =? sqrt(V_R^2+V_L^2)",
    ),
    (
        "Ch 6\n직렬\nR-C",
        "E (2 V p-p) — R (1 kΩ) + C (0.1 uF) 직렬",
        "E = 2 V(p-p) 고정\n1k ~ 10k Hz (1k 단위, 총 10점)",
        "V_R, V_C 측정\nZ_T = E/I, X_C, theta = -tan-1(X_C/R)\nAC KVL 검증: E =? sqrt(V_R^2+V_C^2)",
    ),
]

for i, (ch, circ, src, meas) in enumerate(rows):
    bg = colors.white if i % 2 == 0 else C_GRAY
    proc_data.append([
        Paragraph(ch,    sTDc),
        Paragraph(circ,  sTD),
        Paragraph(src,   sTD),
        Paragraph(meas,  sTD),
    ])

cw3 = [18*mm, 52*mm, 45*mm, W-40*mm-18*mm-52*mm-45*mm]
proc_tbl = Table(proc_data, colWidths=cw3, repeatRows=1)
proc_tbl.setStyle(TableStyle([
    ("BACKGROUND",    (0, 0), (-1, 0), C_LIGHT),
    *[("BACKGROUND",  (0, i+1), (-1, i+1),
       colors.white if i % 2 == 0 else C_GRAY) for i in range(5)],
    ("BOX",           (0, 0), (-1,-1), 0.8, C_BLUE),
    ("INNERGRID",     (0, 0), (-1,-1), 0.4, colors.lightgrey),
    ("VALIGN",        (0, 0), (-1,-1), "TOP"),
    ("TOPPADDING",    (0, 0), (-1,-1), 5),
    ("BOTTOMPADDING", (0, 0), (-1,-1), 5),
    ("LEFTPADDING",   (0, 0), (-1,-1), 5),
    ("RIGHTPADDING",  (0, 0), (-1,-1), 5),
]))
add(proc_tbl)
add(Spacer(1, 5*mm))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 4. 주의사항 / 실험 전 체크리스트
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
add(h1_block("4.  주의사항 & 실험 전 체크리스트"))
add(Spacer(1, 3*mm))

warn_items = [
    ("측정 전 전압 재확인",
     "주파수를 바꿀 때마다 오실로스코프에서 설정 전압(E 또는 V_소자)이 유지되는지 확인. "
     "함수 발생기 출력 임피던스 때문에 실제 전압이 변할 수 있음."),
    ("감지 저항 조건",
     "R_s 는 측정 소자의 리액턴스(X_L 또는 X_C)보다 충분히 작아야 함. "
     "그렇지 않으면 V_소자 = E - V_Rs 로 보정 필요."),
    ("RMS vs Peak-to-Peak",
     "오실로스코프 → p-p 값 직접 읽기.  DMM → RMS 표시.  "
     "두 값 혼용 금지. 변환 시 V_pp = V_rms × 2√2 사용."),
    ("교차 주파수 메모",
     "X_L = R (Ch5) 또는 X_C = R (Ch6) 이 되는 주파수를 계산 후 실험 결과와 비교. "
     "이론값: f_cross = R / (2πL)  또는  f_cross = 1 / (2πRC)."),
    ("위상 측정 (여유 있을 때)",
     "오실로스코프 2채널로 V_R과 V_소자의 파형을 동시에 보고 시간차 Δt 측정 → "
     "θ = Δt / T × 360°."),
    ("브레드보드 배선",
     "리드 길이 최소화. 고주파(10 kHz 이상)에서는 기생 인덕턴스/커패시턴스가 측정에 영향을 줄 수 있음."),
]

warn_rows = []
for title, desc in warn_items:
    warn_rows.append([
        Paragraph("<b>☑  " + title + "</b>", sWarn),
        Paragraph(desc, sWarn),
    ])

warn_tbl = Table(warn_rows, colWidths=[38*mm, W-40*mm-38*mm])
warn_tbl.setStyle(TableStyle([
    ("BACKGROUND",    (0, 0), (-1,-1), C_YELLOW),
    ("BOX",           (0, 0), (-1,-1), 0.8, colors.HexColor("#f9a825")),
    ("INNERGRID",     (0, 0), (-1,-1), 0.3, colors.HexColor("#ffe082")),
    ("VALIGN",        (0, 0), (-1,-1), "TOP"),
    ("TOPPADDING",    (0, 0), (-1,-1), 4),
    ("BOTTOMPADDING", (0, 0), (-1,-1), 4),
    ("LEFTPADDING",   (0, 0), (-1,-1), 6),
    ("RIGHTPADDING",  (0, 0), (-1,-1), 6),
]))
add(warn_tbl)
add(Spacer(1, 5*mm))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 5. 준비물 요약
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
add(h1_block("5.  준비물 요약"))
add(Spacer(1, 3*mm))

equip_data = [
    [Paragraph("소자/장비", sTH), Paragraph("규격", sTH),
     Paragraph("사용 챕터", sTH), Paragraph("용도", sTH)],
    [Paragraph("오실로스코프", sTD), Paragraph("KEYSIGHT MSO X 3022A", sTD),
     Paragraph("전체", sTDc), Paragraph("p-p 전압 파형 측정 + Wave Gen", sTD)],
    [Paragraph("디지털 멀티미터", sTD), Paragraph("—", sTDc),
     Paragraph("전체", sTDc), Paragraph("AC 전압·저항 측정 (RMS)", sTD)],
    [Paragraph("탄소 저항 1 kΩ", sTD), Paragraph("1개", sTDc),
     Paragraph("Ch4 P1, Ch6", sTDc), Paragraph("저항 주파수 응답 / R-C 회로 R", sTD)],
    [Paragraph("탄소 저항 100 Ω", sTD), Paragraph("1개", sTDc),
     Paragraph("Ch4 P2, Ch5", sTDc), Paragraph("감지 저항(R_s) / R-L 회로 R", sTD)],
    [Paragraph("탄소 저항 1.2 kΩ", sTD), Paragraph("1개", sTDc),
     Paragraph("Ch4 P3", sTDc), Paragraph("커패시터 R_s (저주파 대역)", sTD)],
    [Paragraph("탄소 저항 3.3 kΩ", sTD), Paragraph("1개", sTDc),
     Paragraph("Ch4 P3", sTDc), Paragraph("커패시터 R_s (고주파 대역)", sTD)],
    [Paragraph("인덕터 10 mH", sTD), Paragraph("1개", sTDc),
     Paragraph("Ch4 P2, Ch5", sTDc), Paragraph("유도 리액턴스 측정", sTD)],
    [Paragraph("커패시터 0.1 uF", sTD), Paragraph("2개", sTDc),
     Paragraph("Ch4 P3, Ch6", sTDc), Paragraph("용량 리액턴스 측정", sTD)],
    [Paragraph("브레드보드 + 배선", sTD), Paragraph("—", sTDc),
     Paragraph("전체", sTDc), Paragraph("회로 구성", sTD)],
]

cw4 = [32*mm, 38*mm, 22*mm, W-40*mm-32*mm-38*mm-22*mm]
equip_tbl = Table(equip_data, colWidths=cw4, repeatRows=1)
equip_tbl.setStyle(TableStyle([
    ("BACKGROUND",    (0, 0), (-1, 0), C_LIGHT),
    *[("BACKGROUND",  (0, i+1), (-1, i+1),
       colors.white if i % 2 == 0 else C_GRAY) for i in range(9)],
    ("BOX",           (0, 0), (-1,-1), 0.8, C_BLUE),
    ("INNERGRID",     (0, 0), (-1,-1), 0.4, colors.lightgrey),
    ("VALIGN",        (0, 0), (-1,-1), "MIDDLE"),
    ("TOPPADDING",    (0, 0), (-1,-1), 4),
    ("BOTTOMPADDING", (0, 0), (-1,-1), 4),
    ("LEFTPADDING",   (0, 0), (-1,-1), 5),
    ("RIGHTPADDING",  (0, 0), (-1,-1), 5),
]))
add(equip_tbl)
add(Spacer(1, 4*mm))

# 푸터
add(HRFlowable(width="100%", thickness=0.5, color=C_BLUE))
add(Spacer(1, 1*mm))
add(Paragraph(
    "기초전기전자실험  ·  10주차 참고 노트  ·  2026. 04. 28",
    S("Footer", fontSize=8, alignment=1, textColor=colors.gray, leading=12)
))

# ── 빌드 ─────────────────────────────────────────────────────────
doc.build(story)
print(f"PDF 생성 완료: {OUTPUT}")
