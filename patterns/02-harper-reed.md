# 02 — Harper Reed

> 출처: "My LLM codegen workflow atm" (2025-02-16). Obama 2012 캠페인 前 CTO, 엔지니어/창업가.
> 채점: 원문 상 / 원리 중 / 워크플로우 상 / 결과물 하 → 상 2개 = 입장.
> 강점: 복붙 가능한 프롬프트 템플릿 전문 공개(idea-honing / spec-compile / blueprint / todo / review / tests).
> 워크플로우: 아이디어 정련 → 스펙 컴파일 → 청크 분해 → 스텝별 실행(그린필드/레거시 분기).

---

## 한 번에 한 질문 정련 (one-question-at-a-time-honing)
- **단계:** 킥오프
- **언제:** 아이디어가 흐릿한데 스펙으로 굳혀야 할 때. ([[reverse-interview]]의 케이던스 제어판 — 인터뷰 아이디어 자체가 아니라 "한 턴에 한 질문"이 이 패턴의 핵심 기여.)
- **Bad:** "내 앱 아이디어 전체 스펙 써줘: <IDEA>" (한 방에 가정투성이 스펙을 받는다.)
- **Good:** "Ask me one question at a time so we can develop a thorough, step-by-step spec for this idea. Each question should build on my previous answers, and our end goal is to have a detailed specification I can hand off to a developer. Let's do this iteratively and dig into every relevant detail. Remember, only one question at a time. Here's the idea: <IDEA>"
- **왜:** 한 턴에 한 질문으로 묶으면 모델이 가정을 앞당겨 채우지 못한다. 각 답이 다음 질문을 조건화해서, 모델의 추측이 아니라 내 실제 제약에서 스펙이 쌓인다.
- **출처:** Harper Reed, My LLM codegen workflow — https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/

## 대화를 스펙으로 컴파일 (compile-developer-ready-spec)
- **단계:** PRD
- **언제:** 브레인스토밍 대화가 끝났고, 흩어진 요구사항을 하나의 인계 가능한 아티팩트로 굳힐 때.
- **Bad:** 요구사항을 채팅 스크롤백에 흩어둔 채 전체 트랜스크립트를 코딩 모델에 던진다.
- **Good:** "Now that we've wrapped up the brainstorming process, can you compile our findings into a comprehensive, developer-ready specification? Include all relevant requirements, architecture choices, data handling details, error handling strategies, and a testing plan so a developer can immediately begin implementation."
- **왜:** 길고 산만한 대화를 필요한 섹션(요구사항·아키텍처·데이터·에러처리·테스트)을 명시한 단일 아티팩트(spec.md)로 축약한다. 이후 단계에 주입되는 단일 진실원(source of truth)이 되어 모델·세션 간 이동이 가능해진다.
- **출처:** Harper Reed, My LLM codegen workflow — https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/

## 청크로 쪼갠 프롬프트 시퀀스 (blueprint-to-chunked-prompts)
- **단계:** 스코핑
- **언제:** 스펙을 "테스트 가능할 만큼 작고, 전진할 만큼 큰" 스텝들로 분해해 순차 구현 프롬프트로 만들 때.
- **Bad:** "이제 전체 다 만들어줘." (거대 프롬프트 → 복잡도 급점프 → 고아 코드.)
- **Good:** "Draft a detailed, step-by-step blueprint for building this project. Then, once you have a solid plan, break it down into small, iterative chunks that build on each other. Look at these chunks and then go another round to break it into small steps. Review the results and make sure that the steps are small enough to be implemented safely with strong testing, but big enough to move the project forward... Make sure that each prompt builds on the previous prompts, and ends with wiring things together. There should be no hanging or orphaned code that isn't integrated into a previous step... <SPEC>"
- **왜:** 이중 분해("go another round to break it into small steps")가 스텝 크기를 스위트스팟으로 보정한다. 각 프롬프트가 이전 위에 쌓이고 "wiring things together"로 끝나게 강제하면, LLM 코드생성의 고질병인 통합 안 된 고아 코드가 사라진다.
- **출처:** Harper Reed, My LLM codegen workflow — https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/

## todo.md 체크리스트 외부화 (todo-md-checklist)
- **단계:** 구현위임
- **언제:** 긴 프롬프트 시퀀스를 스텝별로 실행하며 진행 상태를 추적할 때.
- **Bad:** 진행 상황을 머릿속이나 스크롤백으로 추적한다.
- **Good:** "Can you make a `todo.md` that I can use as a checklist? Be thorough."
- **왜:** 상태를 외부화한다. 무상태 LLM은 긴 시퀀스에서 뭘 끝냈는지 잃는다. 지속되는 todo.md가 사람과 모델 양쪽에 안정된 장부를 줘서 다단계 실행을 온-레일·재개 가능하게 만든다.
- **출처:** Harper Reed, My LLM codegen workflow — https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/

## 시니어 역할 코드리뷰 (senior-dev-review-pass)
- **단계:** 검증기
- **언제:** 특히 레거시 코드베이스에서, 산출물을 다음 사람이 쓸 수 있는 형태로 리뷰할 때.
- **Bad:** "내 코드 리뷰해줘." (역할·형식 없음 → 두루뭉술한 칭찬.)
- **Good:** "You are a senior developer. Your job is to do a thorough code review of this code. You should write it up and output markdown. Include line numbers, and contextual info. Your code review will be passed to another teammate, so be thorough. Think deeply before writing the code review. Review every part, and don't hallucinate."
- **왜:** 역할 지정("senior developer") + 하류 소비자 명시("passed to another teammate") + 형식 제약(markdown, line numbers)이 기준을 올리고 출력을 실행 가능하게 한다. "don't hallucinate" + "think deeply"가 실제 코드에서 날조를 억제한다. repomix로 전체 코드베이스를 컨텍스트로 넣는 것과 짝.
- **출처:** Harper Reed, My LLM codegen workflow — https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/

## 누락 테스트를 이슈 형식으로 (missing-tests-as-issues)
- **단계:** 검증루프
- **언제:** 부족한 테스트를 찾아 바로 다음 단계(개발자·에이전트)가 집어갈 작업 항목으로 만들 때.
- **Bad:** "테스트 뭐 빠졌어?" (비정형 답 → 다시 포맷·라우팅해야 함.)
- **Good:** "You are a senior developer. Your job is to review this code, and write out a list of missing test cases, and code tests that should exist. You should be specific, and be very good. Do Not Hallucinate. Think quietly to yourself, then act - write the issues. The issues will be given to a developer to executed on, so they should be in a format that is compatible with github issues"
- **왜:** 출력을 GitHub 이슈 형식으로 못 박으면 다음 단계가 바로 소비할 수 있다. 청중을 명시("given to a developer to execute on")하면 구체성이 강제되고, 리뷰가 곧바로 디스패치 가능한 백로그가 된다.
- **출처:** Harper Reed, My LLM codegen workflow — https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/
