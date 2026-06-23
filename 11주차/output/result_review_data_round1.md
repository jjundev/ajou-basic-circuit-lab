## 실험 결과 검증

### Table 7.1
- Table 구조: FAIL (교재 원형은 `R | X_C | E_(p-p) | V_R(p-p) Calculated/Measured | θ_1 Calculated/Measured | D_1 | D_2`; 결과보고서는 R/X_C/E/D_1을 표 본체에서 누락하고 D_2를 행으로 옮겼으며 교재에 없는 `%(Difference)` 열을 추가함)
- Measured 원본 대조: PASS (V_R=2.13 V, θ_1=58.84°, D_2=0.817 div 원본과 일치)
- Calculated 재계산: PASS (R=970 Ω, C=0.47 μF, f=200 Hz, E=4 Vpp 기준 V_R≈1.99 V, θ_1≈60.19°, D_2≈0.836 div)
- %(Difference) 계산: FAIL (교재 원형에 `%(Difference)` 열 없음; 임의 추가)

### Table 7.2
- Table 구조: FAIL (교재 원형은 `R | X_C | E_(p-p) | V_R(p-p) Calculated/Measured | θ_1 Calculated/Measured`; 결과보고서는 R/X_C/E를 표 본체에서 누락하고 교재에 없는 D_2 행 및 `%(Difference)` 열을 추가함)
- Measured 원본 대조: PASS (V_R=3.54 V, θ_1=26.00° 원본과 일치)
- Calculated 재계산: PASS (R=3270 Ω 기준 V_R≈3.55 V, θ_1≈27.37°, D_2≈0.380 div)
- %(Difference) 계산: FAIL (교재 원형에 `%(Difference)` 열 없음; 임의 추가)

### Table 7.3
- Table 구조: FAIL (교재 원형은 Table 7.2와 동일 구조; 결과보고서는 R/X_C/E를 표 본체에서 누락하고 교재에 없는 D_2 행 및 `%(Difference)` 열을 추가함)
- Measured 원본 대조: PASS (V_R=3.90 V, θ_1=13.24° 원본과 일치)
- Calculated 재계산: PASS (R=6720 Ω 기준 V_R≈3.88 V, θ_1≈14.14°, D_2≈0.196 div)
- %(Difference) 계산: FAIL (교재 원형에 `%(Difference)` 열 없음; 임의 추가)

### Table 7.4
- Table 구조: FAIL (교재 원형은 `R | X_C | E_(p-p) | V_C(p-p) Calculated/Measured | θ_2 Calculated/Measured | D_1 | D_2`; 결과보고서는 R/X_C/E/D_1을 표 본체에서 누락하고 교재에 없는 `%(Difference)` 열을 추가함)
- Measured 원본 대조: PASS (V_C=3.34 V, θ_2=-31.83°, D_2=0.442 div 원본과 일치)
- Calculated 재계산: PASS (R=970 Ω 기준 V_C≈3.47 V, θ_2≈-29.81°, D_2≈0.414 div)
- %(Difference) 계산: FAIL (교재 원형에 `%(Difference)` 열 없음; 임의 추가)

### Table 7.5
- Table 구조: FAIL (교재 원형은 `R | X_C | E_(p-p) | V_C(p-p) Calculated/Measured | θ_2 Calculated/Measured`; 결과보고서는 R/X_C/E를 표 본체에서 누락하고 교재에 없는 D_2 행 및 `%(Difference)` 열을 추가함)
- Measured 원본 대조: PASS (V_C=1.82 V, θ_2=-62.49° 원본과 일치)
- Calculated 재계산: PASS (R=3270 Ω 기준 V_C≈1.84 V, θ_2≈-62.63°, D_2≈0.870 div)
- %(Difference) 계산: FAIL (교재 원형에 `%(Difference)` 열 없음; 임의 추가)

### Table 7.6
- Table 구조: FAIL (교재 원형은 Table 7.5와 동일 구조; 결과보고서는 R/X_C/E를 표 본체에서 누락하고 교재에 없는 D_2 행 및 `%(Difference)` 열을 추가함)
- Measured 원본 대조: PASS (V_C=1.01 V, θ_2=-75.06° 원본과 일치)
- Calculated 재계산: PASS (R=6720 Ω 기준 V_C≈0.977 V, θ_2≈-75.86°, D_2≈1.054 div)
- %(Difference) 계산: FAIL (교재 원형에 `%(Difference)` 열 없음; 임의 추가)

