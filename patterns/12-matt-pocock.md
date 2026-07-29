# 12 — Matt Pocock

> 출처: YouTube "Full Walkthrough: Workflow for AI Coding — Matt Pocock" (AI Engineer, 1:36:29) — https://www.youtube.com/watch?v=-QFHIoCo-Ko
> TypeScript 에듀케이터(Total TypeScript).
> 루브릭: 원문 **상**(2026-07-29 재채굴 — `grill-me` SKILL.md 전문을 화면에서 확보, 아래 verbatim) / 원리 상 / 워크플로우 상 / 결과물 상 = **상 4**.
> 이력: 1차 채굴 시 "grill-me 전문 미확보"로 원문 **중**(상 3) 채점이었다. `/watch`로 자막+프레임을 뽑아 원문을 확보해 **상 4로 승격**.
> 검증 근거: 96분 라이브 워크숍 전체(브리프→그릴링→PRD→칸반→병렬 구현→QA) 재현.

---

## grill-me 인터뷰를 1단계로 (grill-me-first)
- **단계:** 킥오프
- **언제:** 러프한 아이디어·클라이언트 요청을 받았을 때. 구현 전에 모호함을 강제로 걷어내고 싶을 때.
- **Bad:** "이거 만들어줘" (모호한 채 바로 구현 진입). 또는 plan mode에 그냥 던지기 — "It would really eagerly try to produce a plan for me. It would say, 'Okay, I think I've got enough. I'm just going to poof plan plan.'" (16:42)
- **Good:** `.claude/skills/grill-me/SKILL.md`를 만들어 **모든 작업의 1단계로 호출**한다. 파일 전문(11줄이 전부):
  ```markdown
  ---
  name: grill-me
  description: Interview the user relentlessly about a plan or design until reaching
  shared understanding, resolving each branch of the decision tree. Use when user wants
  to stress-test a plan, get grilled on their design, or mentions "grill me".
  ---

  Interview me relentlessly about every aspect of this plan until we reach a shared
  understanding. Walk down each branch of the design tree, resolving dependencies
  between decisions one-by-one. For each question, provide your recommended answer.

  Ask the questions one at a time.

  If a question can be answered by exploring the codebase, explore the codebase instead.
  ```
  호출은 `/grill-me <클라이언트 브리프 파일>` 한 줄. 컨텍스트를 비운 뒤 **스킬 + 브리프 두 개만** 준 상태로 시작한다(15:11, 15:55).
- **왜:** 목표는 계획서가 아니라 **합의된 이해**다 — "I didn't need a plan, I needed to be on the same wavelength as the AI." (17:24, Frederick P. Brooks의 *design concept* 인용). 세 문장이 각각 다른 실패를 막는다: ① **질문마다 추천답을 달게** 하면 사람이 답을 지어낼 필요가 없어 인터뷰가 40~100문항까지도 버틴다(20:52 — "I've had it ask me 80 questions"). ② **한 번에 한 질문**은 [[one-question-at-a-time-honing]]과 같은 원리. ③ **"코드베이스로 답할 수 있으면 묻지 말고 직접 조사해라"** 가 고유하다 — 인터뷰 예산을 사람이 아니라 에이전트가 아끼게 만든다(서브에이전트가 93.7k 토큰을 태워 탐색하는 동안 사용자 컨텍스트는 거의 안 늘어남, 17:51). 산출물은 문서가 아니라 **대화 기록 자체**이며, 회의록·도메인 전문가 미팅 트랜스크립트를 그릴링 입력으로 넣어 가정을 검증하는 데도 쓴다(21:35).
- **출처:** Matt Pocock — https://www.youtube.com/watch?v=-QFHIoCo-Ko (12:17~21:40, SKILL.md 화면 캡처 16:24)

## compact 금지·항상 clear (always-clear-never-compact)
- **단계:** 컨텍스트주입
- **언제:** 긴 세션에서 컨텍스트가 늘어질 때, 요약 압축 대신 결정론적 리셋을 원할 때.
- **Bad:** 컨텍스트가 차면 `/compact`로 요약 압축하고 계속.
- **Good:** "Memento" 규칙 — **compact 금지, 항상 `/clear`로 fresh context**. 필요한 상태는 문서로 다시 주입. 새 작업 시작 전에도 먼저 컨텍스트를 비운다(15:11).
- **왜:** compact 요약은 비결정적이고 조용히 열화된다("dumb zone"). 매번 시스템 프롬프트 상태로 리셋하면 반복가능·고성능 상태가 유지된다. [[context-hygiene]]·[[session-reonboarding]]의 하드룰판.
- **출처:** Matt Pocock — https://www.youtube.com/watch?v=-QFHIoCo-Ko

## 구현/리뷰 모델 분리 + fresh 리뷰 (implement-review-model-split)
- **단계:** 검증기
- **언제:** 구현물을 리뷰시킬 때, 같은 세션에서 자기 코드를 자평하는 열화를 피하고 싶을 때.
- **Bad:** 구현한 그 세션에서 "이 코드 리뷰해줘."
- **Good:** **구현=Sonnet / 리뷰=Opus**, 그리고 리뷰는 반드시 **fresh context**에서(같은 세션 금지).
- **왜:** 같은 맥락에서 리뷰하면 모델이 자기 결정을 방어하고 "dumb zone" 열화가 겹친다. 다른 모델·새 맥락으로 리뷰하면 적대적 시선이 생긴다. [[adversarial-review-subagent]]에 모델 역할 분리를 결합.
- **출처:** Matt Pocock — https://www.youtube.com/watch?v=-QFHIoCo-Ko

