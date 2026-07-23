# Worker D 정찰 — 블로그·뉴스레터·GitHub (AI 코딩 워크플로우)

> 담당 소스: 개인 블로그·뉴스레터·GitHub README/gist. 개발자가 **글로 정리한** 실제 AI 코딩/프롬프팅 작업 방식.
> 기준선(candidates.md / workstyle-overseas.md / workstyle-baseline.md) 대조 완료 — 이미 있는 인물은 재발굴 금지.
> RUBRIC 4항목(원문공개/원리/워크플로우/결과물) 사전 적용, **상 2개 이상만 본 표.** 미달은 하단 기각.
> 규칙 준수: 링크 없는 주장 없음. 홍보성·일반론·리스티클 제외.

---

## 본 표 (입장 — 상 2개 이상)

| 인물/핸들 | 출처 링크 | 방식 1~3개 (재현 가능한 절차로) | 기준선에 이미 있음? | 신규 패턴 후보 | RUBRIC 채점 |
|--|--|--|--|--|--|
| **Indragie Karunaratne** (@indragie) — macOS 개발자, `Context`(MCP 디버거 앱) 제작 | https://www.indragie.com/blog/i-shipped-a-macos-app-built-entirely-by-claude-code | ① **읽고-요약시켜 이해를 검증한 뒤 구현.** 구현 전 프롬프트: "Read [파일들] to learn how [기존 기능] is implemented. Then read [외부 문서 URL]. After reading these sources, **summarize what you've learned.**" — 요약을 못 하면 컨텍스트가 부족한 것. ② **사고 강도를 단어로 계단식 조절.** `think` → `think hard` → `think harder` → `ultrathink` + "Make a plan first, don't implement until the plan is accepted." ③ **UI는 '제안 메뉴' 먼저.** "Come up with suggestions for how to make this UI more beautiful" → 랭크된 후보를 받고 골라서 적용(바로 "예쁘게 해줘" 금지). 스크린샷 ⌘V 붙여넣기로 시각 피드백 루프. | ❌ 신규 | **read-then-summarize 게이트**(요약 실패=컨텍스트 부족 신호), **escalating-think 계단**(think/…/ultrathink), **design-suggestion-menu**(제안 랭크 먼저→선택). "context engineering > prompt engineering — 요즘 모델은 지저분한 입력도 처리, 진짜 제약은 컨텍스트 창." | 원문 **상** (verbatim 트리거 문구·CLAUDE.md 스니펫·read+summarize 템플릿) / 원리 **상** / 워크플로우 **상** (plan→context prime→spec→verify) / 결과물 **상** (`Context` 앱 20k줄 中 손코딩 <1k, 2,000줄 릴리스 자동화 스크립트) → **상 4 = 입장** |
| **Russ Poldrack** — 신경과학자(스탠퍼드), 오픈소스 `parcelextract` 저자 | https://russpoldrack.substack.com/p/workflows-for-agentic-coding-and | ① **PRD를 먼저 프롬프트로 생성 → 그걸 재료로 나머지 문서를 연쇄 생성.** "Help me create a Project Requirement Document (PRD) for a Python module called parcelextract that…" → 이어서 "Based on the attached CLAUDE.md and PRD.md files, create a **PLANNING.md**…" / "…create a **TASKS.md** with tasks divided into milestones." (PRD→CLAUDE.md→PLANNING→TASKS→SCRATCHPAD 5파일 척추). ② **컨텍스트 50%에서 리프레시.** `/context`로 사용률 감시, 절반 넘으면 `/freshstart` 커스텀 커맨드로 새 세션 온보딩, 마일스톤 끝에서 `/summ+commit`. ③ **TDD 강제 감독.** 에이전트가 red-green-refactor를 건너뛰면 사람이 되돌려 사이클을 지킨다. | ❌ 신규 | **PRD-체이닝**(한 문서를 다음 문서 생성의 첨부 재료로 연쇄), **50%-컨텍스트 리프레시 임계값**(감으로가 아니라 `/context` 수치로), **정직한 실패 경계**("vibe coding은 잘 문서화된 흔한 문제에만 성공 — GPU 가속 같은 신규 알고리즘은 도메인 전문성 필요, 실패함"). | 원문 **상** (PRD/PLANNING/TASKS 생성 프롬프트 verbatim) / 원리 **중** (경험 근거+임계값) / 워크플로우 **상** (5파일 spec-driven + 커스텀 커맨드) / 결과물 **상** (`parcelextract` 모듈 + GPU 실패 정직 기록) → **상 3 = 입장** |

