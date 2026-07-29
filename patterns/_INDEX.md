# 패턴 역인덱스

단계 → 패턴 매핑. 엔진(SKILL.md)이 크기 판단 후 이 표에서 패턴을 고른다.
단계 분류는 설계 스펙의 9단계(킥오프/컨텍스트주입/리서치위임/PRD/스코핑/솔루션깎기/검증기/구현위임/검증루프).

| 단계 | 패턴 | 파일 |
|---|---|---|
| 킥오프 | 역인터뷰 (reverse-interview) | 00-silvally-alex.md |
| 킥오프 | 원문 통째 복붙 (paste-full-source) | 00-silvally-alex.md |
| 컨텍스트주입 | 조기 발산 차단 (block-early-divergence) | 00-silvally-alex.md |
| 컨텍스트주입 | 인터뷰 상시 개방 (interview-always-open) | 00-silvally-alex.md |
| 리서치위임 | 산출물 구조 지정 (structured-output-spec) — 필드 스펙 | 00-silvally-alex.md |
| 리서치위임 | 프롬프트 파일화·템플릿화 (prompt-as-file-template) — 템플릿 파일화 | 00-silvally-alex.md |
| 리서치위임 | 금지어로 뾰족함 강제 (banned-words-for-sharpness) | 00-silvally-alex.md |
| PRD | 심사자 취향 명시 (judge-taste-explicit) | 00-silvally-alex.md |
| PRD | 수미상관 반복 점검 (coherence-recheck) | 00-silvally-alex.md |
| 스코핑 | 스코핑 재보정 (scoping-recalibration) — ⚠️크게 잡기(위 4개와 방향 반대) | 00-silvally-alex.md |
| 솔루션깎기 | 최종 순간 시뮬레이션 (final-moment-simulation) | 00-silvally-alex.md |
| 솔루션깎기 | 기준 상향 언어 (bar-raising-language) | 00-silvally-alex.md |
| 검증기 | 채점기 선제작 (build-grader-first) — 생성 전 채점기 | 00-silvally-alex.md |
| 구현위임 | 자가수렴 루프 위임 (self-converging-loop-delegation) | 00-silvally-alex.md |
| 구현위임 | 투웨이 검증 (two-way-validation) | 00-silvally-alex.md |
| 구현위임 | 실데이터 강제 (real-data-enforcement) | 00-silvally-alex.md |
| 검증루프 | 평가 기준 자체를 업데이트 (update-the-rubric-itself) | 00-silvally-alex.md |
| 컨텍스트주입 | 세션 재-온보딩 (session-reonboarding) | 00-silvally-alex.md |
| 컨텍스트주입 | 프로젝트 상수 메모리화 (persistent-context-file) | 00-silvally-alex.md |
| 리서치위임 | 레퍼런스로 스타일 학습 (learn-from-reference) | 00-silvally-alex.md |
| 구현위임 | 작동 스냅샷·롤백 (checkpoint-rollback) | 00-silvally-alex.md |
| 구현위임 | 멀티채널 팬아웃 변환 (multichannel-fanout) | 00-silvally-alex.md |
| 검증루프 | 회귀 델타 디버깅 (regression-delta-debug) | 00-silvally-alex.md |
| 리서치위임 | 옵션 메뉴 리서치 (options-menu-research) | 01-simon-willison.md |
| 구현위임 | 함수 시그니처 지정 (function-signature-spec) | 01-simon-willison.md |
| 검증루프 | 테스트 즉시 후속 (tests-as-followup) | 01-simon-willison.md |
| 솔루션깎기 | 대화형 정정 (conversational-refinement) | 01-simon-willison.md |
| 스코핑 | 산출물 파일·입출력 명시 (named-script-spec) — 단일 구현 산출물 | 01-simon-willison.md |
| 컨텍스트주입 | 아키텍처 개요 요청 (architectural-overview) | 01-simon-willison.md |
| 킥오프 | 한 번에 한 질문 정련 (one-question-at-a-time-honing) | 02-harper-reed.md |
| PRD | 대화를 스펙으로 컴파일 (compile-developer-ready-spec) | 02-harper-reed.md |
| 스코핑 | 청크로 쪼갠 프롬프트 시퀀스 (blueprint-to-chunked-prompts) — 순차 청크 | 02-harper-reed.md |
| 구현위임 | todo.md 체크리스트 외부화 (todo-md-checklist) | 02-harper-reed.md |
| 검증기 | 시니어 역할 코드리뷰 (senior-dev-review-pass) | 02-harper-reed.md |
| 검증루프 | 누락 테스트를 이슈 형식으로 (missing-tests-as-issues) | 02-harper-reed.md |
| 스코핑 | 코드 전에 논의 강제 (discuss-before-code) | 03-peter-steinberger.md |
| 컨텍스트주입 | 모델별 톤 조절 (model-specific-tone) | 03-peter-steinberger.md |
| PRD | 스펙을 다른 모델로 교차 비평 (spec-cross-critique) | 03-peter-steinberger.md |
| 솔루션깎기 | 저스펙 후 렌더 보고 다듬기 (under-specify-then-morph) | 03-peter-steinberger.md |
| 구현위임 | 블래스트 반경 산정 (blast-radius-sizing) | 03-peter-steinberger.md |
| 구현위임 | 스캐폴드 후 채우기 (scaffold-then-fill) — 뼈대 먼저 | 04-mitchell-hashimoto.md |
| 솔루션깎기 | 좁은 범위 수술 편집 (narrow-scope-iteration) | 04-mitchell-hashimoto.md |
| 검증기 | 오라클 상담 읽기전용 리뷰 (consult-the-oracle) | 04-mitchell-hashimoto.md |
| 검증루프 | 반슬롭 클린업 세션 (manual-cleanup-pass) | 04-mitchell-hashimoto.md |
| 검증루프 | 실수를 가드레일로 (mistake-to-guardrail) | 04-mitchell-hashimoto.md |
| 킥오프 | 탐색-계획-구현-커밋 (explore-plan-code-commit) | 05-anthropic-cc-bestpractices.md |
| 검증루프 | 합격/불합격 체크 부여 (verification-loop) — 인라인 합격조건 | 05-anthropic-cc-bestpractices.md |
| 구현위임 | 증상 말고 근본원인 (root-cause-fix) | 05-anthropic-cc-bestpractices.md |
| 컨텍스트주입 | 컨텍스트 위생 (context-hygiene) | 05-anthropic-cc-bestpractices.md |
| 리서치위임 | 조사는 서브에이전트에 위임 (delegate-research-to-subagents) — 위임 기본형 | 05-anthropic-cc-bestpractices.md |
| 검증기 | 새 맥락의 적대적 리뷰 (adversarial-review-subagent) | 05-anthropic-cc-bestpractices.md |
| 구현위임 | ralph 루프 (ralph-loop) | 06-geoffrey-huntley.md |
| 스코핑 | 루프당 한 작업 (one-item-per-loop) — 루프 1작업 | 06-geoffrey-huntley.md |
| 컨텍스트주입 | 스택 결정론적 할당 (deterministic-stack-allocation) | 06-geoffrey-huntley.md |
| 리서치위임 | 서브에이전트를 스케줄러로 (subagents-as-scheduler) — 스케줄링 | 06-geoffrey-huntley.md |
| 검증루프 | 테스트로 백프레셔·반스텁 (backpressure-via-tests) | 06-geoffrey-huntley.md |
| PRD | 스펙을 단일 진실원으로 (specs-as-source-of-truth) | 06-geoffrey-huntley.md |
| 솔루션깎기 | 사인으로 루프 튜닝 (tune-with-signs) | 06-geoffrey-huntley.md |
| 킥오프 | 예시 API로 스펙 지정 (spec-by-example-api) | 07-kenton-varda.md |
| 검증루프 | 프롬프트를 diff와 함께 커밋 (commit-the-prompt) | 07-kenton-varda.md |
| 검증기 | 결함 구성을 집어서 교정 (name-the-flawed-construction) | 07-kenton-varda.md |
| 구현위임 | 백업하고 딱 하나만 (back-up-and-do-only-one-thing) | 07-kenton-varda.md |
| 리서치위임 | 스키마 문서도 AI에게 맡겨 검증 (delegate-the-schema-doc) | 07-kenton-varda.md |
| 컨텍스트주입 | 지식 공백 점검 (knowledge-gap-audit) | 08-thorsten-ball.md |
| 스코핑 | 페인트-바이-넘버 스코핑 (paint-by-numbers-scoping) — 지시 해상도 | 08-thorsten-ball.md |
| 킥오프 | 티켓급 첫 프롬프트 (ticket-grade-first-prompt) | 08-thorsten-ball.md |
| 검증루프 | 남이 쓴 코드로 셀프리뷰 (self-review-as-stranger) | 08-thorsten-ball.md |
| 컨텍스트주입 | 읽고-요약시켜 이해 검증 (read-then-summarize) | 09-indragie-karunaratne.md |
| 스코핑 | 사고 강도 계단식 조절 (escalating-think) | 09-indragie-karunaratne.md |
| 솔루션깎기 | UI는 제안 메뉴 먼저 (design-suggestion-menu) | 09-indragie-karunaratne.md |
| 리서치위임 | PRP 생성→실행 2커맨드 파이프라인 (prp-generate-execute) | 10-cole-medin.md |
| 컨텍스트주입 | examples 폴더로 패턴 프라이밍 (examples-folder-priming) | 10-cole-medin.md |
| 구현위임 | 병렬 서브에이전트 웨이브로 발산 생성 (parallel-divergent-waves) — 같은 스펙 N개 변형 | 11-indydevdan-disler.md |
| 리서치위임 | (재게시) 병렬 웨이브로 발산 생성 (parallel-divergent-waves) — 병렬 리서치에도 걸림 | 11-indydevdan-disler.md |
| 솔루션깎기 | 웨이브별 점진 정교화 (progressive-sophistication) | 11-indydevdan-disler.md |
| 컨텍스트주입 | 프롬프트를 프로그래밍 가능한 자산으로 (prompts-as-programmable-assets) | 11-indydevdan-disler.md |
| 킥오프 | grill-me 인터뷰를 1단계로 (grill-me-first) | 12-matt-pocock.md |
| 컨텍스트주입 | compact 금지·항상 clear (always-clear-never-compact) | 12-matt-pocock.md |
| 검증기 | 구현/리뷰 모델 분리 + fresh 리뷰 (implement-review-model-split) | 12-matt-pocock.md |
| 스코핑 | 순차 계획 대신 칸반 DAG (kanban-dag-not-sequential-plan) — 병렬 DAG(에이전트 여럿일 때) | 12-matt-pocock.md |
| PRD | 모듈 맵은 내가, 구현은 위임 (module-map-then-delegate) — 인터페이스 소유권 | 12-matt-pocock.md |
| 컨텍스트주입 | push냐 pull이냐로 지시를 배치 (push-vs-pull-instructions) | 12-matt-pocock.md |
| PRD | PRD 체이닝 — 문서를 다음 문서의 재료로 (prd-document-chaining) | 13-russ-poldrack.md |
| 컨텍스트주입 | 50% 컨텍스트 리프레시 임계값 (context-refresh-threshold) | 13-russ-poldrack.md |
| 스코핑 | 정직한 실패 경계 명시 (honest-failure-boundary) | 13-russ-poldrack.md |
| 검증루프 | 리뷰를 메모리로 되먹임 (review-to-memory) | 14-boris-cherny.md |
| 구현위임 | 반복 명령을 precompute 커맨드로 (precompute-slash-command) | 14-boris-cherny.md |
| 검증기 | PR 열기 전 내가 심문당한다 (grill-before-pr) | 14-boris-cherny.md |
| 솔루션깎기 | 알고 난 뒤 갈아엎기 (scrap-and-reimplement-with-hindsight) | 14-boris-cherny.md |
| 컨텍스트주입 | prompt-drift 방지 — 반복 지시를 커맨드로 (prompt-drift-prevention) | 15-avi-chawla.md |
| 구현위임 | 실패 시 즉시 중단하는 절차 커맨드 (fail-fast-command-chain) | 16-taehojo-vibecoding.md |
| 구현위임 | 역할 릴레이 파이프라인 (agent-relay-pipeline) | 16-taehojo-vibecoding.md |
| 검증기 | 모호성 표현을 감사 대상으로 명문화 (ambiguity-audit-rules) | 16-taehojo-vibecoding.md |
| 컨텍스트주입 | 갈래별 메모리 분기 (per-variant-memory-split) | 16-taehojo-vibecoding.md |
| 컨텍스트주입 | 압박 시나리오로 규칙을 벼리기 (pressure-test-the-rule) | 17-jesse-vincent.md |
| 검증기 | 실패를 눈으로 본 뒤에만 구현 (verify-red-first) | 17-jesse-vincent.md |
| 검증루프 | 증거 없는 완료 선언 금지 (evidence-before-claim) — 증거 제출 강제 | 17-jesse-vincent.md |
| 구현위임 | 재시도 라운드 에스컬레이션·상한 (escalating-retry-rounds) | 17-jesse-vincent.md |
| 검증기 | 판정은 이진으로, 척도 금지 (binary-verdict-not-scale) — LLM 판정기 설계 | 18-hamel-husain.md |
| 검증기 | 비평 먼저, 판정 나중 (critique-before-verdict) — LLM 판정기 설계 | 18-hamel-husain.md |
| 검증기 | 전문가 비평을 few-shot 재료로 승격 (expert-critique-as-fewshot) — LLM 판정기 설계 | 18-hamel-husain.md |
| 검증기 | 판정기 자체를 검수한다 (judge-alignment-check) — LLM 판정기 설계 | 18-hamel-husain.md |
| 컨텍스트주입 | 적정 고도의 지시문 (right-altitude-instructions) | 19-anthropic-engineering-agents.md |
| 컨텍스트주입 | 내용 말고 참조를 줘라 (just-in-time-context) | 19-anthropic-engineering-agents.md |
| 리서치위임 | 위임 예산을 숫자로 배정 (delegation-effort-budget) — 예산·경계 숫자화 | 19-anthropic-engineering-agents.md |
| 검증루프 | 검증 대장과 '테스트 손대기 금지' 조항 (verification-ledger-no-test-edits) — 검증자산 보호 | 19-anthropic-engineering-agents.md |
| 컨텍스트주입 | 인계 요약은 재현율 먼저 (compaction-recall-first) | 19-anthropic-engineering-agents.md |
| PRD | 스펙을 깰 권한 + 편차 1줄 로그 (spec-override-with-decision-log) | 20-snowflow-brief.md |
| 스코핑 | 노력 예산을 부위별로 배분 (effort-budget-allocation) — 부위별 힘 배분 | 20-snowflow-brief.md |
| 검증루프 | 못생긴 마일스톤에서 진행 금지 (milestone-visual-gate) | 20-snowflow-brief.md |
| 검증기 | 테스트를 명시적으로 끄고 이유를 말한다 (tests-off-by-design) | 20-snowflow-brief.md |

