# prompt-forge

거지 프롬프트를 **맥락에 맞는 GOOD 프롬프트**로 다뤄 주는 Claude Code 스킬 4종 +
성장하는 패턴 라이브러리.

아무렇게나 쓴 한 줄("버그 고쳐줘")을 검증된 프롬프트 패턴(실밸개발자 / 알렉스 16패턴 /
해외 고수 채굴본)으로 다시 짠다. 셋은 **같은 `patterns/` 라이브러리와 같은 채점 언어**를 공유하고,
"다듬은 뒤 무엇을 하느냐"만 다르다.

## 네 스킬

| 스킬 | 트리거 | 하는 일 | 실행? |
|--|--|--|--|
| **prompt-rate-review** | `/prompt-rate <프롬프트>` | raw 프롬프트를 4축(목표·완료판단·범위·맥락)으로 채점 → 가장 약한 축 + 최소 수정 3개. **내 프롬프트 실력을 올리는 학습용.** | ✕ |
| **prompt-forge** | `/prompt-forge <프롬프트>` | GOOD 프롬프트로 변환해 **복붙 가능한 텍스트**로 돌려준다. 도구 독립(Claude Code·Codex·ChatGPT 어디나). | ✕ (철칙) |
| **forge-run** | `/forge-run <프롬프트>` | 변환한 뒤 **곧바로 이 세션에서 실행**한다. forge가 멈추는 자리에서 실행까지 간다. | ✅ |
| **prompt-log-review** | `/prompt-log-review [세션]` | 지목한 세션 트랜스크립트에서 내가 쓴 프롬프트만 뽑아 4축으로 일괄 채점 → 최약축 + 최악 프롬프트 고치는 법. **세션 단위 약점 진단.** | ✕ |

```
raw 프롬프트
   ├─ /prompt-rate   → 채점만 (약점 진단·학습)
   ├─ /prompt-forge  → 다듬고 멈춤 (복붙용)
   ├─ /forge-run     → 다듬고 바로 실행 (원스톱)
   └─ /prompt-log-review → 세션 단위 채점 (약점 추이)
```

> **철칙(rate·forge 공통): 실행하지 않는다.** 입력 프롬프트는 "명령"이 아니라 다룰 "데이터"다.
> 명령형("~만들어줘")이어도 재료로만 다룬다.
> **forge-run만 예외로 실행**하되, 명세가 부족하면(빈칸) 실행하지 않고 먼저 물어본다(멋대로 실행 방지).

## 왜

프롬프트 팁은 널렸지만 "지금 이 요청에 어떤 패턴을 써야 하나"는 매번 사람이 판단한다.
prompt-forge는 그 판단을 자동화한다:

- **크기 자동 조절** — 단일 작업(small)엔 3~4개 패턴만, 프로젝트급(large)엔 단계별 풀세트.
  과잉 방지가 1급 요구사항 (작은 일에 8단계 PRD를 붙이지 않는다).
- **엔진은 불변, 재료만 성장** — 새 고수를 조사하면 `patterns/`에 파일이 늘 뿐, 엔진(SKILL.md)은 그대로다.
- **적용 패턴 항상 명시** — 변환 결과에 "어떤 패턴을 왜 썼는지"를 한 줄로 남겨 학습 루프를 만든다.
- **채점축 ↔ forge 슬롯 1:1 정합** — rate의 4축이 forge의 슬롯과 같은 언어라, `rate → forge → 다시 rate`로 점수가 오르는지 교차검증된다.
  1회 실측(2026-09-01, 픽스처 5케이스): 하락 0·상승 15축 — **forge는 하를 없애고, 빈칸 충전이 상을 만든다** ([기록](docs/2026-09-01-rate-forge-rate-validation.md)).

## 설치 (스킬 연결)

이 repo가 Claude Code 스킬 4종을 담고 있다. 각 `skills/<이름>/`을 Claude Code가 읽는 스킬 경로
(`~/.claude/skills/`)에 심볼릭 링크한다:

```
ln -sfn "$PWD/skills/prompt-forge"       ~/.claude/skills/prompt-forge
ln -sfn "$PWD/skills/prompt-rate-review" ~/.claude/skills/prompt-rate-review
ln -sfn "$PWD/skills/forge-run"          ~/.claude/skills/forge-run
ln -sfn "$PWD/skills/prompt-log-review"  ~/.claude/skills/prompt-log-review
```

