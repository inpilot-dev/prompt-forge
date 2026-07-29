# 14 — Boris Cherny

> 출처: X 스레드 @bcherny 1차 https://x.com/bcherny/status/2007179832300581177 · **2차(신규 확보) https://x.com/bcherny/status/2017742741636321619**
> + 본인 커밋 커맨드 파일 https://github.com/anthropics/claude-code/blob/main/.claude/commands/commit-push-pr.md (author `bcherny`, 2025-08-05, 이후 무수정)
> Claude Code 창시자/책임자(Anthropic).
> 루브릭: 원문 **상**(2026-07-29 재추적 — 커맨드 파일 전문 + 복붙용 지시문 확보) / 원리 상 / 워크플로우 상 / 결과물 **중**(팀 CLAUDE.md는 여전히 비공개 404, 스크린샷 수준) = **상 3, 경계선 해제**.
> 이력: 1차 채굴 시 "커맨드 본문 전문 미공개"로 원문 중(상 2) 경계선이었다. GitHub 저작자 대조로 본인 커밋임을 확정하고 전문을 확보해 승격.
> ⚠️ baseline #5 Anthropic 공식문서(CLAUDE.md·verify 게이트·Explore→Plan→Code)와 원리 일부 중복 — 겹치는 부분은 제외하고 "갱신 트리거" 심화만 채택.
> ⚠️ 2차 스레드는 본인 습관이 아니라 **그가 공개한 Claude Code 팀 팁**이다("sourced directly from the Claude Code team… The way the team uses Claude is different than how I use it"). 아래 해당 패턴에 표기.

---

## 리뷰를 메모리로 되먹임 (review-to-memory)
- **단계:** 검증루프
- **언제:** PR 리뷰나 코드 리뷰에서 모델의 실수를 발견했을 때, 코드만 고치고 끝내지 않고 재발을 막고 싶을 때.
- **Bad:** 리뷰에서 틀린 부분을 발견 → 그 코드만 수정하고 넘어감(다음에 또 같은 실수).
- **Good:** 팀이 **CLAUDE.md 하나를 git에 체크인해 공유**하고 주 여러 번 갱신한다 — "Anytime we see Claude do something incorrectly we add it to the CLAUDE.md, so Claude knows not to do it next time." 리뷰 중엔 동료 PR에 **@claude를 태그해 규칙 갱신을 PR의 일부로** 만든다(GitHub action `/install-github-action`).
  그리고 개별 정정마다 **이 한 줄을 끝에 붙인다**(팀 팁):
  > "Update your CLAUDE.md so you don't make that mistake again."
  > — "Claude is eerily good at writing rules for itself. Ruthlessly edit your CLAUDE.md over time. Keep iterating until Claude's mistake rate measurably drops."
- **왜:** 실수를 일회성 수정이 아니라 영구 규칙으로 승격시키면 같은 오류가 반복되지 않는다. 규칙을 **모델 자신에게 쓰게 하는 것**이 핵심 — 사람이 규칙 문구를 고민하는 비용이 사라지고, 방금 틀린 맥락이 그대로 규칙에 반영된다. 완료 판정은 느낌이 아니라 **오류율이 눈에 띄게 떨어질 때까지**다. [[persistent-context-file]]이 *무엇을 담느냐*라면 이건 *언제 갱신하느냐*의 트리거이고, [[mistake-to-guardrail]]의 메모리판.
- **출처:** Boris Cherny (@bcherny) — https://x.com/bcherny/status/2007179832300581177 (4/·5/) + 팀 팁 https://x.com/bcherny/status/2017742741636321619

## 반복 명령을 precompute 커맨드로 (precompute-slash-command)
- **단계:** 구현위임
- **언제:** 자주 쓰는 inner-loop 작업(커밋·PR 등)을 슬래시 커맨드로 고정하되, 매번 상태를 다시 묻지 않게 하고 싶을 때.
- **Bad:** 매번 "git status 보고, 스테이징하고, 커밋 메시지 쓰고, 푸시하고, PR 열어줘"를 타이핑. 모델이 상태를 되묻거나 추측한다.
- **Good:** 본인이 커밋한 `.claude/commands/commit-push-pr.md` 전문 — 하루에 수십 번 쓴다고 밝힌 커맨드다:
  ```markdown
  ---
  allowed-tools: Bash(git checkout --branch:*), Bash(git add:*), Bash(git status:*), Bash(git push:*), Bash(git commit:*), Bash(gh pr create:*)
  description: Commit, push, and open a PR
  ---

  ## Context

  - Current git status: !`git status`
  - Current git diff (staged and unstaged changes): !`git diff HEAD`
  - Current branch: !`git branch --show-current`

  ## Your task

  Based on the above changes:
  1. Create a new branch if on main
  2. Create a single commit with an appropriate message
  3. Push the branch to origin
  4. Create a pull request using `gh pr create`
  5. You have the capability to call multiple tools in a single response. You MUST do all of the above in a single message. Do not use any other tools or do anything else. Do not send any other text or messages besides these tool calls.
  ```
