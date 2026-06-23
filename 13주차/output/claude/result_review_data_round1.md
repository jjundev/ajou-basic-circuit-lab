## 실험 결과 검증

### [Table 10.5]
- Markdown 무결성: PASS (4-column header/separator/body 일치, escape·줄바꿈 없음)
- Table 구조: FAIL — 교재 원형은 Calculated | Measured 2열이며 %(Difference) 열은 교재에 없다. 보고서는 임의로 %(Difference) 열을 추가했다 (HTML 주석에 "보고서 비교용 추가"로 명시되어 있으나 SKILL 규칙상 FAIL).
- Measured 원본 대조: PASS — V_R_1 = 2.25 V, V_R_2 = 1.49 V는 측정값.md (line 38–39)와 일치. 도출된 I_1_meas = 2.296 mA_pp, I_2_meas = 3.218 mA_pp, |I_s_meas| = 3.871 mA_pp, Z_T_meas = 1033.32 Ω 재계산 모두 일치.
- Calculated 재계산: PASS — X_L = 628.32 Ω, X_C = 795.78 Ω, |Z_1| = 1164.13 Ω ∠+32.66°, |Z_2| = 920.67 Ω ∠−59.81°, I_1_calc = 3.436 mA_pp, I_2_calc = 4.345 mA_pp, |I_s_calc| = 5.423 mA_pp ∠+20.54°, Z_T_calc = 737.6 Ω 재계산 모두 일치. 페이저 합산 직각변환 (cos/sin 계산값 0.8419, −0.5396, 0.5028, 0.8645)도 일치.
- %(Difference) 계산: PASS (공식 자체는 정확) — Z_T 40.09%, I_s 28.62%, I_1 33.18%, I_2 25.94% 모두 |Calc−Meas|/Calc × 100 공식대로 재계산 일치.
- ⚠️ 모든 행 %(Difference) > 20% — Z_T 40.09%, I_s 28.62%, I_1 33.18%, I_2 25.94%. 측정값(V_R_1 = 2.25 V_pp, V_R_2 = 1.49 V_pp)이 이론값(V_R_1_calc = I_1×R_1 = 3.436e-3 × 980 = 3.367 V_pp, V_R_2_calc = I_2×R_2 = 4.345e-3 × 463 = 2.012 V_pp)에서 일관되게 약 1/1.5 비율로 작게 나옴. E = 8 V_pp(교재 명목값)으로 측정했지만 4 V_pp 기준으로 환산을 빼먹었거나, 측정 시 채널 감도 오인 가능성 — 측정값 재확인 권고.

### [Table 10.6]
- Markdown 무결성: PASS
- Table 구조: PASS — 교재 원형(D_1 | D_2 | θ, 행: E and I_1, E and I_2)과 동일.
- Measured 원본 대조: PASS — D_1 = 5.0 div, D_2 = 0.45/0.83 div 모두 측정값.md (line 51–52)와 일치.
- 측정 기반 산출값 검증 (θ): PASS — θ_1 = 360 × 0.45/5.0 = 32.40°, θ_2 = 360 × 0.83/5.0 = 59.76° 재계산 일치. 부호 규약(인덕성 가지 lag → −, 용량성 가지 lead → +)도 절차 일치. Table 10.5의 calculated 각도(32.66°, 59.81°)와 0.26°/0.05° 편차로 일관성 확보.

