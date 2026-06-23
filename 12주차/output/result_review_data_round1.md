## 실험 결과 검증

### Table 9.5
- Markdown 무결성: PASS (4-col 헤더·구분자·본문 5행 일관)
- Table 구조: FAIL — 교재 원형(p.362)은 `Calculated | Measured` 2열만 존재하며 `%(Difference)` 열은 교재에 없음. 보고서는 3열로 임의 추가.
- Measured 원본 대조: PASS
  - I_s = 1.366 × 2√2 = 3.864 mA ✓
  - I_C = 0.814 × 2√2 = 2.302 mA ✓
  - I_R = 1.144 × 2√2 = 3.236 mA (보고서 3.235 — 둘째자리 반올림 미세 차이)
  - V_Rs(I_s) = 47 mV ✓, V_Rs(I_C) = 27 mV ✓
- Calculated 재계산: PASS
  - X_C = 1591.55 Ω ✓, I_R = 4.124 mA ✓, I_C = 2.513 mA ✓
  - |I_s| = √(4.124² + 2.513²) = √23.322 = 4.829 mA ✓
  - V_Rs(I_s) = 48.29 mV ✓, V_Rs(I_C) = 25.13 mV ✓
- %(Difference) 계산: PASS(조건부 — 단, 열 자체가 교재에 없음)
  - I_R 행: 보고서 21.55%, 정확값 |4.124-3.235|/4.124 × 100 = 21.5567 → 21.56%. 둘째자리 반올림 방향 차이 (정상 반올림 시 21.56). 자체 표 측정값 3.235 사용 기준 미세 표기 차이.
  - 나머지 I_s(19.98%), I_C(8.40%) 정확.
  - **>20% 항목**: I_s (19.98% — 임계 직전), I_R (21.55%) — 측정값 재확인 권고.

### Table 9.6
- Markdown 무결성: PASS
- Table 구조: PASS — 교재 원형(p.364) `D_1 | D_2 | Angle in Degrees` 3열 × `θ_s / θ_C` 2행 구조 일치, Calculated/%(Difference) 열 미추가.
- Measured 원본 대조: PASS — D_2 = 0.44, 1.19 div ✓
- 환산값 검증: PASS
  - θ_s = 360 × 0.44/5 = 31.68° ✓ (+, I_s leads E)
  - θ_C = 360 × 1.19/5 = 85.68° ✓ (+, I_C leads E)
- %(Difference) 계산: 해당 없음 (교재에 비교 열 없음)

### Table 9.7
- Markdown 무결성: PASS
- Table 구조: FAIL — 교재 원형은 `Z_T / X_C` 2행 × `Calculated | Measured` 2열. 보고서는 `%(Difference)` 열을 임의로 추가하여 3열로 확장.
- Measured 원본 대조: PASS (측정값 파일에 별도 항목 없음 — Table 9.5의 측정 I_s, I_C 로부터 도출. Z_T = E/I_s = 4/3.864 mA = 1035.20 Ω ✓, X_C = E/I_C = 4/2.302 mA = 1737.62 Ω ✓)
- Calculated 재계산: PASS (미세 차이)
  - |Z_T| = 970/√(1 + 0.60947²) = 970/1.17111 = 828.28 Ω. 보고서 828.30 — 둘째자리에서 0.02 미세 차이. %(Diff) 결과 동일 자릿수 표기.
  - X_C = 1591.55 Ω ✓
- %(Difference) 계산: PASS(조건부)
  - Z_T: 24.98% ✓ — **>20% 측정값 재확인 권고** (I_s 측정 저편차가 Z_T 비교에 그대로 전이)
  - X_C: 9.18% ✓

### Table 9.8
- Markdown 무결성: PASS
- Table 구조: PASS — 교재 원형 단일행 × `I_s(diagram) / I_s(calculated) / θ_s / θ_C / θ_T` 5열 일치, Calculated/Measured/%(Difference) 열 미추가.
- Measured 원본 대조: 해당 없음 (Table 9.5 측정 I_R, I_C 로부터 페이저 합성)
- 산출값 재계산: PASS
  - I_s(diagram) = √(3.235² + 2.302²) = √15.764 = 3.971 mA ✓
  - I_s(calculated) = 3.971 mA ✓ (도면과 식 일치)
  - θ_s = arctan(2.302/3.235) = arctan(0.7117) = 35.42° ✓
  - θ_C = 90 - 35.42 = 54.58° ✓
  - θ_T = 35.42 + 54.58 = 90.00° ✓

### Table 9.9
- Markdown 무결성: PASS
- Table 구조: FAIL — 교재 원형(p.368)은 7행 × `Calculated | Measured` 2열. 보고서는 `%(Difference)` 열을 임의 추가하여 3열로 확장.
- Measured 원본 대조: PASS
  - I_s = 1.63 × 2√2 = 4.610 mA ✓
  - I_L = 1.82 × 2√2 = 5.148 mA ✓
  - I_C = 0.8 × 2√2 = 2.263 mA ✓
  - I_R = 1.12 × 2√2 = 3.168 mA ✓
  - V_Rs 3행 모두 측정값 일치 (54.7 / 38.3 / 25.3 mV)
