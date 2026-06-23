---
name: create-measurement-template
description: 기초전기실험 프로젝트 안에서 동작하는 프로젝트 스킬. `<주차>\측정체크리스트\요구목록.md` 를 받아 학생이 실험실에서 손으로 채울 `<주차>\output\측정값.md` 빈 템플릿을 생성한다. 사용자가 "측정값 템플릿", "10주차 측정값.md 만들어줘", "측정값 파일 초기화", "/create-measurement-template" 등을 호출할 때 사용한다.
---

# create-measurement-template

`create-measurement-checklist` 가 만들어둔 v3 캐시(`<주차>\측정체크리스트\요구목록.md`)를 펼쳐 학생이 실험실에서 손으로 채울 `<주차>\output\측정값.md` **빈 템플릿**을 생성한다. 이 템플릿은 그대로 `check-lab-measurements` 가 소비할 수 있는 형식이고, 이미 존재하는 측정값.md 는 명시적 `overwrite` 없이는 절대 덮어쓰지 않는다.

이 스킬은 이 프로젝트(`C:\Users\Hyunjun\Desktop\현준대학\기전실`) 안에서만 동작한다. cwd 가 다른 프로젝트로 바뀌면 자동 트리거되지 않는다.

## 0. 부트스트랩 (완료된 상태로 가정)

이 SKILL.md 가 존재한다는 것은 `<프로젝트>\.claude\skills\create-measurement-template\` 가 이미 만들어졌다는 뜻이다. 별도 부트스트랩 단계는 없다.

## 1. 입력 해석 (인자 필수)

`ARGUMENTS` 를 반드시 받는다. 형식:

```
/create-measurement-template <N주차> [overwrite]
```

해석 규칙:
- 비어 있으면 한 줄 안내 후 종료:
  > 측정값 템플릿을 생성할 주차를 인자로 주세요. 예: `/create-measurement-template 11주차`
- 첫 토큰이 `N주차` → 프로젝트 루트 아래의 `<N주차>` 폴더를 `WEEK_DIR` 로 사용. 폴더 부재면 거절.
- 첫 토큰이 디렉토리 경로면 그 디렉토리를 `WEEK_DIR` 로 사용 (이름이 `N주차` 형태여야 한다).
- `overwrite` 토큰: 기존 `output\측정값.md` 존재 시 백업 후 덮어쓰기 허용 (§5 참조).
- 그 외 토큰(`refresh` 포함)은 무시한다. 본 스킬은 캐시를 관리하지 않으므로 `refresh` 를 지원하지 않는다.

## 2. 소스 (단일)

이 스킬은 **단 하나의 입력**만 읽는다:

- `<WEEK_DIR>\측정체크리스트\요구목록.md` (v3 스키마)

부재 시 한 줄 안내 후 종료:
> `<주차>\측정체크리스트\요구목록.md` 가 없습니다. 먼저 `/create-measurement-checklist <주차>` 를 실행해 정답지를 생성하세요.

v3 스키마 검증: 파일 첫 줄에 `<!-- SCHEMA: v3 -->` 태그가 없으면 다음 안내 후 종료:
> 요구목록.md 가 구 스키마입니다. `/create-measurement-checklist <주차> refresh` 로 v3 로 갱신하세요.

책 사진·PDF·예비보고서를 다시 읽지 않는다. 캐시 신선도는 create-checklist 의 책임이며, 본 스킬은 결정론적 텍스트 변환만 수행한다.

## 3. 요구목록.md 파싱

다음 트리 구조를 추출한다:

```
## AC <N>
### Part <N>
#### Table <N.N>   (선택)
- 회로 모형: <한 줄>
- 고정조건:
  - <기호> = <값> <단위> (<qualifier>)
  ...
- 독립변수: <기호> = [<값1>, <값2>, ...] <단위>
- 컬럼:
  - <기호> [<단위>] | kind: <independent|measured|computed|fixed> | ...