### Table 7.7
- Table 구조: PASS (교재 원형 `R | θ_1(meas., part 1) | θ_2(meas., part 2) | |θ_T|=|θ_1|+|θ_2| | % Difference 90° vs. θ_T` 반영)
- Measured 원본 대조: PASS (Tables 7.1~7.6 측정 θ 값으로 산출)
- Calculated 재계산: PASS (θ_T=90.67°, 88.49°, 88.30°)
- %(Difference) 계산: PASS (0.74%, 1.68%, 1.89%)

### Table 7.8
- Table 구조: PASS (교재 원형 `R | y_o | y_m | θ_1` 반영)
- Measured 원본 대조: PASS (y_o/y_m 값 원본과 일치)
- Calculated 재계산: PASS (sin^-1(y_o/y_m) 결과 58.21°, 28.07°, 16.13°)
- %(Difference) 계산: PASS (해당 없음; 교재 원형에 `%(Difference)` 열 없음)

### Table 7.9
- Table 구조: PASS (교재 원형 `R | θ_1(Tables 7.1,7.2,7.3) | θ_1(Table 7.8) | % Difference` 반영)
- Measured 원본 대조: PASS (Table 7.1~7.3 및 7.8 값 사용)
- Calculated 재계산: PASS
- %(Difference) 계산: PASS (1.07%, 7.96%, 21.83%; 6.8 kΩ 항목은 20% 초과로 측정값 재확인 권고)

### Table 8.1
- Table 구조: FAIL (교재 원형은 `V_R/V_L(p-p) | D_1 | D_2 | θ(measured) | θ(calculated)` 두 행 구조이며 `%(Difference)` 열 없음; 결과보고서는 표를 둘로 분리하고 `%(Difference) θ` 열을 임의 추가함)
- Measured 원본 대조: PASS (V_R=3.10 V, D_2=0.437 div, θ_1=31.43°, V_L=1.93 V, D_2=0.770 div, θ_2=55.44° 원본과 일치)
- Calculated 재계산: PASS (R=970 Ω, L=10 mH 기준 θ_1≈32.93°, θ_2≈57.07°)
- %(Difference) 계산: FAIL (교재 원형에 `%(Difference)` 열 없음; 임의 추가)

### Table 8.2
- Table 구조: FAIL (교재 원형은 `Quantity | Measured(or Calculated from Measured Values) | Theoretical(Calculated)`이며 `%(Difference)` 열 없음; 결과보고서가 `%(Difference)` 열을 임의 추가함)
- Measured 원본 대조: PASS (V_R, V_L 및 V_R/R 기반 I, Z_T, θ_T 산출값 일치)
- Calculated 재계산: PASS (E=4 V, V_R≈3.36 V, V_L≈2.17 V, I≈3.461 mA, Z_T≈1155.72 Ω, θ_T≈32.93°)
- %(Difference) 계산: FAIL (교재 원형에 `%(Difference)` 열 없음; 임의 추가)

### Table 8.3
- Table 구조: FAIL (교재 원형은 Table 8.1과 같은 두 행 구조이며 `%(Difference)` 열 없음; 결과보고서는 표를 둘로 분리하고 `%(Difference) θ` 열을 임의 추가함)
- Measured 원본 대조: PASS (V_R=2.13 V, θ_1=56.67°, V_C=3.26 V, θ_2=-33.82° 원본과 일치)
- Calculated 재계산: PASS (R=970 Ω, C=0.01 μF 기준 V_R≈2.08 V, V_C≈3.42 V, θ_1≈58.64°, θ_2≈-31.36°)
- %(Difference) 계산: FAIL (교재 원형에 `%(Difference)` 열 없음; 임의 추가)

### Table 8.4
- Table 구조: FAIL (교재 원형은 `Quantity | Measured(or Calculated from Measured Values) | Theoretical(Calculated)`이며 `%(Difference)` 열 없음; 결과보고서가 `%(Difference)` 열을 임의 추가함)
- Measured 원본 대조: PASS (V_R, V_C 및 V_R/R 기반 I, Z_T, θ_T 산출값 일치)
- Calculated 재계산: PASS (E=4 V, V_R≈2.08 V, V_C≈3.42 V, I≈2.146 mA, Z_T≈1863.85 Ω, θ_T≈-58.64°)
- %(Difference) 계산: FAIL (교재 원형에 `%(Difference)` 열 없음; 임의 추가)