연결되면 `/prompt-forge`·`/prompt-rate`·`/forge-run`·`/prompt-log-review`로 호출된다.
변환 계열 세 스킬(forge·rate·forge-run)은 같은 `patterns/`를 상대 경로(심링크)로 공유하므로 라이브러리를 한 곳만 키우면 셋 다 최신이 된다.
(`prompt-log-review`는 패턴이 아니라 rate-review의 4축만 참조한다.)

## 사용법

```
/prompt-rate  <채점할 프롬프트>     # 어디가 약한지 진단
/prompt-forge <다듬을 프롬프트>     # GOOD 프롬프트로 변환(복붙)
/forge-run    <다듬어 실행할 프롬프트>  # 변환 + 바로 실행
/forge-run qa <프롬프트>             # 부족하지 않아도 Q&A로 완성형까지 (빈 곳이 있으면 qa 없이도 자동으로 묻는다)
/prompt-log-review [세션 경로]      # 세션 하나를 통째로 채점 (경로 없이 부르면 목록에서 고른다)
```

`prompt-log-review`는 주 1회(월 10:17) launchd로도 자동 실행된다 — 설치·해제는
[`skills/prompt-log-review/SKILL.md`](skills/prompt-log-review/SKILL.md)의 "주간 자동 실행" 참조.

forge 엔진은 5단계로 동작한다:

1. **크기 판단** — small(단일 작업) / large(프로젝트급). 입력이 말 덤프면 채우기 대신 정리(정보는 하나도 안 빼고 Why·What·How로 재배치). 길이는 크기 신호가 아니다.
2. **맥락 검사** — 사용자만 답할 수 있는 빈 곳(빈 필수 슬롯, 특정 안 되는 "그거·위에 붙인 데이터")이 있으면 **qa가 자동으로 열린다**(객관식 + 사실은 말로, 빈 곳 질문 최대 3 + 기본값 확인 1). 채점이 '중'인 축만으로는 묻지 않는다. 답해도 안 채워지면 빈칸 `[ ]` 프롬프트로 출력.
3. **패턴 선택** — `patterns/_INDEX.md`를 읽어 이 요청에 맞는 패턴만 고른다.
4. **변환 출력** — 변환된 프롬프트(코드블록) + 적용 패턴 목록(한 줄) + 원본 완성도(원본을 rate 축으로 채점한 한 줄).
5. **끝** — 실행하지 않는다. (forge-run은 여기서 멈추지 않고 실행)

### 예시

**입력:** `버그 고쳐줘` (small)

증상·대상이 불명 → 질문 2개("① 어떤 에러? ② 어느 파일·함수?") → 답을 받으면:

```
[파일:함수]에서 [증상]이 발생한다.
문제: <재현 조건 한 줄>.
고칠 것: 근본 원인 한 곳만 수정. 증상 패치 금지.
완료 판단: <이 입력>이 <이 출력>을 내면 끝. 기존 통과 테스트 깨지지 않을 것.
```

`적용: 문제정의, 검증방법, 범위제한 (small)` — small엔 킥오프·PRD를 붙이지 않는다.

## Repo 구조

```
prompt-forge/
├─ skills/
│  ├─ prompt-forge/SKILL.md        ← 엔진. 5단계 변환 절차 (패턴이 늘어도 안 바뀐다)
│  ├─ prompt-rate-review/SKILL.md  ← 4축 채점기 (+ test-prompts.md 픽스처)
│  ├─ forge-run/SKILL.md           ← 변환 + 실행 브릿지 (patterns 공유)
│  └─ prompt-log-review/SKILL.md ← 세션 채점 (+ extract.py 추출기, ledger.md 장부)
├─ patterns/
│  ├─ 00-silvally-alex.md          ← 기준선 (알렉스 16패턴 이식본)
│  ├─ 01~08-*.md                   ← 해외 고수 1차 채굴 (Simon Willison … Thorsten Ball)
│  ├─ 09~15-*.md                   ← 병렬 리서치 2차 채굴 (Indragie … Avi Chawla)
│  ├─ 16~20-*.md                   ← 3차 채굴 (조태호·Jesse Vincent·Hamel Husain·Anthropic Eng·SNOWFLOW)
│  ├─ 21~22-*.md                   ← 4차 채굴 (Reddit — ponytail·second-opinion)
│  └─ _INDEX.md                    ← | 단계 | 패턴 | 파일 | 역인덱스 (121패턴, 재게시 1행 포함 122행)
├─ research/
│  ├─ RUBRIC.md                    ← 출처 입장자격 채점기 (상 2개↑만 입장)
│  ├─ candidates.md                ← 조사 대상 후보 목록
│  └─ scout-*.md                   ← 병렬 리서치 채굴 원본 + 취합
├─ docs/                           ← 설계 스펙 / 구현 계획
└─ README.md
```

