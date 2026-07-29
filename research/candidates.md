# 조사 후보 (candidates)

패턴 라이브러리를 키울 **조사 대상 목록**. 이 파일은 *틀*이다 — 실제 조사(C)는
스킬 완성 후 별도 세션에서 한다. 여기선 후보를 나열하고 [[RUBRIC]]으로 채점만 준비한다.

## 규칙

- **조사 1회 = 패턴 파일 1개 추가.** 한 번에 몰아서 100개 긁지 않는다.
- 후보는 [[RUBRIC]]로 먼저 채점 → **상 2개 이상만 입장.**
- 우선순위: **① 알렉스 전체 채굴 → ② 해외 고수 5~10명.** 순서대로.
- 넓게 훑기 금지. 깊게 하나씩. 순도 > 양.

## 후보 상태 표기

- `대기` — 아직 채점 안 함
- `입장` — 채점 통과, 조사 예정
- `조사완료 → patterns/<파일>` — 패턴 파일로 이식됨
- `기각(사유)` — 루브릭 탈락

---

## ① 알렉스 전체 채굴 (최우선)

기존 16패턴은 `patterns/00-silvally-alex.md`에 이식됨(기준선). 알렉스의 **나머지**
콘텐츠(다른 영상·글·스레드)에서 아직 안 뽑은 패턴을 채굴한다.

> **3차 채굴(2026-07-29) 결과: 추가 재료 없음 — 이 축은 소진으로 판단.**
> 실밸개발자는 유튜브 외 공개 원문 채널이 없고(핸들 `@sv.developer` 확인, 영상 목록 크롤 실패),
> 알렉스의 신규 공개 콘텐츠는 코딩이 아닌 **마케팅 프롬프트** 쪽으로 이동(범위 밖 기각).
> Threads 최근 글엔 verbatim 프롬프트 없음(원문 하 = 기각). 새 콘텐츠가 올라오기 전엔 재시도 가치 낮음.

| 후보 | 링크/출처 | 상태 | 비고 |
|--|--|--|--|
| 알렉스 — (추가 영상 1) | [ ] | 소진(2026-07-29) | 원 16패턴 밖의 단계 보강 |
| 알렉스 — (추가 글/스레드) | [ ] | 대기 | 검증루프·스코핑 심화 예상 |

> 채점 예시 (실제 조사 시 채워넣기):
> ```
> 채점: 원문 상 / 원리 상 / 워크플로우 상 / 결과물 중 → 상 3개 = 입장
> ```

## ② 해외 고수 5~10명 (C조사 Worker2 완료 — 2026-07-22, 2차 추가 동일자)

1차 6명 + 2차 3명 = 총 9명 발굴 → 채점 → **8명 입장(패턴 이식) / 1명 기각(Armin) / 1명 입장했으나 범위 밖 미이식(Litt)**.
각 이식 입장자 = 패턴 파일 1개. (2차 추가 = Kenton Varda, Thorsten Ball, Geoffrey Litt.)