- Calculated 재계산: PASS
  - X_L = 628.32 Ω ✓, X_C = 1591.55 Ω ✓
  - I_R = 4.124, I_L = 6.366, I_C = 2.513 mA ✓
  - |I_s| = √(4.124² + (2.513-6.366)²) = √31.853 = 5.644 mA ✓
  - V_Rs 3행 모두 계산값 일치 (56.44 / 63.66 / 25.13 mV)
- %(Difference) 계산: PASS(조건부 — 교재 비교 열 없음)
  - I_s 18.32% ✓, I_L 19.13% ✓, I_C 9.95% ✓, I_R 23.18% ✓
  - V_Rs(I_s) 3.08% ✓, V_Rs(I_L) 39.84% ✓, V_Rs(I_C) 0.68% ✓
  - **>20% 항목**: I_R (23.18%), V_Rs(I_L) (39.84%) — 측정값 재확인 권고. 특히 V_Rs(I_L) 38.3 mV 는 계산값 63.66 mV 와 큰 격차 (인덕터 내부저항·결선 영향 가능).

### Table 9.10
- Markdown 무결성: PASS
- Table 구조: PASS — 교재 원형 `θ_s / D_1 / D_2 / Z_T` 4행 × `Method One | Method Two` 2열 구조 일치. D_1, D_2 의 Method One 칸은 음영 처리(—) 적용 ✓.
- Measured 원본 대조: PASS — D_1 = 5, D_2 = 0.59 div ✓
- Calculated 재계산: PASS
  - Method One θ_s = arctan((2.263-5.148)/3.168) = arctan(-0.9107) = -42.32° ✓
  - Method One |Z_T| = 4/5.644 mA = 708.72 Ω ✓
  - Method Two θ_s = -360 × 0.59/5 = -42.48° (L 우세, lag 부호) ✓
  - Method Two |Z_T| = 4/4.610 mA = 867.68 Ω ✓
- %(Difference) 계산: 해당 없음 (교재에 비교 열 없음 — Method One/Two 비교 구조)

### Table 10.1
- Markdown 무결성: PASS
- Table 구조: FAIL — 교재 원형(p.376)은 7행 × `Calculated | Measured` 2열. 보고서는 `%(Difference)` 열을 임의 추가하여 3열로 확장.
- Measured 원본 대조: PASS
  - Z_T = 837.49 Ω ✓, I_s = 4.78 mA ✓
  - V_1 = 2.23 V ✓, V_2 = 2.19 V ✓, V_3 = 2.19 V ✓
  - I_2 = 2.26 mA ✓, I_3 = 3.49 mA ✓
- Calculated 재계산: PASS
  - X_L = 628.32 Ω ✓
  - Z_2 ‖ Z_3 = 527.27∠+57.07° = 286.57 + j442.59 Ω ✓
  - Z_T = 753.57 + j442.59 → |Z_T| = 873.93 Ω, ∠+30.43° ✓
  - I_s = 4/873.93 = 4.577 mA ✓
  - V_1 = 4.577 × 467 = 2.137 V ✓
  - V_2 = V_3 = 4.577 × 527.27 = 2.413 V ✓
  - I_2 = 2.413/970 = 2.488 mA ✓
  - I_3 = 2.413/628.32 = 3.840 mA ✓
  - KCL 검산: √(I_2² + I_3²) = 4.576 ≈ I_s 4.577 ✓
- %(Difference) 계산: PASS(조건부 — 교재 비교 열 없음)
  - Z_T 4.17% ✓, I_s 4.44% ✓, V_1 4.35% ✓, V_2/V_3 9.24% ✓, I_2 9.16% ✓, I_3 9.11% ✓
  - 모두 20% 이하.

### Table 10.2
- Markdown 무결성: PASS
- Table 구조: PASS — 교재 원형 `E and V_2 / E and I_s / E and V_1` 3행 × `D_1 | D_2 | θ` 3열 구조 일치. E and V_1 행의 D_1/D_2 음영(—) 적용 ✓.
- Measured 원본 대조: PASS — D_2 = 0.37, 0.43 div ✓
- 환산값 검증: PASS
  - E and V_2: 360 × 0.37/5 = +26.64° (V_2 leads E) ✓
  - E and I_s: 360 × 0.43/5 = 30.96° → -30.96° (회로 유도성, I_s lags E) ✓
  - E and V_1: -30.96° (V_1 ∥ I_s 동상) ✓
- %(Difference) 계산: 해당 없음

### Table 10.3
- Markdown 무결성: PASS
- Table 구조: FAIL — 교재 원형은 7행 × `Calculated | Measured` 2열. 보고서는 `%(Difference)` 열을 임의 추가하여 3열로 확장.
- Measured 원본 대조: PASS
  - Z_T = 1010.10 Ω ✓, I_s = 3.96 mA ✓
  - V_1 = 1.85 V ✓, V_2 = 2.23 V ✓, V_3 = 2.23 V ✓
  - I_2 = 2.30 mA ✓, I_3 = 2.80 mA ✓
