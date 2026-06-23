## KVL/KCL 검증 결과

### 회로 1: Ch 7 R-C 직렬 회로
- KVL: PASS. Table 7.1~7.6의 페이저 합 `sqrt(V_R^2 + V_C^2) = E`는 E = 4 V(p-p) 기준으로 재계산 시 성립함.
- KCL: 해당 없음. 직렬 단일 루프 회로로 전류는 모든 소자에 동일함.
- 계산/단위: FAIL. Table 7.1~7.6의 `E_(p-p)` 행이 `8 V (교재 표기, 실제 인가 4 V)`로 적혀 있어, 같은 표 안의 계산값이 사용하는 E = 4 V와 불일치함. 실제 예상값 표의 입력 전압은 4 V(p-p)로 표기되어야 함.
- 계산/단위: FAIL. Table 7.8 Lissajous 계산에서 Fig 7.12의 vertical 축은 Channel 1 = E인데, 보고서는 `y_m = V_R(p-p)`로 두고 R 값에 따라 `y_m`을 2.03/3.56/3.88 div로 계산함. 교재 회로 기준으로 `y_m`은 E의 vertical 최대값/스케일에 대응해야 하므로 축 해석이 잘못됨.

### 회로 2: Ch 8 R-L, R-C, R-L-C 직렬 회로
- KVL: PASS. Table 8.1, 8.3, 8.5의 `sqrt(V_R^2 + V_L^2)`, `sqrt(V_R^2 + V_C^2)`, `sqrt(V_R^2 + (V_L - V_C)^2)`는 E = 4 V(p-p) 기준으로 재계산 시 허용 반올림 범위 내에서 성립함.
- KCL: 해당 없음. 직렬 단일 루프 회로로 전류는 모든 소자에 동일함.
- 계산/단위: PASS. `X_L = 628.32 Ω`, `X_C = 1591.55 Ω`, `Z_T`, `I_(p-p)`, 위상각 계산은 반올림 오차 수준임.

### 회로 3: Ch 9 R-L 병렬 회로
- Topology: FAIL. Fig 9.2 교재 원도는 `source(+) -> R||L 상단 노드 -> R||L 하단 노드 -> R_s -> source(-)/GND` 구조인데, 보고서는 `source(+) -> R_s -> node X -> R||L -> GND`로 기술함. 전기적으로 총전류 센싱이라는 목적은 유사하나, 교재의 접지/측정 노드 topology와 일치하지 않음.
- KCL: PASS. 이상적 병렬 R-L 기준으로 `I_R = 4.00 mA`, `I_L = 6.366 mA`, `I_s = sqrt(I_R^2 + I_L^2) = 7.52 mA`는 성립함.
- 계산/단위: FAIL. Table 9.2의 `θ_L`은 교재 Part 1(h) 기준으로 Fig 9.3에서 `E`와 `I_L` 사이의 위상각이며, 이상적 인덕터에서는 약 90°이고 `D_2 = (90/360)*5 = 1.25 div`가 되어야 함. 보고서는 이를 Table 9.4의 `I_s`와 `I_L` 사이 각인 32.14°로 잘못 기입함.
- 계산/단위: FAIL. Table 9.1에서 `V_Rs(p-p)`의 Calculated 칸이 `—`로 비어 있고 Measured 칸에 이상적 계산값 75.18 mV, 63.66 mV가 들어 있음. 계산값과 측정값 열의 의미가 뒤바뀌거나 누락됨.
- STT 교차검증: FAIL. `input/stt/9-1 Parallel Sinusoidal Circuits.txt`에는 4 V(p-p) 사용, `I_s ≈ 2.38 mA`, `I_R ≈ 1.2 mA`, `I_L ≈ 2.1 mA`, `R_s ≈ 12.6 Ω`, `V_Rs ≈ 80 mV / 68 mV`가 언급됨. 보고서는 Measured 칸을 STT 측정값이 아니라 이상적 p-p 계산값으로 채웠고, `R_s`도 STT의 12.6 Ω 대신 명판값 10 Ω만 사용함.

### 단위 일관성
- PASS/FAIL: FAIL. 대부분의 전압, 전류, 저항, 커패시턴스, 시간 단위는 명시되어 있으나, Ch 7 표의 `E_(p-p)`가 8 V와 실제 4 V를 한 칸에 혼재하고, Ch 9 STT 전류값은 RMS/측정값 가능성이 있는데 보고서의 p-p 표와 직접 대응 정리가 없음.

### 발견된 오류
- [Topology] Fig 9.2의 센싱 저항 위치가 교재 원도와 다름.
- [Table 7.1~7.6] `E_(p-p)` 행이 실제 계산 기준 4 V(p-p)가 아니라 8 V 표기를 포함해 표 내부 기준이 불일치함.
- [Table 7.8] Lissajous vertical 축 `y_m`을 E가 아니라 V_R로 계산함.
- [Table 9.2] `θ_L`을 교재의 `E` vs `I_L` 각도(이상적 90°)가 아니라 `I_s` vs `I_L` 각도(32.14°)로 잘못 기입함.
- [Table 9.1] `V_Rs(p-p)` Calculated 칸이 비어 있고 이상적 계산값이 Measured 칸에 들어 있음.
- [STT] Ch 9 측정값 및 `R_s ≈ 12.6 Ω`가 보고서 Measured 칸에 반영되지 않음.

최종 판정: FAIL
