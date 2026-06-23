---
name: create-measurement-checklist
description: 기초전기실험 프로젝트 안에서 동작하는 프로젝트 스킬. 실험 전에 그 주차의 모든 Table 을 순서대로 나열하고 각 셀에 `[측정]` / `[계산]` / `[환산]` 라벨과 예상값을 붙여 학생이 실험실에서 무엇을 직접 측정해야 하고 어느 정도 값이 나와야 하는지 한눈에 보게 해준다. 책 표 양식(column-major / column-major-paired / row-major / single-row)을 보존해 Calc/Meas 두 컬럼 구조도 그대로 렌더한다. HTML + PDF 한 쌍을 `<주차>\output\` 에 생성한다. 사용자가 "측정 체크리스트", "이번 실험에서 뭐 측정해야 해", "11주차 측정 항목 미리 알려줘", "/create-measurement-checklist" 등을 호출할 때 사용한다.
---

# create-measurement-checklist

실험에 들어가기 전에 그 주차의 모든 Table 을 순서대로 나열하고, 각 셀에 **`[측정]`** / **`[계산]`** / **`[환산]`** (= 측정값에서 도출한 derived value) 라벨 + **예상값**을 붙여 실험실에서 즉시 "이 값이 이론대로 나오는가" 비교할 수 있게 해주는 스킬이다. 책 표 헤더가 `Calculated | Measured` 처럼 짝지어진 양식도 그대로 보존한다 (table_shape 메타 참조). 출력은 미니멀 모노크롬 A4 디자인의 `<N>주차_측정체크리스트.html` 과 같은 폴더에 떨어지는 `.pdf` 한 쌍.

이 스킬은 이 프로젝트(`C:\Users\Hyunjun\Desktop\현준대학\기전실`) 안에서만 동작한다. cwd 가 다른 프로젝트로 바뀌면 자동 트리거되지 않는다.

## 0. 부트스트랩 (완료된 상태로 가정)

이 SKILL.md 가 존재한다는 것은 `<프로젝트>\.claude\skills\create-measurement-checklist\` 가 이미 만들어졌다는 뜻이다.

## 1. 입력 해석 (인자 필수)

`ARGUMENTS` 를 반드시 받는다. 비어 있으면 한 줄 안내 후 종료:
> 검토할 주차를 인자로 주세요. 예: `/create-measurement-checklist 11주차`

해석 규칙:
- 인자가 `N주차` 토큰 → 프로젝트 루트(=cwd 에서 상위로 올라가며 `.claude\` 가진 가장 가까운 디렉토리) 아래의 `<N주차>` 폴더를 `WEEK_DIR` 로 사용. 폴더 부재면 거절.
- 인자가 디렉토리 경로 → 그 디렉토리를 `WEEK_DIR` 로 사용 (이름이 `N주차` 형태면 OK).
- 그 외 거절.
- 인자에 `refresh` 가 포함되면 `요구목록.md` 캐시 무시하고 강제 재생성.

## 2. 참고자료 (소스) 디스커버리

`WEEK_DIR` 에서 다음 패턴을 순서대로 찾아 발견된 항목을 `SOURCES` 로 수집한다. 모든 항목이 비어 있으면 거절. 하나라도 있으면 진행.

| 우선순위 | 패턴 | 비고 |
|---|---|---|
| 1 | `<WEEK_DIR>\output\*예비보고서*.md` | §2.1 의 단일 우승 파일만 사용 |
| 2 | `<WEEK_DIR>\책\` 또는 이미지 ≥3장인 다른 폴더의 `*.jpg`/`*.jpeg`/`*.png` | |
| 3 | `<WEEK_DIR>\강의노트\*.pdf` 또는 `<WEEK_DIR>\*강의노트*.pdf` | 폴더 없으면 루트의 PDF |
| 4 | `<WEEK_DIR>\*참고노트*.pdf` 또는 `<WEEK_DIR>\*정리노트*.pdf` | 주차마다 둘 중 하나만 있음 |

명시 **제외** (이론값 회귀 방지):
- `pre_review*.md`, `pre_review_theory*.md`, `result_review*.md`, `*결과보고서*.md`

`<WEEK_DIR>\output\` 폴더가 없으면 먼저 생성한다.

### 2.1 예비보고서 단일 우승 규칙
`*예비보고서*.md` 다중 매치 시:
1. `ver\d+` 또는 `v\d+` 가 있으면 최대 버전.
2. 그 외 mtime 최신.
3. `(수정본)`/`_final`/`_최종` 동률 우선.

## 3. 요구목록(정답지) 해결 — 스키마 v5 공유

`<WEEK_DIR>\측정체크리스트\요구목록.md` 가 다음 조건 중 하나라도 만족하면 **재생성**:
- 파일 부재.
- 인자에 `refresh` 포함.
- 첫 줄에 `<!-- SCHEMA: v5 -->` 태그 부재 (v4 이하 구 캐시).
- 헤더 `<!-- SOURCES -->` 블록의 어떤 소스든 (a) 파일 시스템에서 사라졌거나 (b) mtime 이 더 최신.
- 디스커버리에서 잡힌 새 소스가 헤더에 기록되지 않은 경우.

`check-lab-measurements` 스킬도 동일한 v5 스키마를 읽으므로 캐시는 양쪽이 공유한다. v4 이하 캐시는 v5 빌더에서 빌드 실패시키고, 다음 호출에서 `refresh` 로 재생성한다.

표의 모든 셀은 dependency graph 의 노드다. **Leaf** = 학생이 손으로 적는 raw 측정(`measured`, `independent | measured: true`, `측정 입력 (공통)`, `inputs-by-row`). **Internal** = leaf 로부터 환산되는 `derived`. **External** = 표 밖에서 결정되는 `computed`/`fixed`/`graph-lookup`. 학생이 실험실에서 "지금 무엇을 측정해야 하는가"의 답은 항상 leaf 셀들이다.

### 3.1 v5 스키마

v4 대비 변경점:
- **환산 입력 dependency 의무화**: `kind: derived` 는 raw 입력 source 를 반드시 가져야 한다. source 는 `측정 입력 (공통)`, `inputs-by-row`, sibling measured column, `inputs: same-row`, `inputs: measured-rows`, `inputs: graph-lookup` 중 하나다.
- **행별 kind 지원**: row-major 표처럼 한 컬럼 안에 직접 측정 행과 환산 행이 섞이면 `kind-by-row:` 로 effective kind 를 행 순서대로 지정한다.
- **파서 안전성**: `|Z_Th|` 같은 물리량 표기의 `|` 는 필드 구분자가 아니다. 필드 구분은 ` | kind:` 처럼 known key 앞에서만 발생한다.

```markdown
<!-- SCHEMA: v5 -->
<!-- SOURCES
<상대경로 1> | <mtime epoch>
<상대경로 2> | <mtime epoch>
... -->

