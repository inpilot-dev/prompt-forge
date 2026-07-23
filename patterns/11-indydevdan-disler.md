# 11 — IndyDevDan (disler)

> 출처: YouTube "The One Agent to RULE them ALL" (https://www.youtube.com/watch?v=p0mrXfwAbCg) + 원문 repo https://github.com/disler/infinite-agentic-loop (커맨드 원문 `.claude/commands/infinite.md`), https://github.com/disler/claude-code-is-programmable.
> 15년+ 실무, "Agentic Engineering". 루브릭: 원문 상(커맨드 `.md` verbatim) / 원리 중 / 워크플로우 상 / 결과물 상 = 상 3, 입장.
> ⚠️ 심화 프레임(유료 강의 Tactical Agentic Coding)은 미인용 — 무료 repo+영상 범위만.

---

## 병렬 서브에이전트 웨이브로 발산 생성 (parallel-divergent-waves)
- **단계:** 구현위임
- **언제:** 하나의 정답이 아니라 한 스펙에서 다양한 변형을 병렬로 대량 생성하고 싶을 때(디자인 후보·구현 변주 등).
- **Bad:** "이 스펙으로 여러 버전 만들어줘." (순차·중복 생성, 수렴형)
- **Good:** `spec 파일 1개` + `/project:infinite <spec> <out_dir> <count>` 커맨드. 커맨드는 5단계(스펙 분석→출력디렉토리 상태 점검→시작번호·전략 수립→**병렬 서브에이전트 웨이브 배치**→연속 생성). 각 서브에이전트에 `Spec Context`+`Iteration Assignment(고유 번호)`를 배분, 중복 번호 금지.
- **왜:** 서브에이전트를 "수렴"(한 정답으로 좁히기)이 아니라 "발산"(N개 고유 변형 병렬 생성)에 쓴다. Iteration 번호를 강제 배분해 각 에이전트가 겹치지 않는 변형을 낸다. [[subagents-as-scheduler]]와 방향이 반대(다변량 생성).
- **출처:** IndyDevDan — https://github.com/disler/infinite-agentic-loop

## 웨이브별 점진 정교화 (progressive-sophistication)
- **단계:** 솔루션깎기
- **언제:** 발산 생성을 여러 웨이브로 돌릴 때, 뒤 웨이브가 앞보다 더 정교해지도록 강제하고 싶을 때.
- **Bad:** 매 반복 같은 수준의 변형만 반복.
- **Good:** 커맨드에 "웨이브가 진행될수록 기본 구현→스펙 경계를 미는 고급 개념으로 정교화하라"를 명시.
- **왜:** 그냥 N개를 뽑으면 다 비슷한 난이도로 몰린다. 웨이브 진행 = 정교화 상승을 규칙으로 박으면 후반 산출물이 스펙의 한계를 탐색한다.
- **출처:** IndyDevDan — https://github.com/disler/infinite-agentic-loop

## 프롬프트를 프로그래밍 가능한 자산으로 (prompts-as-programmable-assets)
- **단계:** 컨텍스트주입
- **언제:** 반복 쓰는 프롬프트·슬래시 커맨드를 일회성 복붙이 아니라 버전관리 자산으로 다루고 싶을 때.
- **Bad:** 매번 프롬프트를 채팅에 다시 타이핑.
- **Good:** 슬래시 커맨드/프롬프트를 `.claude/commands/*.md`로 파일화해 repo에 커밋(claude-code-is-programmable) — 재사용·리뷰·diff 가능.
- **왜:** 프롬프트가 코드처럼 버전관리되면 팀·에이전트가 공유하고, 개선이 diff로 누적된다. [[prompt-as-file-template]]·[[commit-the-prompt]]와 같은 계열.
- **출처:** IndyDevDan — https://github.com/disler/claude-code-is-programmable
