# Scout — Threads / X (Worker B)

담당 소스: **Threads(threads.com) 및 X(트위터)**. 개발자들이 자기 AI 코딩/프롬프팅 실제 작업 방식을 푼 트윗·스레드 조사.
기준선(`candidates.md` / `workstyle-overseas.md` / `workstyle-baseline.md`) 대조 후, **새 근거·새 인물만** 수집.

> 접근 한계(정직 기록): X 게시물 본문은 대부분 로그인 게이트다. thread-reader 미러(twitter-thread.com)로 접근 가능한 것만 인용했고,
> 실패한 항목은 하단 '기각/스킵'에 사유를 남겼다. Threads 게시물은 WebFetch로 본문 요약은 되나 **verbatim 프롬프트 전문은 거의 노출 안 됨** → 원문(RUBRIC #1) 대부분 미달.
> 링크 없는 주장은 넣지 않았다.

---

## 본 표 (RUBRIC 상 2개 이상 통과)

| 인물/핸들 | 출처 링크 | 방식 1~3개 (재현 가능한 절차) | 기준선에 이미 있음? | 신규 패턴 후보 | RUBRIC 채점 |
|--|--|--|--|--|--|
| **Boris Cherny** (@bcherny) — Claude Code 창시자/책임자 (Anthropic) | X 스레드 https://x.com/bcherny/status/2007179832300581177 (미러: https://twitter-thread.com/t/2007179832300581177), 코버리지 https://venturebeat.com/technology/the-creator-of-claude-code-just-revealed-his-workflow-and-developers-are | ① **Plan 모드로 시작(shift+tab 2회)** → 계획이 마음에 들 때까지 왕복 → 마음에 들면 **auto-accept edits 모드**로 전환해 구현. ② **자주 쓰는 inner-loop는 슬래시 커맨드로 고정** — 예 `/commit-push-pr`는 inline bash로 git status를 미리 계산. 커맨드는 `.claude/commands/`에 git 체크인해 팀·Claude가 공유. ③ **CLAUDE.md를 자기수정 루프로** — "Claude가 뭘 틀리면 그걸 CLAUDE.md에 추가해 다음엔 안 하게 한다." PR 리뷰 중 오류를 보면 코드만 고치지 말고 **@claude를 태그해 규칙 파일을 PR의 일부로 갱신**. ④ **검증 수단을 반드시 쥐여준다** — "give Claude a way to verify its work → 최종 품질 2~3배". Chrome extension으로 UI 열어 직접 테스트·반복. | 부분 중복: baseline #5 Anthropic 공식문서(CLAUDE.md·verify 게이트·Explore→Plan→Code)와 원리 겹침. **하지만 개인 셋업 특유의 구체가 신규**: 슬래시 커맨드 이름/inline-bash precompute, code-simplifier·verify-app 서브에이전트, PR 리뷰 태그로 메모리 갱신. | **① review-to-memory 루프**: PR 리뷰 코멘트를 코드 수정으로만 끝내지 말고 "@claude 태그 → CLAUDE.md 규칙 추가"로 규칙화(기준선 `persistent-context-file`의 *갱신 트리거* 심화). **② precompute-slash-command**: 반복 명령을 inline bash로 상태를 미리 계산해 넣는 커맨드로 고정(`/commit-push-pr`). | 원문 **중**(커맨드 이름·절차는 공개, 커맨드 본문 전문은 미공개) / 원리 **상**(verify→2~3배, CLAUDE.md 자기수정 메커니즘 설명) / 워크플로우 **상**(Plan→auto-accept→verify→commit-push-pr, 재현 가능) / 결과물 **중**(팀 PR·터미널 셋업 스샷 수준) → **상 2 = 입장** |
| **Avi Chawla** (@_avichawla, Daily Dose of DS) — AI 엔지니어/에듀케이터 | X 스레드 https://x.com/_avichawla/status/2043086745231892982 → 전문 https://www.dailydoseofds.com/p/10-must-use-slash-commands-in-claude-code/ | 재사용 슬래시 커맨드 10종을 **실제 ML 서비스(FastAPI·scikit-learn·Alembic)에 데모**하며 제시(각 커맨드 = 재현 절차): `/env-check`(런타임·의존성·env·git hook 검증) · `/orient`(대화 clear 후 미커밋 변경+최근 커밋+TODO로 작업 맥락 재구성) · `/preflight`(커밋 전 디버그문·TODO·하드코딩 시크릿·skip된 테스트 스캔) · `/dissect`(에러 처리·엣지케이스·동시성·의존성 다차원 구조 리뷰) · `/testmatch`(프로젝트 기존 테스트 관례를 학습해 동일 스타일 테스트 생성) · `/refactor-safe`(public API 시그니처 보존한 채 내부만 리팩터) · `/ship`(테스트 실행+diff 규모 판단 후 PR 설명 자동 생성) · `/migrate-draft`(기존 마이그레이션 관례 학습→up/down+롤백 체크리스트) · `/debt-scan`(복잡도·의존성 노후·테스트 공백을 심각도/공수로 랭크). 핵심 원리: "매번 10~15줄 지시를 기억으로 재타이핑하면 **prompt drift**가 생김 → 커맨드로 고정해 Git 버전관리". | 신규(기준선에 이 커맨드 세트 없음). `/orient`는 baseline `session-reonboarding`과 원리 동일(재프레이밍만). | **prompt-drift 방지**: 반복 지시를 `.claude/commands/*.md`로 굳혀 버전관리 → 매 실행 동일 문구(케이던스 일관성). **/orient 재온보딩**: clear 후 "미커밋+최근커밋+TODO"만으로 맥락 복원하는 경량 재진입 절차. | 원문 **중**(커맨드 스펙·YAML 프론트매터·`$ARGUMENTS` 구조 공개, 일부 본문은 게이트) / 원리 **상**(prompt drift 명시) / 워크플로우 **상**(각 커맨드가 실제 레포에 데모된 절차) / 결과물 **중**(데모 레포) → **상 2 = 입장 (경계선)** ⚠️튜토리얼/에듀케이터성 — 순도 유의 |

---

## 기각 / 스킵 (사유 한 줄)

| 후보 | 출처 | 사유 |
|--|--|--|
| **Andrej Karpathy** (@karpathy) | X 게시물(2026-01-26): 코딩 워크플로우가 80% 수동→80% 에이전트로 뒤집혔다 + LLM 코드생성 함정 관찰. https://miraflow.ai/blog/karpathy-claude-md-100k-github-stars-ai-coding-2026 | 원문 **하** — 그의 이름을 단 화제의 65줄 CLAUDE.md는 **본인이 아니라 Forrest Chang이 그의 관찰을 정리해 만든 것**(X 유출 기반). 본인 게시물엔 복붙 가능한 verbatim 프롬프트 없음. 원리 상(함정 4원칙: think before acting·keep simple·surgical change·success criteria)이나 워크플로우 중·원문 하 → **상 1 = 기각**. ※'원리 소스'로는 최상급이나 프롬프트 재료 순도 미달(Armin 케이스와 동형). |
| **@steady__study.dev** | Threads https://www.threads.com/@steady__study.dev/post/DUGFSwzgfmA + https://www.stdy.blog/growing-custom-workflow/ | 하네스(superpowers 39k·everything-claude-code 34k·compound-engineering 6.6k·oh-my-claudecode 3.4k) **큐레이션·비교 리뷰**. 본인 verbatim 프롬프트/재현 절차 없음 → 원문 하·워크플로우 중 = 기각. (다른 Worker가 이 repo들 직접 채굴은 별개 가치) |
| **@myoons.k** | Threads https://www.threads.com/@myoons.k/post/DTKc-0oDM_7 | CLI 미숙자용 멀티에이전트 자동배정 **아키텍처 소개**(창 생성→명령 실행→유휴 에이전트 자동배정). "설정 파일·verbatim 프롬프트는 명시 안 함"(WebFetch 확인) → 원문 하 = 기각. |
| **@specal1849** | Threads https://www.threads.com/@specal1849/post/DVAxTwjErQM | Claude Code Teams 기능 vs 자기 워크플로우 **초기 인상평**(고점 높으나 시기상조). 구체 프롬프트·절차 없음 → 원문 하·워크플로우 하 = 기각. |
| **@qjc.ai / @aicoffeechat** | Threads https://www.threads.com/@qjc.ai/post/DXnXgvaE1W2 , https://www.threads.com/@aicoffeechat/post/DXLEB-ak-0V | 코덱스 CLI 비교·서브에이전트 개념 **설명(explainer)** 콘텐츠. 일반론에 가깝고 본인 재현 절차·verbatim 프롬프트 부족 → 기각. |
| 박진형(사이오닉AI, 클로드코드 글로벌 사용량 1위) | 코버리지만 확보: ZDNet https://zdnet.co.kr/view/?no=20251218124432 , 요즘IT 매거진 기사 | **본인 X/Threads 핸들·원문 게시물을 특정 못 함**(검색으로 미확보) → 담당 소스(Threads/X)에서 근거 링크 없음 → 스킵. 코딩 워크플로우 verbatim 미확보. |
| Avi Chawla 슬래시 커맨드 **본문 전문** | https://blog.dailydoseofds.com/p/10-must-use-slash-commands-in-claude | 이메일/프리뷰판은 "size 제약으로 전문은 링크에서"로 게이트. 커맨드 스펙은 위 본 표에 반영, **각 커맨드 markdown 본문 verbatim은 미확보**(스킵). |

---

## 요약 메모 (코디네이터용)

- **담당 소스 특성**: X 본문은 로그인 게이트, Threads는 요약만 노출 → 이 레인은 구조적으로 **원문(RUBRIC #1) 확보가 어렵다**. 그래서 입장 2명 모두 원문이 '중'이고 '경계선'에 걸림.
- **가장 값진 신규 각도**: Boris Cherny의 **review-to-memory 루프**(PR 리뷰 오류 → @claude 태그로 CLAUDE.md 규칙화)와 **precompute-slash-command**. 기준선의 `persistent-context-file`을 *언제·어떻게 갱신하는가*로 심화. 이식 시 patterns 계약서 형식 준수 권장.
- Karpathy는 프롬프트 재료로는 기각이나, **'원리 소스'로는 최상급** — 라이브러리의 원리 주석/근거로 인용 가치는 있음(candidates.md의 Armin 판단과 동일 틀).
