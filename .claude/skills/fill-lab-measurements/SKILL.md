---
name: fill-lab-measurements
description: 기초전기실험 프로젝트 안에서 동작하는 프로젝트 스킬. `<주차>\output\측정값.md` 의 빈칸을 같은 Table 안의 다른 측정행과 조화로운 시뮬레이션 값으로 채워 별도 파일 `<주차>\output\측정값_시뮬레이션.md` 를 생성한다. 원본 측정값.md 는 절대 수정하지 않는다. 사용자가 "측정값 빈칸 채워줘", "10주차 측정값 시뮬레이션", "안 한 측정 메꿔줘", "/fill-lab-measurements" 등을 호출할 때 사용한다. 학습·디버깅 보조 도구이며 출력값을 그대로 보고서에 옮기는 용도가 아니다.
---

# fill-lab-measurements

`측정값.md` 의 빈칸 (`____`) 과 누락 행을 같은 Table 의 다른 측정행으로부터 캘리브레이션된 이론값에 잡음을 부여해 채운 별도 파일 `측정값_시뮬레이션.md` 를 생성한다. 원본 `측정값.md` 는 읽기 전용으로 다룬다. 출력 파일은 `측정값.md` 와 시각적으로 구분되지 않도록 작성된다 — 시뮬레이션 여부는 **파일명에서만** 식별 가능하며, 사용자가 직접 출처를 관리해야 한다. 출처·실패 정보는 실행 시 콘솔에만 출력되고 파일에는 어떤 흔적도 남지 않는다.

이 스킬은 이 프로젝트(`C:\Users\Hyunjun\Desktop\현준대학\기전실`) 안에서만 동작한다. cwd 가 다른 프로젝트로 바뀌면 자동 트리거되지 않는다.

## 0. 부트스트랩 (완료된 상태로 가정)

