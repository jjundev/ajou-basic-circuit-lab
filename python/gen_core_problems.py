# -*- coding: utf-8 -*-
"""핵심 보충 4문제(강의노트 범위) PNG 생성 + 검산 해답 키.
grill-review Blocker 수정: 존재하지 않는 Nilsson 추출 대신 강의노트 공식 기반 생성."""
import os, math, cmath
from PIL import Image, ImageDraw, ImageFont

ROOT = r"C:\Users\Hyunjun\Desktop\현준대학\기전실"
DEST = os.path.join(ROOT, "기말고사 대비")
FONTS = r"C:\Windows\Fonts"
F_TITLE = ImageFont.truetype(os.path.join(FONTS, "malgunbd.ttf"), 30)
F_BODY  = ImageFont.truetype(os.path.join(FONTS, "malgun.ttf"), 25)
NAVY = (26, 58, 107)
BLACK = (20, 20, 20)
GRAY = (120, 120, 120)

WIDTH = 1040
MARGIN = 44
MAXW = WIDTH - 2 * MARGIN
LH_T, LH_B, PARA = 46, 40, 12

def wrap(text, font):
    out, cur = [], ""
    for ch in text:
        if font.getlength(cur + ch) <= MAXW:
            cur += ch
        else:
            out.append(cur); cur = ch
    out.append(cur)
    return out

def render(path, title, paras):
    # measure
    blocks = [("t", wrap(title, F_TITLE))]
    for p in paras:
        blocks.append(("b", wrap(p, F_BODY)))
    h = MARGIN
    h += len(blocks[0][1]) * LH_T + 14  # title + rule
    for kind, lines in blocks[1:]:
        h += len(lines) * LH_B + PARA
    h += MARGIN
    img = Image.new("RGB", (WIDTH, h), (255, 255, 255))
    d = ImageDraw.Draw(img)
    y = MARGIN
    for line in blocks[0][1]:
        d.text((MARGIN, y), line, font=F_TITLE, fill=NAVY); y += LH_T
    d.line((MARGIN, y + 2, WIDTH - MARGIN, y + 2), fill=(180, 180, 180), width=2); y += 14
    for kind, lines in blocks[1:]:
        for line in lines:
            d.text((MARGIN, y), line, font=F_BODY, fill=BLACK); y += LH_B
        y += PARA
    d.text((MARGIN, h - 30), "[생성 문제 · 9~15주차 강의노트 범위 · 해답: 생성문제_해답.md]",
           font=ImageFont.truetype(os.path.join(FONTS, "malgun.ttf"), 16), fill=GRAY)
    img.save(path)
    return img.size

def polar(z):
    return abs(z), math.degrees(cmath.phase(z))

ans = []
SQ2 = math.sqrt(2)

# ── 9.91 (6/10) 직렬 RLC 임피던스 크기·위상 (유도성) ──
render(os.path.join(DEST, "6월10일", "01_new_09-91.png"),
 "[생성 9.91] 직렬 RLC 회로 — 임피던스 크기·위상",
 ["60 Hz 전원 v(t) = 170 cos(2π·60·t) [V] 가 R = 50 Ω, L = 0.2 H, C = 40 μF 인 직렬 RLC 회로에 인가된다.",
  "(a) 리액턴스 X_L = ωL, X_C = 1/(ωC) 를 구하라.",
  "(b) 총 임피던스 Z = R + j(X_L - X_C) 와 크기 |Z| = √(R² + X²), 위상 θ = arctan(X/R) 를 구하라.",
  "(c) 전류 페이저 I (피크와 rms) 를 구하라.",
  "(d) V_R, V_L, V_C 를 구하고 E = √(V_R² + (V_L - V_C)²) 로 KVL(페이저 합)을 검증하라."])
w = 2 * math.pi * 60; XL = w * 0.2; XC = 1 / (w * 40e-6); Z = 50 + 1j * (XL - XC)
mZ, aZ = polar(Z); Ipk = 170 / mZ; Irms = Ipk / SQ2
VR, VL, VC = Ipk * 50, Ipk * XL, Ipk * XC; E = math.sqrt(VR**2 + (VL - VC)**2)
ans.append(("9.91 직렬 RLC 임피던스(유도성)",
 [f"X_L = ωL = {XL:.2f} Ω,  X_C = 1/(ωC) = {XC:.2f} Ω  (ω=377 rad/s)",
  f"Z = 50 + j({XL:.1f}-{XC:.1f}) = 50 + j{XL-XC:.2f} Ω,  |Z| = {mZ:.2f} Ω,  θ = +{aZ:.2f}° (유도성)",
  f"I_peak = 170/|Z| = {Ipk:.3f} A,  I_rms = {Irms:.3f} A",
  f"V_R={VR:.1f}, V_L={VL:.1f}, V_C={VC:.1f} V (피크) → E=√(V_R²+(V_L-V_C)²)={E:.1f} V ≈ 170 V ✓"]))

# ── 9.92 (6/10) 직·병렬 등가 임피던스 ──
render(os.path.join(DEST, "6월10일", "02_new_09-92.png"),
 "[생성 9.92] 직·병렬 회로 — 등가 임피던스",
 ["ω = 1000 rad/s. 직렬 가지 Z1 은 R1 = 30 Ω 과 L = 40 mH 의 직렬, 병렬 가지 Z2 는 R2 = 100 Ω 과 C = 10 μF 의 병렬이다. 두 가지는 서로 직렬이다 (Z_T = Z1 + Z2).",
  "(a) Z_L = jωL, Z_C = 1/(jωC) 를 구하라.",
  "(b) 병렬부 Z2 = R2 ∥ Z_C 를 직교형(a + jb)으로 구하라.",
  "(c) 전체 등가 임피던스 Z_T 와 |Z_T|, ∠Z_T 를 구하라."])
