# 해외 고수들의 '일하는 방식' (재현 가능한 것만)

> C조사 Worker2 산출물. 입장 통과자 7명(Simon Willison / Harper Reed / Peter Steinberger / Mitchell Hashimoto / Geoffrey Huntley / Kenton Varda / Thorsten Ball)
> + 참조 출처(Anthropic 공식)의 **재현 가능한 습관**만 추린다. 프롬프트 자체는 `patterns/01~08`에.
> 원리·철학은 여기, 복붙 프롬프트는 patterns에 — 역할 분리.
> (2차 추가: Kenton Varda, Thorsten Ball. Geoffrey Litt는 입장했으나 범위 밖이라 patterns·여기 모두 미이식.)

---

## 관통하는 공통점 (5인 중 3인 이상에서 독립적으로 관찰)

1. **컨텍스트가 근본 제약이다.** 스레드가 오염되면 고치지 말고 리셋한다.
   - Simon: "the fix for a conversation that has stopped being useful is to wipe the slate clean and start again." — https://simonwillison.net/2025/Mar/11/using-llms-for-code/
   - Anthropic: "After two failed corrections, /clear and write a better initial prompt." — https://code.claude.com/docs/en/best-practices
   - Huntley: 매 루프가 새 컨텍스트(≈170k). 진행은 파일+git에 남긴다. — https://ghuntley.com/ralph/

2. **계획과 실행을 분리한다.** 곧바로 코딩하면 엉뚱한 문제를 푼다.
   - Mitchell: 수동으로 아키텍처를 러프하게 스케치한 뒤 plan-only 프롬프트. — https://mitchellh.com/writing/non-trivial-vibing
   - Anthropic: Explore→Plan→Code→Commit 4단계. — https://code.claude.com/docs/en/best-practices
   - Harper: 아이디어 정련(chat) → 계획(reasoning 모델) → 실행(coding 에이전트)로 모델을 분업. — https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/

3. **새 맥락의 리뷰어가 자기 코드를 검증하는 것보다 낫다.**
   - Mitchell "consult the oracle"(읽기전용) / Steinberger 스펙을 별 모델에 교차비평 / Anthropic 서브에이전트로 diff를 PLAN.md 대조. 각각 patterns 04·03·05.

4. **실행 가능한 합격/불합격 게이트를 준다.** "looks done"은 신호가 아니다.
   - Anthropic: "Give Claude something that produces a pass or fail, and the loop closes on its own." — best-practices
   - Huntley: 타입·컴파일러·테스트를 백프레셔로 배선, 반스텁 사인. — ghuntley.com/ralph/
   - Simon: 구현 직후 "Now write me the tests using pytest", 코드는 반드시 실행해 검증. — using-llms-for-code

---

## 개인별 재현 가능한 습관

### Simon Willison
- **위험한 핵심부터 프로토타입.** 옵션 리서치("options ... include usage examples")로 어려운 부분이 되는지 먼저 확인한 뒤 설계에 커밋. — https://simonwillison.net/2025/Mar/11/using-llms-for-code/
- **안 돌린 코드는 절대 믿지 않는다.** 샌드박스에서 실행 가능한 툴만 선호, 환각 메서드는 실행으로 잡는다. — 같은 URL
- **영수증을 공개한다.** 콜로폰 기능 17분·$0.61·GitHub Pages 배포, 프롬프트 시퀀스 전문을 Gist로. 비용·시간·트랜스크립트 공개가 그 자체로 결과 검증 규율. — 같은 URL

### Harper Reed
- **아티팩트를 파일로 굳혀 레포에 커밋.** spec.md / prompt_plan.md / todo.md가 워크플로우의 척추 — 채팅 스크롤백이 아니라. 맥락 이동·재개 가능. — https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/
- **작업마다 모델을 갈아 쓴다.** 정련=chat, 계획=o1/o3급 reasoning, 실행=Claude/Aider. 한 모델로 세 단계를 다 하지 않는다. — 같은 URL
- **레거시는 repomix로 통째 팩킹 후 리뷰/이슈/테스트 프롬프트.** 무엇을 묻기 전에 전체 코드베이스를 컨텍스트로. — 같은 URL
- **반복 프롬프트를 CLI 태스크로 고정**(`LLM` 툴 + mise). 복붙이 아니라 한 커맨드. — 같은 URL

### Peter Steinberger
- **에이전트 3~8개를 터미널 그리드에서 같은 폴더로 병렬**(worktree는 "너무 느리다"고 거부). 작업 전 blast-radius를 재 원자 커밋 유지, "continue" 메시지 큐잉 후 자리 비움. — https://steipete.me/posts/just-talk-to-it
- **음성 우선 스펙.** Wispr Flow로 받아쓰기, 코드의 "pretty much 100%"를 에이전트가 작성. — 같은 URL, https://steipete.me/posts/2025/the-future-of-vibe-coding
- **단일 AGENTS.MD(→CLAUDE.md 심링크) + `vt title` 관찰성.** 모든 툴이 읽는 규칙 파일 하나(Conventional Commits, push/파괴적-git 가드레일, 내러티브 PR 리캡). 병렬 세션은 `vt title`로 한눈에 감독. — https://github.com/steipete/agent-scripts/blob/main/AGENTS.MD , https://steipete.me/posts/command-your-claude-code-army-reloaded

