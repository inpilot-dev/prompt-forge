# 04 — Mitchell Hashimoto

> 출처: mitchellh.com "My Non-Trivial Vibing Workflow"(2025) + 인터뷰 노트. HashiCorp 공동창업자, Ghostty 터미널 제작자.
> 채점: 원문 상 / 원리 상 / 워크플로우 상 / 결과물 상 → 상 4개 = 입장(앵커 출처).
> 검증: 실제 출시 PR(Ghostty #9116, 21파일) + 공개 통계(16세션 / 2일 / ~8h / $15.98). 실 프로덕션 코드에서 검증된 패턴.

---

## 스캐폴드 후 채우기 (scaffold-then-fill)
- **단계:** 구현위임
- **언제:** 내 아키텍처 의도를 강제한 채 구현을 위임할 때.
- **Bad:** "Update 기능 전체 만들어줘." (에이전트가 자기 마음대로 설계.)
- **Good:** 함수 시그니처 + TODO 주석 + 서술적 이름만 채운 불완전 파일을 먼저 만들고 → "fill-in-the-blank / draw-the-rest-of-the-owl" 위임. 실제 예: "Complete the @macos/Sources/Features/Update/UpdateDriver.swift. Read the Sparkle documentation as necessary."
- **왜:** 이름·시그니처가 내 설계 의도를 인코딩한다. 에이전트가 자기 아키텍처를 발명하는 대신 내 골격에 맞춰 본문을 채우게 된다. ([[function-signature-spec]]의 파일 스캐폴딩판.)
- **출처:** Mitchell Hashimoto, Non-Trivial Vibing — https://mitchellh.com/writing/non-trivial-vibing

## 좁은 범위 수술 편집 (narrow-scope-iteration)
- **단계:** 솔루션깎기
- **언제:** 큰 리팩터를 통째 위임하지 않고, 리뷰 가능한 작은 편집으로 쪼갤 때.
- **Bad:** "Update 기능 리팩터해줘." (거대 diff, 리뷰 불가.)
- **Good:** "Let's move the pill background, foreground, and badge functions from @.../UpdateAccessoryView.swift to @.../UpdateViewModel.swift." / "Turn each @.../UpdatePopoverView.swift case into a dedicated fileprivate Swift view that takes the typed value as its parameter so that we can remove the guards."
- **왜:** 작은 청크는 리뷰 가능하다. 커밋을 "save point"로 남겨서 방향이 어긋나면 리셋한다. 정확히 무엇을→어디로 옮길지 지정해 애매함을 제거.
- **출처:** Mitchell Hashimoto, Non-Trivial Vibing — https://mitchellh.com/writing/non-trivial-vibing

## 오라클 상담(읽기 전용 리뷰) (consult-the-oracle)
- **단계:** 검증기
- **언제:** 코딩 에이전트가 자기 작업을 자평하지 않게, 코드를 안 건드리는 전략적 리뷰가 필요할 때.
- **Bad:** 구현하던 에이전트가 자기 결과물을 채점.
- **Good:** "Are there any other improvements you can see to be made with the @macos/Sources/Features/Update feature? Don't write any code. Consult the oracle. Consider parts of the code that can also get more unit tests added."
- **왜:** 더 느리고 비싼 읽기 전용 서브에이전트가 코드를 안 건드리고 전략적 비평만 한다 — 구현하지 않은 새 리뷰어. (스펙 리뷰는 [[spec-cross-critique]], diff 컴플라이언스는 [[adversarial-review-subagent]].)
- **출처:** Mitchell Hashimoto, Non-Trivial Vibing — https://mitchellh.com/writing/non-trivial-vibing

## 반슬롭 클린업 세션 (manual-cleanup-pass)
- **단계:** 검증루프
- **언제:** AI 출력을 이해하지 못한 채 그대로 출시하지 않도록, 별도 정리 세션을 둘 때.
- **Bad:** AI 출력을 그대로 받아 출시.
- **Good:** (원리 인용) "The cleanup step is really important. To cleanup effectively you have to have a pretty good understanding of the code, so this forces me to not blindly accept AI-written code." + "Please don't ever ship AI-written code without a thorough manual review." (예: optional 범벅 struct를 tagged union으로 손수 전환해 이후 세션을 성공하게 셋업.)
- **왜:** 재구조화·이름변경·문서화 전용 세션이 사람의 코드 이해를 강제한다. 이해 못 하는 코드는 출시하지 않는다.
- **출처:** Mitchell Hashimoto, Non-Trivial Vibing — https://mitchellh.com/writing/non-trivial-vibing

## 실수를 가드레일로 (mistake-to-guardrail)
- **단계:** 검증루프
- **언제:** 에이전트가 같은 실수를 반복할 때, 대화로 매번 고치지 않고 영구 방어를 심을 때.
- **Bad:** 같은 실수를 볼 때마다 대화로 재교정.
- **Good:** (인터뷰 노트, 요약) 에이전트가 실수하면 그걸 자가검증할 테스트 하니스/검증 스크립트/lint 규칙을 만들고, 그 규칙을 CLAUDE.md / agents.md에 추가해 재발을 막는다.
- **왜:** 일회성 교정을 영구 가드레일로 바꿔 시간에 따라 복리로 쌓인다. (평가 기준을 갱신하는 [[update-the-rubric-itself]]와 같은 정신 — 이쪽은 lint/테스트/규칙 파일로 고정.)
- **출처:** Mitchell Hashimoto, 인터뷰 노트 — https://www.samuelliedtke.com/blog/notes-on-agentic-engineering-in-action-with-mitchell-hashimoto/
