## 실험 결과 검증

### Table 9.5
- Markdown 무결성: PASS (3-col 헤더·구분자·본문 5행 일관)
- Table 구조: PASS — 교재 원형(p.362) `I_s / I_C / I_R / V_Rs(for I_s) / V_Rs(for I_C)` 5행 × `Calculated | Measured` 2열 일치. **이전 round %(Difference) 열 제거됨 ✓**. V_Rs Calculated 칸은 (—) 음영 처리.
- Measured 원본 대조: PASS
  - I_s = 1.366 × 2√2 = 3.864 mA ✓
  - I_C = 0.814 × 2√2 = 2.302 mA ✓
  - I_R = 1.144 × 2√2 = 3.236 mA (보고서 3.235 — 둘째자리 반올림 미세 차이, Q5 정책 PASS)
  - V_Rs(I_s) = 47 mV ✓, V_Rs(I_C) = 27 mV ✓
- Calculated 재계산: PASS
  - X_C = 1/(2π × 10⁴ × 10⁻⁸) = 1591.55 Ω ✓
  - I_R = 4/970 = 4.124 mA ✓, I_C = 4/1591.55 = 2.513 mA ✓
  - |I_s| = √(4.124² + 2.513²) = √23.322 = 4.829 mA ✓
  - V_Rs(I_s) = 48.29 mV, V_Rs(I_C) = 25.13 mV (본문 풀이에 명시, 표는 음영 (—))
- %(Difference) 계산: 해당 없음 (교재에 비교 열 없음 — 정상)

### Table 9.6
- Markdown 무결성: PASS
- Table 구조: PASS — 교재 원형(p.364) `D_1 | D_2 | Angle in Degrees` 3열 × `θ_s / θ_C` 2행 일치
- Measured 원본 대조: PASS — D_2 = 0.44, 1.19 div ✓
- 환산값 검증: PASS
  - θ_s = 360° × 0.44/5 = +31.68° (I_s leads E) ✓
  - θ_C = 360° × 1.19/5 = +85.68° (I_C leads E) ✓
- %(Difference) 계산: 해당 없음

### Table 9.7
- Markdown 무결성: PASS
- Table 구조: PASS — 교재 원형(p.365) `Z_T / X_C` 2행 × `Calculated | Measured` 2열 일치. **이전 round %(Difference) 열 제거됨 ✓**.
- Measured 원본 대조: PASS (Table 9.5 측정 I_s, I_C 로부터 도출)
  - Z_T(meas) = 4 V / 3.864 mA = 1035.20 Ω ✓
  - X_C(meas) = 4 V / 2.302 mA = 1737.62 Ω ✓
- Calculated 재계산: PASS
  - |Z_T| = 970/√(1 + (0.6095)²) = 970/1.1711 = 828.29 Ω (보고서 828.30 — Q5 미세 표기, 최종 자릿수 영향 없음)
  - X_C = 1591.55 Ω ✓
- %(Difference) 계산: 해당 없음

### Table 9.8
- Markdown 무결성: PASS
- Table 구조: PASS — 교재 원형 단일행 × `I_s(diagram) / I_s(calculated) / θ_s / θ_C / θ_T` 5열 일치
- Measured 원본 대조: 해당 없음 (Table 9.5 측정 I_R, I_C 로부터 페이저 합성)
- 산출값 재계산: PASS
  - I_s(diagram) = √(3.235² + 2.302²) = √15.764 = 3.971 mA ✓
  - I_s(calculated) = 3.971 mA ✓
  - θ_s = arctan(2.302/3.235) = arctan(0.7117) = +35.42° ✓
  - θ_C = 90 - 35.42 = +54.58° ✓
  - θ_T = +90.00° ✓
- %(Difference) 계산: 해당 없음

### Table 9.9
- Markdown 무결성: PASS
- Table 구조: PASS — 교재 원형(p.368) 7행 × `Calculated | Measured` 2열 일치. **이전 round %(Difference) 열 제거됨 ✓**.
- Measured 원본 대조: PASS
  - I_s = 1.63 × 2√2 = 4.610 mA ✓
  - I_L = 1.82 × 2√2 = 5.148 mA ✓
  - I_C = 0.8 × 2√2 = 2.263 mA ✓
  - I_R = 1.12 × 2√2 = 3.168 mA ✓
  - V_Rs 3행 (54.7 / 38.3 / 25.3 mV) 모두 일치 ✓