이 SKILL.md 가 존재한다는 것은 `<프로젝트>\.claude\skills\fill-lab-measurements\` 가 이미 만들어졌다는 뜻이다. 별도 부트스트랩 단계는 실행하지 않는다.

## 1. 입력 해석 (인자 필수)

`ARGUMENTS` 를 반드시 받는다. 형식:

```
/fill-lab-measurements <N주차 | *.md 경로> [expand-skipped] [overwrite] [refresh-formula]
```

비어 있으면 한 줄 안내 후 종료:
> 빈칸을 채울 주차 또는 `측정값.md` 경로를 인자로 주세요. 예: `/fill-lab-measurements 10주차`

해석 규칙:
- 첫 토큰이 `*.md` 로 끝나는 경로면 그 파일을 `MEAS_FILE` 로 사용 (파일명 무관). 부모 디렉토리를 `OUTPUT_DIR`, 그 위를 `WEEK_DIR` 로 잡는다.
- 첫 토큰이 `N주차` 패턴이면 `<프로젝트>\<N주차>\output\측정값.md` 로 해석. 파일 부재 시 한 줄 안내 후 종료 (자동 생성 안 함):
  > `<N주차>\output\측정값.md` 가 없습니다. 먼저 측정값을 기록하거나 다른 파일 경로를 인자로 주세요.

추가 토큰:
- `expand-skipped`: "실험을 진행하지 않았음" 같은 **블록 전체 부재 표지** 및 row 임베디드 부재 표지 (`최대치... 까지밖에`, `진행할 수 없었음` 등) 가 붙은 행도 채움. 단 row 임베디드의 경우 §6.6 의 sanity check 가 통과한 것만 채우고, 충돌하면 빈칸 유지 + 한 줄 경고.
- `overwrite`: 기존 `<OUTPUT_DIR>\측정값_시뮬레이션.md` 가 있을 때 백업 후 덮어쓰기 허용 (§7).
- `refresh-formula`: 이론식 캐시 `<WEEK_DIR>\측정체크리스트\이론식.md` 를 무시하고 강제 재생성.
- 그 외 토큰은 무시.

## 2. 요구목록.md 의존 — v4/v5 허용, v3 거절, 부재 시 ad-hoc

본 스킬은 누락 셀 탐지와 회로 모형 / 컬럼 kind 정보의 1차 출처로 `<WEEK_DIR>\측정체크리스트\요구목록.md` 를 사용한다. 스키마 버전이 프로젝트 내에서 통일되어 있지 않으므로 (11주차 v4, 12·13주차 v5, 10주차 부재) 다음 분기로 처리한다.

### 2.1 캐시 발견 + 버전 분기

`<WEEK_DIR>\측정체크리스트\요구목록.md` 첫 줄의 `<!-- SCHEMA: v? -->` 태그를 읽어:

- `v5` → **풀 기능 모드**. measured 컬럼의 `expected:` / `confidence:` 와 derived 컬럼의 `formula:` 를 모두 활용.
- `v4` → **부분 기능 모드**. measured 컬럼에 `expected:` 가 없을 수 있다 (v4 → v5 마이그레이션 전 캐시). 그 경우 §6 의 캘리브레이션이 측정행 0 개일 때 fallback 식을 §3 이론식 캐시에서 가져온다.
- `v3` 이하 또는 태그 부재 → 거절:
  > 요구목록.md 가 구 스키마(v3 이하)입니다. `/prep-measurement-checklist <주차> refresh` 로 v4 이상으로 갱신하세요.

### 2.2 캐시 부재 시 ad-hoc 요구목록 (인-메모리)

`측정체크리스트\요구목록.md` 가 아예 없는 경우 (예: 10주차 시범 사례) 다음 절차로 인-메모리 ad-hoc 요구목록을 만든다. 파일로는 저장하지 않는다 (cache owner 는 prep-checklist).

1. `WEEK_DIR\책\*.{jpg,jpeg,png}` 와 `OUTPUT_DIR\*예비보고서*.md` 를 찾는다 (create-measurement-checklist §2 디스커버리 규칙과 동일 — `pre_review*.md`, `result_review*.md`, `*결과보고서*.md` 는 제외).
2. 둘 다 부재면 거절:
   > 요구목록.md 도 없고 책/예비보고서도 못 찾았습니다. 본 스킬은 회로 모형 정보 없이는 실행할 수 없습니다.
3. 발견된 자료를 Read (이미지는 비전) 로 읽어 create-measurement-checklist §3.1 의 v5 스키마와 동일한 구조를 **메모리 안에서만** 만든다. expected 값을 못 산출하면 그 컬럼은 `expected: -` 로 두고 §6 의 0-row 분기를 강제한다.
4. ad-hoc 사용 사실을 출력 보고서 헤더와 한 줄 요약에 명시한다 (`이번 실행은 ad-hoc 요구목록을 사용했습니다 — 정확도가 캐시 기반보다 떨어질 수 있습니다`).

### 2.3 측정값.md 부재 표지 처리

`측정값.md` 본문에서 다음 표지는 **자동으로 fill 제외 후보**로 분류한다:

| 표지 | 적용 범위 | 기본 동작 | `expand-skipped` 적용 시 |
|---|---|---|---|
| `- 실험을 진행하지 않았음.` (Part / AC heading 직속 단일 줄) | 해당 블록 전체 | fill 제외, 원본 보존 | 블록 안의 요구목록 행을 모두 채움 |
| row 안 임베디드: `최대치... 까지밖에`, `올라가지 않아 실험을 진행할 수 없었음`, `진행 안 함`, `측정 안 함` | 해당 row 1줄 | fill 제외, 원본 보존 | §6.6 의 sanity check 통과 시에만 채움 |

row 임베디드 부재 표지가 있는 행은 같은 Table 의 다른 행들이 정상 측정되어 있어도 그 행만 빠진다. 이를 **자동 fill 대상에서 분리**해 학생이 직접 관측한 물리적 한계를 보존하는 것이 본 스킬의 핵심 가드레일이다.

## 3. 이론식 캐시 `이론식.md`

measured 컬럼의 forward 식 (예: V_Rs = V_L · R_s / (2πfL · √(...))) 은 요구목록.md (v4/v5 어느 쪽이든) 에 담기지 않는다. 본 스킬이 **별도 캐시 `<WEEK_DIR>\측정체크리스트\이론식.md` (v1 스키마)** 를 관리한다.

### 3.1 캐시 스키마 v1

```markdown
<!-- SCHEMA: v1 -->
<!-- REQS_HASH: <요구목록.md 의 sha256 앞 12자> -->
<!-- REQS_MTIME: <요구목록.md mtime epoch> -->
<!-- GENERATED: <ISO timestamp> -->

