## 실험 결과 검증

검토 대상: `output/10주차_결과보고서.md` (`# 실험 결과` 섹션, 고찰 섹션 미작성)
교재 원형 대조: `input/book/` (p.289 ~ p.319)
실측 소자값 (보고서·측정값 파일에서 인용): R_s = 103.4 Ω, R = 997.4 Ω, L = 10 mH (명판), C = 0.1 μF (명판), V_L(p-p) = V_C(p-p) = 2 V (강의노트 기준), E_s(p-p) = 2 V (Ch 6)
이전 라운드 누락 항목 처리: implementor가 Table 4.1, 5.1, 5.2, 5.3, 5.4, 5.5의 교재 원형 구조를 모두 보완함. 데이터 부재 셀은 "—"로 표기하여 행/열만 유지.

### Table 4.1 (Part 1 — Resistors, p.289)

- Table 구조: PASS
    교재 원형: Frequency | V_R(p-p) | V_R(rms) [Calculation] | I_rms [Measurement] | R = V_R(rms)/I_rms [Calculation], 5행 (50/100/200/500/1000 Hz)
    결과보고서: 동일한 5열 × 5행 구조. 실험 미진행으로 데이터 셀은 "—". 임의 열 추가 없음.
- Calculated 재계산: 해당 없음 (데이터 미기재)
- %(Difference) 계산: 해당 없음 (교재 원형에 %(Difference) 열 없음)

### Table 4.2 (Part 2 — Inductors, p.290)

- Table 구조: PASS
    교재 원형: Frequency | V_L(p-p) | V_Rs(p-p) | I_p-p | X_L(measured) | X_L(calculated)=2πfL, 5행 (1/3/5/7/10 kHz). 결과보고서 동일. 1 kHz 행은 측정 불가로 "—" 기재(행 자체는 존재).
- Calculated 재계산: PASS
    X_L(calculated) = 2πfL (L = 10 mH 명판값): 3 kHz → 188.50 Ω, 5 kHz → 314.16 Ω, 7 kHz → 439.82 Ω, 10 kHz → 628.32 Ω. 일치.
    V_Rs(p-p) = V_Rs(DMM) × 2√2: 3 kHz → 1007.37 mV, 5 kHz → 617.39 mV, 7 kHz → 446.27 mV, 10 kHz → 314.66 mV. 일치.
    I_p-p = V_Rs(p-p)/R_s: 3 kHz → 9.7424 mA(보고서 9.74), 5 kHz → 5.971 mA(보고서 5.97), 7 kHz → 4.316 mA(보고서 4.32), 10 kHz → 3.043 mA(보고서 3.04). 일치.
    X_L(measured) = V_L(p-p)/I_p-p: 3 kHz → 205.29 Ω, 5 kHz → 334.96 Ω(보고서 335.00, 반올림 차 0.04), 7 kHz → 463.40 Ω, 10 kHz → 657.21 Ω(보고서 657.22, 반올림 차 0.01). 모두 반올림 허용 범위.
- %(Difference) 계산: 해당 없음

### Table 4.3 (Part 2 — 인덕턴스 역산, p.291)

- Table 구조: PASS
    교재 원형: X_L | L (calc.) | L (nameplate), 단행 구조. 결과보고서 동일.
- Calculated 재계산: PASS
    Graph 4.1에서 f = 1.5 kHz, X_L = 100 Ω 가정 시 L = 100 / (2π × 1500) = 10.61 mH. 일치.
- %(Difference) 계산: 해당 없음

### Table 4.4 (Part 3 — Capacitors, p.292)

- Table 구조: PASS
    교재 원형: Frequency | V_C(p-p) | V_Rs(p-p) | I_p-p | X_C(measured) | X_C(calculated)=1/(2πfC), 8행 (100/200/300/400/500/800/1000/2000 Hz). 결과보고서 동일. 100 Hz 행은 측정 불가로 "—" 기재.