- Calculated 재계산: PASS
  - X_L = ωL = 62831.85 × 10⁻² = 628.32 Ω ✓, X_C = 1591.55 Ω ✓
  - I_R = 4.124 mA ✓, I_L = 6.366 mA ✓, I_C = 2.513 mA ✓
  - |I_s| = √(4.124² + (2.513-6.366)²) = √31.853 = 5.644 mA ✓
  - V_Rs(I_s) = 56.44 mV ✓, V_Rs(I_L) = 63.66 mV ✓, V_Rs(I_C) = 25.13 mV ✓
- %(Difference) 계산: 해당 없음

### Table 9.10
- Markdown 무결성: PASS
- Table 구조: PASS — 교재 원형 `θ_s / D_1 / D_2 / Z_T` 4행 × `Method One | Method Two` 2열 일치. D_1, D_2 의 Method One 칸 음영 (—) ✓.
- Measured 원본 대조: PASS — D_1 = 5, D_2 = 0.59 div ✓
- Calculated 재계산: PASS
  - Method One θ_s = arctan((2.263-5.148)/3.168) = arctan(-0.9107) = -42.32° ✓
  - Method One |Z_T| = 4 V / 5.644 mA = 708.72 Ω ✓
  - Method Two θ_s = -360° × 0.59/5 = -42.48° (인덕터 우세, lag 부호) ✓
  - Method Two |Z_T| = 4 V / 4.610 mA = 867.68 Ω ✓
- %(Difference) 계산: 해당 없음

### Table 10.1
- Markdown 무결성: PASS
- Table 구조: PASS — 교재 원형(p.376) 7행 × `Calculated | Measured` 2열 일치. **이전 round %(Difference) 열 제거됨 ✓**.
- Measured 원본 대조: PASS
  - Z_T = 837.49 Ω ✓, I_s = 4.78 mA ✓
  - V_1 = 2.23 V ✓, V_2 = V_3 = 2.19 V ✓
  - I_2 = 2.26 mA ✓, I_3 = 3.49 mA ✓
- Calculated 재계산: PASS
  - X_L = 628.32 Ω ✓
  - Z_2 ‖ Z_3 = 527.27∠+57.07° = 286.57 + j442.59 Ω ✓
  - Z_T = 753.57 + j442.59 → |Z_T| = √763754 = 873.93 Ω, ∠+30.43° ✓
  - I_s = 4/873.93 = 4.577 mA ✓
  - V_1 = 4.577 × 467 = 2.137 V ✓
  - V_2 = V_3 = 4.577 × 527.27 = 2.413 V ✓
  - I_2 = 2.413/970 = 2.488 mA ✓, I_3 = 2.413/628.32 = 3.840 mA ✓
  - KCL 검산: √(2.488² + 3.840²) = 4.576 ≈ I_s 4.577 ✓
- %(Difference) 계산: 해당 없음

### Table 10.2
- Markdown 무결성: PASS
- Table 구조: PASS — 교재 원형 `E and V_2 / E and I_s / E and V_1` 3행 × `D_1 | D_2 | θ` 3열 일치. E and V_1 의 D_1, D_2 음영 (—) ✓.
- Measured 원본 대조: PASS — D_2 = 0.37, 0.43 div ✓
- 환산값 검증: PASS
  - E and V_2: +26.64° (V_2 leads E) ✓
  - E and I_s: -30.96° (회로 유도성, I_s lags E) ✓
  - E and V_1: -30.96° (V_1 ∥ I_s 동상) ✓
- %(Difference) 계산: 해당 없음

### Table 10.3
- Markdown 무결성: PASS
- Table 구조: PASS — 교재 원형 7행 × `Calculated | Measured` 2열 일치. **이전 round %(Difference) 열 제거됨 ✓**.
- Measured 원본 대조: PASS
  - Z_T = 1010.10 Ω ✓, I_s = 3.96 mA ✓
  - V_1 = 1.85 V ✓, V_2 = V_3 = 2.23 V ✓
  - I_2 = 2.30 mA ✓, I_3 = 2.80 mA ✓
- Calculated 재계산: PASS
  - X_C = 1/(62831.85 × 2 × 10⁻⁸) = 795.77 Ω ✓
  - Z_2 ‖ Z_3 = 615.23∠-50.64° = 390.18 - j475.69 Ω ✓
  - Z_T = 857.18 - j475.69 → |Z_T| = √961039 = 980.33 Ω, ∠-29.02° ✓
  - I_s = 4/980.33 = 4.080 mA ✓
  - V_1 = 4.080 × 467 = 1.905 V ✓
  - V_2 = V_3 = 4.080 × 615.23 = 2.510 V ✓
  - I_2 = 2.510/970 = 2.587 mA ✓, I_3 = 2.510/795.77 = 3.154 mA ✓
  - KCL 검산: √(2.587² + 3.154²) = 4.079 ≈ I_s 4.080 ✓
