## KVL/KCL 검증 결과

### Topology 대조
- [Fig 9.4]: PASS (R = 1 kΩ, C = 0.01 μF 병렬, 전원 양단에 직접 연결)
- [Fig 9.5]: FAIL (보고서가 `R_s`를 "generator와 node A 사이"라고 설명했으나, 교재 Fig 9.5의 `R_s`는 전원 return/GND 측 직렬 위치에 삽입되어 source current `I_s`를 측정한다. 올바른 topology: generator(+) -> 병렬 R-C 상단 노드, 병렬 하단 노드 -> `R_s` -> generator(-)/GND)
- [Fig 9.6]: PASS (C 가지의 GND 측에 `R_s`를 직렬 삽입하여 `I_C` 측정)
- [Fig 9.7]: PASS (R, L, C 세 가지가 전원 양단에 병렬 연결)
- [Fig 10.3]: PASS (`R_1 = 470 Ω` 직렬 후 `R_2 = 1 kΩ`와 `L = 10 mH` 병렬)
- [Fig 10.4]: PASS (`R_1 = 470 Ω` 직렬 후 `R_2 = 1 kΩ`와 `C = 0.02 μF` 병렬)

### Table 9.5
- Topology: PASS (Fig 9.4 기준 R-C 병렬 계산)
- KVL: 해당 없음 (병렬 전압 `V_R = V_C = E`)
- KCL: PASS (`I_s = sqrt(4.000^2 + 2.513^2) = 4.724 mA`)
- 계산: PASS (`X_C = 1591.55 Ω`, `V_Rs(I_s) = 47.24 mV`, `V_Rs(I_C) = 25.13 mV`)
- 단위: PASS

### Table 9.6
- Topology: PASS
- KVL: 해당 없음
- KCL: FAIL (위상각 정의 오류. 교재 Part 2(h)는 Fig 9.6에서 `E`와 `I_C`의 위상각 `θ_C`를 구하라고 하며, 이상적 R-C 병렬에서 `I_C`는 `E`보다 90° lead한다. 보고서는 `θ_C = 90° - θ_s = 57.86°`, `D_1 = 0.8467`로 기입했으나, Table 9.6의 `E` and `I_C` 측정 기준으로는 `θ_C = 90.00°`, `D_1/D_2 = sin 90° = 1.000`이어야 한다.)
- 계산: FAIL (`θ_s = 32.14°`는 맞지만 `θ_C` 행은 90.00°가 필요)
- 단위: PASS

### Table 9.7
- Topology: PASS
- KVL: 해당 없음
- KCL: PASS (`Z_T = E/I_s` 검산과 병렬 임피던스 공식이 일치)
- 계산: PASS (`Z_T ≈ 846.69 Ω`, `X_C ≈ 1591.55 Ω`)
- 단위: PASS

### Table 9.8
- Topology: PASS
- KVL: 해당 없음
- KCL: PASS 조건부 (`θ_C`를 `I_s`와 `I_C` 사이 각도로 정의하면 57.86°가 맞다. 단 Table 9.6의 `θ_C`와 같은 의미로 사용했다면 FAIL)
- 계산: PASS 조건부 (`I_s = 4.724 mA`, `θ_s = 32.14°`, `θ_T = 90.00°`)
- 단위: PASS

### Table 9.9
- Topology: PASS
- KVL: 해당 없음 (병렬 전압 동일)
- KCL: PASS (`I_s = sqrt(I_R^2 + (I_C - I_L)^2) ≈ 6366.2 mA`)
- 계산: PASS (`X_L = 0.6283 Ω`, `X_C = 1.5916 MΩ`, 이상적 `R_l ≈ 0` 가정 명시)
- 단위: PASS

### Table 9.10
- Topology: PASS
- KVL: 해당 없음
- KCL: PASS (`Z_T = E/I_s ≈ 0.6283 Ω`)
- 계산: PASS (`Method One`과 `Method Two`가 일치)
- 단위: PASS