# 이론식 — <주차>

## AC <N>
### Table <N.N>
- 회로 모형: <한 줄>
- 미지 파라미터: [<sym1>, <sym2>, ...]    <!-- least-squares fit 의 자유도. 없으면 [] -->
- domain 제약:
  - <sym>: <한 줄> (예: L > 0, R_s ≥ nominal × 0.9)
- forward 식:
  - <target_sym>: <식 문자열, Python 표현식 가능. f, R, L, C, ... 를 변수로>
- 단위 sanity:
  - <target_sym>: <expected SI unit, 예: V, mV, A>
```

### 3.2 신선도 검사

- `이론식.md` 부재 → 재생성.
- `refresh-formula` 토큰 → 재생성.
- `REQS_HASH` 가 현 요구목록.md 의 sha256 앞 12자와 다르거나 `REQS_MTIME` 이 더 옛날 → 재생성.
- ad-hoc 요구목록 (§2.2) 이면 캐시 사용·저장하지 않고 매번 LLM 유도 (파일로 저장 안 함).

### 3.3 생성 절차

요구목록의 각 Table 에 대해:

1. `회로 모형` + 고정조건 + 컬럼 정의를 LLM 프롬프트에 넘겨 forward 식을 유도. 책 이미지가 SOURCES 에 있으면 추가 컨텍스트로 첨부.
2. LLM 응답을 다음 sanity check 로 검증:
   - **단위 일관성**: 식에 들어가는 변수의 SI 단위를 대입했을 때 target 단위와 매칭되는지.
   - **극한 거동**: f → ∞ 또는 f → 0 일 때 식이 발산/0 으로 자연스럽게 가는지.
   - **요구목록 expected 일치**: v5 의 expected 값 중 1 개라도 있으면 그 (independent, target) 대입 결과가 expected 의 ±10% 이내인지.
3. sanity 실패 → 한 번 재유도. 두 번째도 실패 → 이 Table 은 `미지 파라미터: [], forward 식: <UNRESOLVED>` 로 캐시에 기록하고 §6 에서 항상 0-row fallback (순수 이론 불가 → 빈칸 유지 + 한 줄 경고).
4. sanity 통과 → 캐시 저장.

### 3.4 비-목표

- SPICE / numerical solver 호출 안 함.
- 자기/상호 인덕턴스, 비선형 소자, 트랜지스터 — 본 캐시 스코프 밖. 이런 회로가 등장하면 `<UNRESOLVED>` 처리.

## 4. 측정값.md 파싱 (Pass A)

`측정값.md` 를 헤더 단위 (`# AC N` / `## Part N` / `### Table N.N`) 로 블록 분할한 뒤 각 블록 안의 행을 다음 패턴으로 추출. **빈칸 보존**을 위해 원본 문자열도 함께 저장한다 (출력 렌더링용).

각 추출 항목은 다음 구조:

```python
ParsedRow:
  raw_line: str             # 원본 한 줄 (출력 시 사용)
  block: (AC, Part, Table)
  symbol: str               # 예: V_Rs(DMM)
  independent: {sym: str, value: float, unit: str} | None
  value: float | None       # None = 빈칸 (____ 잔존) 또는 부재
  unit: str | None
  measured_qualifier_blank: bool   # (실측 = ____) 패턴 — value/unit 와 별개
  absence_marker: 'block' | 'row' | None
  decimal_places: int | None       # 측정값이 있을 때 원본 자릿수
```