> small 케이스(단일 작업)에는 문제정의+검증방법+범위제한 3~4개만 골라 쓴다. 8단계 풀세트 금지.
> large 케이스에만 해당 단계 풀세트를 적용.
>
> 해외 출처(01~08)는 C조사 Worker2 채굴. 채점·기각 근거는 `research/candidates.md`, 재현 가능한 일하는 방식은 `research/workstyle-overseas.md` 참조.
> 신규 출처(09~15)는 병렬 4워커(Reddit·Threads/X·YouTube·블로그) 채굴 — 취합·채점 근거는 `research/scout-SUMMARY.md` 및 `research/scout-*.md`. 15는 경계선(상2), 기존 패턴 "갱신 트리거"로 좁혀 이식. **14는 2026-07-29 재추적으로 원문 확보 → 상3 승격(경계선 해제).**
> **12·14 원문 재추적(2026-07-29):** 12는 `/watch`로 영상 자막+화면 프레임에서 `grill-me` SKILL.md 전문을 확보(상3→상4), 14는 본인 커밋 커맨드 파일 전문 + 2차 스레드 확보(상2→상3). 각각 신규 패턴 3개·1개 추가.
> 3차 채굴(16~20, 2026-07-29)은 4워커 병렬(한국어권·해외신규·1차공식·미완소스재시도). 채점 근거는 `research/candidates.md` §③.
> ⚠️ 충돌 주의: 19의 [[just-in-time-context]](참조만 주기)와 00의 [[paste-full-source]](통째 붙이기)는 표면상 반대다.
> 실격조건·숨은 규격처럼 **누락이 치명적인 자료는 통째로**, 어디가 필요한지 모르는 **대량 코드베이스는 참조만** — 자료 성격으로 갈린다. 19 파일 상단 메모 참조.
