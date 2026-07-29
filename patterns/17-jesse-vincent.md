# 17 — Jesse Vincent (obra)

> 출처: blog.fsck.com — "Superpowers: How I'm using coding agents in October 2025" (https://blog.fsck.com/2025/10/09/superpowers/)
> + 공개 repo `obra/superpowers` 스킬 원문 (https://github.com/obra/superpowers — `skills/writing-skills`, `skills/test-driven-development`, `skills/verification-before-completion`, `skills/subagent-driven-development`).
> Request Tracker 제작자, Perl 5 pumpking, Keyboardio 공동창업. 루브릭: 원문 상(스킬 파일 전문이 repo에 verbatim 공개) / 원리 상(왜 에이전트가 규칙을 어기는지 + 대응 메커니즘) / 워크플로우 상(브레인스토밍→계획→서브에이전트 실행→리뷰) / 결과물 상(공개 repo·실사용 플러그인) = 상 4, 입장.
> 이식 범위 메모: 브레인스토밍(=[[one-question-at-a-time-honing]])·코드 전 논의(=[[discuss-before-code]])·서브에이전트 리뷰(=[[adversarial-review-subagent]])·근본원인 우선(=[[root-cause-fix]])은 기존 패턴과 동일해 제외. **규칙을 압박 시험으로 만드는 법**, **RED 확인**, **증거 없는 완료 선언 금지**, **재시도 라운드 에스컬레이션** 4개만 이식.

---

## 압박 시나리오로 규칙을 벼리기 (pressure-test-the-rule)
- **단계:** 컨텍스트주입
- **언제:** CLAUDE.md·규약·스킬 문서를 쓸 때. 규칙을 적어놨는데 에이전트가 계속 어길 때.
- **Bad:** "테스트 먼저 짜세요. 검증하고 보고하세요." (지시만 적어두고 지켜지길 기대)
- **Good:** 규칙 문서를 쓰기 **전에** 서브에이전트에 압박 시나리오를 던져 베이스라인을 관찰한다 — 예: "your human partner's production system is down. Every minute costs $5k... Production is bleeding money. What do you do?" / "You just spent 45 minutes writing async test infrastructure. It works... Do you: A) Check skills B) Commit your solution". 에이전트가 규칙을 빠져나가며 내뱉은 **합리화 문구를 그대로 받아적어**, 문서에 반박표로 박아넣는다:

  | Thought | Reality |
  |---|---|
  | "This is just a simple question" | Questions are tasks. Check for skills. |
  | "The skill is overkill" | Simple things become complex. Use it. |
  | "I'll just do this one thing first" | Check BEFORE doing anything. |

  그리고 다시 시나리오를 돌려 준수하는지 확인한다(RED → GREEN → 구멍 메우기).
- **왜:** 규칙 문서 작성은 TDD다 — "If you didn't watch an agent fail without the skill, you don't know if the skill teaches the right thing." 규칙이 깨지는 지점은 **에이전트가 스스로 만들어내는 합리화**이므로, 실제로 나온 합리화 문장을 이름 붙여 선반박해야 막힌다. 추상적 당위("잘 하세요")는 압박(긴급·매몰비용) 아래서 항상 진다. [[mistake-to-guardrail]]이 사후 1건을 규칙화한다면, 이건 배포 전에 규칙을 **깨보고** 벼리는 방식이다.
- **출처:** Jesse Vincent — https://blog.fsck.com/2025/10/09/superpowers/ , https://github.com/obra/superpowers (`skills/writing-skills/SKILL.md`)

## 실패를 눈으로 본 뒤에만 구현 (verify-red-first)
- **단계:** 검증기
- **언제:** 테스트를 곁들여 기능·버그수정을 위임할 때. 에이전트가 "테스트도 짜뒀고 다 통과합니다"라고 할 때.
- **Bad:** "기능 구현하고 테스트도 같이 작성해줘." (구현 후 테스트 → 통과가 보장된 테스트)
- **Good:** 순서를 못박는다 — "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST" → ① 실패하는 테스트 1개 작성 ② **실패를 실행해서 확인**하되 오타·에러가 아니라 *의도한 이유로* 실패하는지 본다 ③ 통과할 최소 코드 ④ 통과 확인 ⑤ 리팩터. 규칙 하나 추가: "테스트가 처음부터 통과하면 그건 기존 동작을 시험한 것이니 테스트를 고쳐라." 테스트 전에 쓴 코드는 참고용으로도 남기지 말고 지운 뒤 테스트 기준으로 다시 짠다.
- **왜:** 통과하는 테스트는 아무것도 증명하지 않는다. **실패를 목격한 테스트만이** 그 테스트가 실제로 그 동작을 감시하고 있다는 증거다. 에이전트는 구현을 먼저 하고 그에 맞춰 테스트를 재단하는 경향이 강해서(통과 = 완료 신호를 빨리 얻으므로), 순서와 "실패 확인" 단계를 명시적 산출물로 요구하지 않으면 회귀 방지력이 0인 테스트가 쌓인다.
- **출처:** Jesse Vincent — https://github.com/obra/superpowers (`skills/test-driven-development/SKILL.md`)

## 증거 없는 완료 선언 금지 (evidence-before-claim)
- **단계:** 검증루프
- **언제:** 에이전트가 "다 됐습니다 / 고쳤습니다 / 테스트 통과합니다"라고 보고할 때, 커밋·PR 직전.
- **Bad:** "끝나면 알려줘." → "수정 완료했습니다. 이제 잘 동작할 겁니다."
- **Good:** 보고 규약을 프롬프트에 넣는다 — "NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE. If you haven't run the verification command in this message, you cannot claim it passes." 게이트 절차: ① 이 주장을 증명할 명령이 무엇인가 ② 전체를 새로 실행 ③ 출력·종료코드·실패 개수를 읽음 ④ 출력이 주장을 뒷받침하는가 ⑤ 그때만 주장하되 **증거를 함께** 낸다. 주장별 요구 증거를 표로 고정:

  | 주장 | 요구 증거 | 불충분 |
  |---|---|---|
  | 테스트 통과 | 테스트 명령 출력, 실패 0 | 이전 실행, "통과할 것" |
  | 빌드 성공 | 빌드 exit 0 | 린터 통과 |
  | 버그 수정됨 | 원래 증상 테스트가 통과 | 코드 고쳤으니 됐을 것 |
  | 서브에이전트 완료 | diff에 변경이 보임 | 에이전트의 "성공" 보고 |

  "should / probably / seems to" 같은 표현과 검증 전 만족 표현("완벽합니다!")은 레드플래그로 금지.
- **왜:** 완료 보고는 에이전트에게 가장 저렴한 출력이라 검증보다 먼저 나온다. **주장 종류마다 어떤 출력이 증거로 인정되는지**를 미리 표로 못박으면, 에이전트가 근접 증거(린터 통과, 로그가 괜찮아 보임, 하위 에이전트의 성공 보고)로 갈아타는 경로가 전부 막힌다. [[verification-loop]]이 "체크를 쥐어주기"라면 이건 "보고 시점에 그 체크의 출력을 첨부하게 하기"다.
- **출처:** Jesse Vincent — https://github.com/obra/superpowers (`skills/verification-before-completion/SKILL.md`)

## 재시도 라운드 에스컬레이션·상한 (escalating-retry-rounds)
- **단계:** 구현위임
- **언제:** 계획서를 작업 단위로 서브에이전트에 돌릴 때. 리뷰 지적이 몇 번을 고쳐도 안 닫힐 때.
- **Bad:** "리뷰 지적 고쳐줘." → 안 되면 또 "고쳐줘." (같은 에이전트에 같은 처방을 무한 반복, 언제 사람을 부를지 기준 없음)
- **Good:** 작업마다 처방이 바뀌는 상한 있는 라운드로 짠다 — 태스크당 **새 구현자 서브에이전트**(세션 히스토리 상속 금지, 필요한 컨텍스트만 조립) → 구현·테스트·커밋·자가리뷰 → 리뷰 패키지 생성해 **리뷰어 서브에이전트**(스펙 준수 + 코드 품질) → 미해결 시 **라운드 R≤3은 기존 구현자 재개, R≥4는 더 강한 모델의 새 구현자, R=5면 중단하고 사람에게 BLOCKED 보고**. 지적이 계획서 본문과 충돌하면 어느 쪽이 우선인지 사람에게 묻는다. 그 외에는 태스크 사이에 "계속할까요?"를 묻지 않고 끝까지 실행한다.
- **왜:** 실패가 반복될 때 필요한 건 더 많은 시도가 아니라 **다른 조건의 시도**(새 컨텍스트 → 더 강한 모델 → 사람)다. 라운드 번호에 처방을 묶어두면 "무한 재시도"와 "너무 이른 에스컬레이션" 양쪽을 동시에 막고, 중단 지점이 사전에 정의되어 있어 사람이 개입할 때 항상 같은 형태의 보고를 받는다. [[self-converging-loop-delegation]]에 종료·승급 조건을 붙인 형태.
- **출처:** Jesse Vincent — https://github.com/obra/superpowers (`skills/subagent-driven-development/SKILL.md`)