분류:
- value 가 채워졌고 absence_marker 가 없으면 → **measured row**.
- value 가 비었거나 행 자체가 부재(요구목록과 매칭 시 발견) → **fill candidate**.
- absence_marker = 'block' → 그 블록 전체가 부재.
- absence_marker = 'row' → 그 row 만 부재 (다른 row 는 measured 가능).

## 5. 요구목록 ↔ 측정값 매칭 (Pass B)

요구목록 ↔ 측정값 매칭 규칙 (kind: measured 와 derived 모두 측정값.md 와 매칭, `<기호>_실측` 가상 항목, R.0 carry-over §3.3 등) 을 적용한다. 본 스킬은 매칭 결과를 ✓/△/✗ 로 분류하지 않고 **fill 작업 항목 리스트**로 변환한다:

```python
FillTask:
  table_key: (AC, Part, Table)
  column_sym: str
  independent: {sym, value, unit} | None
  kind: 'measured' | 'derived' | 'measured_qualifier' | 'independent_measured'
  tool: str | None           # FG / DMM / Oscilloscope / LCR / 함수발생기 / ...
  expected: float | None     # 요구목록 v5 의 expected (v4 면 None)
  confidence: '상'|'중'|'하'|None
  formula: str | None        # derived 만, 요구목록의 formula:
  absence_marker: 'block' | 'row' | None
  reason: '인라인_____' | '요구_있으나_행없음' | '부재표지_block' | '부재표지_row'
```

fill 후보 분류:
- absence_marker = 'block' + `expand-skipped` 없음 → 스킵 (출력에서 원본 보존).
- absence_marker = 'row' + `expand-skipped` 없음 → 스킵 (출력에서 원본 보존).
- absence_marker = 'row' + `expand-skipped` 있음 → §6.6 sanity check 후 조건부 fill.
- 그 외 → 무조건 fill 대상.

## 6. 캘리브레이션 + Fill (Pass C, 핵심)

각 Table 별로 독립 수행. 알고리즘:

### 6.1 Fill 순서 (위상정렬)

같은 Table 안 fill 대상의 의존성:
- `independent_measured` (row-bound `<기호>_실측`) → 같은 행 measured 의 캘리브레이션에 입력으로 들어감.
- `measured_qualifier` (고정조건 `(measured)`) → Table 의 모든 measured 캘리브레이션에 입력으로 들어감.
- `measured` → derived 의 입력으로 들어감 (요구목록 `inputs: measured-rows` / `inputs-by-row` 가 가리키는 경우).
- `derived` → 항상 마지막.

순서:
1. **measured_qualifier 채우기**: nominal × Uniform(1 - tol, 1 + tol). tol 은 §6.5 의 tool 별 분포표.
2. **independent_measured 채우기**: nominal × Uniform(1 - tol, 1 + tol). 행 단위로 처리.
3. **measured 채우기**: §6.2~6.4 의 캘리브레이션.
4. **derived 채우기**: 요구목록 `formula:` 에 (이제 모두 채워진) 입력을 대입. 노이즈 부여 없음 (derived 는 환산 자리).

cycle 이 생기면 (희소) Table 전체를 unsolvable 로 마크하고 §6.7 의 unsolvable 분기로.

### 6.2 미지 파라미터 결정

이론식 캐시의 `미지 파라미터: [<sym1>, ...]` 를 읽는다:

- `[]` (미지 없음) → 순수 이론 모드. measured 의 forward 식에 고정조건 nominal 만 대입.
- 1 개 이상 → 측정행 개수 `N_meas` 와 비교:
  - `len(unknowns) ≤ N_meas` → **least-squares fit** (§6.3). 각 미지 파라미터를 fit.
  - `len(unknowns) > N_meas` → fit 불가. **0-row fallback** (§6.4) 로 강등.

