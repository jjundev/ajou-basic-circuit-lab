## 실험 결과 검증

---

### DC Ch 17 Part 3 — Table 17.3

- Table 구조: 해당 없음 — 실험 미진행으로 Table 전체 생략. 측정값 파일도 "실험을 진행하지 않았음"으로 일치. 생략 자체는 정상 처리.
- Measured 원본 대조: PASS (측정값 파일과 일치 — 미진행)
- Calculated 재계산: 해당 없음
- %(Difference) 계산: 해당 없음

---

### AC Ch 2 Part 3 — Fig 2.6 / Fig 2.7 (Table 없음)

교재 원형에 수치 Table 없음. 파형 스케치·감도 설정 및 서술 항목.

- Table 구조: 해당 없음 (교재에 Table 없음)
- Measured 원본 대조: PASS

    | 항목 | 측정값 파일 | 결과보고서 |
    |---|---|---|
    | (g)-1 Vertical Sensitivity | 100 mV/div | 100 mV/div ✅ |
    | (g)-1 Horizontal Sensitivity | 500 μs/div | 500 μs/div ✅ |
    | (g)-2 대체 신호 | v = 2 sin 2π500t (5V 한계) | v = 2 sin 2π500t ✅ |
    | (g)-2 Vertical Sensitivity | 1 V/div | 1 V/div ✅ |
    | (g)-2 Horizontal Sensitivity | 500 μs/div | 500 μs/div ✅ |
    | (h) 실험 가능 여부 | 진행 불가 (5V 한계) | 진행 불가 ✅ |
    | (i) V_eff | 0.35 V (rms) | 0.35 V (rms) ✅ |
    | (i) V_pp (오실로스코프) | 1 V | 1 V ✅ |

- Calculated 재계산: PASS — (i) V_eff = 0.707 × 0.5 = 0.3535 V ≈ 0.35 V, V_pp = 1.0 V 모두 정확

---

### AC Ch 2 Part 4 — Fig 2.8 / Fig 2.9 (Table 없음)

교재 원형에 수치 Table 없음. f, T 계산 및 감도 기입 항목.

- Table 구조: 해당 없음 (교재에 Table 없음)
- Measured 원본 대조: PASS

    | 항목 | 측정값 파일 | 결과보고서 |
    |---|---|---|
    | v1 Vertical Deflection | 2 div | 2 div ✅ |
    | v1 Vertical Sensitivity | 200 mV/div | 200 mV/div ✅ |
    | v1 Horizontal Deflection | 5 div | 5 div ✅ |
    | v1 Horizontal Sensitivity | 20 μs/div | 20 μs/div ✅ |
    | v2 Vertical Deflection | 5 div | 5 div ✅ |
    | v2 Vertical Sensitivity | 1 V/div | 1 V/div ✅ |
    | v2 Horizontal Deflection | 3.333 div | 3.333 div ✅ |
    | v2 Horizontal Sensitivity | 5 ms/div | 5 ms/div ✅ |

- Calculated 재계산: PASS

    | 항목 | 재계산 | 결과보고서 |
    |---|---|---|
    | v1: f = 62832/(2π) | 10,000 Hz | 10,000 Hz ✅ |
    | v1: T = 1/10000 | 100 μs | 100 μs ✅ |
    | v1: V_m = 2 div × 200 mV/div | 400 mV | 400 mV ✅ |
    | v1: T = 5 div × 20 μs/div | 100 μs | 100 μs ✅ |
    | v2: f = 377/(2π) | 60.0 Hz | 60.0 Hz ✅ |
    | v2: T = 1/60 | 16.67 ms | 16.67 ms ✅ |
    | v2: V_m = 5 div × 1 V/div | 5 V | 5 V ✅ |
    | v2: T = 3.333 div × 5 ms/div | 16.665 ms ≈ 16.67 ms | 16.665 ms ✅ |

---

### AC Ch 2 Part 5 — Fig 2.11 (Table 없음)

교재 원형에 수치 Table 없음. 커플링 모드별 정성 관찰 항목.

- Table 구조: 해당 없음
- Measured 원본 대조: PASS (측정값 파일에 "그래프 사진은 직접 첨부할 예정"만 기재, 정성 관찰 일치)
- Calculated 재계산: 해당 없음

---

### AC Ch 3 Part 1 — Table 3.1 / Table 3.2