### Mitchell Hashimoto
- **커밋을 save point로.** 자주 커밋해서 어긋난 방향을 언제든 리셋. — https://mitchellh.com/writing/non-trivial-vibing
- **에이전트를 항상 바쁘게.** 전환 전에 "느리게 시킬 다음 일이 뭐지?"를 물어 리서치·엣지케이스를 넘긴다. — https://www.teamday.ai/ai/hashimoto-new-way-of-writing-code
- **밀도 높은 주석을 미리 깐다.** AI가 주석-코드 불일치를 잡게 하는 사전 습관. — https://ldirer.com/blog/posts/mitchell-hashimoto-zed-agents-2025
- **이해 못 하는 코드는 출시 안 한다.** 어려운 문제에선 에이전트를 멈추고 "educate myself and think critically." — non-trivial-vibing

### Geoffrey Huntley (ralph)
- **두 프롬프트, 한 루프.** `PROMPT_plan.md`(gap 분석만, 구현 금지 → 우선순위 TODO)와 `PROMPT_build.md`(가장 중요한 항목 1개 구현·테스트·커밋)를 스왑. 계획은 자유롭게 버리고 재생성. — https://raw.githubusercontent.com/ghuntley/how-to-ralph-wiggum/main/files/PROMPT_plan.md
- **매 루프는 git으로 끝난다.** 테스트 통과 시 fix_plan 갱신 → add/commit/push → 태그(0.0.0부터 patch 증가). 진실원은 파일+히스토리. — https://ghuntley.com/ralph/
- **샌드박스 + `--dangerously-skip-permissions`.** 루프는 승인 대기가 불가하므로 샌드박스가 유일한 보안 경계("It's not if it gets popped, it's when. And what is the blast radius?"). — https://github.com/ghuntley/how-to-ralph-wiggum/blob/main/files/loop.sh
- **루프 안이 아니라 위에 앉아라.** 스트림을 일찍 보고 실패를 사인(가드레일·AGENT.md 학습)으로 변환. 막히면 `git reset --hard` 재시작 vs 구조 프롬프트를 판단. 컴파일러 에러 폭주는 다른 모델(Gemini)에 넘겨 계획. — https://ghuntley.com/ralph/

### Kenton Varda
- **프롬프트를 코드처럼 버전관리한다.** AI가 만든 매 변경을, 그것을 만든 프롬프트 원문과 함께 커밋 — 커밋 히스토리가 (지시 → 결과) 감사 로그가 된다. "not vibe coded — every line reviewed against the RFCs." — https://github.com/cloudflare/workers-oauth-provider
- **모든 줄을 RFC/스펙에 대고 읽는다.** 자칭 회의론자로서 AI 출력을 표준 문서와 대조 검토. AI가 낸 실수(평문 키 백업, SHA-256을 키유도·토큰ID에 이중 사용)를 직접 잡아냄 — 리뷰가 "less mentally tiring"이라 오히려 빠르다고 평가. — https://neilmadden.blog/2025/06/06/a-look-at-cloudflares-ai-coded-oauth-library/
- **모델이 헤매면 손으로 한다.** class 한 줄 옮기기 같은 사소한 편집에서 thrashing하자 "I could have done this one faster by hand" — 언제 프롬프트를 멈추고 직접 칠지의 기준선. — 커밋 9c38943
- **적정 사용처를 안다.** "well-known standard on a well-known platform with a clear API spec" 같은 표준 구현이 AI의 스위트스팟이라고 명시 — 아무 데나 쓰지 않는다. — HN kentonv 코멘트

### Thorsten Ball
- **보내기 전에 '지식이 어디 사는가'를 자문한다.** 태스크에 필요한 지식이 프롬프트·코드베이스·학습데이터 셋 중 어디에도 없으면 프롬프트에 넣는다 — 이게 프롬프트에 무엇을 담을지 정하는 규칙. — https://registerspill.thorstenball.com/p/joy-and-curiosity-80
- **아키텍처는 내가, 채우기는 에이전트가.** 아키텍처 결정·핵심 코드·새 구조 도입은 사람이 붙들고, 에이전트에겐 "colors"(구현)만 맡긴다. — https://ampcode.com/notes/how-i-use-amp
- **첫 프롬프트를 티켓처럼 쓴다.** 스레드 첫 메시지에 목표·의심 위치·스크린샷·제약·증분 계획을 front-load(가장 무게가 크므로). — 같은 URL
- **자주 새 스레드.** ~100k 토큰 넘으면 첫 지시를 잊거나 "doom loop"에 빠지므로, 태스크당 작은 스레드로 자주 리셋(05 context-hygiene와 같은 습관). — 같은 URL
- **diff를 '남이 쓴 코드'로 리뷰시킨다.** "code someone else wrote"로 재프레이밍해 자기변호 편향을 벗김. — 같은 URL

---

## 우리 엔진에 적용 시 주의
- 위 습관 다수는 **CLI 에이전트(Claude Code/Aider) 전제**다. prompt-forge는 툴 불문 텍스트만 뽑으므로, "파일로 굳혀라"·"서브에이전트 위임" 같은 습관은 *프롬프트 문구*(patterns)로 이미 증류됨 — 습관 자체를 엔진에 하드코딩하지 말 것.
- Anthropic·Steinberger·Huntley의 병렬/자율 루프는 **large 케이스 전용**. small(단일 작업)엔 과합 — `_INDEX.md` 하단 규칙(3~4개만) 준수.
