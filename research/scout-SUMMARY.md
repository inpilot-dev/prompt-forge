# 1차 리서치 병렬 재수행 — 취합 (코디네이터)

4개 워커(Reddit·Threads/X·YouTube·블로그) 병렬 조사 결과를 dedup·RUBRIC 채점해 취합.
원본 근거: `scout-reddit.md` · `scout-threads.md` · `scout-youtube.md` · `scout-blogs.md`.
기준선: `candidates.md` · `RUBRIC.md` · `workstyle-overseas.md` · `workstyle-baseline.md`.

## 소스별 산출

| 워커 | 소스 | 입장 | 기각/스킵 | 비고 |
|--|--|--|--|--|
| A | Reddit | **0** | 전체 | 3중 차단(fetch 차단+검색 인덱스 제외+브라우저 미연결). 지어내지 않고 공백 기록 |
| B | Threads/X | 2 | 6 | 소스 특성상 원문(RUBRIC#1) 확보난 → 입장 2명 원문 '중'·경계선 |
| C | YouTube | 3 | 3 | 워크플로우=영상, verbatim=연동 공개 repo 조합으로 채점 |
| D | 블로그/깃허브 | 2 | 5 | 최고 순도 소스(verbatim 프롬프트 다수) |

## 취합 표 (신규 입장 7명 — RUBRIC 점수순, 인물 중복 없음)

| # | 인물/핸들 | 소스 | 채점 | 핵심 신규 패턴 후보 |
|--|--|--|--|--|
| 1 | **Indragie Karunaratne** (@indragie) | 블로그 | **상4** | read-then-summarize 게이트 / escalating-think 계단(think→ultrathink) / design-suggestion-menu |
| 2 | **Cole Medin** (@ColeMedin) | YouTube | 상3 | PRP generate→execute 2커맨드 파이프라인 + execute에 자가 검증루프 내장 |
| 3 | **IndyDevDan** (disler) | YouTube | 상3 | 병렬 서브에이전트 웨이브로 "발산(N개 고유 변형)" 생성 (수렴의 반대) |
| 4 | **Matt Pocock** (@mattpocockuk) | YouTube | 상3 | compact 금지·항상 /clear(fresh context) 하드룰 / 구현Sonnet↔리뷰Opus 모델 분리 |
| 5 | **Russ Poldrack** | 블로그 | 상3 | PRD-체이닝(문서→다음 문서 첨부 재료) / 50%-컨텍스트 리프레시 임계값 / 정직한 실패 경계 |
| 6 | **Boris Cherny** (@bcherny) | Threads/X | 상2⚠️ | review-to-memory 루프(PR리뷰 오류→@claude태그로 CLAUDE.md 규칙화) / precompute-slash-command |
| 7 | **Avi Chawla** (@_avichawla) | Threads/X | 상2⚠️ | prompt-drift 방지용 재사용 슬래시커맨드 세트 / /orient 경량 재온보딩 |

⚠️ 6·7은 경계선(원문 '중'). Boris는 baseline #5 Anthropic과 원리 일부 중복이나 개인 셋업 구체가 신규.

## 코디네이터 판단 — 이식 우선순위

- **즉시 이식감(상3~4, 순도 높음):** Indragie, Cole Medin, Matt Pocock, Russ Poldrack.
  → 기준선과 안 겹치는 신규 각도가 뚜렷하고 verbatim/재현 절차 확보됨.
- **조건부(경계선):** Boris Cherny·Avi Chawla — review-to-memory·precompute-slash-command·prompt-drift는
  기준선 `persistent-context-file`/`session-reonboarding`의 *심화*라 "갱신 트리거"로만 좁혀 이식 권장.
- **기록만(원리 소스):** Karpathy·Dex Horthy·Böckeler — verbatim 미공개라 패턴 재료 미달, 원리 주석용으로만.

## 재수집 조건 (미완 소스)

- **Reddit:** robots 차단은 하드팩트. claude-in-chrome 확장 연결·로그인 후 브라우저 활성으로 재디스패치하면 채굴 가능.
- **박진형**(클로드코드 글로벌 사용량 1위): 본인 X/Threads 원문 핸들 특정 실패 — 핸들 확보 시 재조사 가치.
