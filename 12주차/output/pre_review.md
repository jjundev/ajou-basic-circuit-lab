## KVL/KCL 검증 결과

### Topology 대조
- [Fig 9.4]: PASS (R = 1 kΩ, C = 0.01 μF 병렬, 전원 양단에 직접 연결)
- [Fig 9.5]: PASS (교재와 보고서 모두 병렬 R-C 하단 공통 노드와 generator(-)/GND 사이의 return/GND 측 직렬 위치에 R_s 삽입, source current I_s 측정)
- [Fig 9.6]: PASS (C 가지의 GND 측에 R_s 직렬 삽입, I_C 측정)
- [Fig 9.7]: PASS (R = 1 kΩ, L = 10 mH, C = 0.01 μF 세 가지가 전원 양단에 병렬 연결)
- [Fig 10.3]: PASS (R_1 = 470 Ω 직렬 후 R_2 = 1 kΩ와 L = 10 mH 병렬)
- [Fig 10.4]: PASS (R_1 = 470 Ω 직렬 후 R_2 = 1 kΩ와 C = 0.02 μF 병렬)

### Table 9.5
- Topology: PASS (Fig 9.4~9.6 기준 R-C 병렬 및 R_s 측정 위치 반영)
- KVL: 해당 없음 (병렬 회로이므로 V_R = V_C = E)
- KCL: PASS (I_s = sqrt(4.000^2 + 2.513^2) = 4.724 mA)
- 계산: PASS (X_C = 1591.55 Ω, V_Rs(I_s) = 47.24 mV, V_Rs(I_C) = 25.13 mV)
- 단위: PASS

### Table 9.6
- Topology: PASS (Fig 9.5는 I_s 측정, Fig 9.6은 I_C 측정)
- KVL: 해당 없음
- KCL: PASS (θ_s = 32.14°, Table 9.6의 θ_C는 E와 I_C 기준으로 90.00°)
- 계산: PASS (D_1/D_2 = sin 32.14° = 0.5318, sin 90° = 1.000)
- 단위: PASS

### Table 9.7
- Topology: PASS
- KVL: 해당 없음
- KCL: PASS (Z_T = E/I_s = 4 V / 4.724 mA ≈ 846.73 Ω)
- 계산: PASS (보고서 Z_T = 846.69 Ω, X_C = 1591.55 Ω은 반올림 범위)
- 단위: PASS

### Table 9.8
- Topology: PASS
- KVL: 해당 없음
- KCL: PASS (I_R와 I_C 직교 phasor 합으로 I_s = 4.724 mA, θ_s + θ_C = 90.00°)
- 계산: PASS (Table 9.8의 θ_C는 I_s와 I_C 사이 각도 57.86°로 정의되어 일관됨)
- 단위: PASS

### Table 9.9
- Topology: PASS (Fig 9.7 병렬 R-L-C)
- KVL: 해당 없음 (병렬 전압 동일)
- KCL: PASS (I_s = sqrt(4.000^2 + (0.002513 - 6366.2)^2) ≈ 6366.2 mA)
- 계산: PASS (X_L = 0.6283 Ω, X_C = 1.5916 MΩ, R_l ≈ 0 이상적 가정 명시)
- 단위: PASS

### Table 9.10
- Topology: PASS
- KVL: 해당 없음
- KCL: PASS (Method Two의 E/I_s = 4 V / 6.3662 A ≈ 0.6283 Ω)
- 계산: PASS (Method One |Z_T| ≈ 0.6283 Ω와 Method Two 일치, θ_s ≈ -89.964°)
- 단위: PASS

### Table 10.1
- Topology: PASS (Fig 10.3 R-L series-parallel)
- KVL: PASS (V_1 + V_2 phasor 합 ≈ 4.00 + j0 V = E)
- KCL: PASS (I_2 + I_3 phasor 합 ≈ I_s, sqrt(I_2^2 + I_3^2) ≈ 4.56 mA)
- 계산: PASS (정확 재계산 Z_T ≈ 877.50 Ω, 보고서 877.19 Ω은 중간 반올림 영향)
- 단위: PASS

### Table 10.2
- Topology: PASS
- KVL: PASS (Table 10.1의 V_1, V_2 phasor 관계와 일관)
- KCL: PASS (Table 10.1의 I_s, I_2, I_3 phasor 관계와 일관)
- 계산: PASS (E&V_2 ≈ +26.97°, E&I_s ≈ -30.89°, E&V_1 ≈ -30.89°)
- 단위: PASS

### Table 10.3
- Topology: PASS (Fig 10.4 R-C series-parallel)
- KVL: PASS (V_1 + V_2 phasor 합 ≈ 4.00 + j0 V = E)
- KCL: PASS (I_2 + I_3 phasor 합 ≈ I_s, sqrt(I_2^2 + I_3^2) ≈ 4.055 mA)
- 계산: PASS (정확 재계산 Z_T ≈ 986.45 Ω, 보고서 986.39 Ω은 반올림 범위)
- 단위: PASS

### Table 10.4
- Topology: PASS
- KVL: PASS (Table 10.3의 V_1, V_2 phasor 관계와 일관)
- KCL: PASS (I_2와 I_3가 90° 차이이며 phasor 합이 I_s)
- 계산: PASS (E&I_s ≈ +29.60°, E&I_2 ≈ -21.89°, I_2&I_3 = +90.00°)
- 단위: PASS

### 경계 침범 체크
- 명판값 외 수치 사용: PASS (계산에는 4 V p-p, 1 kΩ, 470 Ω, 10 Ω, 10 mH, 0.01 μF, 0.02 μF 등 명판/강의노트 수치 사용)
- R_l 수치화 여부: PASS (구체 실측값 없이 R_l ≈ 0 이상적 가정만 사용)

### Type A 채움 체크
- 측정 의존 예측칸: PASS (V_Rs, Z_T, 전류, 위상각 등을 이론 예측값으로 채움)
- 명판값 불일치: PASS

### Type B 정성 파트 체크
- 해당 없음

### 보드 연결도 필터링
- 비-회로 Fig 포함: PASS (보드 연결도에는 Fig 9.4~9.7, Fig 10.3~10.4만 포함)

### STT 교차검증 및 노출 체크
- STT 관련 문자열 등장: PASS (보고서 본문에 `STT`, `input/stt`, `실험 영상`, `측정값 대조`, `stt/` 노출 없음)
- STT 수치 비교: PASS 조건부 (STT는 8 V p-p 대신 4 V p-p 사용을 확인한다. 9-2 STT의 약 I_s 1.47, I_C 0.83 mA, I_R 1.2 mA 및 V_Rs 약 55 mV 발화는 RMS/측정 조건/발화 인식이 혼재된 실측값으로 보이며, 보고서 예상값 Table은 p-p 이론값이므로 직접 FAIL 근거로 삼지 않음)
- STT 절차/회로 변형: PASS (보조 Table이 필요한 새로운 topology 변형 발화 없음)

### 발견된 오류 목록
- 미세 표기 불일치 - Table 10.1: 정확 재계산 Z_T ≈ 877.50 Ω vs 보고서 877.19 Ω, 중간 반올림 영향으로 최종 판정 영향 없음.
- 미세 표기 불일치 - Table 10.3: 정확 재계산 Z_T ≈ 986.45 Ω vs 보고서 986.39 Ω, 중간 반올림 영향으로 최종 판정 영향 없음.

최종 판정: PASS
