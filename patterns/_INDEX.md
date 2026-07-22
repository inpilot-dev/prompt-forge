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

> small 케이스(단일 작업)에는 문제정의+검증방법+범위제한 3~4개만 골라 쓴다. 8단계 풀세트 금지.
> large 케이스에만 해당 단계 풀세트를 적용.
