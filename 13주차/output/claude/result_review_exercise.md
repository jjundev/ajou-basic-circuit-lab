## 연습 문제 검증

- 섹션 위치: PASS (`# 연습 문제` 가 `# 실험 결과` 뒤에 위치, `# 고찰` 섹션은 아직 작성 전이므로 위치 충돌 없음)
- Exercise 누락: PASS (입력 2개 이미지에 담긴 Exercise 1·2·3 모두 보고서에 작성됨)
- 입력 파싱: PASS (Fig 10.3/10.4/10.5 식별, Part 1(l)·Part 2·Part 3(j) 참조 정확. Ex2는 페이지 383-384 미포함을 명시적으로 보고)
- 단위 변환: PASS (이번 Exercise들은 모두 위상각 문제로 p-p ↔ rms 변환 불필요)
- 단계별 계산 흐름: PASS (Ex3에서 X_L → Z_1 → ∠Z_1 → ∠I_1 → θ_1 흐름 정상)
- 공식 정확성: PASS (X_L = 2πfL, X_C = 1/(2πfC), |Z| = √(R²+X²), θ = arctan(X/R), I = E/Z 모두 정확)
- 재계산 일치: PASS
  - Ex1: 90° (E² = V_1² + V_2² ⟺ cos(θ) = 0 ⟺ θ = 90°) — 정확
  - Ex3: atan(628.32/980) = 32.6585°, atan(795.78/463) = 59.8113°, 합 = 92.4698° ≈ 92.47° — 보고서 값 일치
- 단위 표기: PASS (Ω, mH, μF, V_pp, kHz, ° 모두 표기됨)
- 정답-본문 일관성: PASS
  - Ex1: 본문 "θ_(V_1,V_2) = 90°" ↔ 정답 "θ_s (V_1 vs V_2) = 90°" 일치
  - Ex2: 본문 "Case A 기준 θ_s = 0°" ↔ 정답 동일 + 분기 회로 시 재계산 권고 명시
  - Ex3: 본문 "θ_1 = +92.47°" ↔ 정답 "θ_1 (I_1 vs I_2) = 92.47°" 일치
- Calculated/Experimental Table 형식: PASS
  - Ex1: `구분 | Calculated | Experimental`, Experimental = "실험 측정값" placeholder 유지
  - Ex3: 동일 형식, placeholder 유지
  - Ex2: 회로도 식별 불가로 조건부 답안 (bullet) — Type 3 회로 임피던스/전압 계산 아닌 위상각 조건부 답안이라 bullet 처리 허용
- 스타일 규칙 (헤더 단독·빈 줄·결론/요약 bullet·italic·시각 기호): PASS
  - `### Exercise 1/2/3` 모두 단독 헤더 (제목·괄호 부착 없음)
  - **조건**, **풀이**, **정답**, ①/②/③ 직후 빈 줄 모두 확인
  - Ex2 **정답** 하위 두 문장이 모두 top-level `-` bullet
  - **Case A/B/C — ...** bold 사용은 케이스 분기 라벨 규칙에 부합 (허용)
  - italic `*text*` 사용 없음
  - ✓/✗/❌/✅ 등 시각 기호 본문 사용 없음 (Phase 2 검토 영역 한정)

### 발견된 오류 목록
- 없음

최종 판정: PASS