w = 1000.0; ZL = 1j * w * 40e-3; ZC = 1 / (1j * w * 10e-6); Z1 = 30 + ZL
R2 = 100.0; Z2 = (R2 * ZC) / (R2 + ZC); ZT = Z1 + Z2; mT, aT = polar(ZT)
ans.append(("9.92 직·병렬 등가 임피던스",
 [f"Z_L = jωL = j{ZL.imag:.1f} Ω,  Z_C = 1/(jωC) = -j{abs(ZC.imag):.1f} Ω",
  f"Z1 = 30 + j40 Ω,  Z2 = R2∥Z_C = {Z2.real:.2f} {'+' if Z2.imag>=0 else '-'} j{abs(Z2.imag):.2f} Ω",
  f"Z_T = Z1 + Z2 = {ZT.real:.2f} {'+' if ZT.imag>=0 else '-'} j{abs(ZT.imag):.2f} Ω",
  f"|Z_T| = {mT:.2f} Ω,  ∠Z_T = {aT:.2f}°"]))

# ── 9.93 (6/10) 페이저 전압 분배 ──
render(os.path.join(DEST, "6월10일", "03_new_09-93.png"),
 "[생성 9.93] 정현파 회로 — 페이저 전압 분배",
 ["V_s = 120∠0° V(rms), ω = 2000 rad/s. 전원에 R = 40 Ω 이 직렬, 그 뒤 L = 20 mH 와 C = 10 μF 의 병렬(L ∥ C)이 연결된다. 병렬부 양단 전압 V_o 를 구한다.",
  "(a) Z_L, Z_C, 병렬부 Z_p = L ∥ C 를 구하라.",
  "(b) 전압 분배 V_o = V_s · Z_p/(R + Z_p) 를 크기·위상으로 구하라.",
  "(c) V_o 와 V_s 의 위상차를 말하라."])
w = 2000.0; ZL = 1j * w * 20e-3; ZC = 1 / (1j * w * 10e-6); Zp = (ZL * ZC) / (ZL + ZC)
Vs = 120 + 0j; Vo = Vs * Zp / (40 + Zp); mVo, aVo = polar(Vo)
ans.append(("9.93 페이저 전압 분배",
 [f"Z_L = j{ZL.imag:.0f} Ω,  Z_C = -j{abs(ZC.imag):.0f} Ω,  Z_p = L∥C = {Zp.real:.1f}+j{Zp.imag:.1f} = j{Zp.imag:.0f} Ω",
  f"V_o = 120·Z_p/(40+Z_p) = {Vo.real:.2f}+j{Vo.imag:.2f} V",
  f"|V_o| = {mVo:.2f} V(rms),  ∠V_o = {aVo:.2f}°  → V_s 보다 {aVo:.1f}° 앞섬(진상)"]))

# ── 9.94 (6/14 모의) 직렬 RLC KVL 페이저 합 (용량성) ──
render(os.path.join(DEST, "6월14일", "11_mock_09-94.png"),
 "[생성 9.94 · 모의] 직렬 RLC — KVL 페이저 합 검증",
 ["v(t) = 100 cos(2π·60·t) [V] 가 R = 20 Ω, L = 50 mH, C = 20 μF 직렬 RLC 에 인가된다.",
  "(a) X_L, X_C 를 구하라.",
  "(b) Z = R + j(X_L - X_C), |Z|, θ 를 구하고 유도성/용량성을 판정하라.",
  "(c) 전류 I (rms) 를 구하라.",
  "(d) V_R, V_L, V_C 를 구하고 E = √(V_R² + (V_L - V_C)²) 가 전원 전압과 일치하는지 검증하라."])
w = 2 * math.pi * 60; XL = w * 50e-3; XC = 1 / (w * 20e-6); Z = 20 + 1j * (XL - XC)
mZ, aZ = polar(Z); Ipk = 100 / mZ; Irms = Ipk / SQ2
VR, VL, VC = Ipk * 20, Ipk * XL, Ipk * XC; E = math.sqrt(VR**2 + (VL - VC)**2)
ans.append(("9.94 직렬 RLC KVL 합(용량성·모의)",
 [f"X_L = {XL:.2f} Ω,  X_C = {XC:.2f} Ω  (ω=377 rad/s)",
  f"Z = 20 + j({XL:.1f}-{XC:.1f}) = 20 - j{XC-XL:.2f} Ω,  |Z| = {mZ:.2f} Ω,  θ = {aZ:.2f}° → 용량성(X_C>X_L)",
  f"I_peak = {Ipk:.3f} A,  I_rms = {Irms:.3f} A",
  f"V_R={VR:.1f}, V_L={VL:.1f}, V_C={VC:.1f} V (피크) → E={E:.1f} V ≈ 100 V ✓"]))

# ── 해답 키 ──
lines = ["# 생성 문제 해답 키 (검산값)", "",
         "> grill-review Blocker 수정에 따라 강의노트 공식 기반으로 **생성**한 보충 4문제(9.91~9.94)의 해답이다.",
         "> 값은 Python(cmath)으로 계산해 문제 수치와 정확히 일치한다. solve-exam-prep 풀이와 대조용.", ""]
for title, rows in ans:
    lines.append(f"## {title}")
    for r in rows:
        lines.append(f"- {r}")
    lines.append("")
with open(os.path.join(DEST, "생성문제_해답.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("생성 완료:")
for p in ["6월10일/01_new_09-91.png", "6월10일/02_new_09-92.png",
          "6월10일/03_new_09-93.png", "6월14일/11_mock_09-94.png", "생성문제_해답.md"]:
    fp = os.path.join(DEST, *p.split("/"))
    print(f"  {p}: {'OK' if os.path.exists(fp) else 'FAIL'}")