## 순차 계획 대신 칸반 DAG (kanban-dag-not-sequential-plan)
- **단계:** 스코핑
- **언제:** PRD를 실행 단위로 쪼갤 때. 특히 에이전트를 여러 개 동시에 돌릴 생각이 있을 때.
- **Bad:** "이 PRD를 단계별 계획으로 만들어줘" → 1→2→3 순차 계획이 나온다. "A sequential plan can really only be picked up by one agent." (51:11)
- **Good:** 계획을 **차단 관계(blocking)를 명시한 독립 티켓 집합**으로 만들게 한다. 각 티켓에 ① 무엇을 하는지 ② **무엇에 의해 막혀 있는지**(`blocked by 1, 2` / `blocked by nothing`) ③ **AFK인지 human-in-the-loop인지** 태그를 붙인다. 예: "schema and gamification service — blocked by nothing, type: AFK" / "wire points and streaks into lesson completion — blocked by 1 and 2" / "retroactive backfill — blocked by 1 only" (40:15~41:00).
- **왜:** 순차 계획은 구조상 에이전트 1개만 붙는다. 차단 관계를 명시하면 계획이 **DAG**가 되고, 같은 층의 티켓을 독립 에이전트가 동시에 집어갈 수 있다(49:40~51:11). AFK 태그는 그 위에 **위임 가능 여부를 계획 단계에서 미리 판정**해 두는 장치다 — 실행 중에 "이건 사람이 봐야 하나?"를 다시 고민하지 않는다. [[blueprint-to-chunked-prompts]]가 *순차* 청크라면 이건 *병렬* 그래프고, [[parallel-divergent-waves]]가 같은 스펙의 N개 변형이라면 이건 서로 다른 작업의 의존 정렬이다. 티켓 생성을 AI에 완전히 맡기지 않고 사람이 검토하는 이유는 "이건 하는 데 아주 싸고 빠르다 — 그런데 보면 바로 문제가 보인다"(41:24).
- **출처:** Matt Pocock — https://www.youtube.com/watch?v=-QFHIoCo-Ko (40:00~51:30)

## 모듈 맵은 내가, 구현은 위임 (module-map-then-delegate)
- **단계:** PRD
- **언제:** AI에게 기능을 맡기면서도 코드베이스의 형태를 내가 계속 쥐고 있고 싶을 때.
- **Bad:** 기능 단위로만 지시 → AI가 작은 파일을 잔뜩 만들고(shallow modules) 의존 그래프가 뒤엉킨다. "if you don't watch AI carefully, it's going to produce a code base that looks [like that]" (1:18:00). 그러면 테스트 경계도 못 긋는다.
- **Good:** PRD 안에 **수정·생성할 모듈 목록과 각 모듈의 인터페이스**를 먼저 박는다 — "this gamification service is a new deep module... it's going to have this particular interface. We're modifying the progress service, we're modifying the lesson route, the dashboard route." 그리고 그 모듈 맵을 계획~구현 내내 유지한다: "I'm being really specific about the modules that I'm editing, and I'm making sure that I keep that module map in my mind at all times." (1:19:00)
- **왜:** John Ousterhout의 deep module 개념을 위임 경계로 쓴다 — **인터페이스는 사람이 설계하고 구현은 회색상자로 위임**한다. 이러면 두 가지를 동시에 얻는다: 테스트 경계가 모듈 경계와 일치해 테스트가 의미를 갖고, 사람이 코드베이스 전체를 다 읽지 않고도 "형태"를 계속 안다. 그가 지목한 진짜 위험은 속도가 아니라 **감각 상실**이다 — "because we're delegating more things, we end up losing a sense of our code base. And if we lose the sense of our code base... we're essentially delegating the shape of it to AI." (1:19:40) [[scaffold-then-fill]]이 뼈대를 먼저 세우는 것이라면 이건 **경계와 인터페이스의 소유권**을 사람이 계속 갖는 규칙이다.
- **출처:** Matt Pocock — https://www.youtube.com/watch?v=-QFHIoCo-Ko (1:14:00~1:20:30)

## push냐 pull이냐로 지시를 배치 (push-vs-pull-instructions)
- **단계:** 컨텍스트주입
- **언제:** 코딩 규약·리뷰 기준 같은 지시를 어디에 둘지 정할 때. CLAUDE.md에 다 넣을지, 스킬로 뺄지 매번 헷갈릴 때.
- **Bad:** 모든 규약을 CLAUDE.md에 몰아넣기 → 매 요청마다 전부 토큰으로 밀려 들어간다. 반대로 전부 스킬로 빼기 → 정작 항상 지켜야 할 규칙을 에이전트가 안 당겨 온다.
- **Good:** 두 축으로 나눈다. **push** = CLAUDE.md에 넣는 것 — "that instruction is always going to be sent to the agent. You're pushing tokens to it." 항상 예외 없이 적용돼야 하는 것만. **pull** = 스킬로 두는 것 — "a skill is something that can sit in the repo, and it has a little description header that says: okay, agent, you may pull this when you want to." 상황에 걸릴 때만 필요한 것.
- **왜:** 지시의 비용 구조가 다르다. push는 **항상 내는 고정비**고 pull은 **걸릴 때만 내는 변동비**다. 이 구분 없이 CLAUDE.md를 키우면 모든 요청이 무거워지고, 그 무게가 정작 중요한 규칙의 신호를 묻는다. [[persistent-context-file]]과 [[prompt-drift-prevention]]이 "무엇을 고정할까"를 다룬다면, 이건 그 앞단의 **어디에 둘 것인가** 판정 규칙이다.
- **출처:** Matt Pocock — https://www.youtube.com/watch?v=-QFHIoCo-Ko (1:28:30~)
