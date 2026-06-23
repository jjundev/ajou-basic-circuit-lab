## 실험 결과 검증

### Markdown 표 무결성 (Step 0a)
- 11개 표 전부 컬럼 수 일관(헤더=구분자=본문 셀 수), `\|` escape 없음, raw newline/`<br>` 없음 → PASS

### Table 14.1
- Markdown 무결성: PASS
- Table 구조: PASS (교재 원형 = 단일 계산 열, 행 R / f_p(Eq.14.3) / f_p(Eq.14.4) / Z_p / Q_l / Q_p. Measured·%(Difference) 열 없음)
- Measured 원본 대조: 해당 없음 (전부 계산 컬럼)
- Calculated 재계산: PASS
  - R = R_1 + R_l = 4.38 + 24.73 = 29.11 Ω
  - f_p(Eq.14.4) = 1/(2π√(10 mH·0.1 μF)) = 5032.9 Hz
  - f_p(Eq.14.3) = 5032.9·√(1 - 29.11²·0.1 μF/10 mH) = 5011.6 Hz → 보고서 5011.5 Hz 일치
  - Z_p = L/(RC) = 0.01/(29.11·0.1 μF) = 3435.2 Ω = 3.44 kΩ
  - Q_l = X_L/R = 316.23/29.11 = 10.86, Q_p = 10.86
- %(Difference) 계산: 해당 없음 (교재 원형에 %(Difference) 열 없음)

### Table 14.2
- Markdown 무결성: PASS
- Table 구조: PASS (교재 원형 = Frequency | V_C(p-p) | V_Rs(p-p) | I_s(p-p) | Z_p = V_C/I_s. Calculated·%(Difference) 열 없음)
- Measured 원본 대조: PASS (측정값 파일의 V_C, V_Rs와 보고서 값 일치. 5033 Hz·4980 Hz는 측정 불가로 보존)
- Calculated 재계산: PASS
  - I_s = 5.00 V / 100.6 kΩ = 0.0497 mA
  - Z_p = V_C/I_s 전 행 일치: 예) 5000 Hz 0.115 V / 49.7018 μA = 2313.8 Ω, 4900 Hz = 2193.1 Ω, 5200 Hz = 2152.8 Ω
- %(Difference) 계산: 해당 없음

### Table 15.1
- Markdown 무결성: PASS
- Table 구조: PASS (교재 원형 = 행 f_c / V_o/V_i(2 kHz), 열 Calculated | Graph | Graph(45°). V_o/V_i 행의 Graph(45°) 칸 공란 처리 정상)
- Measured 원본 대조: 해당 없음 (계산·그래프 판독 컬럼)
- Calculated 재계산: PASS
  - f_c = 1/(2π·985.6 Ω·0.1 μF) = 1614.8 Hz
  - 2 kHz에서 X_C = 795.8 Ω, V_o/V_i = 985.6/√(985.6²+795.8²) = 0.778
  - Graph f_c: Table 15.2의 1.4 kHz(0.668)~1.6 kHz(0.708) 사이 0.707 보간 → 약 1.60 kHz
  - Graph(45°) f_c: Table 15.3의 1 kHz(55.64°)~2 kHz(36.42°) 사이 45° 보간 → 약 1.55 kHz
- %(Difference) 계산: 해당 없음

### Table 15.2
- Markdown 무결성: PASS
- Table 구조: PASS (교재 원형 = Frequency(kHz) | V_o(p-p) | A_v)
- Measured 원본 대조: PASS (측정값 파일 V_o 전 항목 1:1 일치)
- Calculated 재계산: PASS (A_v = V_o/5 전 행 일치)
- %(Difference) 계산: 해당 없음

### Table 15.3
- Markdown 무결성: PASS
- Table 구조: PASS (교재 원형 = Frequency(kHz) | θ)
- Measured 원본 대조: PASS (측정값 파일 θ 전 항목 1:1 일치)
- Calculated 재계산: 해당 없음 (직접 측정값)
- %(Difference) 계산: 해당 없음