- Calculated 재계산: PASS
    X_C(calculated): 200 Hz → 7957.75, 300 Hz → 5305.16, 400 Hz → 3978.87, 500 Hz → 3183.10, 800 Hz → 1989.44, 1000 Hz → 1591.55, 2000 Hz → 795.77. 일치.
    V_Rs(p-p): 200 Hz → 22.80, 300 Hz → 36.69, 400 Hz → 48.45, 500 Hz → 60.25, 800 Hz → 95.46, 1000 Hz → 118.84, 2000 Hz → 233.34 mV. 일치.
    X_C(measured) = V_C(p-p)/I_p-p: 200 Hz → 9071, 300 Hz → 5637, 400 Hz → 4268, 500 Hz → 3433, 800 Hz → 2166, 1000 Hz → 1740, 2000 Hz → 886 Ω. 모두 반올림 허용.
- %(Difference) 계산: 해당 없음

### Table 4.5 (Part 3 — 커패시턴스 역산, p.294)

- Table 구조: PASS
    교재 원형: X_C | C (calc.) | C (nameplate), 단행. 결과보고서 동일.
- Calculated 재계산: PASS
    Graph 4.2에서 f = 650 Hz, X_C = 2650 Ω 가정 시 C = 1/(2π × 650 × 2650) = 9.24 × 10⁻⁸ F = 0.0924 μF. 일치.
- %(Difference) 계산: 해당 없음

### Table 5.1 (직렬 R-L 주파수 응답, p.301)

- Table 구조: PASS
    교재 원형: Frequency | V_L(p-p) | V_R(p-p) | I_p-p, 11행 (0.1/1/2/3/4/5/6/7/8/9/10 kHz). 결과보고서 동일. 실험 미진행으로 데이터 셀 "—".
- Calculated 재계산: 해당 없음 (데이터 미기재)
- %(Difference) 계산: 해당 없음

### Table 5.2 (V_L = V_R 교차점, p.303)

- Table 구조: PASS
    교재 원형: V(V_L=V_R) | X_L | R, 단행. 결과보고서 동일.
- Calculated 재계산: 해당 없음
- %(Difference) 계산: 해당 없음

### Table 5.3 (전압 산술합 vs 전원전압, p.303)

- Table 구조: PASS
    교재 원형: V_L(p-p) | V_R(p-p) | Sum, 단행. 결과보고서 동일.
- Calculated 재계산: 해당 없음
- %(Difference) 계산: 해당 없음

### Table 5.4 (X_L 비교 — f = 8 kHz, p.304)

- Table 구조: PASS
    교재 원형: 행 라벨 X_L | Calculated | From Table 5.1 data, 단행. 결과보고서 동일.
- Calculated 재계산: 해당 없음
- %(Difference) 계산: 해당 없음

### Table 5.5 (피타고라스 정리 검증 — f = 5 kHz, p.305)

- Table 구조: PASS
    교재 원형: 행 라벨 V_L(p-p) | Calculated | Measured, 단행. 결과보고서 동일.
- Calculated 재계산: 해당 없음
- %(Difference) 계산: 해당 없음

### Table 6.1 (직렬 R-C 주파수 응답, p.315)

- Table 구조: PASS
    교재 원형: Frequency | V_C(p-p) | V_R(p-p) | I_p-p, 9행 (0.1/0.2/0.5/1/2/4/6/8/10 kHz). 결과보고서 동일. 0.1/0.2/0.5 kHz 행은 측정 불가로 "—" 기재.
- Calculated 재계산: PASS
    V_R(p-p) = V_R(DMM) × 2√2, I_p-p = V_R(p-p)/R(R = 997.4 Ω):
    1 kHz → 1.0167, 1.019 mA (보고서 1.02 / 1.02)
    2 kHz → 1.4866, 1.490 mA (보고서 1.49 / 1.49)
    4 kHz → 1.7613, 1.766 mA (보고서 1.76 / 1.77)
    6 kHz → 1.8215, 1.826 mA (보고서 1.82 / 1.83)
    8 kHz → 1.8583, 1.863 mA (보고서 1.86 / 1.86)
    10 kHz → 1.8724, 1.877 mA (보고서 1.87 / 1.88). 모두 반올림 허용 범위.
