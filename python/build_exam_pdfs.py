# -*- coding: utf-8 -*-
"""
기전실 기말 시험지 PDF 생성기 (가로 A4, 표지 1p + 문제당 1p, 태블릿 풀이용).

manifest.csv 주도:
- kind=new(핵심)·mock(6/14 미니모의)만 싣고 cut(=_제외/)은 배제.
- mock 4개는 물리 폴더(6/11·6/13·6/14)에서 manifest 경로로 끌어와 전부 6/14 키스톤 PDF로 라우팅.

방향 인식 배치(좁고 긴 기전실 문제 대응):
- 세로형(ar < TALL_AR): 좌측 절반에 크게 배치, 우측이 풀이공간.
- 가로형(ar >= TALL_AR): 폭맞춤, 하단 절반이 풀이공간.

6/15는 풀 문제가 없어 표지-only 복습 시트(오답 재풀이 안내 + 함정 체크리스트) 1p.
한글: Malgun Gothic. 재실행 가능(덮어쓰기).
"""
import os, csv
from PIL import Image
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = r"C:\Users\Hyunjun\Desktop\현준대학\기전실"
DEST = os.path.join(ROOT, "기말고사 대비")
MANIFEST = os.path.join(DEST, "manifest.csv")
W, H = landscape(A4)          # 842 x 595
M = 36                        # margin
SOLVE_MIN_FRAC = 0.5          # 가로형: 페이지 하단 이 비율은 풀이공간(이미지 높이 상한)
TALL_AR = 1.6                 # ar < 이 값이면 세로형(우측 풀이공간)
LEFT_FRAC = 0.5               # 세로형 이미지가 차지할 좌측 폭 비율

# ---- fonts ----
FONTS = r"C:\Windows\Fonts"
BODY, BOLD = "Malgun", "MalgunBd"
try:
    pdfmetrics.registerFont(TTFont(BODY, os.path.join(FONTS, "malgun.ttf")))
    pdfmetrics.registerFont(TTFont(BOLD, os.path.join(FONTS, "malgunbd.ttf")))
except Exception as e:
    print("WARN: malgun 등록 실패, Helvetica 폴백(한글 깨질 수 있음):", e)
    BODY = BOLD = "Helvetica"

CHAPMAP = {6: "L·C 직병렬 합성", 9: "정현파·phasor·임피던스",
           10: "최대전력전달", 14: "필터·공진"}

# 날짜 → (요일, 범위제목, 떠올릴 개념 불릿)
DAYMAP = {
    "6월7일":  ("일", "Ch6 L·C 직병렬 합성 (지남)",
               ["L 직렬 합산 / 병렬 역수합",
                "C 병렬 합산 / 직렬 역수합",
                "(v-i 미적분·에너지는 시험범위 밖)"]),
    "6월8일":  ("월", "Ch9 정현파·phasor·임피던스",
               ["ω = 2πf, 진폭·주기·위상",
                "rms = peak / √2 (정현파)",
                "Z_R=R, Z_L=+jωL, Z_C=−j/(ωC)"]),
    "6월9일":  ("화", "Ch9 정현파·AC 테브난",
               ["정현파 식·위상·rms = peak/√2",
                "AC 테브난: Z_Th = Z1∥Z2, E_Th 전압분배",
                "(source transform·node/mesh는 범위 밖)"]),
    "6월10일": ("수", "Ch9 직·병렬 RLC 임피던스·페이저",
               ["Z=R+j(X_L−X_C), |Z|=√(R²+X²), θ=arctan(X/R)",
                "직·병렬 합성 1/Z_T=Σ1/Z, 전압·전류 분배",
                "직렬 KVL 합 E=√(V_R²+(V_L−V_C)²)"]),
    "6월11일": ("목", "Ch10 최대평균전력전달",
               ["최대전력 ⇔ Z_L = Z_Th* (켤레 정합)",
                "P_max = |V_Th,rms|² / (4·R_Th)",
                "rms/peak · ½계수 주의"]),
    "6월12일": ("금", "Ch14 저역·고역 통과 필터",
               ["cutoff ω_c = 1/RC (RC), R/L (RL)",
                "|H(jω)| · 위상, ω→0/∞ 극한"]),
    "6월13일": ("토", "Ch14 대역통과·대역저지 필터",
               ["center ω₀ = 1/√(LC)",
                "대역폭 β,  Q = ω₀/β"]),
    "6월14일": ("일", "누적 실전 (키스톤)",
               ["Ch9·10·14 전 범위 (Ch6은 직병렬만)",
                "미니모의 4 (9.94·10.42·14.23·14.40) 시간 재고",
                "부호·rms/peak·½계수 최종 점검"]),
    "6월15일": ("월", "최종 점검 (복습 전용)",
               ["오답.md 재풀이 — 식 세팅부터 다시",
                "최대전력·cutoff·공진·Q 공식 재유도",
                "부호·단위·rms↔peak 변환만 마지막 점검"]),
}