### Table 15.4
- Markdown 무결성: PASS
- Table 구조: PASS (교재 원형 = 단일 열, 행 f_s / Q_s / BW(f/Q) / V_o/V_i(at f_s) / BW / A_v_max / f_1(low) / f_2(high))
- Measured 원본 대조: 해당 없음 (이론+그래프 판독 컬럼)
- Calculated 재계산: PASS
  - f_s = 5032.9 Hz, X_L = 316.23 Ω
  - Q_s = 316.23/(90.4+24.73) = 2.75, BW(f/Q) = 5032.9/2.7467 = 1832 Hz
  - V_o/V_i(at f_s) = 90.4/115.13 = 0.785
  - A_v_max = 3.92/5 = 0.784, f_1 ≈ 4230 Hz, f_2 ≈ 6150 Hz, BW(graph) = 1920 Hz
- %(Difference) 계산: 해당 없음

### Table 15.5
- Markdown 무결성: PASS
- Table 구조: PASS (교재 원형 = Frequency(kHz) | V_o(p-p) | A_v)
- Measured 원본 대조: PASS (측정값 파일 V_o 전 항목 일치, 5.033 kHz 측정 불가 보존)
- Calculated 재계산: PASS (A_v = V_o/5 전 행 일치)
- %(Difference) 계산: 해당 없음

### Table 15.6
- Markdown 무결성: PASS
- Table 구조: PASS (교재 원형 = 단일 열, 행 f_p / Q_l / BW(Calc) / Z_Tp / V_o/V_i(Calc) / BW(graph) / V_o/V_i(graph) / f_1(low) / f_2(high))
- Measured 원본 대조: 해당 없음 (이론+그래프 판독 컬럼)
- Calculated 재계산: PASS
  - f_p = 1/(2π√(1 mH·0.2 μF)) = 11254 Hz 수준 → 보고서 11254.6 Hz 허용
  - Q_l = 70.71/5 = 14.14, Z_Tp = 1 mH/(5 Ω·0.2 μF) = 1000 Ω
  - BW(Calc) = 11254.6/14.14 = 796 Hz, V_o/V_i(Calc) = 90.4/(90.4+1000) = 0.083
  - Graph: 0.707 교점 보간 f_1 ≈ 7600 Hz, f_2 ≈ 16300 Hz, BW(graph) = 8700 Hz, V_o/V_i(graph) = 0.84/5 = 0.168
- %(Difference) 계산: 해당 없음

### Table 15.7
- Markdown 무결성: PASS
- Table 구조: PASS (교재 원형 = Frequency(kHz) | V_o(p-p) | A_v)
- Measured 원본 대조: PASS (측정값 파일 V_o 전 항목 일치, 7.957 kHz·11.255 kHz·15.916 kHz 측정 불가 보존)
- Calculated 재계산: PASS (A_v = V_o/5 전 행 일치)
- %(Difference) 계산: 해당 없음

### 측정 기반 산출값 검증
- PASS — 측정 기반 표는 측정 V_C·V_o·θ와 환산식(I_s=V_Rs/R_s, Z_p=V_C/I_s, A_v=V_o/V_i)으로 산출되었고, 그래프 판독값은 인접 측정점 보간으로 산출됨. 이론 기준값으로 측정 기반 결과를 덮어쓴 사례 없음.

### 내부 일관성 cross-reference
- PASS — 실험 결과 섹션 내 R_s=100.6 kΩ, R_1=4.38 Ω, R_l(10 mH)=24.73 Ω, R_HPF=985.6 Ω, R_BPF·BSF=90.4 Ω, R_l(1 mH)=5 Ω, f_s/f_p 값 사용 일관. 연습 문제 섹션은 Phase 2에서 별도 검증.

### 발견된 오류 목록
- 없음

### 참고 (FAIL 아님)
- 교재 도면에는 V_i 또는 E가 8 V/10 V(p-p)로 보이나, 측정값 파일과 강의노트 조건은 5 V(p-p)이며 보고서의 측정 기반 표는 5 V 기준 데이터와 일치함.
- 교재 원형상 어느 실험 결과 표에도 %(Difference) 열이 없어 오차율 열 검산 대상은 없음.

최종 판정: PASS
