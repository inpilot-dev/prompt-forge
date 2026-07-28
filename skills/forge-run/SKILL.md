---
name: forge-run
description: Use when the user runs `/forge-run <프롬프트>`, says "다듬어서 바로 실행해 / forge하고 돌려 / forge-run", or wants a rough prompt improved AND executed in one shot. Silently forges the rough prompt into a GOOD prompt using shared patterns/, shows it, then executes it in this session. Unlike prompt-forge (which never executes), forge-run does the task.
---

# forge-run (다듬고 바로 실행)

거지 프롬프트를 GOOD 프롬프트로 다듬은 뒤 **곧바로 이 세션에서 실행**한다.
prompt-forge와 재료(`patterns/`)를 공유하지만, forge가 멈추는 자리에서 forge-run은 실행한다.

> **forge와의 차이:** prompt-forge는 다듬고 **멈춘다**(복붙용). forge-run은 다듬고 **실행한다**.
> 이 스킬만 실행하며, 원본 prompt-forge는 건드리지 않는다. 실행은 지금 이 Claude 세션이 한다(외부 LLM 아님).

## 트리거
- `/forge-run <프롬프트>`
- "다듬어서 바로 실행해", "forge하고 돌려"
원본 프롬프트가 없으면 한 줄로: "실행할 프롬프트를 붙여줘."

## 절차

### 1. 다듬기 (prompt-forge 방식, 조용히)
prompt-forge와 동일 규칙으로 다듬는다:
- **크기 판단** small(단일 작업) / large(프로젝트급). 애매하면 small.
- **슬롯 검사** small: 목표·완료판단 / large: 목표·평가자·산출물.
- **패턴 선택** `patterns/_INDEX.md`(심링크로 공유)에서 걸리는 패턴만. small은 3~4개(문제정의·검증방법·범위제한 중심, 8단계 풀세트 금지), large는 해당 단계 풀세트.
- **변환** 다듬은 완결 프롬프트를 만든다.

### 2. 안전 게이트 (실행 전 필수)
- **부족분 ≤ 3개** → 실행하지 말고 그 개수만큼 먼저 질문(최대 3). 답 받은 뒤 실행.
- **부족분 > 3개** → 실행하지 말고, 빈칸 `[ ]` 남긴 다듬은 프롬프트를 보여준 뒤 어디를 채워야 하는지 물어본다.
- **빈칸 채운 채 멋대로 실행 금지 — 1급 안전규칙.**
- 원본에 이미 다 있으면 질문 없이 3단계로.

### 3. 보여주고 실행
1. 다듬은 프롬프트를 코드블록 하나로 출력(무엇을 실행하는지 투명하게) + 적용 패턴 한 줄.
2. 곧바로 이 세션에서 그 다듬은 프롬프트를 수행한다.
- 다듬은 작업이 파괴적·외부발신(삭제·배포·이메일·push 등)이면 평소 실행 안전규칙대로 확인받고 진행한다. "자동 실행"이 "안전 무시"는 아니다.
- 실행 중 실패는 그대로 보고한다(숨기지 않음).

## 자가 점검 (완료 전)
- [ ] 다듬은 프롬프트를 코드블록으로 보여줬다(실행 전).
- [ ] 부족분이 있으면 실행하지 않고 먼저 물었다(빈칸 실행 방지).
- [ ] small에 8단계 풀세트를 붙이지 않았다.
- [ ] 파괴적/외부발신 작업은 평소 확인규칙을 지켰다.
- [ ] 원본 prompt-forge 파일은 건드리지 않았다.