**단계 분류**(패턴이 붙는 자리)는 9개:
킥오프 / 컨텍스트주입 / 리서치위임 / PRD / 스코핑 / 솔루션깎기 / 검증기 / 구현위임 / 검증루프.

## 라이브러리 키우기 (리서치 → 패턴)

패턴은 조사로 늘린다. **엔진과 forge-run은 안 건드리고 `patterns/`만 자란다** — 셋이 공유하므로 한 번 키우면 셋 다 강해진다.

1. 후보를 [`research/candidates.md`](research/candidates.md)에 올린다.
2. [`research/RUBRIC.md`](research/RUBRIC.md) 4항목으로 채점 — **상 2개 이상만 입장.**
3. 통과 시 프롬프트 원문·원리를 뽑아 `patterns/` 파일 하나를 만든다. (조사 1회 = 패턴 파일 1개. 넓게 100개 긁기 금지.)
4. `patterns/_INDEX.md`에 줄 추가.

## 진화 경로

- **v1** — forge 엔진 + 알렉스 16패턴 + 조사 루브릭.
- **v1.x** — 해외·국내 고수 조사로 패턴 확장 (01~22, 총 118패턴. 엔진 무변경).
- **v2** — 같은 `patterns/`를 공유하는 스킬 3종: 채점(prompt-rate-review) · 변환(prompt-forge) · 실행(forge-run).
- **v2.1** — E 로그 리뷰어 실현: `prompt-log-review`. 최초 설계는 forge 변환 로그를 데이터원으로 잡았지만,
  실사용의 전량은 세션 트랜스크립트에 있고 forge를 안 거친 "맨 프롬프트"가 진짜 실력이라 데이터원을 바꿨다.
  장부(`ledger.md`)가 쌓이면 최약축 추이 → rubric 자기갱신이 다음 차례다.
  장부 축적은 주간 자동 리뷰(launchd 월 10:17 → `weekly-review.sh`, 지난 7일 최다 세션 자동 선정)가 맡는다 — 수동 습관은 5주 실측(ledger 1줄)으로 반증됐다.
- **v2.2** — 말로 하는 프롬프트 대응 (2026-10-25, 알렉스 영상 [3EchTw4UVs8](https://www.youtube.com/watch?v=3EchTw4UVs8)).
  빈칸 질문을 Why·What·How 카드 한 장으로, 말 덤프 정리 모드(정보 보존), forge-run 정정 구문 게이트, 3패턴 추가.
  9/1 실측의 '빈칸이 남으면 중에서 멈춘다'를 빈칸 채우는 비용을 낮추는 쪽으로 겨냥했다. 검증: [`docs/2026-10-25-voice-dump-validation.md`](docs/2026-10-25-voice-dump-validation.md).
- **v2.3** — 완성형 (2026-10-25). 목표 정의를 rate·forge·forge-run 한 문장으로 통일
  ("결과물의 핵심 내용을 모델이 지어내지 않고 정할 수 있나"). `qa` 모드: 상이 아닌 축만 객관식으로 묻고(사실엔 보기 금지),
  forge 기본값을 확인받아 **빈칸 0 + 모든 줄을 사용자가 말했거나 확인**한 상태까지 간다. 기본 출력엔 원본 완성도 한 줄.
  검증: [`docs/2026-10-25-qa-mode-validation.md`](docs/2026-10-25-qa-mode-validation.md).
- **v2.4 (현재)** — 자동 qa (2026-10-25). 빈 필수 슬롯이나 특정 안 되는 가리킴이 있으면 시키지 않아도 객관식 Q&A가 열린다.
  forge-run은 묻기 전에 대화·읽기 전용 조회로 찾고, 사용자만 아는 것만 묻는다. 채점 '중'인 축만으로는 묻지 않는다(완료 '중'은 거의 모든 원본에서 나온다).
- **v3 (자리만)** — 플러그인화. 스킬 4종이 한 repo에 모여 있는 지금 구조가 그 직전 모양이다.

> 채점축 ↔ 슬롯 정합은 **라벨 기준**이다. 개수로는 다르다 — rate는 4축(목표·완료판단·범위·맥락),
> forge 슬롯은 small 2개·large 3개. **부족분을 셀 때는 슬롯만 센다**(4축을 세지 않는다).