- Calculated 재계산: PASS
  - X_C = 1/(4π × 10⁻⁴) = 795.77 Ω ✓
  - Z_2 ‖ Z_3 = 615.23∠-50.64° = 390.18 - j475.69 Ω ✓
  - Z_T = 857.18 - j475.69 → |Z_T| = 980.33 Ω, ∠-29.02° ✓
  - I_s = 4.080 mA ✓
  - V_1 = 1.905 V ✓, V_2 = V_3 = 2.510 V ✓
  - I_2 = 2.587 mA ✓, I_3 = 3.154 mA ✓
  - KCL 검산: √(I_2² + I_3²) = 4.079 ≈ I_s 4.080 ✓
- %(Difference) 계산: PASS(조건부)
  - Z_T 3.04% ✓, I_s 2.94% ✓, V_1 2.89% ✓, V_2/V_3 11.16% ✓, I_2 11.09% ✓, I_3 11.22% ✓
  - 모두 20% 이하.

### Table 10.4
- Markdown 무결성: PASS
- Table 구조: PASS — 교재 원형 `E and I_s / E and I_2 / I_2 and I_3` 3행 × `D_1 | D_2 | θ` 3열 일치.
- Measured 원본 대조: PASS — D_2 = 0.41, 0.31, 1.24 div ✓
- 환산값 검증: PASS
  - E and I_s: 360 × 0.41/5 = +29.52° (회로 용량성, I_s leads E) ✓
  - E and I_2: 360 × 0.31/5 = 22.32° → -22.32° (I_2 = V_2/R_2 ∥ V_2, V_2 lags E) ✓
  - I_2 and I_3: 360 × 1.24/5 = +89.28° (이상적 90° 직교) ✓

### 내부 일관성 cross-reference
- PASS
  - E = 4 V(p-p) 모든 Table·풀이에서 일관 사용 ✓
  - R = 970 Ω, R_1 = 467 Ω, R_2 = 970 Ω, R_s = 10 Ω 일관 ✓
  - X_C(10 kHz, 0.01 μF) = 1591.55 Ω — Table 9.5, 9.7, 9.9 모두 동일 ✓
  - X_C(10 kHz, 0.02 μF) = 795.77 Ω — Table 10.3 ✓
  - X_L(10 kHz, 10 mH) = 628.32 Ω — Table 9.9, 10.1 모두 동일 ✓
  - I_R = 4.124 mA (Calculated) — Table 9.5, 9.9 동일 ✓
  - I_C = 2.513 mA (Calculated) — Table 9.5, 9.9 동일 ✓
  - I_R(meas) = 3.235 mA — Table 9.5 / Table 9.8 페이저 도면 동일 사용 ✓
  - I_C(meas) = 2.302 mA — Table 9.5 / Table 9.8 동일 ✓
  - I_s(meas) = 3.864 mA → Table 9.7 Z_T(meas) 1035.20 Ω 도출에 일관 사용 ✓
  - I_C(meas) = 2.302 mA → Table 9.7 X_C(meas) 1737.62 Ω 도출에 일관 사용 ✓
  - Table 9.9 측정 I_L(5.148), I_C(2.263), I_R(3.168), I_s(4.610) mA → Table 9.10 Method One/Two 도출에 일관 사용 ✓
  - Table 10.1 측정 I_s(4.78), Table 10.2 위상측정 0.43 div → 30.96°·-30.96°·-30.96° 도출 일관 ✓

### 단위 일관성
- PASS — 전류(mA), 전압(V/mV), 임피던스/저항(Ω/kΩ), 시간(s/μs/div), 각도(°), 주파수(kHz), 인덕턴스(mH), 커패시턴스(μF) 모두 표기 일관.

### 발견된 오류 목록
- **[Structural FAIL]** Table 9.5, 9.7, 9.9, 10.1, 10.3 — 교재 원형(p.362/365/368/376/378)은 `Calculated | Measured` 2열만 존재하며 `%(Difference)` 열이 교재에 없음. 보고서는 5개 표 모두에 `%(Difference)` 열을 임의 추가함. 수치는 정확하나 교재 원형 구조 위반.
- [미세 표기 불일치] Table 9.5 I_R Measured: 1.144 × 2√2 = 3.236 mA 가 정확값 (보고서 3.235 mA). %(Diff) 보고서 21.55% vs 정확값 21.56% — 둘째자리 반올림 방향 차이 1건. 최종 결론 영향 없음.
- [미세 표기 불일치] Table 9.7 Z_T Calculated: 정확 828.28 Ω vs 보고서 828.30 Ω. %(Diff) 표시 자릿수에서 동일 (24.98%).
- [측정값 재확인 권고 >20%] Table 9.5 I_R 21.55%, Table 9.7 Z_T 24.98%, Table 9.9 I_R 23.18%, Table 9.9 V_Rs(for I_L) 39.84%. 특히 V_Rs(for I_L) 38.3 mV vs 이론 63.66 mV 는 인덕터 내부저항 R_l 가 무시될 수 없는 수준임을 시사 — 측정 재확인 또는 고찰에서 정량 논의 필요.

최종 판정: FAIL