- Table 구조: 해당 없음 — 실험 미진행으로 Table 생략. 측정값 파일 일치.
- Measured 원본 대조: PASS (측정값 파일과 일치 — 미진행)
- Calculated 재계산: 해당 없음

---

### AC Ch 3 Part 2 — Table 3.3 (Capacitive Reactance)

#### 교재 Table 3.3 원형 구조 (p.279)

교재 열: `V_Rs(DMM)` | `I_p-p` | `X_C(meas.)` | `X_C(calc.)` | `C`
교재 행: `Parts (b)-(f)`, `Parts (g)-(j)`

- Table 구조: PASS — 결과보고서 Table 열·행 구조가 교재 원형과 완전 일치. `Measured`, `%(Difference)` 등 임의 열 없음.
- Measured 원본 대조: PASS

    | 항목 | 측정값 파일 | 결과보고서 |
    |---|---|---|
    | R_s (실측) | 103.1 Ω | 103.1 Ω ✅ |
    | V_Rs(DMM) Parts(b)-(f) | 96.55 mV | 96.55 mV ✅ |
    | Parts(g)-(j) | 미진행 | 미진행 ✅ |

- Calculated 재계산: PASS

    실측값: R_s = 103.1 Ω, V_Rs(DMM) = 96.55 mV, V_C = 4 V(p-p), f = 100 Hz, C = 1 μF

    | 항목 | 재계산 | 결과보고서 |
    |---|---|---|
    | V_Rs(peak) = 96.55 mV × √2 | 136.54 mV | 136.5 mV ✅ |
    | V_Rs(p-p) = 2 × 136.54 mV | 273.08 mV | 273.1 mV ✅ |
    | I_p-p = 273.08 mV / 103.1 Ω | 2.6486 mA | 2.649 mA ✅ |
    | X_C(meas.) = 4 V / 2.6486 mA | 1510.1 Ω | 1510.0 Ω ✅ |
    | X_C(calc.) = 1/(2π×100×1μF) | 1591.55 Ω | 1591.5 Ω ✅ |
    | C = 1/(2π×100×1510.0) | 1.054 μF | 1.054 μF ✅ |

- %(Difference) 계산: 해당 없음 (교재 Table 3.3에 %(Difference) 열 없음)

---

### AC Ch 3 Part 3 — Table 3.4 (Inductive Reactance)

#### 교재 Table 3.4 원형 구조 (p.283)

교재 열: `V_Rs(DMM)` | `V_Rs(p-p)` | `I_p-p` | `X_L(meas.)` | `X_L(calc.)` | `L`
교재 행: `parts (b)-(i)`, `parts (j)-(n)`

- Table 구조: PASS — 결과보고서 Table 열·행 구조가 교재 원형과 완전 일치. `Measured`, `%(Difference)` 등 임의 열 없음.
- Measured 원본 대조: PASS

    | 항목 | 측정값 파일 | 결과보고서 |
    |---|---|---|
    | R_s (실측) | 103.1 Ω | 103.1 Ω ✅ |
    | V_Rs(DMM) Parts(b)-(i) | 266.16 mV | 266.16 mV ✅ |
    | Parts(j)-(n) | 미진행 | 미진행 ✅ |

- Calculated 재계산: PASS

    실측값: R_s = 103.1 Ω, V_Rs(DMM) = 266.16 mV, V_L = 1 V(p-p), f = 2 kHz, L = 10 mH

    | 항목 | 재계산 | 결과보고서 |
    |---|---|---|
    | V_Rs(peak) = 266.16 mV × √2 | 376.41 mV | 376.4 mV ✅ |
    | V_Rs(p-p) = 2 × 376.41 mV | 752.82 mV | 752.8 mV ✅ |
    | I_p-p = 752.82 mV / 103.1 Ω | 7.3018 mA | 7.302 mA ✅ |
    | X_L(meas.) = 1 V / 7.3018 mA | 136.95 Ω | 136.9 Ω ✅ |
    | X_L(calc.) = 2π×2000×10mH | 125.664 Ω | 125.7 Ω ✅ |
    | L = 136.9/(2π×2000) | 10.895 mH | 10.90 mH ✅ |

- %(Difference) 계산: 해당 없음 (교재 Table 3.4에 %(Difference) 열 없음)

---

### 발견된 오류 목록

- 없음

---

최종 판정: PASS
