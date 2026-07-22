# 03 — Peter Steinberger (steipete)

> 출처: steipete.me (2025) — "Just Talk To It", "The Future of Vibe Coding", "Command your Claude Code Army" + 공개 AGENTS.MD.
> PSPDFKit 창업자. 채점: 원문 중 / 원리 상 / 워크플로우 중 / 결과물 상 → 상 2개 = 입장.
> 강점: WHY 설명이 촘촘하고, 실제 출시물이 구체적(VibeMeter·VibeTunnel, ~300k LOC 모노레포 데일리드라이버).
> 원문은 vibe-coding 포스트의 스펙 프롬프트 + AGENTS.MD 규칙이 복붙 가능.

---

## 코드 전에 논의 강제 (discuss-before-code)
- **단계:** 스코핑
- **언제:** 에이전트가 곧바로 큰 diff를 쓰기 전에, 결정 지점을 값싼 단계(말)에서 잡고 싶을 때.
- **Bad:** "X 구현해." (에이전트가 돌진 → 큰 diff를 사후에 리뷰.)
- **Good:** "let's discuss" / "give me options before making changes" / "give me a few options before making changes"
- **왜:** 지시 준수가 강한 모델은 별도 plan mode가 필요 없다. 평문 게이트("let's discuss")가 실행 전 승인 대기를 만들어, 값싼 단계(단어)에서 조종하고 비싼 단계(diff 되돌리기)를 피한다.
- **출처:** Peter Steinberger, Just Talk To It — https://steipete.me/posts/just-talk-to-it

## 모델별 톤 조절 (model-specific-tone)
- **단계:** 컨텍스트주입
- **언제:** 하드 제약을 반드시 지키게 하려는데, 모델마다 반응이 다를 때.
- **Bad:** 모든 모델에 같은 톤으로 지시.
- **Good:** Claude엔 — "🚨 SCREAMING ALL-CAPS 🚨 commands"로 실패의 무게를 강조("if it runs command X … ultimate failure"). GPT-5엔 — "drop all of that and just use words like a human."
- **왜:** 모델별 강조법. 대문자/스테이크는 Claude에게 하드 제약의 현저성을 올리지만, GPT-5는 오히려 불안정해져 중립 산문이 필요하다. 습관이 아니라 하니스에 맞춰 톤을 튜닝하라.
- **출처:** Peter Steinberger, Just Talk To It — https://steipete.me/posts/just-talk-to-it

## 스펙을 다른 모델로 교차 비평 (spec-cross-critique)
- **단계:** PRD
- **언제:** AI가 쓴 스펙을 그대로 믿지 않고, 빌드 전에 구멍을 드러낼 때.
- **Bad:** 첫 AI 스펙을 받아들여 바로 구현.
- **Good:** (스펙을 **별개** 모델 인스턴스에 넣고) "You are an AI tasked with implementing this spec in one go. Before you start, what questions do you have? What's unclear? What's missing for you to build this successfully?" → 비평을 원 스펙에 다시 반영.
- **왜:** 저자 맥락이 없는 새 인스턴스는 저자-에이전트가 합리화한 구멍을 찾는다. "implement in one go" 프레이밍이 모든 모호함을 앞에서 드러내게 강제한다. (스펙 단계 리뷰 — 코드 단계는 [[consult-the-oracle]], diff 단계는 [[adversarial-review-subagent]].)
- **출처:** Peter Steinberger, The Future of Vibe Coding — https://steipete.me/posts/2025/the-future-of-vibe-coding

## 저스펙 후 렌더 보고 다듬기 (under-specify-then-morph)
- **단계:** 솔루션깎기
- **언제:** 시각/UI 작업에서, 픽셀을 사전 지정하지 않고 렌더 결과에 반응하며 수렴할 때.
- **Bad:** 프롬프트에 레이아웃 픽셀을 과잉 지정.
- **Good:** "Make this settings screen look more like a native, clean macOS settings panel, using standard SwiftUI controls." / (버그 위임) "It looks like the CSS for the settings dialog isn't loading correctly. Please investigate and fix." — 의도적으로 저스펙하고 브라우저 라이브 업데이트를 보며 반복.
- **왜:** 눈앞에 렌더된 결과에 반응하는 편이 눈감고 지정하는 것보다 싸다. 시각 작업은 사전 스펙보다 반복이 더 빨리 수렴한다.
- **출처:** Peter Steinberger, The Future of Vibe Coding — https://steipete.me/posts/2025/the-future-of-vibe-coding

## 블래스트 반경 산정 (blast-radius-sizing)
- **단계:** 구현위임
- **언제:** 여러 에이전트(그가 3~8개)를 같은 폴더에서 병렬로 돌리며 커밋을 원자적으로 유지할 때.
- **Bad:** 작업 크기를 재지 않고 던져서 커밋이 뒤엉킴.
- **Good:** 각 작업 전에 "blast radius"(소요 시간 + 건드릴 파일 수)를 추정해 작업을 원자적 커밋 단위로 쪼갠다. 손 떼려면 — "Queue up continue messages if you wanna go away and just see it done."
- **왜:** 처리량은 에이전트별 완벽함이 아니라 병렬성에서 온다. 블래스트 반경으로 크기를 미리 재고 원자 커밋을 유지하면, 같은 폴더 충돌도 되돌릴 수 있어 worktree 오버헤드 없이 회복 가능하다.
- **출처:** Peter Steinberger, Just Talk To It — https://steipete.me/posts/just-talk-to-it