# 요구목록 — <주차>

## AC <N>
### Part <N>
#### Table <N.N>   (해당하는 경우)
- 표 양식: <column-major | column-major-paired | row-major | single-row>
- 회로 모형: <한 줄 설명>
- 고정조건:
  - <기호> = <값> <단위> (nominal | measured | calc)
  - ...
- 측정 입력 (공통):       (모든 derived row 가 같은 raw 입력 집합을 공유할 때)
  - <기호> [<단위>] | tool: <DMM|Oscilloscope|...> | expected: <값> | confidence: <상|중|하>
- 독립변수: <기호> = [<값1>, <값2>, ...] <단위>     (row-major 면 측정대상 리스트)
- 컬럼:
  - <기호> [<단위>] | kind: independent
  - <기호> [<단위>] | kind: independent | measured: true                       (R-class 가 row 변수일 때)
  - <기호> [<단위>] | kind: measured | tool: <DMM|Oscilloscope|함수발생기|...> | expected: <값1>, <값2>, ... | confidence: <상|중|하>
  - <기호> [<단위>] | kind: derived | inputs-by-row: <입력1>; —; <입력3> | tool: <환산 출처 한 줄> | formula: <식 문자열> | expected: <값1>, <값2>, ...
  - <기호> [<단위>] | kind: derived | inputs: measured-rows | kind-by-row: measured; derived; measured | tool: <...> | formula: <...> | expected: <...>
  - <기호> [<단위>] | kind: derived | inputs: graph-lookup | tool: <그래프 출처> | formula: <식 문자열> | expected: <값>
  - <기호> [<단위>] | kind: derived | kind-by-row: measured; derived; computed | tool: <...> | formula: <...> | expected: <...>
  - <기호> [<단위>] | kind: computed | formula: <식 문자열>
  - <기호> [<단위>] | kind: fixed | value: <값>   (표 안에 박힌 고정값일 때만)
