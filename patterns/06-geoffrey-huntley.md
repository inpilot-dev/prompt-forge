# 06 — Geoffrey Huntley (ralph)

> 출처: ghuntley.com/ralph/ (공개, web.archive 스냅샷으로 전문 검증) + github.com/ghuntley/how-to-ralph-wiggum (PROMPT/loop 파일 전문).
> ex-Gitpod/Canva. 채점: 원문 상 / 원리 상 / 워크플로우 상 / 결과물 중 → 상 3개 = 입장.
> 결과물이 중인 이유: CURSED(신규 컴파일 언어) 등 강한 주장은 트윗 스크린샷 수준이고 공개 실행물이 withheld.
> ⚠️ /stdlib/ · /specs/ 본문은 구독 게이트 — 인용 안 함. ralph 페이지 + 공개 repo만 원문 근거.
> 이 파일은 "자율 루프(ralph)" 운영 체계 하나로 묶인 패턴군이다.

---

## ralph 루프 (ralph-loop)
- **단계:** 구현위임
- **언제:** 스펙·계획이 파일로 있고, 한 레포에서 에이전트를 while 루프로 자율 실행할 때.
- **Bad:** IDE에서 대화형 원샷 "implement XYZ, please".
- **Good:** `while :; do cat PROMPT.md | claude-code ; done` — 강화판(loop.sh, 요약)은 매 반복 `claude -p --dangerously-skip-permissions --output-format=stream-json --model opus`로 돌리고 매 루프 `git push`, plan/build 모드 + 최대 반복 캡.
- **왜:** "Ralph works autonomously ... as a single process that performs one task per loop." 진행은 컨텍스트가 아니라 파일 + git에 남는다. "deterministically bad in an undeterministic world" — 반복 + 백프레셔로 최종 일관성에 수렴.
- **출처:** Geoffrey Huntley, ralph — https://ghuntley.com/ralph/ (loop.sh: github.com/ghuntley/how-to-ralph-wiggum)

## 루프당 한 작업 (one-item-per-loop)
- **단계:** 스코핑
- **언제:** 컨텍스트 예산 안에서 품질을 유지하도록 작업을 쪼갤 때.
- **Bad:** 한 긴 세션에서 여러 기능을 한꺼번에 시킨다.
- **Good:** "you need to ask Ralph to do one thing per loop. Only one thing." + "you only have approximately 170k of context window to work with. So it's essential to use as little of it as possible."
- **왜:** 출력 품질이 "clips at the 147k-152k mark". 매 루프가 새로 시작하므로, 한 작업으로 좁게 묶어야 작업 전체가 고품질 컨텍스트 영역 안에 들어온다. 무엇이 가장 중요한지는 LLM이 정하도록 신뢰.
- **출처:** Geoffrey Huntley, ralph — https://ghuntley.com/ralph/

## 스택 결정론적 할당 (deterministic-stack-allocation)
- **단계:** 컨텍스트주입
- **언제:** 매 루프의 시작 상태를 재현 가능하게 고정할 때.
- **Bad:** 대화 메모리에 의존하거나 매 실행마다 로드 내용을 바꾼다.
- **Good:** "deterministically allocate the stack the same way every loop. The items ... are your plan ('@fix_plan.md') and your specifications." repo 프롬프트는 매 루프를 "0a. Study `specs/*` ... 0b. Study @IMPLEMENTATION_PLAN.md"로 시작.
- **왜:** 매 루프 같은 파일로 컨텍스트를 채우면 모델이 알려진 상태에서 출발한다. 비결정성에도 재현 가능한 시작점. "낭비적"이지만 재사용보다 재현성이 우선.
- **출처:** Geoffrey Huntley, ralph — https://ghuntley.com/ralph/