### 6.3 Least-squares fit

각 measured row 에 대해:
1. forward 식에 그 row 의 independent 값과 고정조건 nominal 을 대입.
2. 미지 파라미터를 변수로 둔 residual `r_i = measured_i - forward(unknowns, row_i)` 를 만든다.
3. 모든 row 의 r_i² 합을 최소화. scipy 없이 손계산이 가능하면 (1차원 unknown 일 때 closed-form) 그것을 쓰고, 다차원이면 LLM 에게 grid-search (≤ 100 점) 를 시킨다.
4. fit 결과가 `domain 제약` (§3.1) 을 위반하면 그 솔루션 폐기 → 0-row fallback.
5. fit 통과 시 각 row 의 residual % 의 RMS 를 `noise_scale` 로 저장 (단 최소 0.005, 최대 0.05 로 clamp).

### 6.4 0-row fallback (이론값 + 잡음)

- forward 식에 고정조건 nominal + independent 값을 대입.
- 노이즈 = Uniform(-0.03, +0.03) × theory_value.
- 출처 태그 = `이론-fallback` (콘솔 요약 분류 용도, 파일에는 등장하지 않음).

이론식이 `<UNRESOLVED>` 이면 fill 불가 → 그 셀은 `____` 그대로 유지, 콘솔 요약의 'Fill 실패' 목록에 `<UNRESOLVED> 회로` 사유로 등록 (파일에는 아무 마커도 박지 않는다).

### 6.5 tool 별 ±tolerance 분포표

`measured_qualifier` 및 `independent_measured` 의 nominal-기반 채우기에 사용. 요구목록의 `tool:` 필드 또는 컬럼 기호로 분기:

| tool / 기호 | 분포 | 비고 |
|---|---|---|
| `함수발생기` / `FG` / 기호 `f` | Uniform(-0.005, +0.005) | 함수발생기 frequency counter, ±0.5% |
| `DMM` (Ω 측정) / 기호 `R`, `R_s` | Uniform(-0.01, +0.01) | 카본 필름 ±1% |
| `LCR meter` / 기호 `L`, `C` | Uniform(-0.02, +0.02) | 인덕터 / 콘덴서 명판 ±2% |
| `Oscilloscope` (전압 직접 측정) | Uniform(-0.02, +0.02) | DSO 채널 정확도 |
| tool 명시 없음 | Uniform(-0.01, +0.01) | 기본값 |

(measured 컬럼 자체의 noise 는 §6.3 의 fit residual 기반이고, 본 표는 nominal-기반 채우기 전용.)

### 6.6 row 임베디드 부재 표지의 sanity check (`expand-skipped` 시)

row 임베디드 부재 표지가 붙은 행을 `expand-skipped` 로 채울 때, 다음 둘 다 통과해야 채운다:

1. **물리적 한계 sanity**: 측정값.md 의 같은 row 또는 인접 코멘트에 명시된 한계값 (예: "V_L=1.87V까지밖에") 을 추출. 캘리브레이션 결과 fill 값이 그 한계를 위반하는지 확인. 위반 시 빈칸 `____` 그대로 유지, 콘솔 요약의 'Fill 실패' 목록에 `물리적 한계 충돌, 관측 한계 = <값>` 사유로 등록 (파일에는 아무 마커도 박지 않는다).
2. **단위·부호**: fill 값이 양수이고 단위가 일관적인지.

통과 시 정상 fill. 출처 태그(`캘리브레이션-N행` / `이론-fallback`)는 콘솔 요약 분류 용도로만 메모리에 기록되며 파일에는 등장하지 않는다.

### 6.7 Unsolvable Table 분기