```

규칙:
- `kind` 5상태: `independent` (행 라벨) / `measured` (실측 빈칸) / `derived` (환산 빈칸, Meas 컬럼) / `computed` (식으로 채움) / `fixed` (표 안에 박힌 고정값).
- `table_shape:` 가 누락되면 빌더가 `column-major` 로 fallback 하지만, 신규 카드는 명시할 것. row-major / column-major-paired / single-row 표는 반드시 명시.
- `independent` 컬럼은 `measured: true` 플래그 **외** 다른 필드 (`expected:`, `confidence:`, `tool:`, `formula:`, `value:`) 를 **부착 금지**. nominal 값의 단일 진실원은 같은 Table 의 `독립변수:` 줄 이다.
- `measured` / `derived` 컬럼은 `expected: 값1, 값2, ...` 를 반드시 가진다. 순서는 `독립변수` 리스트(또는 측정대상 리스트)와 동일.
- **`derived` 의 raw input source 는 필수다.** 다음 중 하나도 없으면 빌더는 `BuildError` 로 실패한다: 표 레벨 `측정 입력 (공통)`, 컬럼 `inputs-by-row`, 공식 토큰과 sibling measured column 자동 매칭, `inputs: same-row`, `inputs: measured-rows`, `inputs: graph-lookup`.
- `inputs-by-row:` 는 한 줄에서 `;` 로 행을 구분한다. 빈 행은 `—` 로 쓴다. 예: `V_R_L@FIG12.5 [V] @ Oscilloscope → 1.480 [상]; —; E_oc [V] @ Oscilloscope → 2.933 [상]`.
- `kind-by-row:` 는 한 컬럼 안에서 행별 effective kind 가 다를 때만 쓴다. 값 개수와 행 개수는 같은 순서여야 한다.
- `inputs: measured-rows` 는 row-major 표의 같은 컬럼 안에서 일부 행이 raw measured leaf 이고 나머지 행이 그 measured 행들에서 환산될 때 쓴다.
- `derived` 의 `formula` 는 환산 공식(예: `V_Rs(meas)/R_s(meas) ≈ 7.52`). 학생이 결과보고서에서 채울 때 참조한다.
- `expected` 가 단일 값(독립변수에 무관)이면 한 개만 적는다.
- `confidence` 는 예상값 신뢰도 (`상`/`중`/`하`). 회로 모형·파라미터가 모두 명확하면 상, 한두 값 가정하면 중, 정성적이면 하. `independent | measured: true` 의 기본 신뢰도는 항상 `상` 으로 간주 (별도 표기 없음).
- `고정조건:` qualifier 4상태: `(nominal)` (명판값), `(measured)` (DMM/FG-counter 등으로 실측), `(calc)` (다른 nominal 로부터 계산), qualifier 없음 (장비 설정 등). sub-qualifier (예: `(nominal sensing)`, `(measured by Frequency Counter)`) 는 두지 말고 단일형으로 정규화.

마이그레이션 정책:
- v4 이하 캐시는 v5 빌더에서 빌드 실패한다.
- 다음 호출에 `refresh` 가 있거나 schema 태그가 v5 미만이면 강제 재생성한다.
- 기존 11/12주차 캐시는 follow-up 에서 수동 마이그레이션하거나, 사용자가 해당 주차를 `refresh` 로 호출해 v5로 재생성한다. 10주차는 기존 측정체크리스트 캐시가 없으므로 신규 생성 시 v5로 만든다.

### 3.2 자동 생성 절차
`SOURCES` 를 읽어 위 스키마로 작성한다. **소스 읽기는 §3.3 의 토큰 효율 워크플로를 따른다** — 책 이미지·PDF를 main 컨텍스트에 직접 쌓지 말고 서브에이전트가 구조만 전사하게 하며, 소자값·`E_s` 등 핵심 스칼라만 main 이 직접 확인한다. 작성 시 박을 룰:
1. **책 사진이 가장 권위 있는 출처.** 강의노트·예비보고서가 책과 충돌하면 책 우선.
2. 예비보고서의 수치(이론 풀이)는 정답지에 옮기지 말 것. 구조(어떤 항목을 측정해야 하는가)만 가져온다.
3. **예상값 계산**: 회로 모형과 고정조건/공칭값을 사용해 이론식으로 계산. 잡음·오차는 부여하지 않는다 (예상값이므로 깔끔한 이론값). 유효숫자는 측정 도구 분해능에 맞춤 (DMM mV → 소수 둘째 자리, V → 셋째 자리).
4. 단위 SI 원본 유지 (mV/V/Hz/kHz/Ω).
5. **R-class 정규화 (v3 신규 룰)**: R-class 부품값 (R, R_s) 은 책의 실험 절차상 항상 DMM 저항 모드로 실측한 뒤 회로에 사용한다 → `(measured)` qualifier 부착. C, L 은 nameplate 값만 쓰므로 `(nominal)` 유지. R-class 가 `독립변수:` 로 등장하면 그 컬럼에 `| measured: true` 플래그 부착. sub-qualifier (sensing, internal 등) 는 단일 `(measured)` 로 정규화. 예시 3개:
   - `R = 1 kΩ (nominal)` → `R = 1 kΩ (measured)`
   - `R_s = 10 Ω (nominal sensing)` → `R_s = 10 Ω (measured)`
   - `L = 10 mH (nominal, R_l ≈ 0 가정)` → 변경 없음 (R_l 은 본 스코프 외)
6. **f / 그 외**: 본 PR 의 create-checklist 입력측 룰은 R-class 만 다룬다. f 의 `(measured)` 일관성 정리는 후속 PR. (단, 이미 `(measured by Frequency Counter)` 같이 박힌 라인은 §3.1 의 sub-qualifier 정규화 룰을 적용해 단순 `(measured)` 로 줄인다.)
7. **표 양식 분류 (v4 회귀 방지 핵심)**: 책 사진의 각 Table 헤더를 글자 단위로 옮겨와 매핑하고 `table_shape:` 메타를 명시한다. **헤더 우선 (B.7) → 절차문 보조 (B.8) 순서**로 판정한다.
   - 헤더에 `Calculated` 와 `Measured` 가 **인접 페어로 같은 측정대상에 대해 반복** 되면 (예: V_R Calc · V_R Meas · θ_1 Calc · θ_1 Meas) → `column-major-paired`. 행은 독립변수 값(또는 단일행), 각 측정대상마다 Calc 컬럼(`kind: computed`) + Meas 컬럼(`kind: measured` 또는 `derived`) 한 쌍.
   - 헤더가 정확히 두 컬럼 `Calculated | Measured` 이고 행이 측정대상(I_s, I_L, V_Rs 등)이면 → `row-major`. 컬럼 2개: Calc(`kind: computed`, 행별 formula), Meas(`kind: measured` 또는 `derived`, 행별 tool/expected).
   - 헤더가 측정 항목들(V_R, V_C, D_1, D_2, θ 등)이고 행이 R 값 같은 독립변수면 → `column-major`.
   - 단일행이면 → `single-row`.
   - 분류 후 책 표 헤더와 카드의 `<th>` 라벨이 1:1 매칭되는지 self-check. row-major / paired 케이스를 column-major 단일 형태로 환원하지 말 것 (이전 회귀의 핵심 원인).
8. **derived vs measured 판정**: 책 절차문의 동사로 판정한다 (룰 7 의 헤더 분류가 모호할 때 보조).
   - "measure ... and record in Table" → `kind: measured` (오실로스코프/DMM 으로 빈 칸 직접 읽기).
   - "calculate ... using the measured value of X ... and insert in second column" (Meas 컬럼에 들어가지만 환산값) → `kind: derived`. `tool:` 에 환산 출처(예: `V_Rs(meas)/R_s(meas)`), `formula:` 에 식, `expected:` 에 이론 예측치.
   - 책의 "Calculated" 컬럼은 항상 `kind: computed` (nameplate 기반 이론값).
9. **R-class 측정 일관성**: 같은 AC 챕터에서 R 값(R, R_s)이 여러 표에 걸쳐 반복 사용되면 **챕터 첫 표 직전에 별도 "Resistor Measurements" 카드** 를 두어 R 의 DMM 측정을 한 번에 받는다. 후속 표들의 `고정조건:` 줄은 `R = 1 kΩ (measured)` 로 표기. 한 표 안에서만 R 이 독립변수로 변하면 그 표에 R meas. 컬럼 직접 추가 (column-major-paired 의 경우).
10. **환산 셀 추출 워크플로**:
   - 절차문에서 "calculate ... using the measured value of X" 패턴을 발견하면 해당 셀을 `kind: derived` 후보로 표시한다.
   - X(raw 입력)를 같은 행의 sibling column 에서 찾는다. 있으면 sibling 모드로 두고 별도 메타를 추가하지 않는다.
   - sibling 이 없으면 절차문에서 X 를 어떤 회로/도구로 측정하는지 찾아 `(symbol, unit, tool, expected, confidence)` 5튜플을 만든다.
   - 같은 표의 모든 derived row 가 동일 5튜플 집합을 참조하면 표 레벨 `측정 입력 (공통):` 에 한 번만 기록한다.
   - 행마다 입력이 다르면 `inputs-by-row:` 에 행 순서대로 기록한다.
   - 그래프에서 읽는 값은 `inputs: graph-lookup` 을 명시한다.
   - 한 컬럼 안에서 직접 측정/환산/계산 행이 섞이면 `kind-by-row:` 로 effective kind 를 행별 지정한다. 같은 컬럼의 measured 행을 raw 입력으로 쓰는 derived 행은 `inputs: measured-rows` 를 함께 명시한다.
   - self-check: 빌더 lint 를 정신적으로 시뮬레이션한다. source 없는 derived 가 남아 있으면 위 단계를 다시 수행한다.

### 3.3 토큰 효율 워크플로 (인제스트·검증)

**배경.** 한 번 생성에 책 이미지(20장 ≈ 49k), 강의노트 PDF(≈30k), 예비보고서 PDF(≈60k), 산출 PDF 시각 재독(≈42k)이 main 컨텍스트를 ~300k 까지 채운 회귀가 있었다. vision 이 약 60%. 아래 워크플로로 main 점유를 **~120–140k (약 55%↓)** 로 줄인다. (서브에이전트도 이미지를 읽으므로 총 $ 비용 감소폭은 더 작다 — 줄이는 대상은 **main 컨텍스트 창**이다.)

1. **소스 인제스트 = 서브에이전트 구조 전사.** 책 이미지 + 강의노트 PDF 를 `Agent`(general-purpose) 서브에이전트 1개에 넘겨 **구조 digest 텍스트만** 받는다. 이미지·PDF는 서브에이전트 컨텍스트에 머물고 main 에는 digest(~6–10k)만 들어온다. digest 출력 스키마(엄격):
   - 표별: 헤더 라벨 **글자 그대로**, `table_shape` 힌트(§3.2 룰7), 독립변수/주파수 **전체 리스트**(누락 금지), 컬럼별 `{kind 후보, tool, 절차문 동사(measure/calculate)}`.
   - 소자 명판값(R·L·C·R_s …), `E_s`/`V_i`, **책↔강의노트 충돌**(예: E 10Vpp→5Vpp override).
   - `unresolved_from_book[]` — 책만으로 못 푸는 모호점(예: "R_s 정체 불명").
   서브에이전트는 **읽기/전사만**; 예상값 계산·스키마 조립은 main 이 한다(서브 오류 표면 축소).
2. **핵심 스칼라는 main 이 직접 확인.** 모든 계산값을 좌우하는 소자값·`E_s`·주파수 범위는 digest 를 그대로 믿지 말고, main 이 **setup/절차 단일 페이지**(강의노트의 소자·전압·주파수 슬라이드 1장)만 직접 Read 해 확정한다(≈2–3k). 추가로 digest 의 `L/C` 로 anchor 주파수(`f_p`/`f_c`/`f_s`)를 재계산해 digest 표기와 일치하는지 확인한다(서브 오독 자기검출).
3. **예비보고서 PDF 는 조건부.** §2 정식 SOURCE 아님 → **기본 미독**. digest 의 `unresolved_from_book[]` 이 비어있지 않을 때만, 2차 서브에이전트가 보고서의 **해당 페이지만**(브레드보드 그림 페이지 제외) 읽어 회로 모호성을 해소한다. 보고서 **수치는 정답지로 옮기지 않는다**(§3.2.2) — 구조 확인용.
4. **예상값 = compute 스크립트 (손복사 금지).** ~100 개 예상값을 stdout 에서 손으로 캐시에 옮기지 말 것. 주차별 `<WEEK_DIR>\측정체크리스트\_compute_expected.py` 를 작성·실행해 `_expected.json`(값 source of truth) + 캐시용 `expected:` 라인을 출력하고, 그 라인을 그대로 `요구목록.md` 에 넣는다. JSON 키는 캐시 table code · 컬럼명(단위 제거)과 정확히 일치시킨다.
5. **검증 = 프로그래매틱 + 스모크 1쪽 (PDF 재독 금지).** 빌드 후 `python .claude\skills\create-measurement-checklist\_verify_checklist.py "<WEEK_DIR>"` 를 돌린다. 검사: 캐시 v5 파싱·검증 / measured·derived `expected` 길이 == 행수(누락 셀) / 캐시 `expected` == `_expected.json`(손복사·오독) / anchor == 고정조건 / HTML 스모크(카드수, `예상` 셀수 == measured+derived). **PASS 면 산출 PDF 는 보지 않는다**; 레이아웃 확인이 필요하면 **최대 1쪽만** Read. (이전 회귀: 8회 호출로 21쪽 재독 ≈ 42k 낭비.)
6. **대형 주차 옵션.** 표가 많으면(예: 2개 AC 챕터) 인제스트를 챕터별 2개 병렬 서브에이전트로 분할해 단일 컨텍스트 후미 품질 저하를 막는다.

## 4. HTML 렌더 (`template.html`)

`<프로젝트>\.claude\skills\create-measurement-checklist\template.html` 의 플레이스홀더를 치환해 작성.

### 4.1 문서 구조
- A4 (210×297mm), 12mm 여백, 미니멀 모노크롬, `make-lab-report-cover` 와 동일 폰트 스택(Pretendard / Malgun Gothic).
- 헤더: `<주차> · 측정 체크리스트`, 우상단에 생성일.
- 본문 상단 요약 박스:
  - 총 Table 수, 측정 셀 수, computed 셀 수, **derived 셀 수 (환산)**, fixed 셀 수, 사용 기기 리스트. `측정`은 학생이 손으로 적는 모든 빈 칸의 합이다: `measured` 셀 + `independent | measured: true` 셀 + `측정 입력 (공통)` + `inputs-by-row`.
  - 우승 예비보고서 파일명 (있으면).
- 각 Table = 카드 한 장. **atomic 단위는 카드 전체가 아니라 `tbody tr` (행).** `card-head` / `card-meta` 에는 `break-after: avoid` 를 걸어 첫 행과 결합되도록 둔다. `.card` 자체에 `page-break-inside: avoid` 를 다시 걸지 말 것 — 큰 카드가 통째로 다음 페이지로 밀려 직전 페이지에 흰 공간이 누적되는 회귀가 발생한다 (검증 완료, A4 가로 9페이지 → 8페이지).
  - 카드 헤더: `AC N · Part N · Table N.N — <회로 모형>`
  - 메타 라인: `고정조건: …` / `독립변수: …`
  - HTML `<table>` (`table_shape:` 별 행/열 의미가 다름):
    - `column-major` (default): 행 = 독립변수 값마다 1행 (독립변수가 없으면 단일 행), 열 = 컬럼 리스트 순서.
    - `column-major-paired`: 같은 측정대상마다 Calc·Meas 두 컬럼을 인접 배치. 행은 column-major 와 동일.
    - `row-major`: 행 = 측정대상(`rows=["I_s(p-p)", "V_Rs for I_s", ...]`), 열 = Calc(`computed`) + Meas(`measured` 또는 `derived`). 행별로 다른 formula/tool/expected 가 필요하므로 빌더가 `formula: list[str]` / `tool: list[str]` / `expected: list[...]` 의 row_idx 분기를 지원.
    - `single-row`: 단일행 종합표. `rows=["—"]`.
    - `independent` 셀: 회색 텍스트, 값 표시.
    - `independent | measured: true` 셀: 회색 텍스트 + 좌상단 검정 `측정` 배지 (measured 셀과 동일 스타일 — `badge-measure` 재사용) + 그 옆에 작게 `예상 1.0 [상]` 라벨. nominal 값은 `독립변수:` 줄에서, 신뢰도는 항상 `상` (§3.1 규칙). 카드 푸터의 `측정 셀` 합계에 포함.
    - `measured` 셀: 흰 배경 + 좌상단 검정 `측정` 배지 + 그 옆에 작게 `예상 412 mV [상]` 형태. 측정값을 적을 빈 공간(`____ mV`)이 셀 본체.
    - 공통 입력 패널: `card-meta` 와 본문 `<table>` 사이에 `<div class="card-inputs">` 를 둔다. 헤더는 "직접 측정 입력 (모든 환산 행 공통)". 각 entry 는 오렌지 `입력` 배지 + 측정 위치 + 빈 칸 + 예상값으로 렌더하고 카드 푸터의 `측정` 합계에 포함한다.
    - `derived` 셀: 옅은 하늘 배경(`#eef4fa`) + **좌측 4px solid 회청 보더** (B&W 인쇄에서도 식별 단서로 잔존) + 좌상단 회청 `환산` 배지 + 식 + 빈 칸. shared 모드는 작은 `↑ 공통 입력 참조`, per-row 모드는 상단 `input-strip`, sibling 모드는 `↑ <col-name> 셀`, graph 모드는 `그래프 읽기` 라벨을 표시한다. 카드 푸터의 `환산 셀` 합계에 포함.
    - `computed` 셀: 옅은 회색 배경 + 좌상단 회색 `계산` 배지 + 식을 작은 글씨로 셀 안에 표기.
    - `fixed` 셀: 옅은 노란 음영 + `고정` 배지 + 값 표시.
  - 카드 푸터: `측정 N · 계산 M · 환산 D · 고정 K`. `측정`은 실제로 학생이 적어야 하는 raw 입력 빈 칸 수다.
