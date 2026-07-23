# 14 — Boris Cherny

> 출처: X 스레드 @bcherny (https://x.com/bcherny/status/2007179832300581177) + 코버리지 https://venturebeat.com/technology/the-creator-of-claude-code-just-revealed-his-workflow-and-developers-are.
> Claude Code 창시자/책임자(Anthropic). 루브릭: 원문 중(커맨드 이름·절차 공개, 본문 전문 미공개) / 원리 상 / 워크플로우 상 / 결과물 중 = 상 2, **경계선 입장**.
> ⚠️ baseline #5 Anthropic 공식문서(CLAUDE.md·verify 게이트·Explore→Plan→Code)와 원리 일부 중복.
> 이식 범위: 겹치는 부분은 제외하고, **기존 패턴의 "갱신 트리거"를 심화하는 2개만** 좁혀 채택.

---

## 리뷰를 메모리로 되먹임 (review-to-memory)
- **단계:** 검증루프
- **언제:** PR 리뷰나 코드 리뷰에서 모델의 실수를 발견했을 때, 코드만 고치고 끝내지 않고 재발을 막고 싶을 때.
- **Bad:** 리뷰에서 틀린 부분을 발견 → 그 코드만 수정하고 넘어감(다음에 또 같은 실수).
- **Good:** "Claude가 뭘 틀리면 그걸 CLAUDE.md에 추가해 다음엔 안 하게 한다." PR 리뷰 중 오류를 보면 코드만 고치지 말고 **@claude를 태그해 규칙 파일(CLAUDE.md) 갱신을 PR의 일부로** 만든다.
- **왜:** 실수를 일회성 수정이 아니라 영구 규칙으로 승격시키면 같은 오류가 반복되지 않는다. [[persistent-context-file]]이 *무엇을 담느냐*라면, 이건 *언제 갱신하느냐*(리뷰에서 실수 발견 시)의 트리거. [[mistake-to-guardrail]]의 메모리판.
- **출처:** Boris Cherny (@bcherny) — https://x.com/bcherny/status/2007179832300581177

## 반복 명령을 precompute 커맨드로 (precompute-slash-command)
- **단계:** 구현위임
- **언제:** 자주 쓰는 inner-loop 작업(커밋·PR 등)을 슬래시 커맨드로 고정하되, 매번 상태를 다시 묻지 않게 하고 싶을 때.
- **Bad:** 매번 "git status 보고, 스테이징하고, 커밋 메시지 쓰고, 푸시하고, PR 열어줘"를 타이핑.
- **Good:** 반복 명령을 `.claude/commands/`의 슬래시 커맨드로 고정하되 **inline bash로 상태를 미리 계산**해 넣는다 — 예 `/commit-push-pr`가 실행 시점의 `git status`를 커맨드 안에서 선-계산. 커맨드는 git 체크인해 팀·Claude가 공유.
- **왜:** inline bash precompute를 넣으면 모델이 상태를 추측하거나 되묻지 않고 실제 현재 상태 위에서 동작한다. 반복 inner-loop의 왕복이 사라진다. [[prompt-as-file-template]]에 상태 선-계산을 결합.
- **출처:** Boris Cherny (@bcherny) — https://x.com/bcherny/status/2007179832300581177