### [Table 12.1]
- Markdown 무결성: PASS
- Table 구조: PASS — 교재 원형(Original | Thevenin Equivalent, 행: V_R_L(R_L=1kΩ), E_Th, Z_Th, V_R_L(R_L=6.8kΩ))과 동일.
- Measured 원본 대조: PASS — V_R_L(1kΩ, 원회로) = 1.24 V, V_R_L(1kΩ, Thev 등가) = 1.40 V, E_Th(개방전압) = 2.77 V, V_R_L(6.8kΩ, 원회로) = 2.37 V 모두 측정값.md (line 69–72)와 일치.
- Calculated 재계산: **FAIL** — Table 12.1 Thev Eq 열의 E_Th 셀에 2.77 V_pp ∠0°(Part 1(c) 실측 개방전압)이 기록되어 있다. 교재 Part 1(d)는 "Using the measured resistance levels, calculate the magnitude of E_Th and its associated angle ... Record both the magnitude and angle in the second column of Table 12.1" 이라고 명시한다. 즉 두 번째 열은 계산된 E_Th여야 한다: E_Th_calc = E × R_2_meas / (R_1_meas + R_2_meas) = 4 × 3.31/(1.18 + 3.31) = 4 × 3.31/4.49 ≈ **2.949 V_pp ∠0°**. 보고서가 Part 1(d) 계산 단계를 생략하고 첫 번째 열 값을 그대로 옮겨 적었다. 측정-계산 6% 편차가 묻혀 비교 가치가 사라졌다.
  - 단, 같은 보고서 안의 V_R_L(R_L = 6.8 kΩ, Thev Eq) 도출 계산은 Part 1(f) "Insert the measured value of E_Th(p-p) from part 1(c) in Fig. 12.5" 절차상 측정 E_Th(2.77)을 쓰는 것이 맞고 재계산값 2.443 V_pp도 일치한다 (Z_total = √(7549.89² + 628.32²) = 7575.99 Ω, I_load = 2.77/7575.99 = 0.3657 mA_pp, V_RL = 0.3657e-3 × 6680 = 2.443 V_pp). Part 1(d) (Table cell 기록) ≠ Part 1(f) (실험 setup)이므로, Table cell만 수정하면 된다.
  - Original Z_Th 계산: PASS — R_1∥R_2 = (1180 × 3310)/4490 = 869.89 Ω; |Z_Th| = √(869.89² + 628.32²) = 1073.08 Ω; θ = atan(628.32/869.89) = +35.84° 재계산 일치.
  - Thev Eq Z_Th: PASS — Part 2(d) 절차상 Table 12.2 결과(|Z_Th|_exp = 1282.05 ∠+34.23°)를 직각변환 (1282.05 × cos34.23° = 1060.05, × sin34.23° = 721.16) 결과 일치.

### [Table 12.2]
- Markdown 무결성: PASS
- Table 구조: PASS — 교재 원형(단일 Measured 열, 행: V_Rs(p-p), I(p-p), Z_Th, D_1, D_2, θ)과 동일.
- Measured 원본 대조: PASS — V_Rs = 29.3 mV, D_1 = 5.0 div, D_2 = 0.475 div, θ = 34.23° 모두 측정값.md (line 87–90)와 일치.
- 측정 기반 산출값 검증 (I, |Z_Th|): PASS — I = V_Rs/R_s = 29.3e-3/9.39 = 3.120 mA_pp, |Z_Th| = E/I = 4/3.120e-3 = 1282.05 Ω 재계산 일치 (Eq. 12.1, R_s 효과 무시). θ 환산 검증 360 × 0.475/5.0 = 34.20° vs 직접 측정 34.23° 0.03° 편차 — 오실로스코프 디지털 위상측정 보간 정밀도 차이로 설명되며 측정값을 우선 기록한 것은 절차 일치.

### [Table 12.3]
- Markdown 무결성: PASS (8-column header/separator/body 일치)
- Table 구조: PASS — 교재 원형(R_L | X_L | |Z_Th| | C* | X_C | |Z_L| | V_ab(p-p) | P_L = V_ab(p-p)²/(8R_L) 8열, C* 7개 행)과 동일.
- Measured 원본 대조: PASS — V_ab(p-p) 7개 값(0.575, 1.15, 1.37, 1.41, 1.37, 1.35, 1.29) 모두 측정값.md (line 105–111)와 일치.
- Calculated 재계산: PASS
  - 공통값: R_L = 463 Ω, X_L = 628.32 Ω, |Z_Th| = √(463² + 628.32²) = √609 155 = 780.48 Ω 재계산 일치.
  - X_C 행별: 0.0047 μF → 3386.27 Ω, 0.01 μF → 1591.55 Ω, 0.0147 μF → 1082.69 Ω, 0.0247 μF → 644.37 Ω, 0.047 μF → 338.63 Ω, 0.1 μF → 159.15 Ω, 1 μF → 15.92 Ω 모두 재계산 일치 (X_C = 1/(2πfC) 적용).
  - |Z_L| 행별: 모두 √(R_L² + X_C²) 재계산 일치 (3417.78, 1657.53, 1177.53, 793.46, 573.62, 489.59, 463.27 Ω).
  - P_L 행별: 8 × R_L = 3704 사용. 89.26, 357.05, 506.72, 536.74(최대), 506.72, 491.98, 449.27 μW 재계산 일치 (V_ab²/3704 적용).

### [Table 12.4]
- Markdown 무결성: PASS
- Table 구조: PASS — 교재 원형(단일 Measured 열, 행: R_L, X_C, C)과 동일.
- 측정 기반 산출값 검증: PASS — R_L = 463 Ω = R_measured(Part 3(b) 절차), X_C = 644.37 Ω(Graph 12.1에서 P_L 최대점 C* = 0.0247 μF 행의 X_C, 측정 데이터 기반 그래프 판독), C = 0.02533 μF (Part 3(l) "Assuming L is exactly 10 mH" 조건의 이론 계산 1/(2πf·X_L) = 1/(2π × 10⁴ × 628.32) = 25.33 nF). 보고서가 측정 기반 X_C와 이론 기반 C를 적절히 구분해 기록함 (이론 기준값으로 단정하지 않음).

