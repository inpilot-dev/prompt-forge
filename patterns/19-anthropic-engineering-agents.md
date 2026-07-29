# 19 — Anthropic Engineering (컨텍스트 엔지니어링 · 멀티에이전트 · 롱러닝 하네스)

> ⚠️ 플래그: **벤더 공식 문서다 — 개인 고수의 실전 공개가 아니다.** 05와 같은 성격의 출처.
> RUBRIC #4(실전 결과물)가 구조적으로 약하다(자사 시스템 자랑 + 내부 eval 수치, 외부 검증 가능한 출시 아티팩트 없음).
> 그래서 #1 원문·#2 원리·#3 워크플로우 중 **상 2개 이상**인 글만 재료로 채택했다.
>
> 출처 3건 (전부 WebFetch로 원문 확인, 2026-07 기준):
> 1. Effective context engineering for AI agents — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
>    채점: 원문 중 / 원리 상 / 워크플로우 상 / 결과물 하 → 상 2개 = 입장
> 2. How we built our multi-agent research system — https://www.anthropic.com/engineering/multi-agent-research-system
>    채점: 원문 중 / 원리 상 / 워크플로우 상 / 결과물 중 → 상 2개 = 입장
> 3. Effective harnesses for long-running agents — https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
>    채점: 원문 상 / 원리 상 / 워크플로우 상 / 결과물 중 → 상 3개 = 입장
>
> **이식 범위 메모 — 05와 겹치는 것은 전부 버렸다.**
> 서브에이전트가 별도 컨텍스트에서 요약만 돌려준다는 논지는 [[delegate-research-to-subagents]]와 동일 → 미이식.
> 컨텍스트를 리셋한다는 논지는 [[context-hygiene]] / [[context-refresh-threshold]]와 동일 → 미이식(아래 `compaction-recall-first`는 "언제 리셋하냐"가 아니라 **"넘길 요약 프롬프트를 어떻게 쓰냐"**로만 좁혔다).
> 합격 조건을 붙인다는 논지는 [[verification-loop]]와 동일 → 미이식(아래 `verification-ledger-no-test-edits`는 **"검증 자산 자체를 못 건드리게 막는 조항"**으로만 좁혔다).
> 4번째 글 "Harness design for long-running application development"(https://www.anthropic.com/engineering/harness-design-long-running-apps)은 **기각**: 프롬프트가 전부 요약 서술이고(원문 중), 고유해 보이는 sprint contract는 [[build-grader-first]]와 실질 동일.

---

## 적정 고도의 지시문 (right-altitude-instructions)
- **단계:** 컨텍스트주입
- **언제:** 지시문/CLAUDE.md/스킬을 쓸 때, 얼마나 자세히 써야 할지 감이 안 잡힐 때. 규칙을 더 붙일지 뺄지 판단이 필요할 때.
- **Bad:** (한쪽 극단) "만약 파일이 .tsx면 A를 하고, 아니면 B를 하되 테스트가 있으면 C를…" — 분기 조건을 프롬프트에 하드코딩. / (반대 극단) "코드 품질을 높게 유지해줘."
- **Good:** 지시문을 두 극단 사이로 재작성 + 섹션 분리 — `<background_information>`, `<instructions>`, `## Tool guidance`, `## Output description`처럼 XML 태그나 마크다운 헤더로 구획하고, **행동을 완전히 규정하는 최소 정보량**까지 깎는다.
- **왜:** "The right altitude is the Goldilocks zone between two common failure modes. At one extreme, we see engineers hardcoding complex, brittle logic in their prompts to elicit exact agentic behavior. This approach creates fragility and increases maintenance complexity over time. At the other extreme, engineers sometimes provide vague, high-level guidance that fails to give the LLM concrete signals for desired outputs or falsely assumes shared context." 그리고 "you should be striving for the minimal set of information that fully outlines your expected behavior." 즉 규칙을 더 쓰는 게 늘 좋은 게 아니다 — 하드코딩은 **깨지고**, 뭉뚱그리면 **신호가 없다**. 판단 기준은 분량이 아니라 "휴리스틱으로 작동하는 최소량".
- **출처:** Anthropic, Effective context engineering for AI agents — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

## 내용 말고 참조를 줘라 (just-in-time-context)
- **단계:** 컨텍스트주입
- **언제:** 넘길 자료가 많아 다 붙이면 컨텍스트가 터질 때. 어느 부분이 실제로 필요한지 미리 모를 때.
- **Bad:** 관련될 만한 파일·문서·검색 결과를 미리 전부 읽어 프롬프트에 밀어 넣는다(사전 적재).
- **Good:** 내용 대신 **가벼운 식별자**만 준다 — "관련 파일은 `src/auth/`, `docs/session-flow.md`, 그리고 이슈 #412다. 필요한 것만 직접 열어 읽고, 뭘 왜 읽었는지 먼저 말해라."
- **왜:** "Rather than pre-processing all relevant data up front, agents built with the 'just in time' approach maintain lightweight identifiers (file paths, stored queries, web links, etc.) and use these references to dynamically load data into context at runtime using tools." 사람이 자료를 통째로 외우지 않고 파일시스템·북마크로 색인해 두었다가 필요할 때 꺼내는 것과 같은 구조이고, 이렇게 하면 **점진적 발견(progressive disclosure)** 이 가능해진다. ⚠️ [[paste-full-source]]와 정면으로 충돌하는 게 아니라 **자료의 성격이 다르다**: 실격 조건이 디테일에 숨은 과제문·규격은 통째로 붙이고(요약하면 죽는다), 어디가 필요할지 모르는 대량 코드·문서는 참조만 준다.
- **출처:** Anthropic, Effective context engineering for AI agents — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

## 위임 예산을 숫자로 배정 (delegation-effort-budget)
- **단계:** 리서치위임
- **언제:** 서브에이전트에 조사를 위임하는데, 간단한 질문에 과투자하거나 여러 에이전트가 같은 검색을 반복할 때.
- **Bad:** "서브에이전트들 써서 이거 조사해줘." — 몇 명을 쓸지, 각자 어디까지 팔지 미지정.
- **Good:** 위임 프롬프트에 **인원·툴콜 예산 + 각자의 경계**를 명시한다. "이건 단순 사실확인이니 에이전트 1개, 툴콜 3~10회 안에서 끝내라." / "A와 B 비교니까 서브에이전트 2~4개, 각 10~15회." + 각 서브에이전트에게 **목표 / 산출 형식 / 쓸 툴과 출처 / 건드리지 말 범위** 4가지를 반드시 지정 + "짧고 넓은 질의로 시작해서 뭐가 있는지 보고, 점점 좁혀라."
- **왜:** "Simple fact-finding requires just 1 agent with 3-10 tool calls, direct comparisons might need 2-4 subagents with 10-15 calls each, and complex research might use more than 10 subagents with clearly divided responsibilities." 이 규칙이 막는 실패는 두 가지다 — 단순 질의에 대한 "overinvestment", 그리고 지시가 모호해서 "subagents misinterpreted the task or performed the exact same searches as other agents"가 되는 중복 노동. 그래서 "Each subagent needs an objective, an output format, guidance on the tools and sources to use, and clear task boundaries." 검색 전략도 명시한다 — "prompting agents to start with short, broad queries, evaluate what's available, then progressively narrow focus." ([[delegate-research-to-subagents]]가 "위임하라"라면 이건 **위임장에 예산과 경계를 적는 법**이다. [[structured-output-spec]]은 이 4요소 중 '산출 형식' 하나를 깊게 판 것.)
- **출처:** Anthropic, How we built our multi-agent research system — https://www.anthropic.com/engineering/multi-agent-research-system

## 검증 대장과 '테스트 손대기 금지' 조항 (verification-ledger-no-test-edits)
- **단계:** 검증루프
- **언제:** 여러 세션에 걸친 긴 작업에서 에이전트가 "다 됐다"고 선언하는데 실제로는 반만 됐을 때. 테스트가 빨간불이면 테스트를 고쳐버릴 때.
- **Bad:** "테스트 통과시켜줘." — 통과라는 목표만 주면 테스트를 지우거나 완화하는 것이 최단 경로가 된다.
- **Good:** 기계가 읽는 **기능 대장 파일**을 두고(각 항목 `{"category", "description", "steps", "passes": false}`) + 다음 조항을 지시문에 박는다 — "It is unacceptable to remove or edit tests because this could lead to missing or buggy functionality." + "Self-verify all features. Only mark features as 'passing' after careful testing." 세션 시작은 "`pwd`를 실행해 작업 디렉터리를 확인 → git 로그와 진행 파일을 읽어 최근 작업 파악 → 기능 목록에서 아직 안 된 것 중 최우선순위 하나를 골라라"로 연다.
- **왜:** 관측된 실패 모드가 명시돼 있다 — 클로드는 "tended to try to do too much at once", 기능을 "half-implemented and undocumented"로 남겼고, 프로젝트 후반부로 갈수록 "declare the job done"해버렸다. 합격 신호를 **에이전트가 수정할 수 없는 자산**으로 분리하고, `passes` 불린을 사람이 감사할 수 있는 대장에 남겨야 "다 됐다"는 주장이 검증 가능해진다. ([[verification-loop]]는 합격조건을 *주는* 것, [[backpressure-via-tests]]는 *스텁* 구멍을 막는 것 — 이건 *검증 자산을 지워버리는* 구멍을 막는 조항이다. 대장 형식도 [[todo-md-checklist]]의 사람용 체크리스트가 아니라 기계가독 JSON + 합불 플래그다.)
- **출처:** Anthropic, Effective harnesses for long-running agents — https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents

## 인계 요약은 재현율 먼저, 정밀도 나중 (compaction-recall-first)
- **단계:** 컨텍스트주입
- **언제:** 세션을 넘기며 요약을 만들 때(직접 쓰는 인계 프롬프트든 `/compact`류든). 요약이 짧고 깔끔한데 정작 다음 세션이 중요한 걸 모를 때.
- **Bad:** 처음부터 "핵심만 3줄로 요약해줘." — 예쁜 요약을 먼저 만들고 나중에 뭐가 빠졌는지 알게 된다.
- **Good:** 요약 지시를 **2패스로 튜닝**한다. 1패스: "이 세션에서 나온 결정·제약·실패한 시도·미해결 항목을 하나도 빠뜨리지 말고 전부 적어라(길어도 된다)." → 실제로 다음 세션을 돌려보고 → 2패스: 안 쓰인 항목을 지우며 지시문을 깎는다.
- **왜:** "Start by maximizing recall to ensure your compaction prompt captures every relevant piece of information from the trace, then iterate to improve precision by eliminating superfluous content." 누락은 조용히 다음 세션을 망치지만 과잉은 눈에 보인다 — 그래서 **관측 가능한 쪽(과잉)에서 깎아 들어가는 순서**가 맞다. 요약 프롬프트도 한 번 쓰고 마는 글이 아니라 튜닝 대상이다. ([[context-refresh-threshold]]가 *언제* 넘길지, [[session-reonboarding]]이 새 세션을 *어떻게 열지*라면, 이건 *무엇을 실어 보낼지*를 정하는 법.)
- **출처:** Anthropic, Effective context engineering for AI agents — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