- %(Difference) 계산: 해당 없음

### Table 10.4
- Markdown 무결성: PASS
- Table 구조: PASS — 교재 원형 `E and I_s / E and I_2 / I_2 and I_3` 3행 × `D_1 | D_2 | θ` 3열 일치
- Measured 원본 대조: PASS — D_2 = 0.41, 0.31, 1.24 div ✓
- 환산값 검증: PASS
  - E and I_s: +29.52° (회로 용량성, I_s leads E) ✓
  - E and I_2: -22.32° (V_2 lags E → I_2 lags E) ✓
  - I_2 and I_3: +89.28° (이상적 90° 직교) ✓
- %(Difference) 계산: 해당 없음

### 내부 일관성 cross-reference
- PASS
  - E = 4 V(p-p) 모든 Table·풀이에서 일관 ✓
  - R = 970 Ω, R_1 = 467 Ω, R_2 = 970 Ω, R_s = 10 Ω 일관 ✓
  - X_C(10 kHz, 0.01 μF) = 1591.55 Ω — Table 9.5, 9.7, 9.9 동일 ✓
  - X_C(10 kHz, 0.02 μF) = 795.77 Ω — Table 10.3 ✓
  - X_L(10 kHz, 10 mH) = 628.32 Ω — Table 9.9, 10.1 동일 ✓
  - I_R(calc) = 4.124 mA — Table 9.5, 9.9 동일 ✓
  - I_C(calc) = 2.513 mA — Table 9.5, 9.9 동일 ✓
  - I_R(meas) = 3.235 mA — Table 9.5 / Table 9.8 페이저 도면 동일 사용 ✓
  - I_C(meas) = 2.302 mA — Table 9.5 / Table 9.7 / Table 9.8 동일 ✓
  - I_s(meas) = 3.864 mA → Table 9.7 Z_T(meas) 1035.20 Ω 도출에 일관 사용 ✓
  - Table 9.9 측정 I_L(5.148), I_C(2.263), I_R(3.168), I_s(4.610) mA → Table 9.10 Method One/Two 도출 일관 ✓
  - Table 10.1 Z_T calc 873.93 / I_s calc 4.577 / V 들 — 풀이와 표 일관 ✓
  - Table 10.3 Z_T calc 980.33 / I_s calc 4.080 — 풀이와 표 일관 ✓

### 단위 일관성
- PASS — 전류(mA), 전압(V/mV), 임피던스/저항(Ω/kΩ), 시간(s/μs/div), 각도(°), 주파수(kHz), 인덕턴스(mH), 커패시턴스(μF) 모두 표기 일관

### 발견된 오류 목록
- **[이전 round FAIL 해결 확인]** Tables 9.5, 9.7, 9.9, 10.1, 10.3 의 `%(Difference)` 열이 모두 제거되어 교재 원형(`Calculated | Measured` 2열) 구조와 일치하게 수정됨. Structural FAIL 해소 ✓.
- [미세 표기 불일치 — Q5 PASS] Table 9.5 I_R Measured: 1.144 × 2√2 = 3.236 mA 가 정확값 (보고서 3.235 mA). 둘째자리 반올림 방향 차이 1건. 최종 결론 영향 없음.
- [미세 표기 불일치 — Q5 PASS] Table 9.7 Z_T Calculated: 정확 828.29 Ω vs 보고서 828.30 Ω. 마지막 자릿수 미세 차이, 최종 결론 영향 없음.
- [측정 편차 참고] 본 round 에서는 %(Difference) 표가 제거되어 정량 표시가 없으나, Calculated vs Measured 검산 시 큰 편차 항목은 다음과 같음 (고찰 섹션에서 정량 논의 필요):
  - Table 9.5: I_R 편차 약 21.6% (4.124 → 3.235 mA)
  - Table 9.7: Z_T 편차 약 25.0% (828.30 → 1035.20 Ω) — I_s 측정 저편차의 전이
  - Table 9.9: I_R 편차 약 23.2% (4.124 → 3.168 mA), V_Rs(for I_L) 편차 약 39.8% (63.66 → 38.3 mV) — 인덕터 내부저항 R_l 영향 시사
  이들 항목은 측정값 자체의 검증 FAIL이 아니며, 측정값 파일과 1:1 일치함 (실험 자체의 특성).

최종 판정: PASS