### Table 10.1
- Topology: PASS
- KVL: PASS (`V_1 + V_2 ≈ 4.00 + j0 V = E`)
- KCL: PASS (`I_2 + I_3 ≈ I_s`; `sqrt(I_2^2 + I_3^2) ≈ 4.56 mA`)
- 계산: PASS (재계산 기준 `Z_T ≈ 877.50 Ω`, 보고서 `877.19 Ω`는 중간 반올림 영향으로 판정 영향 없음)
- 단위: PASS

### Table 10.2
- Topology: PASS
- KVL: PASS (Table 10.1의 phasor 전압과 일관)
- KCL: PASS (Table 10.1의 phasor 전류와 일관)
- 계산: PASS (`E&V_2 ≈ +26.98°`, `E&I_s ≈ -30.88°`, `E&V_1 ≈ -30.88°`)
- 단위: PASS

### Table 10.3
- Topology: PASS
- KVL: PASS (`V_1 + V_2 ≈ 4.00 + j0 V = E`)
- KCL: PASS (`I_2 + I_3 ≈ I_s`; `sqrt(I_2^2 + I_3^2) ≈ 4.055 mA`)
- 계산: PASS (재계산 기준 `Z_T ≈ 986.45 Ω`, 보고서 `986.39 Ω`는 반올림 범위)
- 단위: PASS

### Table 10.4
- Topology: PASS
- KVL: PASS (Table 10.3의 phasor 전압과 일관)
- KCL: PASS (`I_2`와 `I_3`가 90° 차이이며 phasor 합이 `I_s`)
- 계산: PASS (`E&I_s ≈ +29.61°`, `E&I_2 ≈ -21.88°`, `I_2&I_3 = +90.00°`)
- 단위: PASS

### 경계 침범 체크
- 명판값 외 수치 사용: PASS (계산에 4 V p-p, 1 kΩ, 470 Ω, 10 Ω, 10 mH, 0.01 μF, 0.02 μF 등 명판/강의노트 수치 사용)
- R_l 수치화 여부: PASS (`R_l ≈ 0` 이상적 가정만 사용, 구체 실측값 누수 없음)

### Type A 채움 체크
- 측정 의존 예측칸: PASS (`V_Rs`, `Z_T`, 전류, 위상각 등 이론 예측값으로 채움)
- 명판값 불일치: PASS

### Type B 정성 파트 체크
- 해당 없음

### 보드 연결도 필터링
- 비-회로 Fig 포함: PASS (보드 연결도에는 Fig 9.4~9.7, Fig 10.3~10.4만 포함)

### STT 교차검증 및 노출 체크
- STT 관련 문자열 등장: PASS (보고서 본문에 `STT`, `input/stt`, `실험 영상`, `측정값 대조`, `stt/` 노출 없음)
- STT 수치 비교: PASS 조건부 (STT는 4 V p-p 사용을 확인한다. `9-2` STT의 약 `I_s 1.47`, `I_C 0.83 m`, `I_R 1.2 mA` 발화는 RMS/측정 조건이 혼재된 값으로 보이며, 보고서의 예상값 Table은 p-p 이론값이므로 직접 FAIL 근거로 삼지 않음)
- STT 절차/회로 변형: PASS (보조 Table이 필요한 새로운 topology 변형 발화 없음)

### 발견된 오류 목록
- [Topology] Fig 9.5: `R_s` 위치 설명이 부정확함. 교재 기준 `R_s`는 전원 return/GND 측 직렬 위치에 삽입되어 `I_s`를 측정한다.
- [Table 9.6] `θ_C` 계산 오류: 교재 Fig 9.6 측정 기준 `E`와 `I_C`의 위상차는 90.00°이며 `D_1/D_2 = 1.000`이어야 하나, 보고서는 57.86° 및 0.8467로 기입했다.
- 미세 표기 불일치 - Table 10.1: 재계산 `Z_T ≈ 877.50 Ω` vs 보고서 `877.19 Ω`, 중간 반올림 영향으로 최종 판정에는 독립 오류로 반영하지 않음.

최종 판정: FAIL