다음 중 하나에 해당하면 Table 전체를 unsolvable 로 마크:
- 이론식 캐시가 `<UNRESOLVED>`.
- `len(unknowns) > N_meas` 이고 0-row fallback 의 nominal 도 부재.
- domain 제약 위반이 모든 fit 후보에서 발생.

unsolvable Table 의 fill 대상 셀은 빈칸 `____` 그대로 유지, 콘솔 요약의 'Fill 실패' 목록에 `unsolvable` 사유로 등록 (파일에는 아무 마커도 박지 않는다). 콘솔 요약에 unsolvable Table 수 노출.

## 7. 출력 파일 정책

- 출력 경로: `<OUTPUT_DIR>\측정값_시뮬레이션.md`
- 원본 `측정값.md` 는 **읽기만** 한다. 어떤 분기에서도 절대 수정하지 않는다.
- 기존 시뮬레이션 파일 존재 시:
  - `overwrite` 없음 → 거절하고 한 줄 안내:
    > `<OUTPUT_DIR>\측정값_시뮬레이션.md` 가 이미 존재합니다. 덮어쓰려면 `overwrite` 토큰을 명시하세요.
  - `overwrite` 있음 → `<OUTPUT_DIR>\측정값_시뮬레이션.bak-<YYYYMMDD-HHMMSS>.md` 로 백업 후 덮어쓰기.

## 8. 출력 파일 포맷

핵심 원칙: 출력 파일 `측정값_시뮬레이션.md` 는 원본 `측정값.md` 와 **시각적으로 구분되지 않아야 한다**. 다른 점은 오직 `____` → 숫자 치환뿐이다. 어떤 인라인 마커·전용 헤더·푸터·코멘트도 추가하지 않는다.

### 8.1 파일 헤더 — 원본 측정값.md 그대로 복사

`측정값.md` 의 상단 HTML 주석 (보통 1~3행) 을 1바이트 변경 없이 그대로 복사한다. 시뮬레이션 전용 메타데이터 코멘트(생성시각·소스·캐시 경로) 는 **절대 추가하지 않는다**.

예 (12주차 원본):
```markdown
<!-- 측정값 기록용. 빈 칸 ____ 을 실험실에서 채우세요. -->
<!-- 실험 미진행 시 해당 Part/Table 전체를 "- 실험을 진행하지 않았음." 한 줄로 대체하세요. -->
<!-- generated from 측정체크리스트/요구목록.md @ 2026-05-21 (schema v4) -->
```

ad-hoc 요구목록을 쓴 실행에서도 헤더는 원본 그대로. 사용 사실은 §9.10 콘솔 요약에서만 노출.

### 8.2 본문 — 원본 블록 구조 + 값만 치환

`측정값.md` 의 블록 구조 (`# AC N` / `## Part N` / `### Table N.N`) 와 줄 순서·들여쓰기·코멘트를 모두 그대로 보존한다.

- fill 성공 행: `____` 를 값으로 치환. **인라인 마커·코멘트 없음**.
- fill 실패 행 (sanity 위반 / unsolvable / `<UNRESOLVED>`): `____` 그대로 유지. **인라인 실패 마커 없음**. 원본 측정값.md 의 빈 템플릿과 식별 불가능.
- row 임베디드 부재 표지 행 (`expand-skipped` 없음): 원본 그대로.

### 8.3 출처 태그 (내부 분류 — 파일에는 등장하지 않음)

다음 분류는 메모리 / 콘솔 요약 용도로만 유지된다. 파일 본문에는 **절대 등장하지 않는다**.

| 태그 | 의미 |
|---|---|
| `캘리브레이션-N행` | 같은 Table 의 N 개 measured row 로 least-squares fit 한 결과 + residual-scale 잡음 |
| `이론-fallback` | 0-row fallback. nominal + 이론식 + ±3% Uniform |
| `nominal±tol` | measured_qualifier 또는 independent_measured 의 nominal × tool 별 tolerance |
| `derived-환산` | derived 컬럼을 formula 로 직접 계산 (잡음 없음) |
| `수치한계-skipped` | row 임베디드 부재 표지 + `expand-skipped` 미사용 → 원본 그대로, fill 안 함 |