| # | 후보 (소속·이력) | 채널/출처 | 상태 | 채점 |
|--|--|--|--|--|
| 1 | **Simon Willison** — Django 공동창시자, Datasette·`llm` CLI 제작자 | simonwillison.net ("Here's how I use LLMs to help me write code", 2025-03-11) | 조사완료 → patterns/01-simon-willison.md | 원문 상 / 원리 상 / 워크플로우 상 / 결과물 상 → 상 4개 = 입장 |
| 2 | **Harper Reed** — Obama 2012 캠페인 前 CTO, 엔지니어/창업가 | harper.blog ("My LLM codegen workflow atm", 2025-02-16) | 조사완료 → patterns/02-harper-reed.md | 원문 상 / 원리 중 / 워크플로우 상 / 결과물 하 → 상 2개 = 입장 |
| 3 | **Peter Steinberger** (steipete) — PSPDFKit 창업자 | steipete.me + 공개 AGENTS.MD (2025) | 조사완료 → patterns/03-peter-steinberger.md | 원문 중 / 원리 상 / 워크플로우 중 / 결과물 상 → 상 2개 = 입장 |
| 4 | **Mitchell Hashimoto** — HashiCorp 공동창업자, Ghostty 제작자 | mitchellh.com ("Non-Trivial Vibing", 2025) + 인터뷰 | 조사완료 → patterns/04-mitchell-hashimoto.md | 원문 상 / 원리 상 / 워크플로우 상 / 결과물 상 → 상 4개 = 입장 (앵커) |
| 5 | **Anthropic** — Claude Code Best Practices (공식 문서, ⚠️개인 아님) | code.claude.com/docs/en/best-practices | 조사완료 → patterns/05-anthropic-cc-bestpractices.md | 원문 상 / 원리 상 / 워크플로우 상 / 결과물 하 → 상 3개 = 입장 |
| 6 | **Geoffrey Huntley** — ex-Gitpod/Canva, "ralph" 자율루프 | ghuntley.com/ralph/ + github.com/ghuntley/how-to-ralph-wiggum | 조사완료 → patterns/06-geoffrey-huntley.md | 원문 상 / 원리 상 / 워크플로우 상 / 결과물 중 → 상 3개 = 입장 |
| 7 | **Kenton Varda** — Cloudflare 수석, Protobuf v2/Cap'n Proto 제작자 | github.com/cloudflare/workers-oauth-provider (커밋 메시지에 프롬프트 원문 동봉) | 조사완료 → patterns/07-kenton-varda.md | 원문 상 / 원리 상 / 워크플로우 상 / 결과물 상 → 상 4개 = 입장 |
| 8 | **Thorsten Ball** — Sourcegraph(Amp), "Writing An Interpreter/Compiler In Go" 저자, ex-Zed | ampcode.com/notes/how-i-use-amp + registerspill.thorstenball.com | 조사완료 → patterns/08-thorsten-ball.md | 원문 상 / 원리 상 / 워크플로우 상 / 결과물 상 → 상 4개 = 입장 |
| 9 | **Geoffrey Litt** — MIT CSAIL 박사, Ink & Switch/Anthropic (⚠️#6 Huntley와 다른 인물) | geoffreylitt.com (Stevens AI 비서) | 입장했으나 **미이식**(범위 밖) | 원문 중 / 원리 상 / 워크플로우 상 / 결과물 상 → 상 3개 = 입장 |

### 판단 노트
- **#5 Anthropic**: 후보 조건이 "개인 고수"라 애매하나, 원문 프롬프트 복붙 가능 + 워크플로우 분류가 가장 체계적이라 *재료 출처*로만 채택. 개인 공개가 아닌 **벤더 공식 문서**임을 파일 상단에 플래그. 결과물 축이 약함(하 — 실 출시 아티팩트 없이 이상화 예시).
- **#6 Huntley**: /stdlib/·/specs/ 본문은 구독 게이트 → 인용 안 함. 공개된 /ralph/ + GitHub repo 원문만 근거. 결과물은 트윗 스크린샷 수준(withheld)이라 중.
- **중복 제외**: Harper·Anthropic의 "인터뷰로 스펙 만들기"는 00의 [[reverse-interview]]와 동일 → Anthropic판은 미이식, Harper판은 "한 턴 한 질문" 케이던스로만 재프레이밍해 이식.
- **#7 Kenton Varda(2차)**: 커밋 메시지에 프롬프트 원문을 그대로 넣어 (프롬프트→diff) 감사 로그를 남긴 게 고유. 기존 6인 누구와도 겹치지 않는 '보안·감사 가능한 AI 코딩' 각도라 추가.
- **#8 Thorsten Ball(2차)**: "지식은 프롬프트·코드베이스·학습데이터 셋 중 하나에 있어야 한다 — 셋 다 없으면 실패"라는 프롬프팅 이론이 고유. 05 context-hygiene와 겹치는 fresh-thread 패턴은 제외하고 4개만 이식.
- **#9 Geoffrey Litt(2차) — 입장했으나 미이식**: 채점은 통과(상 3)이나 그의 패턴(단일-테이블 기억·cron 자동 수집·페르소나 앵커)은 *코딩-위임 프롬프트*가 아니라 **LLM 비서 앱 아키텍처**다. 이 라이브러리 도메인(코딩 에이전트에 일을 위임하는 프롬프트) 밖이라 순도 우선으로 미이식. 06 Huntley와 이름만 같은 별개 인물.
- **Armin 재검(2차)**: 2차 조사에서 Armin을 다시 채점했으나(원문 중), 1차의 기각 판단(verbatim 프롬프트 부족 → 순도 미달)과 동일 결론. "원리 소스"로는 최상급이나 프롬프트 재료로는 여전히 미달 → 기각 유지.

## ③ 3차 채굴 (2026-07-29 — 4워커 병렬: 한국어권 / 해외신규 / 1차공식 / 미완소스재시도)

입장 5건, 신규 패턴 21개(16~20). 기존 84 → **105패턴**.

| # | 후보 | 채널/출처 | 상태 | 채점 |
|--|--|--|--|--|
| 10 | **조태호 (taehojo)** — 『혼자 공부하는 바이브코딩』 저자 (한국어권) | github.com/taehojo/vibecoding/PROMPTS.md (장별 프롬프트 전문 + 예제 코드) | 조사완료 → patterns/16-taehojo-vibecoding.md | 원문 상 / 원리 하 / 워크플로우 상 / 결과물 상 → 상 3 = 입장. ⚠️교재성 — 책 본문 유료라 미인용, repo 공개분만 근거. 원리 축이 비어 "왜"는 재구성 |
| 11 | **Jesse Vincent (obra)** — Request Tracker 제작자, Perl 5 pumpking | blog.fsck.com/2025/10/09/superpowers/ + github.com/obra/superpowers | 조사완료 → patterns/17-jesse-vincent.md | 원문 상 / 원리 상 / 워크플로우 상 / 결과물 상 → 상 4 = 입장 |
| 12 | **Hamel Husain** — ex-GitHub ML, 30여 개사 LLM 평가 체계 구축 | hamel.dev/blog/posts/llm-judge/ + /evals-faq/ | 조사완료 → patterns/18-hamel-husain.md | 원문 상 / 원리 상 / 워크플로우 상 / 결과물 중 → 상 3 = 입장. 라이브러리에 없던 **LLM-as-judge(검증기)** 각도 |
| 13 | **Anthropic Engineering 블로그** (⚠️#5와 같은 벤더 공식문서) | anthropic.com/engineering — 롱러닝 하네스·멀티에이전트·컨텍스트 엔지니어링 3편 | 조사완료 → patterns/19-anthropic-engineering-agents.md | 원문 중~상 / 원리 상 / 워크플로우 상 / 결과물 하~중 → 상 2~3 = 입장 |
| 14 | **u/Any-Reputation8118 (SNOWFLOW)** — Reddit r/ClaudeAI | old.reddit.com/r/ClaudeAI/comments/1v94nal/ + github.com/Noniv/snowflow_demo (MIT) + 라이브 데모 | 조사완료 → patterns/20-snowflow-brief.md | 원문 상 / 원리 상 / 워크플로우 상 / 결과물 상 → 상 4 = 입장. 구현 브리프 전문 첨부 + 산출물 공개 |

### 원문 재추적 (2026-07-29) — 기존 입장자 2인 승격

"안 뚫렸는데 넣어둔" 패턴 감사에서 위험 높음으로 지목된 2건을 다시 캤다. **둘 다 뚫렸다.**

| 파일 | 이전 | 이후 | 뚫은 방법 |
|--|--|--|--|
| **12 Matt Pocock** | 원문 중(grill-me 전문 미확보) = 상3 | **원문 상 = 상4** | `/watch`로 96분 영상 자막 + 16:24 화면 프레임 → `grill-me` SKILL.md **11줄 전문** 확보. 1차 워커는 자막 추출 도구가 없어 "repo 없는 인물"로 포기했던 건 |
| **14 Boris Cherny** | 원문 중(커맨드 본문 미공개) = 상2 경계선 | **원문 상 = 상3**(경계선 해제) | GitHub API로 `commit-push-pr.md` 저작자가 `bcherny` 본인임을 확정하고 전문 확보 + 1차에 안 잡힌 2차 스레드 발견 |

부수 수확: 12에서 신규 패턴 3개(칸반 DAG·모듈 맵 소유·push/pull 배치), 14에서 1개(알고 난 뒤 갈아엎기).

**남은 미해결:** 16 조태호의 원리 축(유료 책 본문) — 규칙상 인용 불가라 "왜"는 재구성 유지. 06 Huntley·11 disler의 유료 게이트분도 동일.

### 미완 소스 재시도 결과

- **Reddit — 뚫림.** 1차의 3중 차단 중 fetch·검색인덱스는 여전히 하드팩트지만, `claude-in-chrome` 확장이 연결돼 브라우저 경로로 원문 열람 성공(1차 SUMMARY의 재수집 조건이 충족된 상태였음). 2차 요약이 아니라 게시자 본인 텍스트만 근거로 씀.
  아직 안 훑은 곳: r/ClaudeCode · r/ChatGPTCoding · r/aigamedev — 같은 방식으로 추가 채굴 가능.
- **박진형 — 특정 실패 유지.** 인물은 확인(사이오닉AI 엔지니어, 앤트로픽이 글로벌 헤비유저로 지목)되나, 공개 핸들을 "사용량 1위" 맥락과 직접 잇는 소스가 없고 언론 귀속이 서로 어긋난다(동명이인·오귀속 위험). **핸들이 맞았어도 공개 원문에 프롬프트가 0건이라 RUBRIC 원문 하 = 어차피 기각.** 재시도 조건: 본인이 공개 계정으로 해당 맥락을 밝히거나, 프롬프트 원문이 실린 발표자료·기고문 확보 시.

## 기각함 (참고 — 다시 후보로 올리지 말 것)

| 후보 | 기각 사유 |
|--|--|
| **Armin Ronacher** — Flask/Jinja 제작자, Sentry 공동창업 | 원문 중 / 원리 상 / 워크플로우 중 / 결과물 중 → **상 1개 = 기각**. 원리·아키텍처는 최상급이나 복붙 가능한 verbatim 프롬프트/CLAUDE.md 전문을 거의 안 보여줌(리터럴 프롬프트 1개뿐). "원리 소스"로는 좋지만 프롬프트 라이브러리 재료로는 순도 미달. (lucumr.pocoo.org/2025/6/12/agentic-coding/ 등) |
| _(예)_ "프롬프트 팁 50선" 류 | 원문 없음 + 원리 없음 → 상 0개 |
| **Charles Covey-Brandt (Airbnb)** — 3.5K 테스트 파일 LLM 마이그레이션 | 상 3이나 **복붙 가능한 원문 부재로 기각** — 공개 프롬프트가 truncated 배열 한 조각뿐. ⚠️원문 공개 시 재조사 가치 높음: '대량 배치 마이그레이션'은 라이브러리 공백 |
| **antirez (Salvatore Sanfilippo)** — Redis 제작자 | 원문 중 / 원리 상 / 워크플로우 중 / 결과물 상 → 상 2 경계선. verbatim 프롬프트 없이 지침만 있고, 원리는 [[paste-full-source]]·[[options-menu-research]]와 중복 → 동점 기각 |
| **Paul Gauthier** — aider 제작자 | 원문 하 / 원리 중 / 워크플로우 하 / 결과물 상 → 상 1 = 기각. 모델 벤치마크 수치 중심, 프롬프트 원문 없음 |
| **Anthropic — harness-design-long-running-apps** | 상 1 = 기각. 프롬프트가 전부 요약 서술, 고유해 보이던 sprint contract는 [[build-grader-first]]와 실질 동일 |
| **Anthropic — writing-tools-for-agents** | 상 1 + 도메인 밖(툴 저작). 코딩 위임 프롬프트가 아님 (Litt 미이식과 같은 사유) |
| **Claude Code 공식 문서 (sub-agents / skills 페이지)** | 기능·설정 문서. 재사용 가능한 프롬프트 원문도 "왜 먹히는지"도 없음 → 상 0 = 기각 |
| **u/Osi32** (Karpathy 4조항 + 5번째) — Reddit | 원문 상 / 원리 상 / 워크플로우 하 / 결과물 하 → 상 2 경계선, 하 2개 → "애매하면 기각" 적용 |
| **u/JokeGold5455 (diet103)** — Reddit, 6개월 하드코어 | 상 4로 채점은 통과하나 **패턴이 기존과 다수 중복**(dev-docs 3파일=[[todo-md-checklist]]+[[persistent-context-file]], compact 전 갱신=[[context-refresh-threshold]], 훅/PM2는 프롬프트 아닌 툴링) → 보류 |
| **한국어권 일반**(velog 회고·번역글, GitHub 입문 가이드, 유료 강의) | 공식문서 요약·번역이거나 유료 게이트 → 원문 축에서 탈락 |

---

## 조사 세션 체크리스트 (실행 시)

1. 후보 하나 고른다 (우선순위 ①→②).
2. [[RUBRIC]] 4항목 채점 → 상 2개 미만이면 `기각`, 끝.
3. 통과 시 프롬프트 원문·원리를 뽑아 **패턴 파일 1개** 작성
   (형식은 `patterns/` 계약서 준수 — 단계/언제/Bad/Good/왜/출처).
4. `patterns/_INDEX.md`에 새 패턴 줄 추가.
5. 이 파일의 후보 상태를 `조사완료 → patterns/<파일>`로 갱신.
6. 엔진(SKILL.md)은 **건드리지 않는다** — 재료만 늘린다.
