## 연습 문제 검증

- 섹션 위치: PASS (# 연습 문제는 # 실험 결과 뒤에 위치하며, 보고서 내 # 고찰 섹션은 없음)
- Exercise 누락: FAIL (Exercise 1, 2, 3은 모두 작성되었으나, Exercise 2 원문 요구사항인 complete phasor diagram 도식이 누락됨)
- 입력 파싱: PASS (제공 이미지의 Exercise 1~3 지시문은 반영됨. 단, Fig 10.3~10.5의 회로 소자값 자체는 제공 이미지에 직접 표시되지 않아 이미지 원본만으로는 대조 불가)
- 단위 변환: PASS (p-p ↔ rms 변환 항목 없음)
- 단계별 계산 흐름: PASS (Exercise 1~3에서 앞 단계의 Z, I, V 및 위상값이 다음 단계 입력으로 일관되게 사용됨)
- 공식 정확성: PASS (X_L = 2πfL, X_C = 1/(2πfC), 병렬 임피던스, 페이저 위상 계산 공식 적용이 타당함)
- 재계산 일치: PASS (Exercise 1 θ_s = 57.86°, Exercise 2 θ_s = 51.49°, Exercise 3 θ_I1_I2 = 92.47°로 보고서 92.48°는 반올림 허용)
- 단위 표기: PASS (계산 수치에 Ω, V_pp, mA_pp, ° 등 단위 표기됨)
- 정답-본문 일관성: PASS (정답 섹션의 값이 본문 마지막 계산값과 일치함)
- Calculated/Experimental Table 형식 (해당 시): PASS (Exercise 1, 3의 표 헤더가 구분 | Calculated | Experimental 형식이며 Experimental 칸은 "실험 측정값" placeholder 유지)

### 발견된 오류 목록
- Exercise 2: 입력 문제는 "draw a complete phasor diagram for all the currents of Fig. 10.4"를 요구하지만, 보고서에는 I_1, I_2, I_3의 Phasor 표와 배치 설명만 있고 실제 페이저도 도식이 없음.

최종 판정: FAIL