REVIEW_CHECK = [
    "rms vs peak — ½계수: P=½|I|²R(peak) vs |I_rms|²R(rms)",
    "임피던스 부호: 인덕터 +jωL, 커패시터 −j/(ωC)",
    "각도 단위 ° / rad, 각주파수 ω 값 명시",
    "임피던스 크기·위상: |Z|=√(R²+X²), θ=arctan(X/R)",
    "필터 극한: ω→0, ω→∞, 공진 ω₀ 거동",
]

DATES = ["6월7일", "6월8일", "6월9일", "6월10일",
         "6월11일", "6월12일", "6월13일", "6월14일"]


def num_key(pid):
    try:
        return tuple(int(x) for x in pid.split("."))
    except ValueError:
        return (10 ** 9,)


def chap_of(pid):
    return int(pid.split(".")[0])


def load_manifest():
    with open(MANIFEST, encoding="utf-8") as f:
        return [r for r in csv.DictReader(f)]


def make_item(r, mock):
    pid = r["problem"]
    ch = chap_of(pid)
    return dict(path=os.path.join(DEST, r["date"], r["file"]),  # cross-folder via manifest date
                pid=pid, chap=ch, topic=CHAPMAP.get(ch, f"Ch{ch}"), mock=mock)


def items_for(date, rows):
    # 자기 날짜의 new + mock 을 번호순으로 함께 배치(mock 도 그 날 연습지에 노출)
    core = sorted((r for r in rows if r["date"] == date and r["kind"] in ("new", "mock")),
                  key=lambda r: num_key(r["problem"]))
    items = [make_item(r, r["kind"] == "mock") for r in core]
    if date == "6월14일":   # 다른 날짜의 mock 도 키스톤으로 모음(자기 날짜 mock 은 이미 포함)
        mock = sorted((r for r in rows if r["kind"] == "mock" and r["date"] != date),
                      key=lambda r: num_key(r["problem"]))
        items += [make_item(r, True) for r in mock]
    return items


def wrap(text, font, size, maxw):
    lines, cur = [], ""
    for ch in text:
        if ch == "\n":
            lines.append(cur); cur = ""; continue
        if pdfmetrics.stringWidth(cur + ch, font, size) <= maxw:
            cur += ch
        else:
            lines.append(cur); cur = ch
    if cur:
        lines.append(cur)
    return lines


def dlabel(date):
    return date.replace("6월", "6/").replace("일", "")


def title_bar(c, date):
    wd, rng, _ = DAYMAP[date]
    c.setFillColorRGB(0.13, 0.20, 0.34); c.rect(0, H - 46, W, 46, fill=1, stroke=0)
    c.setFillColorRGB(1, 1, 1); c.setFont(BOLD, 14)
    c.drawString(M, H - 30, f"기초전기실험 기말대비    ·    {dlabel(date)} ({wd}) — {rng}"[:90])


def concept_col(c, date):
    _, _, concepts = DAYMAP[date]
    by = H - 46 - 8 - 26
    col_top = by - 20
    colw = (W - 2 * M) / 2 - 18
    c.setFillColorRGB(0, 0, 0); c.setFont(BOLD, 11)
    c.drawString(M, col_top, "떠올릴 개념")
    c.setFont(BODY, 9.5); y = col_top - 16
    for b in concepts[:7]:
        for li, line in enumerate(wrap(b, BODY, 9.5, colw - 10)):
            if y < M + 24:
                break
            c.drawString(M, y, ("• " if li == 0 else "   ") + line); y -= 12
    return by, col_top, colw


def draw_cover(c, date, items):
    n = len(items)
    title_bar(c, date)
    by = H - 46 - 8 - 26
    c.setFillColorRGB(0.96, 0.95, 0.88); c.rect(M, by, W - 2 * M, 26, fill=1, stroke=0)
    c.setFillColorRGB(0.1, 0.1, 0.1); c.setFont(BODY, 9.5)
    c.drawString(M + 8, by + 8,
                 "①  오답.md 어제 오답부터 재풀이        ②  신규는 공부계획 ID대로        ③  채점: solve-exam-prep 로 풀이 대조")
    _, col_top, _ = concept_col(c, date)
    rx = M + (W - 2 * M) / 2 + 12
    c.setFillColorRGB(0, 0, 0); c.setFont(BOLD, 11)
    c.drawString(rx, col_top, f"문항 목차 (총 {n}문항)")
    c.setFont(BODY, 9.5); y = col_top - 16
    for idx, it in enumerate(items, 1):
        if y < M + 24:
            break
        line = f"[{idx}]  {it['pid']} — {it['topic']}" + ("   · 모의" if it["mock"] else "")
        c.drawString(rx, y, line); y -= 12.5
    c.setFillColorRGB(0.3, 0.3, 0.3); c.setFont(BODY, 9)
    c.drawString(M, M, "한 문제당 1페이지 · 가로모드 · 풀이공간 포함    |    권장: 신규 풀이 → 채점·오답기록 → (6/14·15) 오답 재풀이")
    c.showPage()


