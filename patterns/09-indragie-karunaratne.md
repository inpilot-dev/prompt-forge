# 09 — Indragie Karunaratne

> 출처: indragie.com — "I shipped a macOS app built entirely by Claude Code" (https://www.indragie.com/blog/i-shipped-a-macos-app-built-entirely-by-claude-code).
> macOS 개발자, MCP 디버거 앱 `Context` 제작자. 루브릭 4항목 전부 상.
> 검증 근거: `Context` 앱 20k줄 중 손코딩 <1k, 2,000줄 릴리스 자동화까지 CC로. verbatim 트리거 문구·CLAUDE.md 스니펫·read+summarize 템플릿 공개.
> 관통 원리: "context engineering > prompt engineering — 요즘 모델은 지저분한 입력도 처리한다. 진짜 제약은 컨텍스트 창이다."

---

## 읽고-요약시켜 이해 검증 (read-then-summarize)
- **단계:** 컨텍스트주입
- **언제:** 낯선 코드/외부 문서에 의존하는 작업 전, 모델이 맥락을 실제로 흡수했는지 구현 전에 확인하고 싶을 때.
- **Bad:** "이 기능 어떻게 돼 있는지 보고 비슷하게 구현해줘."
- **Good:** "Read [파일들] to learn how [기존 기능] is implemented. Then read [외부 문서 URL]. After reading these sources, summarize what you've learned."
- **왜:** 요약을 시키면 컨텍스트가 부족한지 즉시 드러난다 — 요약을 못 하거나 얕으면 그 상태로 구현시켜봤자 환각이 난다. 구현 전에 이해를 게이트로 검증하는 값싼 체크포인트. [[block-early-divergence]]의 이해-확인판.
- **출처:** Indragie Karunaratne — https://www.indragie.com/blog/i-shipped-a-macos-app-built-entirely-by-claude-code

## 사고 강도 계단식 조절 (escalating-think)
- **단계:** 스코핑
- **언제:** 문제 난이도에 맞춰 추론 예산을 명시적으로 올리고, 계획 승인 전 구현을 막고 싶을 때.
- **Bad:** "잘 생각해서 제대로 만들어줘."
- **Good:** "think" → 어려우면 "think hard" → "think harder" → "ultrathink" + "Make a plan first, don't implement until the plan is accepted."
- **왜:** 사고 예산을 감이 아니라 단어로 계단식 지정해 쉬운 일에 과추론·어려운 일에 저추론을 막는다. "계획 먼저, 승인 전 구현 금지"를 붙여 발산을 계획 단계에서 잡는다.
- **출처:** Indragie Karunaratne — https://www.indragie.com/blog/i-shipped-a-macos-app-built-entirely-by-claude-code

## UI는 제안 메뉴 먼저 (design-suggestion-menu)
- **단계:** 솔루션깎기
- **언제:** UI/디자인을 다듬을 때, "예쁘게 해줘"처럼 모델이 임의로 하나 밀어붙이는 걸 막고 싶을 때.
- **Bad:** "이 UI 좀 예쁘게 만들어줘."
- **Good:** "Come up with suggestions for how to make this UI more beautiful" → 랭크된 후보 목록을 받고 → 골라서 적용. 스크린샷을 ⌘V로 붙여 시각 피드백 루프.
- **왜:** 바로 실행시키면 취향 하나에 갇힌다. 제안을 랭크로 먼저 받으면 지형이 펼쳐지고 내가 설계자로서 고를 수 있다. [[options-menu-research]]의 디자인판.
- **출처:** Indragie Karunaratne — https://www.indragie.com/blog/i-shipped-a-macos-app-built-entirely-by-claude-code