### [Table 12.5]
- Markdown 무결성: PASS
- Table 구조: PASS — 교재 원형(단일 Measured 열, 행: C, R_Th, R_L(for P_max))과 동일.
- 측정 기반 산출값 검증: PASS — C = 0.0247 μF (Part 4(a) P_max 발생 C), R_Th = 463 Ω = R_measured(Z_Th의 저항 성분 = Fig 12.7의 직렬 R 실측), R_L(for P_max) = 800 Ω (Graph 12.2의 P_L 최대점 R_L = 800 Ω 행, Table 12.6에서 569.24 μW 최댓값과 일치). 이론치 R_Th = 463 Ω과의 차이는 # 고찰에서 해석으로 적절히 분리됨.

### [Table 12.6]
- Markdown 무결성: PASS (3-column 일관)
- Table 구조: PASS — 교재 원형(R_L | V_ab(p-p) | P_L = V_ab(p-p)²/(8R_L) 3열, R_L 8행)과 동일.
- Measured 원본 대조: PASS — V_ab 8개 값(0.372, 0.96, 1.20, 1.39, 1.59, 1.91, 2.11, 1.39 V_pp) 모두 측정값.md (line 148–155)와 일치 (400 Ω 행 "1.2" → 보고서 "1.20"은 trailing zero 추가일 뿐 동일값).
- Calculated 재계산: PASS — P_L = V_ab²/(8 × R_L_실측) 적용 시 8개 행 모두 일치 (176.51, 387.88, 454.09, 483.61, 528.45, 569.24(최대), 564.49, 521.62 μW). 보고서가 target R_L (100, 300, …)이 아닌 실측 R_L (98, 297.0, 396.4, 499.4, 598.0, 801.1, 985.7, 463 Ω)으로 분모를 잡아 정확.

### 내부 일관성 cross-reference
- PASS — E = 4 V_pp (강의노트 override), f = 10 kHz, X_L = 628.32 Ω 모든 Table에서 일관. R_1∥R_2 = 869.89 Ω가 Table 12.1 Original Z_Th와 Table 12.1 V_R_L(6.8k) Thev Eq 계산에서 같은 값으로 사용됨. Table 12.3의 X_C @ 0.0247 μF = 644.37 Ω가 Table 12.4의 X_C와 일치. Table 12.3 P_L 최댓값 행 V_ab = 1.41 V_pp @ 0.0247 μF가 Part 4의 C 선택과 일관. Table 12.5의 R_Th = 463 Ω이 Table 12.3 R_L과 동일(Part 3(b) 절차 일관 — R_L = R_measured = R = 463 Ω). 측정값.md "이론 E_Th = 2.93 V (p-p)"는 nominal 1.2k/3.3k 기준이고 보고서는 실측 1.18k/3.31k 기반 869.89 Ω을 R_1∥R_2로 사용하여 일관.

### 발견된 오류 목록
1. **Table 10.5 구조 FAIL**: 교재 원형 2열(Calculated | Measured)에 %(Difference) 열을 임의 추가. HTML 주석에 "보고서 비교용 추가" 명시되어 있으나 SKILL "임의 열 추가/누락 검증" 규칙상 교재에 없는 %(Difference) 열은 FAIL.
2. **Table 12.1 E_Th 셀(두 번째 열) Calculated FAIL**: 교재 Part 1(d) 절차상 Thev Eq 열은 측정 R 기반 **계산값** E_Th = E × R_2_meas/(R_1_meas + R_2_meas) = 4 × 3.31/4.49 ≈ **2.949 V_pp ∠0°**이어야 하는데, 보고서는 Part 1(c)의 실측 개방전압 2.77 V_pp ∠0°을 그대로 옮겨 적음. 계산 단계 누락. (수정 범위: Table 12.1의 E_Th 행 두 번째 셀만. V_R_L(6.8k) Thev Eq 계산은 Part 1(f) 절차상 측정 E_Th 사용이 정당하므로 재계산 불필요.)
3. **Table 10.5 %(Difference) > 20% 전 행**: Z_T 40.09%, I_s 28.62%, I_1 33.18%, I_2 25.94%. V_R_1, V_R_2 측정값이 E = 4 V_pp 조건의 이론값보다 일관되게 약 2/3 배 수준으로 작게 측정됨. 오실로스코프 채널 감도 설정 오인 또는 E의 실제 인가값 확인 필요 — 사용자에게 측정값 재확인 권고.

최종 판정: FAIL
