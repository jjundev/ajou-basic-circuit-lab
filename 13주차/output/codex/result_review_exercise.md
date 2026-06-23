## 연습 문제 검증

- 섹션 위치: PASS (`# 연습 문제`가 `# 실험 결과` 뒤, `# 고찰` 앞에 위치함)
- Exercise 누락: PASS (입력 이미지의 Exercise 1, 2, 3이 모두 작성됨)
- 입력 파싱: PASS (Exercise 1: Fig 10.3의 `V_1`/`V_2` 위상각, Exercise 2: Fig 10.4의 `I_1 = I_s`와 `I_2` 위상각 및 전체 전류 페이저도, Exercise 3: Fig 10.5의 `I_1`/`I_2` 위상각 비교 요구를 반영함)
- 단위 변환: PASS (p-p ↔ rms 변환을 요구하는 항목 없음)
- 단계별 계산 흐름: PASS (Exercise 1~3에서 리액턴스 → 병렬/전체 임피던스 → 전류/전압 페이저 → 위상각 순서가 일관됨)
- 공식 정확성: PASS (`X_L = 2πfL`, `X_C = 1/(2πfC)`, 병렬 임피던스, 페이저 위상 계산 공식 적용이 타당함)
- 재계산 일치: PASS (Exercise 1 `θ_s = 57.86°`, Exercise 2 `θ_s = 51.49°`, Exercise 3 `θ_I1_I2 = 92.48°` 재계산 일치)
- 단위 표기: PASS (`Ω`, `V_pp`, `mA_pp`, `°` 등 단위 표기됨)
- 정답-본문 일관성: PASS (정답 표/문장의 값이 본문 마지막 계산값과 일치함)
- Calculated/Experimental Table 형식 (해당 시): PASS (Exercise 1, 3의 표가 `구분 | Calculated | Experimental` 형식이며 Experimental 칸은 모두 `실험 측정값` placeholder 유지)
- 스타일 규칙 (헤더 단독·빈 줄·italic·시각 기호): PASS (`### Exercise N` 헤더 단독 사용, bold label과 원숫자 step 다음 빈 줄 존재, italic 강조 및 checkmark/cross류 시각 기호 없음)

### 발견된 오류 목록
- 없음

최종 판정: PASS
