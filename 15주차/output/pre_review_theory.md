## 이론 섹션 검토 결과

### 실험 목적
- Markdown 무결성: PASS — 이론 3개 섹션에 markdown 표 없음(bullet list만), parse 문제 없음.
- 강의노트 1:1 매핑: PASS
    - Ch 14 강의노트 목표 4개 모두 반영: ① 병렬 R-L-C 주파수별 전압·전류 이론 계산+실험(line 7), ② resonant frequency f_p 이론 계산+실험(line 8), ③ input impedance Z_p 측정(line 10), ④ Quality factor·bandwidth 관계(line 11). 누락 없음.
    - Ch 15 강의노트 목표 2개 모두 반영: ① R-C high-pass filter(line 16), ② R-L-C band-pass filter(line 17). band-stop는 교재 Procedure Part 3 보충으로 추가(line 18) — 강의노트 BSF 이론 슬라이드 및 Procedure Part 3(Fig 15.6, Table 15.7) 존재하므로 정당한 완성 보강.
- 회로 유형 enumeration: PASS — 강의노트 목표 enumeration(HPF, BPF) 모두 등장. 강의노트 이론 슬라이드의 LPF는 Procedure에 해당 Part가 없어 본문 미수록은 허용(아래 메모 참조).
- 판정: PASS

### 실험 준비물
- 그룹화/헤더 형식: PASS — 모든 항목이 `**{부품명} {정격값} ({수량})**` 형식, 동일 부품 단일 항목으로 그룹화.
- 사용처 명시: PASS — 다중 사용 부품(100 Ω: Part2·Part3 / 10 mH: Ch14·Ch15 Part2 / 0.1 μF: Ch14·Ch15 Part1·Part2)의 모든 사용처를 sub-bullet로 나열하고 순차 재사용으로 총 1개임을 명시.
- 실측 행동 지시: PASS — 저항·코일 내부저항 R_l에 "DMM으로 실측값 먼저 기록" 행동 지시 포함.
- 부품 수량 정확성 (추가 키워드 매칭): PASS — 교재 Procedure 및 강의노트의 모든 Part가 ×1 표기(100kΩ×1, 4.7Ω×1, 10mH×1, 0.1μF×1, 1kΩ×1, 100Ω×1, 1mH×1, 0.2μF×1). "second/additional/2개/직렬추가" 등 추가 수량 키워드 없음. 보고서 수량과 일치.
- 교재 Equipment Issued(Table 14.0) 대조: DMM, 오실로스코프, 오디오 발진기/함수발생기, 주파수 계수기 모두 포함. 누락 없음.
- 판정: PASS

### 실험 이론
- 핵심 공식 유도: PASS
    - X_C, X_L를 Z_C=1/(jωC), Z_L=jωL 크기에서 유도(line 89-90).
    - f_p를 어드미턴스 서셉턴스=0 조건(Eq 14.1) → Eq 14.3 → Q_coil≥10 근사(Eq 14.4)로 단계 유도(line 102-103). Z_Tp=L/(R_lC) 유도(line 104). 교재 Eq 14.1~14.4 및 강의노트와 일치.
    - f_c를 R=X_C 조건에서 f_c=1/(2πRC)로 유도(line 122).
- 적용 방법 수치 예시 + Part-부품 매핑: PASS
    - 각 이론 섹션에 실제 Part 수치 예시 존재하고 Part-부품 매핑 정확:
      · Ch14 Part1(L=10mH, C=0.1μF, R=4.7Ω): f_p≈5033 Hz, X_L≈316.2 Ω, Q_coil≈67.3, Z_Tp≈21.3 kΩ, BW≈74.8 Hz — 재계산 일치.
      · Ch15 Part1 HPF(R=1kΩ, C=0.1μF): f_c≈1591.5 Hz, f=2kHz에서 |A_v|≈0.782, θ≈38.5° — 재계산 일치.
      · Ch15 Part2 BPF(L=10mH, C=0.1μF, R=100Ω): f_s≈5033 Hz, Q_s≈3.16, BW≈1593 Hz — 재계산 일치.
      · Ch15 Part3 BSF(L=1mH, C=0.2μF, R=100Ω): f_p≈11254 Hz, X_L≈X_C≈70.7 Ω — 재계산 일치.
- 위상각 convention: PASS — HPF를 leading network(V_o가 V_i를 앞섬, θ=arctan(X_C/R))로 올바르게 서술. f_c에서 θ=45° 일치.
- 운용 조건 임의 변경 금지: PASS — E_s=5 V(p-p), Ch14 500 Hz~10 kHz, Ch15 0.1~100 kHz 모두 강의노트 Procedure와 일치. 임의 변경·"진폭 줄임" 등 권고 없음.
- 판정: PASS

### 경계 침범 체크
- 명판값 외 수치 사용: PASS — 모든 계산이 명판값(1 kΩ, 4.7 Ω, 100 Ω, 100 kΩ, 10 mH, 1 mH, 0.1 μF, 0.2 μF) 사용. measured/ 누수 정밀 수치 없음.
- R_l 수치화 여부: PASS — 본문 전체에서 이상적 인덕터(R_l ≈ 0) 가정을 명시(line 48, 53, 108)하고 R_l을 구체 수치로 계산에 반영하지 않음. R=R_1+R_l 대입은 교재 지시(Eq 14.3 R_l 자리)에 부합.

### STT 충돌 처리 체크
- 유형 A (수치 파라미터): 해당 충돌 없음 — 강의노트 운용 조건(E_s=5 Vpp, 주파수 범위) 그대로 사용.
- 유형 B (절차/회로 변형): 보조 Table 필요한 STT 변형 없음. 본문에 STT 노출 문자열("STT", "측정값 대조" 등) 없음.

### 발견된 문제점
- (비차단 메모) Q 기호 표기: line 103은 Q_coil=X_L/R_l, line 110은 Q_coil=X_L/R로 분모 표기가 다름. 단 line 32·108에서 "R_l 자리에 R=R_1+R_l 대입(교재 지시)"을 명시하고 R_l≈0이라 R≈R_1=4.7 Ω이므로 내부 일관됨. 엄밀히는 line 110 값(67.3)은 코일 단독 Q가 아닌 R_1 삽입 후 부하 Q이므로 "회로 Q"로 부르면 더 정확. FAIL 아님.
- (비차단 메모) 강의노트 이론 슬라이드에는 LPF도 등장하나 보고서 이론 본문에 LPF 단독 절은 없음. Procedure에 LPF Part가 없어 허용되나, 필터 개요에 LPF 대비 한 줄 추가 시 완성도 향상.

최종 판정: PASS
