## 실험 결과 검증

### Table 15.1
- Calculated 재계산: PASS (정상 상태에서 I=0, V1=0, V2=10 계산 일치)
- %(Difference) 계산: PASS (V2=0.41% 일치, Calculated=0인 I/V1은 절대오차 표기 적절)

### Table 15.2
- Calculated 재계산: PASS (I1=I2=2.2472 mA, I3=0 mA, V1=2.6517 V, V2=V3=7.3483 V 일치)
- %(Difference) 계산: PASS (I1 0.32%, I2 0.76%, V1 0.69%, V2/V3 0.02% 일치)

### Table 15.3
- Calculated 재계산: PASS (정상 상태 개방회로 가정에서 I1~I4=0 mA 계산 일치)
- %(Difference) 계산: PASS (Measured/%(Difference) 열이 없어 검증 대상 없음)

### Table 15.4
- Calculated 재계산: PASS (V1=0, V2=0, V3=10, V4=10 계산 일치)
- %(Difference) 계산: PASS (V3 0.18%, V4 0.23% 일치, V1/V2는 Calculated=0으로 절대오차 표기 적절)

### Table 15.5
- Calculated 재계산: PASS (tau=R*C=9.844 s 계산 일치)
- %(Difference) 계산: PASS (|9.844-10.13|/9.844*100=2.91% 일치)

### Table 15.6
- Calculated 재계산: PASS (C_measured(100 uF)=102.91 uF, C_measured(220 uF)=257.42 uF 계산 일치)
- %(Difference) 계산: PASS (해당 표에는 %(Difference) 열이 없어 검증 대상 없음)

### Table 16.1
- Calculated 재계산: PASS (CT=360.33 uF, tau=35.47 s, 5tau=177.35 s 계산 일치)
- %(Difference) 계산: PASS (해당 표에는 %(Difference) 열이 없어 검증 대상 없음)

### Table 16.2
- Calculated 재계산: FAIL (Calculated v_C 및 %(Difference)는 일치하지만, v_R 행의 기준이 잘못되었거나 불명확함)
- %(Difference) 계산: PASS (v_C의 %(Difference)는 반올림 전 Calculated 값 기준으로 전 구간 일치)
- 오류 내용: 보고서에는 `v_R = E - v_C = 12*e^(-t/35.47)`로 이론식이 제시되어 있으나, 표의 v_R 값은 이론 v_C가 아니라 Measured v_C를 12 V에서 뺀 값이다. 예를 들어 t=10 s에서 이론 v_R은 12-2.95=9.05 V이어야 하는데 표에는 8.80 V가 기입되어 있다. t=20 s도 이론값은 6.83 V이나 표에는 6.52 V가 기입되어 있다.
- 수정 방향: v_R 행을 이론값으로 유지하려면 `12 - Calculated v_C` 값으로 교체하고, 측정값 기반 파생값을 의도했다면 행 이름을 `Measured/Derived v_R = 12 - Measured v_C`처럼 명확히 바꿔야 한다.

### Table 16.3
- Calculated 재계산: PASS (1tau/5tau/25s 이론식 및 선형 보간 값 자체는 재계산 일치)
- %(Difference) 계산: PASS (25s 식값-그래프값 차이 서술은 반올림 범위 내 일치)
- 확인 필요: 입력 파일은 "선형회귀법" 사용을 지시하지만 보고서는 "선형 보간"을 사용한다. 입력 지시가 authoritative라면 방법 불일치이므로 수정이 필요하다.

### 발견된 오류 목록
- Table 16.2의 v_R 행이 앞의 이론식 `v_R = 12*e^(-t/35.47)`과 일치하지 않는다. 현재 값은 `12 - Measured v_C`로 계산된 값에 가깝지만 행 이름과 설명에 이 기준이 명시되어 있지 않다.
- Table 16.3은 입력 지시의 "선형회귀법"과 보고서의 "선형 보간" 사이에 방법 불일치 가능성이 있다.

최종 판정: FAIL
