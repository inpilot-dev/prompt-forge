# 05 — Anthropic Claude Code Best Practices

> 출처: Anthropic 공식 문서 "Claude Code Best Practices" — https://code.claude.com/docs/en/best-practices
> 채점: 원문 상 / 원리 상 / 워크플로우 상 / 결과물 하 → 상 3개 = 입장.
> ⚠️ 플래그: **개인 고수의 공개가 아니라 벤더 공식 문서**(자사 툴 시연). 결과물 축이 약한(하) 이유 = 실제 출시 아티팩트 없이 이상화된 예시.
> 그럼에도 원문 프롬프트가 복붙 가능하고 워크플로우 분류가 가장 체계적이라 재료로 채택. 중복 제외: interview-me-then-spec은 [[reverse-interview]]와 동일하여 미이식.

---

## 탐색-계획-구현-커밋 (explore-plan-code-commit)
- **단계:** 킥오프
- **언제:** 곧바로 코딩하면 엉뚱한 문제를 풀 위험이 있을 때. 4단계로 리서치와 실행을 분리.
- **Bad:** "the login bug" / 바로 코딩 돌입.
- **Good:** (탐색) "read /src/auth and understand how we handle sessions and login. also look at how we manage environment variables for secrets." → (계획) "I want to add Google OAuth. What files need to change? What's the session flow? Create a plan." → (구현) "implement the OAuth flow from your plan. write tests for the callback handler, run the test suite and fix any failures." → (커밋) "commit with a descriptive message and open a PR"
- **왜:** "Letting Claude jump straight to coding can produce code that solves the wrong problem." 탐색→계획을 실행과 분리하면 방향 오류를 앞에서 잡는다.
- **출처:** Anthropic, Claude Code Best Practices — https://code.claude.com/docs/en/best-practices

## 합격/불합격 체크 부여 (verification-loop)
- **단계:** 검증루프
- **언제:** 구현 프롬프트에 통과/실패를 판정할 구체적 기준을 함께 줄 때.
- **Bad:** "implement a function that validates email addresses"
- **Good:** "write a validateEmail function. example test cases: user@example.com is true, invalid is false, user@.com is false. run the tests after implementing"
- **왜:** "Claude stops when the work looks done. Without a check it can run, 'looks done' is the only signal... Give Claude something that produces a pass or fail, and the loop closes on its own." 주장 대신 증거를 보이게 하라. (리뷰 루브릭을 스킬로 굳히는 [[build-grader-first]]와 짝 — 이쪽은 구현 프롬프트에 인라인 합격조건.)
- **출처:** Anthropic, Claude Code Best Practices — https://code.claude.com/docs/en/best-practices

## 증상 말고 근본원인 (root-cause-fix)
- **단계:** 구현위임
- **언제:** 버그를 억누르지 말고 근본 원인을 고치고 검증하게 할 때.
- **Bad:** "the build is failing"
- **Good:** "the build fails with this error: [paste error]. fix it and verify the build succeeds. address the root cause, don't suppress the error"
- **왜:** 에러를 억제하는 임시방편 대신, 근본 수정 + 검증을 강제해 지속 가능한 해결을 만든다.
- **출처:** Anthropic, Claude Code Best Practices — https://code.claude.com/docs/en/best-practices

## 컨텍스트 위생 (context-hygiene)
- **단계:** 컨텍스트주입
- **언제:** 한 세션에서 같은 문제를 두 번 넘게 교정했을 때. 실패한 시도로 맥락이 오염됨.
- **Bad:** 오염된 세션에서 계속 교정을 쌓는다("kitchen sink session").
- **Good:** (규칙) "After two failed corrections, /clear and write a better initial prompt incorporating what you learned."
- **왜:** "A clean session with a better prompt almost always outperforms a long session with accumulated corrections." 컨텍스트가 근본 제약이므로, 배운 것을 담은 새 초기 프롬프트로 리셋하는 편이 낫다.
- **출처:** Anthropic, Claude Code Best Practices — https://code.claude.com/docs/en/best-practices

## 조사는 서브에이전트에 위임 (delegate-research-to-subagents)
- **단계:** 리서치위임
- **언제:** 메인 대화를 깨끗이 유지하면서 열린-끝 조사를 시킬 때.
- **Bad:** 메인 컨텍스트에서 직접 "인증 시스템 조사해줘"(무한 탐색이 컨텍스트를 채움).
- **Good:** "Use subagents to investigate how our authentication system handles token refresh, and whether we have any existing OAuth utilities I should reuse."
- **왜:** "Subagents run in separate context windows and report back summaries." 컨텍스트가 근본 제약이므로 비싼 탐색을 격리된 창으로 밀어내고 요약만 받는다. (Huntley의 [[subagents-as-scheduler]]는 이 원리의 아키텍처적 극단판.)
- **출처:** Anthropic, Claude Code Best Practices — https://code.claude.com/docs/en/best-practices

## 새 맥락의 적대적 리뷰 (adversarial-review-subagent)
- **단계:** 검증기
- **언제:** diff가 계획을 실제로 구현했는지, 편향 없는 새 맥락에서 검증할 때.
- **Bad:** 코드를 쓴 세션이 자기 diff를 리뷰.
- **Good:** "Use a subagent to review the rate limiter diff against PLAN.md. Check that every requirement is implemented, the listed edge cases have tests, and nothing outside the task's scope changed. Report gaps, not style preferences."
- **왜:** "A reviewer running in a fresh subagent context sees only the diff and the criteria you give it, not the reasoning that produced the change, so it evaluates the result on its own terms." 과다보고 방지 위해 정확성·요구사항 갭만 보고하게 지시. (스펙 단계는 [[spec-cross-critique]], 코드 품질은 [[consult-the-oracle]].)
- **출처:** Anthropic, Claude Code Best Practices — https://code.claude.com/docs/en/best-practices
