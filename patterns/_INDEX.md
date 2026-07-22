# 패턴 역인덱스

단계 → 패턴 매핑. 엔진(SKILL.md)이 크기 판단 후 이 표에서 패턴을 고른다.
단계 분류는 설계 스펙의 9단계(킥오프/컨텍스트주입/리서치위임/PRD/스코핑/솔루션깎기/검증기/구현위임/검증루프).

| 단계 | 패턴 | 파일 |
|---|---|---|
| 킥오프 | 역인터뷰 (reverse-interview) | 00-silvally-alex.md |
| 킥오프 | 원문 통째 복붙 (paste-full-source) | 00-silvally-alex.md |
| 컨텍스트주입 | 조기 발산 차단 (block-early-divergence) | 00-silvally-alex.md |
| 컨텍스트주입 | 인터뷰 상시 개방 (interview-always-open) | 00-silvally-alex.md |
| 리서치위임 | 산출물 구조 지정 (structured-output-spec) | 00-silvally-alex.md |
| 리서치위임 | 프롬프트 파일화·템플릿화 (prompt-as-file-template) | 00-silvally-alex.md |
| 리서치위임 | 금지어로 뾰족함 강제 (banned-words-for-sharpness) | 00-silvally-alex.md |
| PRD | 심사자 취향 명시 (judge-taste-explicit) | 00-silvally-alex.md |
| PRD | 수미상관 반복 점검 (coherence-recheck) | 00-silvally-alex.md |
| 스코핑 | 스코핑 재보정 (scoping-recalibration) | 00-silvally-alex.md |
| 솔루션깎기 | 최종 순간 시뮬레이션 (final-moment-simulation) | 00-silvally-alex.md |
| 솔루션깎기 | 기준 상향 언어 (bar-raising-language) | 00-silvally-alex.md |
| 검증기 | 채점기 선제작 (build-grader-first) | 00-silvally-alex.md |
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
| 스코핑 | 산출물 파일·입출력 명시 (named-script-spec) | 01-simon-willison.md |
| 컨텍스트주입 | 아키텍처 개요 요청 (architectural-overview) | 01-simon-willison.md |
| 킥오프 | 한 번에 한 질문 정련 (one-question-at-a-time-honing) | 02-harper-reed.md |
| PRD | 대화를 스펙으로 컴파일 (compile-developer-ready-spec) | 02-harper-reed.md |
| 스코핑 | 청크로 쪼갠 프롬프트 시퀀스 (blueprint-to-chunked-prompts) | 02-harper-reed.md |
| 구현위임 | todo.md 체크리스트 외부화 (todo-md-checklist) | 02-harper-reed.md |
| 검증기 | 시니어 역할 코드리뷰 (senior-dev-review-pass) | 02-harper-reed.md |
| 검증루프 | 누락 테스트를 이슈 형식으로 (missing-tests-as-issues) | 02-harper-reed.md |
| 스코핑 | 코드 전에 논의 강제 (discuss-before-code) | 03-peter-steinberger.md |
| 컨텍스트주입 | 모델별 톤 조절 (model-specific-tone) | 03-peter-steinberger.md |
| PRD | 스펙을 다른 모델로 교차 비평 (spec-cross-critique) | 03-peter-steinberger.md |
| 솔루션깎기 | 저스펙 후 렌더 보고 다듬기 (under-specify-then-morph) | 03-peter-steinberger.md |
| 구현위임 | 블래스트 반경 산정 (blast-radius-sizing) | 03-peter-steinberger.md |
| 구현위임 | 스캐폴드 후 채우기 (scaffold-then-fill) | 04-mitchell-hashimoto.md |
| 솔루션깎기 | 좁은 범위 수술 편집 (narrow-scope-iteration) | 04-mitchell-hashimoto.md |
| 검증기 | 오라클 상담 읽기전용 리뷰 (consult-the-oracle) | 04-mitchell-hashimoto.md |
| 검증루프 | 반슬롭 클린업 세션 (manual-cleanup-pass) | 04-mitchell-hashimoto.md |
| 검증루프 | 실수를 가드레일로 (mistake-to-guardrail) | 04-mitchell-hashimoto.md |
| 킥오프 | 탐색-계획-구현-커밋 (explore-plan-code-commit) | 05-anthropic-cc-bestpractices.md |
| 검증루프 | 합격/불합격 체크 부여 (verification-loop) | 05-anthropic-cc-bestpractices.md |
| 구현위임 | 증상 말고 근본원인 (root-cause-fix) | 05-anthropic-cc-bestpractices.md |
| 컨텍스트주입 | 컨텍스트 위생 (context-hygiene) | 05-anthropic-cc-bestpractices.md |
| 리서치위임 | 조사는 서브에이전트에 위임 (delegate-research-to-subagents) | 05-anthropic-cc-bestpractices.md |
| 검증기 | 새 맥락의 적대적 리뷰 (adversarial-review-subagent) | 05-anthropic-cc-bestpractices.md |
| 구현위임 | ralph 루프 (ralph-loop) | 06-geoffrey-huntley.md |
| 스코핑 | 루프당 한 작업 (one-item-per-loop) | 06-geoffrey-huntley.md |
| 컨텍스트주입 | 스택 결정론적 할당 (deterministic-stack-allocation) | 06-geoffrey-huntley.md |
| 리서치위임 | 서브에이전트를 스케줄러로 (subagents-as-scheduler) | 06-geoffrey-huntley.md |
| 검증루프 | 테스트로 백프레셔·반스텁 (backpressure-via-tests) | 06-geoffrey-huntley.md |
| PRD | 스펙을 단일 진실원으로 (specs-as-source-of-truth) | 06-geoffrey-huntley.md |
| 솔루션깎기 | 사인으로 루프 튜닝 (tune-with-signs) | 06-geoffrey-huntley.md |
| 킥오프 | 예시 API로 스펙 지정 (spec-by-example-api) | 07-kenton-varda.md |
| 검증루프 | 프롬프트를 diff와 함께 커밋 (commit-the-prompt) | 07-kenton-varda.md |
| 검증기 | 결함 구성을 집어서 교정 (name-the-flawed-construction) | 07-kenton-varda.md |
| 구현위임 | 백업하고 딱 하나만 (back-up-and-do-only-one-thing) | 07-kenton-varda.md |
| 리서치위임 | 스키마 문서도 AI에게 맡겨 검증 (delegate-the-schema-doc) | 07-kenton-varda.md |
| 컨텍스트주입 | 지식 공백 점검 (knowledge-gap-audit) | 08-thorsten-ball.md |
| 스코핑 | 페인트-바이-넘버 스코핑 (paint-by-numbers-scoping) | 08-thorsten-ball.md |
| 킥오프 | 티켓급 첫 프롬프트 (ticket-grade-first-prompt) | 08-thorsten-ball.md |
| 검증루프 | 남이 쓴 코드로 셀프리뷰 (self-review-as-stranger) | 08-thorsten-ball.md |

> small 케이스(단일 작업)에는 문제정의+검증방법+범위제한 3~4개만 골라 쓴다. 8단계 풀세트 금지.
> large 케이스에만 해당 단계 풀세트를 적용.
>
> 해외 출처(01~08)는 C조사 Worker2 채굴. 채점·기각 근거는 `research/candidates.md`, 재현 가능한 일하는 방식은 `research/workstyle-overseas.md` 참조.
