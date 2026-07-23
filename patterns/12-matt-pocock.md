# 12 — Matt Pocock

> 출처: YouTube "Full Walkthrough: Workflow for AI Coding — Matt Pocock" (https://www.youtube.com/watch?v=-QFHIoCo-Ko).
> TypeScript 에듀케이터(Total TypeScript). 루브릭: 원문 중(grill-me 전문 미확보, 절차는 명확) / 원리 상 / 워크플로우 상 / 결과물 상 = 상 3, 입장.
> 검증 근거: 라이브 데모로 준비→실행 루프 재현. grill-me 스킬은 repo 상주.

---

## grill-me 인터뷰를 1단계로 (grill-me-first)
- **단계:** 킥오프
- **언제:** 러프한 아이디어를 던질 때, 구현 전에 모호함을 강제로 걷어내고 싶을 때.
- **Bad:** "이거 만들어줘" (모호한 채 바로 구현 진입).
- **Good:** 모든 기능의 1단계로 `grill-me` 스킬 실행 — AI가 **한 번에 한 질문씩** 집요하게 캐물어(interview) 스코프가 concrete해질 때까지 반복 → 결과를 문서로 굳힘. 짧은 CC 프롬프트(스킬)로 repo에 상주.
- **왜:** 한 번에 한 질문씩 캐묻게 하면 사람이 미처 정하지 못한 결정이 표면화되고, 그 답이 스펙 문서가 된다. [[one-question-at-a-time-honing]]을 "매 기능 1단계 강제"로 굳힌 형태.
- **출처:** Matt Pocock — https://www.youtube.com/watch?v=-QFHIoCo-Ko

## compact 금지·항상 clear (always-clear-never-compact)
- **단계:** 컨텍스트주입
- **언제:** 긴 세션에서 컨텍스트가 늘어질 때, 요약 압축 대신 결정론적 리셋을 원할 때.
- **Bad:** 컨텍스트가 차면 `/compact`로 요약 압축하고 계속.
- **Good:** "Memento" 규칙 — **compact 금지, 항상 `/clear`로 fresh context**. 필요한 상태는 문서로 다시 주입.
- **왜:** compact 요약은 비결정적이고 조용히 열화된다("dumb zone"). 매번 시스템 프롬프트 상태로 리셋하면 반복가능·고성능 상태가 유지된다. [[context-hygiene]]·[[session-reonboarding]]의 하드룰판.
- **출처:** Matt Pocock — https://www.youtube.com/watch?v=-QFHIoCo-Ko

## 구현/리뷰 모델 분리 + fresh 리뷰 (implement-review-model-split)
- **단계:** 검증기
- **언제:** 구현물을 리뷰시킬 때, 같은 세션에서 자기 코드를 자평하는 열화를 피하고 싶을 때.
- **Bad:** 구현한 그 세션에서 "이 코드 리뷰해줘."
- **Good:** **구현=Sonnet / 리뷰=Opus**, 그리고 리뷰는 반드시 **fresh context**에서(같은 세션 금지).
- **왜:** 같은 맥락에서 리뷰하면 모델이 자기 결정을 방어하고 "dumb zone" 열화가 겹친다. 다른 모델·새 맥락으로 리뷰하면 적대적 시선이 생긴다. [[adversarial-review-subagent]]에 모델 역할 분리를 결합.
- **출처:** Matt Pocock — https://www.youtube.com/watch?v=-QFHIoCo-Ko