- 문서 푸터: 사용한 소스 파일 목록(상대경로) + 생성 일시.

### 4.2 긴 식 폴백
컬럼 폭(평균 30mm) 초과 위험이 있는 식(>40자)은 셀 안에는 기호만 두고, 카드 하단 별도 "식 정의" 박스로 분리:
```
식 정의:
  V_Rs(p-p) = V_Rs(DMM) · 2√2
  Z         = V_L(p-p) / V_Rs(p-p) · R_s
```

## 5. 출력 파일

- `<WEEK_DIR>\측정체크리스트\<N>주차 측정체크리스트.html`
- `<WEEK_DIR>\측정체크리스트\<N>주차 측정체크리스트.pdf`
- 빌더 스크립트(`_build_checklist.py`, `_html_to_pdf.py`)와 캐시(`요구목록.md`)도 같은 폴더에 둔다. 사용자 입력물(`output\측정값.md`, `output\*예비보고서*.md` 등)은 `output\` 폴더에 그대로 둔다 — 분리된 구조.
- 검증 스크립트 `_verify_checklist.py` 는 skill 폴더에 둔다(범용·재사용). 주차별 `_compute_expected.py` 와 그 산출 `_expected.json`(값 source of truth·회귀 가드)은 `<WEEK_DIR>\측정체크리스트\` 에 둔다.
- 두 파일 모두 이미 있으면 **별도 확인 없이 덮어쓴다** (본인 산출물, 비파괴적).

## 6. PDF 변환

**Playwright + Chromium** 사용. Edge 헤드리스의 `--print-to-pdf` 는 `--no-pdf-header-footer` / `--print-to-pdf-no-header` 같은 플래그를 모두 무시하고 상단(날짜·제목) / 하단(file:// 경로·페이지 번호) 머릿글을 항상 박아 넣는다 — 검증 완료. Playwright 의 `page.pdf(display_header_footer=False)` 만이 깨끗한 출력을 보장한다.

```python
from playwright.sync_api import sync_playwright
from pathlib import Path