- **왜:** 세 장치가 각각 다른 왕복을 없앤다. ① **inline bash precompute**(`!`git status``)로 모델이 상태를 추측하거나 되묻지 않고 실제 현재 상태 위에서 시작한다 — 본인 표현으로 "to make the command run quickly and avoid back-and-forth with the model". ② **`allowed-tools` 프론트매터**로 이 커맨드가 쓸 명령을 미리 허용해 승인 왕복을 없앤다. ③ **"MUST do all of the above in a single message… Do not send any other text"** 로 중간 보고·확인 질문을 차단해 한 턴에 끝낸다. [[prompt-as-file-template]]에 상태 선-계산과 권한 사전허용을 결합한 형태.
- **출처:** Boris Cherny (@bcherny) — https://github.com/anthropics/claude-code/blob/main/.claude/commands/commit-push-pr.md (본인 커밋, 무수정) + 스레드 7/ https://x.com/bcherny/status/2007179832300581177

## PR 열기 전 내가 심문당한다 (grill-before-pr)
- **단계:** 검증기
- **언제:** 변경분은 다 만들었고 이제 PR을 열려는 순간. 내가 이 변경을 실제로 이해하고 있는지 확신이 안 설 때.
- **Bad:** 다 됐다 싶으면 PR을 연다. 리뷰어(사람)가 첫 질문을 던질 때 비로소 내가 모르는 구석이 드러난다.
- **Good:** 역할을 뒤집어 **내가 심문 대상이 되고, 통과 전에는 PR을 못 열게** 막는다. 원문 항목 6a 전문:
  > **6. Level up your prompting**
  >
  > a. Challenge Claude. Say "Grill me on these changes and don't make a PR until I pass your test." Make Claude be your reviewer.  Or, say "Prove to me this works" and have Claude diff behavior between main and your feature branch
- **왜:** ⚠️ **원문에 메커니즘 설명은 없다**(있는 건 "Challenge Claude" · "Make Claude be your reviewer" 두 조각뿐). 아래는 라이브러리 자체 해석이다.
  이 문장의 고유함은 **심문의 방향과 시점**에 있다. [[grill-me-first]](12)는 킥오프에서 *AI가 사람을 인터뷰해 스펙을 만드는* 도구다 — 아직 아무것도 안 만든 상태고, 산출물은 합의된 이해다. 이건 반대편 끝이다: **이미 만들어진 diff를 놓고, 통과/불통과 판정이 나오며, 떨어지면 PR을 안 연다.** 스펙 생성 도구가 아니라 **출구 차단기**다.
  [[evidence-before-claim]](17)과도 방향이 다르다. 그쪽은 *에이전트가* 증거를 내놓아야 하고, 이건 *사람이* 시험을 통과해야 한다. 자기 변경분을 설명하지 못하면 그건 리뷰어에게 넘길 물건이 아니라는 뜻이고, 그 사실을 **사람 리뷰어의 시간을 쓰기 전에** 알아내는 게 이득이다.
  후반부 "Prove to me this works" + main↔feature 동작 diff는 같은 항목이지만 [[evidence-before-claim]]·[[regression-delta-debug]]와 중복이라 별도 패턴으로 세우지 않았다. 짝으로 함께 쓰면 된다.
- **출처:** Boris Cherny (@bcherny)가 공개한 **Claude Code 팀 팁** — https://x.com/bcherny/status/2017742741636321619 (항목 6a)

## 알고 난 뒤 갈아엎기 (scrap-and-reimplement-with-hindsight)
- **단계:** 솔루션깎기
- **언제:** 고치긴 했는데 결과가 어정쩡할 때. 패치를 덧대는 대신 이번 시도로 얻은 지식을 살려 다시 짜고 싶을 때.
- **Bad:** 어정쩡한 구현 위에 계속 수정 요청을 쌓는다 → 첫 시도의 잘못된 뼈대가 그대로 남는다.
- **Good:** > "Knowing everything you know now, scrap this and implement the elegant solution"
- **왜:** 첫 구현은 문제를 모르는 상태의 산물이고, 그걸 패치로 덮으면 **탐색으로 얻은 지식이 잘못된 구조에 갇힌다.** "지금 아는 걸 다 아는 상태에서"라는 앞머리가 축적된 맥락은 유지하고 산출물만 버리게 만든다 — 컨텍스트를 날리는 [[checkpoint-rollback]]과 다르다. [[conversational-refinement]](그 자리 수정)·[[narrow-scope-iteration]](좁은 수술)과는 **정반대 방향**이며, 언제 그쪽을 포기할지의 판정 문장이다.
- **출처:** Boris Cherny (@bcherny) — https://x.com/bcherny/status/2017742741636321619 (⚠️ Claude Code 팀 팁 공개분)
