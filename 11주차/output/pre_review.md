## KVL/KCL 검증 결과

### Topology 대조
- Fig 7.9/7.11/7.12: PASS. 교재 이미지와 보고서 모두 R-C 직렬 회로이며 측정 대상 소자가 공통 접지 쪽에 오도록 배치한 설명이 일치한다.
- Fig 8.1: PASS. source(+) -> L(10 mH) -> R(1 kΩ) -> GND 직렬 구조로 보고서 Topology와 일치한다.
- Fig 8.2: PASS. source(+) -> C(0.01 μF) -> R(1 kΩ) -> GND 직렬 구조로 보고서 Topology와 일치한다.
- Fig 8.3: PASS. source(+) -> R -> node a -> L -> node b -> C -> GND 직렬 구조이며, V_ab를 L+C 합성 양단 전압으로 해석한 보고서 설명이 교재 회로와 일치한다.
- Fig 9.1/9.2/9.3: PASS. R-L 병렬, 총전류 측정용 R_s 하단 직렬 삽입, 인덕터 가지 전류 측정용 R_s 삽입 topology가 교재 이미지와 일치한다.

### 회로 1: Ch 7 R-C 직렬 위상 측정
- KVL: PASS. Table 7.1~7.6에서 각 R 값별로 sqrt(V_R^2 + V_C^2) = 4 V_p-p 관계가 성립한다.
- KCL: PASS. 직렬 단일 루프 회로로 공통 전류를 사용한 해석이 일관된다.
- 계산/단위: PASS. X_C, V_R, V_C, theta, D_1, D_2 계산 및 V/kΩ/μF/div 단위 표기가 허용 오차 내이다.
- STT 교차검증: PASS. STT 7-1/7-2의 V_R, V_C, D_1, D_2 발화값은 보고서 이상값과 대체로 정합한다. STT 7-3 Lissajous y_o/y_m 발화는 일부 불명확하지만, 보고서가 교재 Fig 7.12 축 정의를 따른 처리는 타당하다.

### 회로 2: Ch 8 직렬 R-L, R-C, R-L-C
- KVL: PASS. Table 8.1은 sqrt(3.388^2 + 2.129^2) ≈ 4.00 V, Table 8.3은 sqrt(2.128^2 + 3.387^2) ≈ 4.00 V, Table 8.5는 sqrt(2.881^2 + (1.810 - 4.585)^2) ≈ 4.00 V로 성립한다.
- KCL: PASS. 직렬 회로이므로 모든 소자에 공통 I_p-p를 적용한 전류 연속 조건이 맞다.
- 계산/단위: PASS. X_L = 628.32 Ω, X_C = 1591.55 Ω, Z_T, I_p-p, RMS 환산값이 명판값 및 이상 소자 가정 기준으로 타당하다.
- STT 교차검증: PASS. 이전 FAIL 항목이 해소되었다. STT 8-1의 V_R ≈ 3.3 V, V_L ≈ 2.9 V를 보고서가 직접 대조하고, V_L 차이 +0.77 V(+36.2%)에 대해 p-p/RMS 혼동 배제, R_l = 50 Ω 가설 불충분, L 실측값/V-div/결선 후보를 정량 검토했다. STT 8-3의 V_C ≈ 4.34 V, V_L ≈ 1.61 V, V_ab ≈ 1.5 V도 직접 대조되어 있으며, V_ab 차이 -1.28 V(-46.0%)는 R_l 단독으로 설명 불가하고 V_L에 가까운 측정 노드 혼동 가능성이 가장 크다고 정리되어 있다.

### 회로 3: Ch 9 병렬 R-L
- KVL: PASS. 병렬 가지 전압을 V_R = V_L = E = 4 V_p-p로 두는 해석이 Fig 9.1 topology와 일치한다.
- KCL: PASS. Table 9.1에서 I_s = sqrt(I_R^2 + I_L^2) = sqrt(4.000^2 + 6.366^2) = 7.518 mA로 페이저 KCL이 성립한다. STT RMS 값으로도 sqrt(1.2^2 + 2.1^2) ≈ 2.42 mA가 STT I_s ≈ 2.38 mA와 1.7% 차이로 정합한다.
- 계산/단위: PASS. p-p와 RMS가 분리되어 있고 V_Rs, I_s, I_L, I_R에 mV/mA 단위가 명시되어 있다. Table 9.2의 theta_L(E와 I_L)과 Table 9.4의 theta_L(I_s와 I_L) 정의 구분도 맞다.
- STT 교차검증: PASS. 이전 FAIL 항목이 해소되었다. STT 9-1의 R_s ≈ 12.6 Ω, V_Rs ≈ 80 mV/68 mV, I_s ≈ 2.38 mA, I_R ≈ 1.2 mA, I_L ≈ 2.1 mA를 보고서가 직접 대조했고, V_Rs는 p-p, 가지 전류는 RMS로 식별했다. 또한 V_Rs/R_s_meas 환산값과 STT 전류값의 대응 및 KCL 정합성을 정리했다.

### 단위 일관성
- PASS. V, mV, mA, Ω, kΩ, μF, div, Hz 단위가 표와 계산식에 명시되어 있고, 오실로스코프 p-p 값과 DMM/RMS 값의 환산 관계가 설명되어 있다.

### 발견된 오류
- 없음

최종 판정: PASS