실패 사유 분류 (`<UNRESOLVED> 회로` / `물리적 한계 충돌, 관측 한계 = <값>` / `unsolvable`) 도 같은 방식으로 메모리·콘솔에만 존재.

### 8.4 본문 검증 (저장 직전 invariant)

파일을 디스크에 쓰기 직전 두 가지 invariant 를 확인한다:

1. **본문 라인 수 일치**: 원본 `측정값.md` 와 시뮬레이션 출력의 줄 수가 동일한가? (`____` 치환만 일어났으므로 줄 수 변경 금지.)
2. **fill 메모리 ↔ 본문 정합**:
   - 메모리의 `filled_cells` 에 등록된 셀이 본문에서 `____` 가 아닌 값으로 치환되어 있는가?
   - 메모리의 `unfilled_cells` (실패·skip) 가 본문에서 여전히 `____` 또는 원본 그대로 보존되어 있는가?

불일치 시 파일 저장 중단 + 콘솔 오류 한 줄:
> 본문 검증 실패: <세부 사유>. 스킬 버그 가능 — 출력 파일을 작성하지 않음.

### 8.5 예시

원본 `측정값.md` Table 4.2 (10주차 가정):
```markdown
### Table 4.2
- R_s(measured) = 103.4(Ω)
- V_L(p-p) = 2(V)로 고정

- F = 1kHz일 때는 E_s의 V_pp를 최대치인 5Vpp로 설정해도 V_L(p-p)의 값이 1.87V까지밖에 올라가지 않아 실험을 진행할 수 없었음.
- F = 3kHz일 때 V_Rs(DMM) = 356.16(mV)
- F = 5kHz일 때 V_Rs(DMM) = 218.28(mV)
- F = 7kHz일 때 V_Rs(DMM) = 157.78(mV)
- F = 10kHz일 때 V_Rs(DMM) = 111.25(mV)
```

기본 동작 (`expand-skipped` 없음) 의 시뮬레이션 출력:
```markdown
### Table 4.2
- R_s(measured) = 103.4(Ω)
- V_L(p-p) = 2(V)로 고정

- F = 1kHz일 때는 E_s의 V_pp를 최대치인 5Vpp로 설정해도 V_L(p-p)의 값이 1.87V까지밖에 올라가지 않아 실험을 진행할 수 없었음.
- F = 3kHz일 때 V_Rs(DMM) = 356.16(mV)
- F = 5kHz일 때 V_Rs(DMM) = 218.28(mV)
- F = 7kHz일 때 V_Rs(DMM) = 157.78(mV)
- F = 10kHz일 때 V_Rs(DMM) = 111.25(mV)
```
(변화 없음 — 1kHz row 는 물리적 한계로 자동 fill 제외, 다른 row 는 이미 measured.)

`expand-skipped` 있는 실행에서 한계 sanity 가 위반된 경우:
```markdown
- F = 1kHz일 때 V_Rs(DMM) = ____(mV)
- F = 3kHz일 때 V_Rs(DMM) = 356.16(mV)
```
(1kHz 셀은 `____` 그대로. 위반 사유는 §9.10 콘솔 요약에만 등장. 파일만 봐서는 단순히 미채워진 빈칸과 구분되지 않는다.)

한계 sanity 통과 가정 (가상 — 실제 10주차는 위반):
```markdown
- F = 1kHz일 때 V_Rs(DMM) = 1041.83(mV)
- F = 3kHz일 때 V_Rs(DMM) = 356.16(mV)
```
(인라인 마커 없음 — 원본 측정값.md 와 시각적 차이 없음.)

## 9. 실행 절차 요약