## 서브에이전트를 스케줄러로 (subagents-as-scheduler)
- **단계:** 리서치위임
- **언제:** 메인 컨텍스트를 얇게 유지하며 비싼(검색·읽기·테스트) 작업을 격리할 때.
- **Bad:** 검색·읽기·테스트를 전부 메인 컨텍스트에서 처리.
- **Good:** "Your primary context window should operate as a scheduler, scheduling other subagents to perform expensive allocation-type work, such as summarising whether your test suite worked." + "You may use up to 500 parallel subagents for all operations but only 1 subagent for build/tests."
- **왜:** 툴 결과가 메인 컨텍스트를 부풀린다("autoregressive queens of failure"). 서브에이전트는 자기 컨텍스트를 가져 GC된다. 단, 빌드/테스트에 수백 개를 부으면 "bad back pressure"라 검증은 서브에이전트 1개로 제한. (Anthropic [[delegate-research-to-subagents]]의 아키텍처적 극단판.)
- **출처:** Geoffrey Huntley, ralph — https://ghuntley.com/ralph/

## 테스트로 백프레셔·반스텁 (backpressure-via-tests)
- **단계:** 검증루프
- **언제:** 컴파일된다고 코드를 믿지 않고, 스텁/플레이스홀더 편향을 게이트로 막을 때.
- **Bad:** 컴파일되니 생성 코드를 신뢰(모델은 "reward function is compiling code"라 최소·플레이스홀더 구현으로 흐른다).
- **Good:** "After implementing functionality or resolving problems, run the tests for that unit of code that was improved. If functionality is missing then it's your job to add it as per the application specifications." + 반스텁 사인 "DO NOT IMPLEMENT PLACEHOLDER OR SIMPLE IMPLEMENTATIONS. WE WANT FULL IMPLEMENTATIONS."
- **왜:** "Code generation is easy now, what is hard is ensuring that Ralph has generated the right thing." 타입·컴파일러·테스트·린터를 게이트로 배선해 "invalid code generation"을 거절. (데모 아닌 실검증 [[real-data-enforcement]]과 같은 정신.)
- **출처:** Geoffrey Huntley, ralph — https://ghuntley.com/ralph/

## 스펙을 단일 진실원으로 (specs-as-source-of-truth)
- **단계:** PRD
- **언제:** 에이전트에 프로젝트를 직접 구현시키지 않고, 스펙을 레포에 파일로 굳혀 매 루프 재로드할 때.
- **Bad:** 에이전트에게 프로젝트를 곧바로 구현하라고 지시.
- **Good:** "Instead of asking the agent to implement the project ... have a long conversation with the LLM about your requirements ... issue a prompt to write the specifications out, one per file, in the specifications folder." (스펙 부재 시 가정 말고 "search before creating".)
- **왜:** 레포에 커밋된 스펙이 재로드되는 지반 진실이 된다. "If Ralph is building the wrong thing completely, then your specifications may be incorrect"(스펙의 중복 렉서 키워드가 한 달을 날렸다). 코드는 값싸고 버릴 수 있지만 스펙은 지속 아티팩트.
- **출처:** Geoffrey Huntley, ralph — https://ghuntley.com/ralph/ (specs 소개: ghuntley.com/specs/, 본문 게이트)

## 사인으로 루프 튜닝 (tune-with-signs)
- **단계:** 솔루션깎기
- **언제:** 완벽한 프롬프트를 앞에서 찾지 않고, 스트림을 관찰하며 실패 유형마다 가드레일을 붙일 때.
- **Bad:** 앞단에서 "완벽한 프롬프트"를 추구("There is no such thing as a perfect prompt").
- **Good:** (가드레일 사인) "Before making changes search codebase (don't assume an item is not implemented) using parallel subagents. Think hard." + 자가개선 운영파일 "When you learn something new about how to run the compiler or examples make sure you update @AGENT.md using a subagent but keep it brief." (단, "DO NOT PLACE STATUS REPORT UPDATES INTO @AGENT.md".)
- **왜:** 스트림에서 나쁜 행동 패턴을 보면 "사인을 하나 붙인다". ripgrep 검색의 비결정성이 "미구현"으로 오판하게 만들면, 사인이 그 실패 부류를 근본에서 막는다. AGENT.md는 "루프의 심장"이라 운영 지시만 담아 오염을 막는다.
- **출처:** Geoffrey Huntley, ralph — https://ghuntley.com/ralph/
