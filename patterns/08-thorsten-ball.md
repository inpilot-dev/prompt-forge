# 08 — Thorsten Ball

> 출처: Thorsten Ball ("Writing An Interpreter/Compiler In Go" 저자, Sourcegraph에서 Amp 코딩 에이전트 개발, ex-Zed).
> "How to Build an Agent"(ampcode.com/how-to-build-an-agent) — 에이전트 = "an LLM, a loop, and enough tokens" 원리.
> "How I use Amp"(ampcode.com/notes/how-i-use-amp) + Amp Owner's Manual + Register Spill 뉴스레터 — 실제 프롬프트·워크플로우.
> 지배 은유: "paint-by-numbers programming: I put in the numbers and the lines and the agent then goes and puts in the colors."
> 채점: 원문 상 / 원리 상 / 워크플로우 상 / 결과물 상 → 상 4개 = 입장.
> (C조사 Worker2 2차 추가분. "지식 공백 = 실패"라는 프롬프팅 이론이 고유 기여. 05 context-hygiene와 겹치는 fresh-thread는 제외.)

---

## 지식 공백 점검 (knowledge-gap-audit)
- **단계:** 컨텍스트주입
- **언제:** 비자명한 태스크를 에이전트에 보내기 전 — 프롬프트에 무엇을 써넣을지 정할 때.
- **Bad:** 에이전트가 "알아서 할 것"이라 가정하고 컨벤션·엔드포인트 추가법을 프롬프트에서 뺀다.
- **Good:** *이 태스크의 지식이 어디 사는가?*를 물어라. 코드베이스나 모델 학습데이터에 있으면 의존 가능; 둘 다에 없으면 프롬프트에 넣어야 한다. "If all the knowledge required to solve the task is available either in your prompt, or in the codebase, or in the training data of the model, then things go fine. Things go badly if there's a gap."
- **왜:** 에이전트의 진실 원천은 딱 셋(프롬프트·코드베이스·학습데이터). 실패는 거의 항상 셋 중 무엇도 못 메운 지식 공백 — 프롬프팅이란 그 공백을 메우는 행위다. *무엇을* 컨텍스트에 넣을지 판단하는 상위 규칙.
- **출처:** Joy & Curiosity #80 — https://registerspill.thorstenball.com/p/joy-and-curiosity-80

## 페인트-바이-넘버 스코핑 (paint-by-numbers-scoping)
- **단계:** 스코핑
- **언제:** 구현은 위임하되 아키텍처 통제권은 사람이 쥘 때.
- **Bad:** 에이전트가 아키텍처를 결정하고 새 구조를 도입하게 둠 ("build me the thing").
- **Good:** 사람이 numbers와 lines를 준다 — "what I think about the architecture, where I suspect the traps are, where I know the relevant code to be… which tests to add and extend and run" — 에이전트는 colors(코드)를 채운다. "The agent doesn't make architectural decisions for me, it doesn't write critical code without close supervision, it doesn't introduce a completely new structure to the codebase. That's what I do."
- **왜:** 아키텍처는 비싸고 되돌리기 힘든 실수가 사는 곳이자 사람이 아직 모델을 앞서는 곳; 코드 채우기는 기계적이고 재생성이 싸다. 그 선을 따라 노동을 나눈다. (04 [[scaffold-then-fill]]이 코드로 스캐폴드를 깔고 채운다면, 이건 그 상위의 *노동 분담 원칙*.)
- **출처:** How I use Amp — https://ampcode.com/notes/how-i-use-amp

## 티켓급 첫 프롬프트 (ticket-grade-first-prompt)
- **단계:** 킥오프
- **언제:** 스레드의 첫 메시지를 쓸 때(가장 무게가 크다).
- **Bad:** "Build a batch tool into the agent"
- **Good:** 잘 쓴 티켓/버그리포트처럼 front-load: 목표, 의심 위치, 스크린샷, 제약, 증분 계획 — 예: "I need your help implementing this: [URL]. We have tools defined in core/src/tools/tools.ts… I imagine it'll be tricky to figure out the types… We should start really simple and then evolve what we have." (그의 슬라이드: 좋은 프롬프트 = 좋은 티켓 = 좋은 버그리포트.)
- **왜:** "The first prompt in the thread carries a lot of weight." 구체성 + 의심-덫 위치가, 코드베이스가 허용하는 열다섯 가지 틀린 길을 우회시킨다.
- **출처:** How I use Amp — https://ampcode.com/notes/how-i-use-amp

## 남이 쓴 코드로 셀프리뷰 (self-review-as-stranger)
- **단계:** 검증루프
- **언제:** 에이전트가 변경을 끝낸 뒤, 수락하기 전.
- **Bad:** "did you do this correctly?" (모델이 자기 작업을 변호하게 만듦)
- **Good:** 출력을 외부인의 것으로 재프레이밍: "Run `git diff` to see the code someone else wrote. Review it thoroughly and give me a report."
- **왜:** diff를 "someone else wrote"로 캐스팅하면 자기정당화 편향이 벗겨져, 모델이 확증 대신 적대적으로 리뷰해 스스로였다면 변호했을 문제를 드러낸다. (05 [[adversarial-review-subagent]]가 *별도 서브에이전트*로 적대 리뷰를 시킨다면, 이건 같은 스레드에서 *역할 재프레이밍*만으로 같은 효과를 노리는 가벼운 버전.)
- **출처:** How I use Amp — https://ampcode.com/notes/how-i-use-amp
