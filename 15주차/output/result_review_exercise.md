## 연습 문제 검증

- 섹션 위치: PASS (`# 연습 문제`는 line 308, `# 실험 결과`(line 5) 뒤와 `# 고찰`(line 462) 앞에 위치. `# 실험 결과` 내부 `## Ch` 사이에 끼어 있지 않음)
- Exercise 누락: PASS (입력 이미지 3개에서 확인되는 4문항 모두 작성됨: Ch14 Exercise 1·2, Ch15 Exercise 1·2)
- 입력 파싱: PASS (Ch14-1: C=0.01 μF 변경 조건 반영. Ch14-2: I_s=5 mA, R_s=∞ Ω, L=100 μH, R_l=5 Ω, C=0.02 μF 반영. Ch15-1: E=8 V(p-p)∠0°, Fig 15.6 조건 반영. Ch15-2: Fig 15.5의 R=100 Ω, R_l=24.73 Ω, L=10 mH, C=0.1 μF, f=f_s·½f_s·2f_s 반영)
- 단위 변환: PASS (p-p ↔ rms 변환이 필요한 문항 없음. Ch15 Exercise 1은 E=8 V(p-p)를 p-p 기준으로 유지)
- 단계별 계산 흐름: PASS (Ch14-2 f_p→X_L→Q_l→BW, Ch15-1 f_p→X_L/X_C→Z_Tp→V_o, Ch15-2 f_s 기준 X_L/X_C 스케일링과 R+R_l=124.73 Ω 전달 정확)
- 공식 정확성: PASS (θ = −arctan[(X_L − X_C)/(R + R_l)] 자체와 X_L=2πfL, X_C=1/(2πfC) 적용은 맞음)
- 재계산 일치: PASS (전 항목 직접 재계산 일치. Ch14-1: 15915.5 Hz / 34.35 kΩ / R_s/Z_p=2.91. Ch14-2: 112540 Hz / 70.71 Ω / Q=14.14 / BW=7959 Hz. Ch15-1: 11254.6 Hz / Z_Tp=1000 Ω / V_o=0.727 V(p-p). Ch15-2: R+R_l=124.73 Ω, θ=0°·+75.27°·−75.27°)
- 단위 표기: PASS (Hz, Ω, kΩ, V(p-p), ° 등 단위 표기 있음. 무차원 비와 Q는 단위 없음이 정상)
- 정답-본문 일관성: PASS (4문항 모두 정답/결론값이 본문 마지막 단계 결과와 일치)
- Calculated/Experimental Table 형식 (해당 시): PASS (Ch15 Exercise 1 표는 `구분 | Calculated | Experimental` 형식이며 Experimental 칸이 모두 `실험 측정값` placeholder로 유지됨)
- 스타일 규칙 (헤더 단독·블록 줄바꿈·결론/요약 bullet·italic·시각 기호): PASS (`### Exercise N` 헤더 단독, 라벨/step/table 앞뒤 빈 줄 1개 유지, 결론/정답 문장 bullet 형식, italic 및 check/cross 기호 없음)

### 발견된 오류 목록
- 없음

최종 판정: PASS