def draw_review_cover(c, date):
    title_bar(c, date)
    by = H - 46 - 8 - 26
    c.setFillColorRGB(0.96, 0.95, 0.88); c.rect(M, by, W - 2 * M, 26, fill=1, stroke=0)
    c.setFillColorRGB(0.1, 0.1, 0.1); c.setFont(BODY, 9.5)
    c.drawString(M + 8, by + 8,
                 "시험 전날 — 새 문제 없음. 오답.md 재풀이 + 공식 재유도 + 함정 점검만.")
    _, col_top, colw = concept_col(c, date)
    rx = M + (W - 2 * M) / 2 + 12
    c.setFillColorRGB(0, 0, 0); c.setFont(BOLD, 11)
    c.drawString(rx, col_top, "자주 틀리는 함정 체크")
    c.setFont(BODY, 9.5); y = col_top - 16
    for b in REVIEW_CHECK:
        for li, line in enumerate(wrap(b, BODY, 9.5, colw - 10)):
            if y < M + 24:
                break
            c.drawString(rx, y, ("□  " if li == 0 else "    ") + line); y -= 13
    c.setFillColorRGB(0.3, 0.3, 0.3); c.setFont(BODY, 9)
    c.drawString(M, M, "마지막 30분: 공식 목록 · 자주 틀린 부호 · 단위 · rms↔peak 변환만.")
    c.showPage()


def draw_problem(c, idx, n, it):
    c.setFillColorRGB(0, 0, 0); c.setFont(BOLD, 11)
    head = f"[{idx}/{n}]   Ch{it['chap']} · {it['pid']}   —   {it['topic']}" + ("   · 모의" if it["mock"] else "")
    c.drawString(M, H - M - 4, head)
    c.setFillColorRGB(0.4, 0.4, 0.4); c.setFont(BODY, 10)
    c.drawRightString(W - M, H - M - 4, f"{idx} / {n}")
    rule_y = H - M - 15
    c.setStrokeColorRGB(0.7, 0.7, 0.7); c.setLineWidth(0.7); c.line(M, rule_y, W - M, rule_y)

    region_top = rule_y - 12
    avail_w = W - 2 * M
    iw, ih = Image.open(it["path"]).size
    ar = iw / ih
    if ar < TALL_AR:
        # 세로형: 좌측 절반에 크게, 우측이 풀이공간
        scale = min((avail_w * LEFT_FRAC) / iw, (region_top - M) / ih)
        sw, sh = iw * scale, ih * scale
        x, y = M, region_top - sh
        c.drawImage(it["path"], x, y, width=sw, height=sh, mask="auto")
        c.setFillColorRGB(0.78, 0.78, 0.78); c.setFont(BODY, 9)
        c.drawString(x + sw + 16, region_top - 10, "— 풀이 —")
    else:
        # 가로형: 폭맞춤, 하단 절반이 풀이공간
        img_max_h = region_top - H * SOLVE_MIN_FRAC
        scale = min(avail_w / iw, img_max_h / ih)
        sw, sh = iw * scale, ih * scale
        x, y = M, region_top - sh
        c.drawImage(it["path"], x, y, width=sw, height=sh, mask="auto")
        c.setFillColorRGB(0.78, 0.78, 0.78); c.setFont(BODY, 9)
        c.drawString(M, y - 16, "— 풀이 —")
    c.showPage()


def build_day(date, rows):
    items = items_for(date, rows)
    if not items:
        print(f"{date}: 문제 없음, 건너뜀"); return
    out = os.path.join(DEST, date, f"문제_{date}.pdf")
    c = canvas.Canvas(out, pagesize=(W, H))
    draw_cover(c, date, items)
    for i, it in enumerate(items, 1):
        draw_problem(c, i, len(items), it)
    c.save()
    print(f"{date}: {len(items)}문제 → 문제_{date}.pdf ({len(items) + 1} pages)")


def build_review_sheet(date="6월15일"):
    out = os.path.join(DEST, date, f"문제_{date}.pdf")
    c = canvas.Canvas(out, pagesize=(W, H))
    draw_review_cover(c, date)
    c.save()
    print(f"{date}: 복습 시트(표지 1p) → 문제_{date}.pdf")


def main():
    rows = load_manifest()
    for date in DATES:
        build_day(date, rows)
    build_review_sheet("6월15일")


if __name__ == "__main__":
    main()