1. `ARGUMENTS` 파싱 → `MEAS_FILE`, `WEEK_DIR`, `OUTPUT_DIR`, `expand-skipped`, `overwrite`, `refresh-formula` 확정.
2. `MEAS_FILE` 존재 검사. 없으면 거절.
3. 요구목록 해결 (§2): 캐시 발견 + 버전 분기 또는 ad-hoc.
4. 이론식 캐시 해결 (§3): 신선도 검사 + 필요 시 재생성. ad-hoc 요구목록이면 인-메모리 유도.
5. Pass A — `측정값.md` 파싱 (§4).
6. Pass B — 요구목록 ↔ 측정값 매칭, `FillTask` 리스트 구축 (§5).
7. Pass C — Table 별 캘리브레이션 + fill (§6). 위상정렬 순서대로.
8. 본문 검증 (§8.4) — 두 invariant 확인 후 실패 시 파일 저장 중단.
9. `OUTPUT_DIR\측정값_시뮬레이션.md` 저장 (§7 의 overwrite 정책).
10. 콘솔 요약 출력 (파일에는 저장되지 않음):
    - **시각적 구분 불가 경고문 (강제 첫 줄)**:
      > ⚠ 본 출력은 측정값.md 와 시각적으로 구분되지 않습니다. 시뮬레이션 여부는 파일명에서만 식별 가능하며, 보고서로 옮길 때는 반드시 어느 파일을 참조하는지 확인하세요.
    - 마크다운 링크
    - Fill 한 셀 수 (출처 태그별 카운트: 캘리브레이션-N행 / 이론-fallback / nominal±tol / derived-환산)
    - Fill 실패 (`____` 유지) 셀 수 + Table / cell / 사유 목록 (있을 때만)
    - row 임베디드 부재 표지 보존 행 수 (자동 fill 제외)
    - unsolvable Table 수 (있을 때만)
    - ad-hoc 요구목록 사용 여부
    - 이론식 캐시 재생성 여부
    - 백업 파일명 (overwrite 시)

## 10. 스킬 파이프라인에서의 위치

| 시점 | 스킬 | 입력 | 출력 |
|---|---|---|---|
| 실험 전 (1) | `create-measurement-checklist` | 주차 | `측정체크리스트\요구목록.md` (v5 캐시) + 체크리스트 PDF |
| 실험 전 (2) | `create-measurement-template` | 요구목록.md | `output\측정값.md` 빈 템플릿 |
| 실험 후 | **`fill-lab-measurements`** | 측정값.md | `output\측정값_시뮬레이션.md` (시뮬레이션 fill) |

**출력 파일은 측정값.md 와 시각적으로 구분되지 않아 보고서로 옮길 때 특히 주의가 필요** — 캘리브레이션이 noise scale 까지 흉내내고 in-file 가드레일이 전혀 없으므로 파일명 식별과 사용자의 출처 관리에 전적으로 의존한다.

## 11. 비-목표

- 원본 `측정값.md` 절대 수정 금지 (학사 무결성 가드레일).
- PDF 변환 안 함.
- 요구목록.md 파일 재생성 안 함 (prep-checklist 의 책임). 캐시 부재 시 인-메모리 ad-hoc 만.
- SPICE / numerical solver 호출 안 함.
- 자기 인덕턴스 / 비선형 소자 / 트랜지스터 회로 — 이론식 캐시에서 `<UNRESOLVED>` 처리.
- 측정값 이론 검토 (✓/△/✗ 비교) 안 함 — 이론 예상값은 `create-measurement-checklist`의 요구목록.md 참조.
- 다중 주차 일괄 처리 안 함.
- 다른 프로젝트에서 동작 안 함.
- 출력 파일은 측정값.md 와 시각적으로 구분되지 않도록 의도된다. 학사 무결성은 **파일명 구분과 사용자의 출처 관리에 전적으로 의존**하며, 스킬은 파일 본문에 어떤 출처 표식·시뮬레이션 마커·푸터도 박지 않는다. 보고서로 옮길 때 파일을 혼동하지 않는 책임은 사용자에게 있다.