---

## 기각 (상 1개 이하 또는 소스 레인 불일치)

| 후보 | 출처 | 기각 사유 (한 줄) |
|--|--|--|
| **Dexter (Dex) Horthy** — HumanLayer 창업, "12-Factor Agents"·RPI(Research→Plan→Implement) | humanlayer 블로그/강연, https://newsletter.pragmaticengineer.com/p/context-engineering-with-dex-horthy | 원리·워크플로우는 최상급이나 **복붙 가능한 verbatim 프롬프트가 공개 글에 거의 없음**(주 매체가 컨퍼런스 강연 영상 — 내 소스 레인인 블로그/깃허브엔 프레스크립티브 요약뿐, 리포는 "pretty much deprecated"). RPI는 기준선 research→plan→implement와 중복. **단, '의도적 압축(intentional compaction — 리서치 문서를 일부러 파일로 굳혀 컨텍스트를 리셋·재수화)' 각도는 신규 아이디어로 기록** → 재료 확보되면 재검토. 현 상태 원문 중/원리 상/워크플로우 상/결과물 중 = 경계선, 순도 우선 기각. |
| **Birgitta Böckeler** — Thoughtworks AI-assisted delivery 리드, "Exploring Gen AI" 메모 시리즈, SPDD | https://birgitta.info/ , martinfowler.com "Exploring Generative AI" | 서사형 메모·컨퍼런스 발표 중심 → **복붙 프롬프트 원문이 사실상 없음**(SPDD는 개념 설명). 원문 중 / 원리 상 / 워크플로우 중 / 결과물 중 = 상 1. "원리 소스"로는 우수하나 프롬프트 라이브러리 재료로는 순도 미달(Armin과 동일 유형). |
| **Kyle (@0xblacklight, HumanLayer)** — "Writing a good CLAUDE.md" | https://www.humanlayer.dev/blog/writing-a-good-claude-md | 프레스크립티브(규범)일 뿐 **자기 CLAUDE.md·verbatim 프롬프트 미공개**("우리 root CLAUDE.md는 60줄 미만"이라 말할 뿐 내용 안 보임). Progressive-disclosure/pointer 전략은 좋으나 원문 하 → 상 1 이하. |
| **sankalp** — "A Guide to Claude Code 2.0" | https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/ | 가이드/팁 종합(Boris Cherny의 plan-mode 워크플로우 재소개 등) — **본인 고유의 verbatim 프롬프트/결과물 증거 약함**. 파생 콘텐츠, 상 0~1. |
| "50 Claude Code Tips", "30 Templates That Actually Work" 류 리스티클 | dev.to / medium / agentsroom 등 다수 | 팁 나열형 + 원문·원리·결과물 증거 없음 → 상 0. (기준선 candidates.md의 "프롬프트 팁 50선 류"와 동일 처리.) |

---

## 접근 한계 (정직 기록)

- **HumanLayer 리포**(github.com/humanlayer/humanlayer)의 `.claude/`·`thoughts/` 실제 프롬프트 파일 내용은 WebFetch로 확인 불가(리스팅만 노출, 본문 렌더 실패) + 리포가 deprecated 표기 → Dex의 verbatim은 미확보로 처리. 로그인·JS 차단 아님, 단순 미노출.
- 담당 레인(블로그/뉴스레터/깃허브)에 한정. 강연 영상(YouTube)이 주 매체인 인물(Dex 등)은 verbatim 근거가 레인 밖이라 보수적으로 기각.
- 순도 우선: 경계선 후보(Dex/Böckeler)는 "원리 소스로는 우수하나 복붙 재료 미달"로 기각 유지(RUBRIC "동점·애매하면 기각").