def html_to_pdf(html_path: Path, pdf_path: Path):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(html_path.resolve().as_uri(), wait_until="load")
        page.pdf(
            path=str(pdf_path),
            format="A4",
            print_background=True,
            display_header_footer=False,
            prefer_css_page_size=True,  # template.html 의 @page 규칙 존중
        )
        browser.close()
```

playwright 없으면 (`pip show playwright`) HTML 만 살리고 에러 노출. 첫 실행 시 `python -m playwright install chromium` 필요할 수 있음.

산출 결과 검증은 §3.3-5 의 `_verify_checklist.py`(프로그래매틱)로 하고, **산출 PDF를 여러 쪽 재독하지 않는다** — 레이아웃 스모크가 필요하면 1쪽만 본다.

## 7. 실행 절차

1. `ARGUMENTS` 파싱 → `WEEK_DIR` 확정, 빈 인자/잘못된 주차면 거절.
2. `<WEEK_DIR>\측정체크리스트\` 없으면 생성. (`<WEEK_DIR>\output\` 은 §2 디스커버리에서 별도 확인.)
3. `SOURCES` 디스커버리 (§2). 0개면 거절.
4. `요구목록.md` 신선도 검사 (§3). 재생성이 필요하면 **§3.3 토큰 효율 워크플로**로:
   - (a) 서브에이전트로 소스 **구조 digest** 수집 (이미지·PDF를 main 에 쌓지 않음).
   - (b) main 이 강의노트 setup **1쪽**을 Read 해 소자값·`E_s`·주파수 범위 확정 + anchor 자기검사.
   - (c) digest 의 `unresolved_from_book[]` 이 있으면 2차 서브에이전트로 예비보고서 **타겟 페이지만** 확인.
   - (d) digest+스칼라로 v5 `요구목록.md` 작성. 예상값은 `_compute_expected.py` 로 계산해 `_expected.json` + 캐시 라인 출력(손복사 금지).
5. `요구목록.md` 파싱 → `_build_checklist.py` 로 HTML 저장.
6. `_verify_checklist.py` 실행. FAIL 이면 원인 수정 후 5 로 복귀. **산출 PDF 시각 재독 금지 — 검증은 스크립트가 한다.**
7. Playwright(§6)로 PDF 변환. 레이아웃 확인이 필요하면 산출 PDF 를 **최대 1쪽만** 본다.
8. 두 파일 마크다운 링크 + 측정/계산 셀 수 한 줄 요약 출력 후 종료.

## 8. 스킬 파이프라인에서의 위치

| 시점 | 스킬 | 입력 | 출력 |
|---|---|---|---|
| 실험 전 (1) | **`create-measurement-checklist`** | 주차 | `측정체크리스트\요구목록.md` (v5 캐시) + 체크리스트 HTML/PDF |
| 실험 전 (2) | `create-measurement-template` | 요구목록.md | `output\측정값.md` 빈 템플릿 |
| 실험 후 | `fill-lab-measurements` | 측정값.md | `output\측정값_시뮬레이션.md` |

캐시(`<WEEK_DIR>\측정체크리스트\요구목록.md`, v5)는 `fill-lab-measurements` 와 공유된다. 본 스킬이 먼저 호출되면 풍부한 v5 스키마로 캐시가 채워져 fill 이 즉시 활용 가능하다.

## 9. 비-목표

- 회로도 SVG 렌더링 안 함 (회로 모형 한 줄 텍스트만).
- 측정값.md 자체를 만들거나 채우지 않는다 (실험 전).
- 추정값(잡음 첨가된 가짜 측정값)을 생성하지 않는다 — 본 스킬은 깔끔한 이론 **예상값**만 다룬다.
- 다중 주차 일괄 처리 안 함.
- 다른 프로젝트에서 동작하지 않는다.
- 디스커버리 0개 거절 — 자료가 빈약한 일부 주차(3·4·12주차 등)는 미지원.

## 10. 회귀 가드

- `kind: derived` 셀이 raw 입력 source 0개인 상태로 빌드되면 안 된다. 빌더는 표 레벨 `측정 입력 (공통)`, 컬럼 `inputs-by-row`, sibling measured match, `inputs: same-row`, `inputs: measured-rows`, `inputs: graph-lookup` 중 하나가 없으면 `BuildError` 를 던진다.
- skill 폴더의 `test_lint.py` 는 source 없는 derived mock table 이 실패하는지 확인한다.
- 빌드 후 `_verify_checklist.py` 가 PASS 해야 한다: `expected` 길이 불일치(누락 셀)·캐시↔`_expected.json` 값 불일치(손복사·서브에이전트 오독)·anchor 불일치·HTML 렌더 누락을 잡는다. 빌더 자체는 `expected` 길이·값을 검증하지 않으므로(`_row_value` 가 부족분을 조용히 빈 칸 처리) 이 스크립트가 그 공백을 메운다.
