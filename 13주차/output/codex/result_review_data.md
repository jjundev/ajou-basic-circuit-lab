## 실험 결과 검증

### Table 10.5
- Markdown 무결성: PASS
- Table 구조: PASS (교재 원형의 `Z_T`, `I_s(p-p)`, `I_1(p-p)`, `I_2(p-p)` 행과 `Calculated`, `Measured` 열 유지. 교재에 없는 `%(Difference)` 열 없음)
- Measured 원본 대조: PASS (`V_R1 = 2.25 V_pp`, `V_R2 = 1.49 V_pp`, Table 10.6 위상 측정값에서 산출한 Measured 값이 측정값 파일과 대응됨)
- Calculated 재계산: PASS (`Z_T = 737.79 ∠-20.52° Ω`, `I_s = 5.42 ∠+20.52° mA_pp`, `I_1 = 3.44 ∠-32.67° mA_pp`, `I_2 = 4.34 ∠+59.81° mA_pp` 일치)
- %(Difference) 계산: PASS (교재 원형상 오차율 열 없음. 참고 오차율은 `Z_T 39.66%`, `I_s 28.40%`, `I_1 33.18%`, `I_2 25.93%`로 모두 20% 초과하므로 `V_R1`, `V_R2`, 전원 `E = 4 V_pp` 재확인 권고)

### Table 10.6
- Markdown 무결성: PASS
- Table 구조: PASS (`D_1`, `D_2`, `θ` 열과 `E and I_1`, `E and I_2` 행 유지)
- Measured 원본 대조: PASS (`D_1 = 5.0 div`, `D_2 = 0.45 div / 0.83 div` 일치)
- Calculated 재계산: PASS (`θ = 360° × D_2 / D_1`; `32.40°`, `59.76°` 일치)
- %(Difference) 계산: PASS (교재 원형상 오차율 열 없음)

### Table 12.1
- Markdown 무결성: PASS
- Table 구조: PASS (교재 원형의 `Original`, `Thevenin Equivalent` 열과 4개 행 유지)
- Measured 원본 대조: PASS (`Original V_RL(1 kΩ) = 1.24 V_pp`, `Original E_Th = 2.77 V_pp`, `Original V_RL(6.8 kΩ) = 2.37 V_pp`, `Thevenin Equivalent V_RL(1 kΩ) = 1.40 V_pp`가 측정값 파일과 일치. `Thevenin Equivalent V_RL(6.8 kΩ)`는 측정값 파일상 보고서 계산 항목)
- Calculated 재계산: PASS (`E_Th = 4 × 3310 / (1180 + 3310) = 2.95 V_pp`, Original `Z_Th = 869.89 + j628.32 Ω = 1073.08 ∠35.84° Ω`, Table 12.2 기반 `Z_Th = 1059.87 + j721.10 Ω = 1281.91 ∠34.23° Ω`, `V_RL(6.8 kΩ) = 2.38 V_pp` 일치)
- %(Difference) 계산: PASS (교재 원형상 오차율 열 없음)

### Table 12.2
- Markdown 무결성: PASS
- Table 구조: PASS (`V_Rs`, `I`, `Z_Th`, `D_1`, `D_2`, `θ` 단일값 기록 구조 유지)
- Measured 원본 대조: PASS (`V_Rs = 29.3 mV_pp`, `D_1 = 5.0 div`, `D_2 = 0.475 div`, `θ = 34.23°` 대응)
- Calculated 재계산: PASS (`I = 0.0293 / 9.39 = 3.12 mA_pp`, `Z_Th = 4 / 0.003120 = 1281.91 Ω`; `360° × 0.475 / 5.0 = 34.20°`는 보고서 `34.23°`와 반올림/원자료 표기 차이 수준)
- %(Difference) 계산: PASS (교재 원형상 오차율 열 없음)

### Table 12.3
- Markdown 무결성: PASS
- Table 구조: PASS (`R_L`, `X_L`, `abs(Z_Th)`, `C*`, `X_C`, `abs(Z_L)`, `V_ab(p-p)`, `P_L` 구조 유지)
- Measured 원본 대조: PASS (`V_ab = 0.575, 1.15, 1.37, 1.41, 1.37, 1.35, 1.29 V_pp` 모두 측정값 파일과 일치)
- Calculated 재계산: PASS (`X_C`, `abs(Z_Th)`, `abs(Z_L)`, `P_L = V_ab^2/(8R_L)` 재계산 일치)
- %(Difference) 계산: PASS (교재 원형상 오차율 열 없음)

### Table 12.4
- Markdown 무결성: PASS
- Table 구조: PASS (`R_L`, `X_C`, `C` 단일값 기록 구조 유지)
- Measured 원본 대조: PASS (Table 12.3/Graph 12.1의 측정 기반 최대점 `R_L = 463 Ω`, `X_C = 644.35 Ω`, `C = 0.0247 μF` 반영)
- Calculated 재계산: PASS (`X_C = 1/(2πfC) = 644.35 Ω`)
- %(Difference) 계산: PASS (교재 원형상 오차율 열 없음)

### Table 12.5
- Markdown 무결성: PASS
- Table 구조: PASS (`C`, `R_Th`, `R_L(for P_max)` 단일값 기록 구조 유지)
- Measured 원본 대조: PASS (`C = 0.0247 μF`, `R_Th = 463 Ω`, Table 12.6 측정 기반 최대점 `R_L = 801.1 Ω` 반영)
- Calculated 재계산: PASS (측정 기반 `P_L` 최대 행은 `801.1 Ω`에서 `569.2 μW`)
- %(Difference) 계산: PASS (교재 원형상 오차율 열 없음)

### Table 12.6
- Markdown 무결성: PASS
- Table 구조: PASS (`R_L`, `V_ab(p-p)`, `P_L` 구조와 `100 Ω`~`1000 Ω`, `R_L = R_Th` 행 유지)
- Measured 원본 대조: PASS (`R_L` 실측값과 `V_ab` 측정값 모두 측정값 파일과 일치)
- Calculated 재계산: PASS (`P_L = V_ab^2/(8R_L)` 재계산값 `176.5`, `387.9`, `454.1`, `483.6`, `528.4`, `569.2`, `564.6`, `521.6 μW` 일치)
- %(Difference) 계산: PASS (교재 원형상 오차율 열 없음)

### 내부 일관성 cross-reference
- PASS (`E_Th`는 Table 12.1에서 Original 측정값 `2.77 V_pp measured`와 Thevenin Equivalent 계산값 `2.95 V_pp calculated`로 구분되어 있으며, 교재 절차상 서로 다른 항목이므로 불일치가 아님. Table 12.1의 Thevenin Equivalent `V_RL(R_L = 1 kΩ) = 1.40 V_pp measured`는 측정값 파일과 일치. Table 12.1의 `Z_Th`와 Table 12.2의 측정 기반 `Z_Th = 1281.91 ∠34.23° Ω`도 상호 일치)

### 발견된 오류 목록
- Table 10.5: 참고 오차율이 전 항목 20% 초과 (`Z_T 39.66%`, `I_s 28.40%`, `I_1 33.18%`, `I_2 25.93%`)하므로 `V_R1`, `V_R2`, 전원 `E = 4 V_pp` 재확인 권고.

최종 판정: PASS