- %(Difference) 계산: 해당 없음

### Table 6.2 (V_C = V_R 교차점, p.317)

- Table 구조: PASS
    교재 원형: V(V_C=V_R) | X_C | R, 단행. 결과보고서 동일.
- Calculated 재계산: PASS
    그래프에서 V_C = V_R 교차점 1.36 V를 읽고, X_C = R = 997.4 Ω(실측 R)로 보고. 합리적.
- %(Difference) 계산: 해당 없음

### Table 6.3 (전압 산술합, p.317)

- Table 구조: PASS
    교재 원형: V_C(p-p) | V_R(p-p) | Sum, 단행. 결과보고서 동일.
- Calculated 재계산: PASS
    Sum = 0.85 + 1.71 = 2.56 V. 일치. 본문에서 √(0.85² + 1.71²) = 1.91 V로 산술합과 벡터합의 차이를 정확히 설명.
- %(Difference) 계산: 해당 없음

### Table 6.4 (X_C 비교 — f = 6 kHz, p.318)

- Table 구조: PASS (조건부)
    교재 원문 column header가 "Calculated | Table 6.2"이지만 절차문(l)은 Table 6.1 데이터 사용을 명시. Table 6.2는 교차점 1행만 있어 6 kHz 데이터 산출이 불가능하므로 절차문 해석이 물리적으로 합당. 결과보고서는 "From Table 6.1 data"로 표기. 사용자 확인 권고.
- Calculated 재계산: PASS
    X_C(calculated) = 1/(2π × 6000 × 0.1 × 10⁻⁶) = 265.26 Ω. 일치.
    X_C(from Table 6.1) = V_C/I_p-p = 0.52 / 1.826 mA = 284.78 Ω (보고서 284.79, 반올림 허용).
- %(Difference) 계산: 해당 없음

### Table 6.5 (피타고라스 정리 검증 — f = 6 kHz, p.319)

- Table 구조: PASS
    교재 원형: 행 라벨 V_C(p-p) | Calculated | Table 6.1, 단행. 결과보고서 동일.
- Calculated 재계산: PASS
    V_C(calculated) = √(E_s² − V_R²) = √(2² − 1.82²) = √0.6876 = 0.83 V. 정확. (V_R 정밀값 1.8215 사용 시 0.8259 V로 미세 차이.)
    Table 6.1 측정값 0.52 V도 일치.
- %(Difference) 계산: 해당 없음

### 측정값 진단 (참고)

Table 6.5의 Calculated(0.83 V)와 Table 6.1 측정값(0.52 V) 간 차이가 절대 기준으로 약 37%로 매우 크다. 결과보고서 본문이 이미 √(0.52² + 1.82²) = 1.89 V ≠ E_s = 2.00 V임을 지적하고 있으며, 6 kHz에서 DMM AC 대역폭 제한으로 V_R(DMM)이 과소 측정될 가능성, 또는 E_s 인가값이 정확히 2.00 V가 아닐 가능성이 있다. 측정값 재확인 권고. (참고: 본 항목은 교재 원형에 %(Difference) 열이 없어 표 안에서 정량화할 수 없음.)

### 발견된 오류 목록

없음. 이전 라운드의 구조 누락(Table 4.1, 5.1, 5.2, 5.3, 5.4, 5.5) 6건은 모두 보완 완료.

### 측정값 재확인 권고

- Table 6.5: V_C(calc) = 0.83 V vs V_C(Table 6.1 측정) = 0.52 V (절대 기준 약 37% 괴리). V_R(DMM) at 6 kHz 또는 E_s 인가값을 재측정·재확인 권고.

### 수치 검산 오류

없음. 결과보고서에 기재된 모든 Calculated/도출값(Table 4.2, 4.3, 4.4, 4.5, 6.1, 6.2, 6.3, 6.4, 6.5)이 실측 소자값(R_s = 103.4 Ω, R = 997.4 Ω) 및 명판값(L = 10 mH, C = 0.1 μF)으로 재계산한 결과와 반올림 허용 범위 내에서 일치.

최종 판정: PASS