### Table 8.5
- Table 구조: FAIL (교재 원형은 `Measured | Calculated` 2열 구조이며 `%(Difference)` 열 없음; 결과보고서가 `%(Difference)` 열을 임의 추가함)
- Measured 원본 대조: PASS (V_R=2.65 V, V_L=1.65 V, V_C=4.14 V, I=2.732 mA, Z_T≈1464 Ω, V_ab=2.61 V 원본과 일치)
- Calculated 재계산: PASS (R=970 Ω, L=10 mH, C=0.01 μF 기준 V_R≈2.84 V, V_L≈1.84 V, V_C≈4.66 V, I≈2.926 mA, Z_T≈1367.0 Ω, V_ab≈2.82 V)
- %(Difference) 계산: FAIL (교재 원형에 `%(Difference)` 열 없음; 임의 추가)

### Table 9.1
- Table 구조: FAIL (교재 원형은 `Calculated | Measured` 2열 구조이며 `%(Difference)` 열 없음; 결과보고서가 `%(Difference)` 열을 임의 추가함)
- Measured 원본 대조: PASS (측정값 파일의 DMM 환산 전류 및 V_Rs 값은 보고서와 일치)
- Calculated 재계산: FAIL (교재 절차상 V_Rs와 R_s로 I_s, I_L을 산출해야 하므로 V_Rs(for I_s)=75 mV, R_s=10 Ω이면 I_s=7.500 mA이고 V_Rs(for I_L)=65 mV이면 I_L=6.500 mA임; 보고서의 I_s=5.892 mA, I_L=5.139 mA와 같은 표 안의 V_Rs 값이 서로 불일치)
- %(Difference) 계산: FAIL (교재 원형에 `%(Difference)` 열 없음; 임의 추가. 또한 I_s, I_R 항목은 20% 초과로 측정값 재확인 권고)

### Table 9.2
- Table 구조: PASS (교재 원형 `D_1 | D_2 | Angle in Degrees` 반영)
- Measured 원본 대조: PASS (D_1=5 div, D_2=0.703/1.171 div, θ_s=50.61°, θ_L=84.30° 원본과 일치)
- Calculated 재계산: PASS (D_2/D_1×360° 결과와 일치)
- %(Difference) 계산: PASS (해당 없음; 교재 원형에 `%(Difference)` 열 없음)

### Table 9.3
- Table 구조: PASS (교재 원형 `Z_T | X_L` 반영)
- Measured 원본 대조: PASS (V_Rs=75 mV, R_s=10 Ω 기반 산출)
- Calculated 재계산: PASS (Z_T=4 V/7.500 mA=533.33 Ω, X_L=2π·10 kHz·10 mH=628.32 Ω)
- %(Difference) 계산: PASS (해당 없음; 교재 원형에 `%(Difference)` 열 없음)

### Table 9.4
- Table 구조: PASS (교재 원형 `I_s(diagram) | I_s(measured) | θ_s | θ_L | θ_T` 반영)
- Measured 원본 대조: FAIL (보고서 Table 9.4의 I_s(measured)=7.500 mA는 V_Rs/R_s 기반값이지만, 같은 보고서 Table 9.1의 I_s Measured=5.892 mA와 불일치)
- Calculated 재계산: PASS (보고서가 사용한 I_R=3.128 mA, I_L=5.139 mA 기준 I_s(diagram)≈6.016 mA, θ_s≈58.66°, θ_L≈31.34°, θ_T=90.00°)
- %(Difference) 계산: PASS (해당 없음; 교재 원형에 `%(Difference)` 열 없음)

### 발견된 오류 목록
- Tables 7.1~7.6: 교재 원형의 R/X_C/E 및 일부 D_1/D_2 열 구조를 유지하지 않고 항목별 Calculated/Measured/% Difference 표로 재구성함.
- Tables 7.1~7.6, 8.1~8.5, 9.1: 교재 원형에 없는 `%(Difference)` 열을 임의 추가함.
- Table 9.1: 같은 표 안의 V_Rs 측정값과 R_s=10 Ω으로부터 I_s=7.500 mA, I_L=6.500 mA가 산출되지만 보고서의 I_s=5.892 mA, I_L=5.139 mA와 불일치함.
- Table 9.4: I_s(measured)=7.500 mA를 사용하지만 Table 9.1의 I_s Measured=5.892 mA와 불일치함.
- Table 7.9의 6.8 kΩ 항목 %(Difference)=21.83%, Table 9.1의 I_s=22.32% 및 I_R=24.15%는 20% 초과이므로 측정값 재확인 권고.

최종 판정: FAIL