```

Table heading 이 없는 Part 도 지원해야 한다 (Part 직속에 컬럼 블록이 있는 경우).

### 3.1 고정조건 분류

`- <기호> = <값> <단위> (<qualifier>)` 의 `<qualifier>` 를 정규식 `\(measured\b` 로 매칭:
- 매칭됨 (`(measured)`. sub-qualifier 는 create-checklist 가 v3 재생성 시 단일형으로 정규화하므로 본 스킬은 단순 매칭만 한다) → **nominal-힌트 동반 빈칸**. 출력: `<값> <단위> (실측 = ____(<단위>))`. 본 형식은 **기호-무차별** — R, R_s, f 등 `(measured)` qualifier 가 박힌 모든 라인에 동일 적용된다. 예외: 라인에 nominal 값이 추출되지 않는 경우 (`R_l = (measured)` 처럼 값 자리가 비었을 때) 만 `____(<단위>)` 단순 형식으로 출력.
- 비매칭 (`nominal`, `calc`, 또는 qualifier 없음) → **고정 라벨**. 템플릿에서 값을 그대로 출력하고 ` (<qualifier>)` 부착.
- **pre_measured 다운그레이드 (§3.4 참조)**: `(measured)` 매칭이라도 `(<기호>, <값>, <단위>)` 가 §3.4 의 `pre_measured` 집합에 들어 있으면 빈칸 출력을 억제하고 라벨을 `(사전 측정, Table R.0 참조)` 로 교체한다. 즉 `R = 1 kΩ (measured)` 이고 R.0 에 같은 (R, 1 kΩ) 가 있으면 → `R = 1 kΩ (사전 측정, Table R.0 참조)`.

### 3.2 컬럼 kind 처리

| kind | flag | 템플릿 처리 |
|---|---|---|
| `independent` | (없음) | 행 라벨로 사용 (Table 의 독립변수와 동일 기호일 것). |
| `independent` | `measured: true` | 행 라벨 + nominal-힌트 동반 실측 블랭크: `<sym> = <val> <unit> (실측 = ____(<unit>))일 때 ...` (§4.2). |
| `measured` | — | 빈칸 (`____(<단위>)`). 각 독립변수 값마다 1행. |
| `fixed` | — | 표 안 박힌 고정값. 고정조건 블록 하단에 `<기호> = <값> (<단위>) [표 내 고정]` 한 줄로 표기. |
| `computed` | — | **템플릿 본문에서 제외**. (단 §3.3 의 zero-measured 예외.) |

### 3.3 Zero-measured Table 예외

Table 안 컬럼이 **전부 `computed`** (또는 `independent` (`measured: true` 없음) + `computed` 조합)인 경우 — 즉 `measured` 컬럼 0개 + `fixed` 컬럼 0개 + `independent | measured: true` 컬럼 0개 — 카드를 생략하지 말고 다음 placeholder 만 출력:

```markdown
### Table <N.N>
<!-- 회로 모형: <한 줄> -->
- 측정 없음 — 전부 계산 컬럼이므로 보고서 작성 시 도출.
```

이 규칙은 11주차의 Table 7.7 같은 derived/summary table 을 위한 것이다. `independent | measured: true` 가 있으면 — 다른 measured/fixed 컬럼이 없어도 — zero-measured 가 아니며 §4.2 후단 분기에 따라 행 라벨만 있는 라인이 출력된다.

### 3.4 사전-측정(pre_measured) 항목 집합 추적

§3.1 의 `(measured)` 분기와 §4.2 의 `independent | measured: true` 행 라벨은 기본적으로 빈칸을 출력한다. 그러나 같은 주차의 **AC 0** 하위 Table 들이 동일한 `(기호, 값)` 을 이미 측정 자리로 잡아놓은 경우, 그 자리는 R.0(또는 동급 측정-전용 Table) 에서 한 번만 적고 다른 Table 에서는 재기재하지 않는 것이 자연스럽다. 이 절은 그 집합을 수집하는 규칙을 정의한다.

#### 3.4.1 수집 시점

요구목록 파싱 (§3) 직후, Table 본문 렌더링 (§4) **전에** Pass 1 으로 한 번 수행한다. 출력 자료구조는 집합

```
pre_measured: Set[ (sym: str, value_in_base_unit: float, base_unit: str) ]
```

#### 3.4.2 수집 대상

다음 두 조건을 모두 만족하는 Table 만 스캔:
1. `AC 0` 하위 (`# AC 0` 또는 `## AC 0` 헤더 직속)
2. `독립변수` 라인이 `항목 = [<sym> = <val> <unit>, <sym> = <val> <unit>, ...]` 형태이고, 컬럼에 `kind: measured` 가 1 개 이상 존재

AC 0 외 다른 AC 의 어떤 Table 도 수집 대상이 아니다. AC 0 부재 시 `pre_measured = ∅` 이고 본 절은 no-op (기존 동작 유지, backward compat).

#### 3.4.3 항목 파싱

`독립변수` 라인의 대괄호 내부를 콤마로 분리한 뒤 각 토큰에 대해:

1. **기호-값 분리**: 정규식 `^\s*([A-Za-z][A-Za-z0-9_]*)\s*=\s*(.+?)\s*$` 로 `(sym, value_expr)` 추출. 매칭 실패 → 그 토큰만 건너뛰고 stderr 에 한 줄 경고 (`pre_measured: skipped token "<원문>"`). 다른 토큰 수집은 계속.
2. **수치-단위 분리**: `value_expr` 에 대해 정규식 `^([+-]?\d+(?:\.\d+)?)\s*(\S+)\s*$` 로 `(numeric_str, unit_str)` 추출. 매칭 실패 → 토큰 건너뛰고 경고.
3. **SI prefix 정규화**: `unit_str` 의 첫 글자가 SI prefix 이고 나머지가 알려진 base unit 이면 numeric 에 prefix 배율을 곱하고 base unit 만 키에 사용. 표:

   | prefix | 배율 | 예 |
   |---|---|---|
   | `k` | 1e3 | `kΩ`, `kHz` |
   | `M` | 1e6 | `MΩ`, `MHz` |
   | `G` | 1e9 | `GΩ`, `GHz` |
   | `m` | 1e-3 | `mH`, `mA`, `mV`, `ms` |
   | `μ` 또는 `u` | 1e-6 | `μF`, `μH`, `μs` |
   | `n` | 1e-9 | `nF`, `nH`, `ns` |
   | `p` | 1e-12 | `pF` |
   | (없음) | 1 | `Ω`, `V`, `A`, `Hz`, `F`, `H`, `s` |

   알려진 base unit: `Ω`, `F`, `H`, `V`, `A`, `Hz`, `s`. 그 외 단위는 정규화 없이 `unit_str` 그대로 사용 (희소 케이스 보존).

산출: `(sym, base_numeric, base_unit)` 튜플을 `pre_measured` 에 추가.

#### 3.4.4 매칭

§3.1 의 `(measured)` 고정조건 라인과 §4.2 의 `independent | measured: true` 행 라벨을 출력할 때, 그 라인/행의 `(sym, val, unit)` 도 §3.4.3 의 정규화를 거쳐 `pre_measured` 와 비교한다 (set membership; 부동소수점 비교는 `abs(a-b) ≤ max(1e-9, 1e-6·abs(a))` 로 수행해 표기 차이에서 오는 round-trip 오차 흡수).

- 일치 → 빈칸 출력 억제 (§3.1 마지막 불릿, §4.2 마지막 불릿 참조).
- 불일치 → 기존 동작(빈칸 출력) 유지. 별도 경고 노출하지 않음.

#### 3.4.5 가정과 한계

- 학생이 R.0 의 **모든 행**을 실제로 측정한다고 가정한다. R.0 에 정의된 (sym, val) 만으로 다운스트림 블랭크를 억제하므로, 학생이 6.8 kΩ 측정을 건너뛰면 다운스트림 Table 7.3/7.6 등에 그 값을 기록할 자리가 사라진 채 남는다. 본 스킬은 이 가정 위반을 검출하지 않는다 — `check-lab-measurements` 가 R.0 ✗ 를 보고할 때 함께 인지된다.
- 같은 (sym, val) 가 R.0 에 중복 등장하면 (실수든 의도든) 집합 동작상 한 번만 들어간다.
- AC 0 외 측정-전용 Table 패턴이 미래 주차에 등장하면 본 절을 확장한다 (§9 비-목표).

## 4. 템플릿 본문 규칙

요구목록의 각 AC/Part/Table 을 다음 형식으로 펼친다.

### 4.1 파일 헤더 (3줄 주석)

파일 최상단:

```markdown
<!-- 측정값 기록용. 빈 칸 ____ 을 실험실에서 채우세요. -->
<!-- 실험 미진행 시 해당 Part/Table 전체를 "- 실험을 진행하지 않았음." 한 줄로 대체하세요. -->
<!-- generated from 측정체크리스트/요구목록.md @ <ISO timestamp> -->
```

### 4.2 Table 블록

```markdown
# AC <N>
## Part <N>
### Table <N.N>
<!-- 회로 모형: <요구목록의 회로 모형 한 줄> -->

- 고정조건
  - <기호> = <값> <단위> (실측 = ____(<단위>))    <!-- (measured) qualifier, nominal-힌트 동반 빈칸 -->
  - <기호> = <값> (<qualifier>)                   <!-- nominal/calc 항목, 값 그대로 -->
  - <기호> = <값> (<단위>) [표 내 고정]            <!-- fixed 컬럼이 있을 때 -->

- <indep_sym> = <val1> <indep_unit>일 때 <measured_sym1> = ____(<unit1>), <measured_sym2> = ____(<unit2>)
- <indep_sym> = <val2> <indep_unit>일 때 <measured_sym1> = ____(<unit1>), <measured_sym2> = ____(<unit2>)
...

# independent | measured: true 인 경우:
- <indep_sym> = <val1> <indep_unit> (실측 = ____(<indep_unit>))일 때 <measured_sym1> = ____(<unit1>), ...
- <indep_sym> = <val2> <indep_unit> (실측 = ____(<indep_unit>))일 때 <measured_sym1> = ____(<unit1>), ...
...
```

규칙:
- **공백 컨벤션 통일**: `<sym>` 과 `<val>` 과 `<unit>` 사이는 모두 공백 1칸 (`R = 1 kΩ`). 고정조건 라인과 row 라인 모두 동일.
- **빈칸 표기는 `____(<단위>)`** (괄호 직전 공백 없음) — 학생이 `____` 만 지우면 자연스럽게 `412(mV)` 가 되어 기존 측정값.md 컨벤션과 일치한다.
- 독립변수가 없으면 단일 행: `- <measured_sym> = ____(<단위>)` (Table 당 1줄, measured 컬럼이 여러 개면 콤마로 이어 적는다).
- 독립변수가 있으면 **모든 measured 컬럼을 한 행에 콤마로 묶는다** (예: `V_C(p-p) = ____(V), V_R(DMM) = ____(V)`). 행은 독립변수 값마다 1개.
- **Trailing measured 0 개일 때** (`independent | measured: true` 만 있고 같은 Table 에 measured 컬럼 없음): `일 때` 부분 자체를 생략하고 행 라벨만 출력. 즉 `- R = 1 kΩ (실측 = ____(kΩ))` (콤마 뒤 trailing 없음, "일 때" 도 없음). 11주차에는 발생하지 않지만 룰의 hole 봉합.
- independent 기호는 `F`/`R`/`L`/`C`/`t` 등 어떤 기호든 동일 규칙. 단위는 요구목록의 단위 그대로 (kHz, kΩ, μF, ms 등).
- 회로 모형은 HTML 주석 안에 둬 본문 line-noise 를 줄인다.
- Table heading 이 없는 Part 는 `### Table` 줄을 생략하고 Part 본문에 바로 고정조건/측정행을 적는다.
- **pre_measured 억제 (§3.4 참조)**: 행 라벨 또는 고정조건 라인의 `(sym, val, unit)` 가 §3.4 의 `pre_measured` 집합에 들어 있으면:
  - **행 라벨**: `(실측 = ____(<unit>))` 절 자체를 삭제하고 `- <indep_sym> = <val> <indep_unit>일 때 ...` 형식으로 출력. 즉 `R = 1 kΩ (실측 = ____(kΩ))일 때 V_R(p-p) = ____(V), ...` → `R = 1 kΩ일 때 V_R(p-p) = ____(V), ...`.
  - **고정조건**: 빈칸 출력을 억제하고 `<기호> = <값> <단위> (사전 측정, Table R.0 참조)` 로 라벨 교체 (§3.1 마지막 불릿).
  - **AC 0 자체의 Table R.0 은 본 억제의 대상이 아니다** (Pass 1 수집 대상이지 Pass 2 억제 대상 아님). R.0 자체의 `kind: measured` 컬럼은 일반 빈칸으로 그대로 출력된다 — 거기가 측정 자리.

### 4.3 expected/confidence 절대 노출 금지

요구목록의 `expected: <값들>` 과 `confidence: <상/중/하>` 필드는 템플릿에 **어떤 형태로도 옮기지 않는다** (주석으로도 X). 학사 무결성 보호. 예상값 비교는 `create-measurement-checklist` PDF / `check-lab-measurements` 보고서에서 한다.

## 5. 출력 파일 정책

- 출력 경로: `<WEEK_DIR>\output\측정값.md`
- `output\` 폴더가 없으면 생성한다.
- 기존 파일 존재 시:
  - `overwrite` 토큰 없음 → 거절하고 한 줄로 안내:
    > `<주차>\output\측정값.md` 가 이미 존재합니다. 실측 데이터가 들어있을 수 있으니 덮어쓰려면 `overwrite` 토큰을 명시하세요. 예: `/create-measurement-template 11주차 overwrite`
  - `overwrite` 토큰 있음 → `<WEEK_DIR>\output\측정값.bak-<YYYYMMDD-HHMMSS>.md` 로 백업한 뒤 새 템플릿으로 덮어쓰기. 백업 파일은 그대로 둔다 (학생이 정리).

## 6. 실행 절차

1. `ARGUMENTS` 파싱 → `WEEK_DIR`, `overwrite` 플래그 확정.
2. `<WEEK_DIR>\측정체크리스트\요구목록.md` 존재·v3 검증 (§2). 실패 시 거절.
3. 요구목록 파싱 → AC/Part/Table 트리 (§3).
4. **Pass 1 — AC 0 스캔**: §3.4 규칙대로 AC 0 하위 Table 들을 스캔해 `pre_measured` 집합 구축. AC 0 부재 시 `∅`.
5. **Pass 2 — 트리 순회 및 렌더**: 요구목록 트리를 §4 규칙으로 마크다운 문자열로 조립.
   - Zero-measured Table 은 §3.3 placeholder.
   - 고정조건은 §3.1 규칙대로 빈칸/라벨 분기 (pre_measured 일치 시 `(사전 측정, Table R.0 참조)` 로 교체).
   - measured 컬럼은 §4.2 콤마 묶음 (pre_measured 일치 시 행 라벨의 `(실측 = ____)` 절 삭제).
6. `<WEEK_DIR>\output\` 폴더 확인·생성.
7. `output\측정값.md` 존재 검사 → §5 정책대로 백업 또는 거절.
8. 파일 저장 후 한 줄 요약 출력:
   - 마크다운 링크
   - 생성된 빈칸 총 개수 (measured 셀 + measured 고정조건 셀)
   - **사전 측정 항목 개수 (R.0 의존) + 다운스트림 억제된 블랭크 개수** (pre_measured ≠ ∅ 일 때만 노출)
   - zero-measured Table 개수 (있을 때만)
   - 백업 파일명 (overwrite 시)

## 7. 산출물 예시 (11주차 Table 7.1–7.3 일부)

전제 — AC 0 / Table R.0 의 `독립변수: 항목 = [R = 1 kΩ, R = 3.3 kΩ, R = 6.8 kΩ, R_s = 10 Ω]` + Measured 컬럼이 §3.4 Pass 1 에서 다음 집합을 만든 상태:
```
pre_measured = {
  (R, 1000.0, "Ω"), (R, 3300.0, "Ω"), (R, 6800.0, "Ω"),
  (R_s, 10.0, "Ω")
}
```

요구목록 입력 (v3, Table 7.1–7.3 합성 패턴):
```
- 고정조건:
  - C = 0.47 μF (nominal)
  - f = 200 Hz (measured)
  - E_(p-p) = 4 V (nominal)
  - X_C = 1693.30 Ω (calc)
- 독립변수: R = [1, 3.3, 6.8] kΩ
- 컬럼:
  - R [kΩ] | kind: independent | measured: true
  - V_R(p-p) [V] | kind: measured | tool: Oscilloscope | expected: ... | confidence: 상
  - D_1 [div] | kind: measured | ...
  - D_2 [div] | kind: measured | ...
```

템플릿 출력:
```markdown
### Table 7.1–7.3
<!-- 회로 모형: Fig 7.9 R-C 직렬 (source → C → node a → R → GND, Ch2 = V_R; R 한쪽이 GND 공통) -->

- 고정조건
  - C = 0.47 μF (nominal)
  - f = 200 Hz (실측 = ____(Hz))                  <!-- f 는 pre_measured 미일치 → 기존 빈칸 -->
  - E_(p-p) = 4 V (nominal)
  - X_C = 1693.30 Ω (calc)

- R = 1 kΩ일 때 V_R(p-p) = ____(V), D_1 = ____(div), D_2 = ____(div)
- R = 3.3 kΩ일 때 V_R(p-p) = ____(V), D_1 = ____(div), D_2 = ____(div)
- R = 6.8 kΩ일 때 V_R(p-p) = ____(V), D_1 = ____(div), D_2 = ____(div)
```

주: R 각 행에서 `(실측 = ____(kΩ))` 가 사라진 것은 §3.4 의 `pre_measured` 와 일치(R.0 에서 이미 측정)했기 때문. f 는 R.0 에 없으므로 그대로 빈칸 유지. 만약 같은 Table 의 고정조건에 `R = 1 kΩ (measured)` 같은 라인이 있었다면, 그 라인은 `R = 1 kΩ (사전 측정, Table R.0 참조)` 로 라벨이 교체되어 빈칸 없이 출력된다 (§3.1 마지막 불릿).

## 8. 스킬 파이프라인에서의 위치

| 시점 | 스킬 | 입력 | 출력 |
|---|---|---|---|
| 실험 전 (1) | `create-measurement-checklist` | 주차 | `측정체크리스트\요구목록.md` (v5 캐시) + 체크리스트 PDF |
| 실험 전 (2) | **`create-measurement-template`** | 요구목록.md | `output\측정값.md` 빈 템플릿 |
| 실험 후 | `fill-lab-measurements` | 채워진 측정값.md | `output\측정값_시뮬레이션.md` |

본 스킬은 캐시(요구목록.md)를 **소비만** 한다. 생성·재생성 책임은 create-checklist 에 있다.

## 9. 비-목표

- 요구목록.md 재생성 안 함 (create-checklist 의 책임).
- HTML/PDF 변환 안 함 — 학생이 IDE 에서 직접 편집하는 plain markdown 한 파일.
- 예상값(`expected`)·신뢰도(`confidence`) 절대 노출 안 함 — 학사 무결성 보호.
- 기존 측정값.md 자동 덮어쓰기 안 함 — `overwrite` 명시 + 백업.
- 측정값 이론 검토(✓/△/✗) 안 함 — 이론 예상값은 `create-measurement-checklist`의 요구목록.md 참조.
- 부분 주차 / 부분 Table 만 생성 옵션 없음 — 전체 트리 일괄.
- 다중 주차 일괄 처리 안 함.
- 다른 프로젝트에서 동작 안 함.
- 회로 시뮬레이션·이론값 계산 안 함.
- **AC 0 외 다른 AC 에 위치한 측정-전용 Table 은 사전-측정으로 인식하지 않음** (§3.4.2). 필요 시 본 SKILL.md 의 §3.4 룰을 확장.
- **pre_measured 매칭 미스(텍스트·SI prefix 정규화 후에도 일치하지 않는 경우)를 별도 경고로 노출하지 않음** — 기존 동작(빈칸 출력)으로 폴백 (§3.4.4 후단). 매칭 누수 가능성은 한 줄 요약의 "다운스트림 억제된 블랭크 개수" 가 0 인지로 학생이 1차 점검.
