# prompt-forge 진행 원장

## 2차 develop — prompt-rate-review
계획: docs/superpowers/plans/2026-07-26-prompt-rate-review.md
브랜치: feat/prompt-rate-review (base: main)

- Task 1: 채점 픽스처 — complete (77adbb6, verbatim 일치)
- Task 2: SKILL.md 작성 — complete (042237c+reframe, 픽스처 5/5 통과)
- Task 3: 교차검증(수동) — complete (rate→forge→rate 델타 확인, #2·#3 점수상승, 축↔슬롯 정합, 심링크 배포)

## 3차 develop — forge-run
계획: docs/superpowers/plans/2026-07-28-forge-run.md

- Task 1: 스킬 파일 + patterns 심링크 — complete (8df0b87)
- Task 2: 전역 배포 + forge 불변 확인 — complete (20b4d81 머지, forge diff 공집합)
- 행동 검증(계획 하단, 컨트롤러 담당) — complete 2026-07-28
  ① 명세 충분 → 다듬은 프롬프트 출력 후 실행, assert 4/4 통과
  ② 명세 부족 → 실행 0건, 빈칸+질문으로 정지
  ③ skills/prompt-forge/ diff 0줄

## 하드닝 (서브에이전트 4각도 검증 후속) — 2026-07-28

4각도(적대적 / 경계선 / large·DRY / 문서정합) 병렬 검증에서 나온 결함 반영:

- **부족분 단위 정의** — "필수 슬롯 중 원본에서 인용 불가한 것의 개수"(small 0~2, large 0~3).
  도달 불가였던 `>3 → 빈칸` 분기 삭제, 빈칸 경로는 "질문해도 안 채워짐"으로 재정의.
  forge·forge-run·설계 스펙 3곳 동시 수정 (같은 모호함이 세 파일에 있었음).
- **스킬 자기수정 금지** — forge-run 자가점검이 forge만 보호하고 자기 자신은 무방비였음.
- **전역 자동화 우선순위** — 전역 CLAUDE.md의 배포/ship 자동화(무확인 push)보다 forge-run 게이트가 앞선다.
- **게이트 무력화 지시 이월 금지 / 부작용 주입 금지 / "알아서 해"는 답 아님 / 파괴적=열거 아닌 정의.**
- **변환 로그 append 추가** — forge-run 경유 변환이 v2 로그 리뷰어 데이터에서 증발하던 구멍.
- **large 단계당 1~2개 상한** — 로그 실측: 13패턴 케이스가 리서치위임 5개 쌓고 구현위임·검증루프 0.
- **심링크 절대경로 → 상대경로**(`../../patterns`). clone·폴더 이동 시 동시 사망 방지.

> 이 하드닝은 "원본 forge 불변" 제약을 의도적으로 깼다. 부족분 모호함이 forge 본체에도
> 있었기 때문(자기 예시가 자기 규칙 위반: `슬롯 3개 초과` ↔ `빈칸 3개`). forge-run만 고치면
> 두 스킬이 같은 입력에 다르게 판정한다.

## 4차 develop — prompt-log-review (feat/prompt-log-review, base ab7a692)
계획: docs/superpowers/plans/2026-07-30-prompt-log-review.md

- Task 1: extract.py 추출기 + 테스트 — complete (커밋 9317b9e..7725c2a, 재리뷰 clean)
  - 리뷰 지적 반영: 태그 언급 프롬프트 생존(startswith 가드), 비객체 JSON 내성(isinstance 가드),
    죽은 import 제거, 절단 경계 정확 assert + 회귀 테스트 4개
  - dedup 접두 삭제는 스펙 명시 동작이라 유지 (Task 2 SKILL.md에 손실 가능성 명시하기로)
  - [Minor·최종리뷰 이관] --list 출력 포맷을 검증하는 테스트 없음
- Task 2: SKILL.md + ledger.md + 전역 배포 — complete (커밋 7804191..594ca0c, 재리뷰 clean)
  - 리뷰 지적 반영: 자가점검에 '축 정의 복제 금지'·'프롬프트당 서브에이전트 금지' 2줄 추가,
    장부 최빈등급 동률 규칙(낮은 등급, 보수적) 명시
  - 컨트롤러 판단: 계획서가 "전문 그대로"를 지시했으나 Global Constraints가 목적이라 자가점검 보강
- Task 3: 실세션 행동 검증 — complete (커밋 1bff557..ca5dd0c, 재리뷰 clean)
  - 실세션 10개(7개 프로젝트)+38MB 최대파일 검증: 노이즈 매치 0/0, 크래시 없음(60ms)
  - 검증 중 발견해 수정: 배시 봉투(<bash-input>/<bash-stdout>)·중단 마커·컨텍스트 압축 서문이
    필터를 통과하던 문제 → SKIP_PREFIXES 접두 검사 추가(언급은 생존)
  - SKILL.md에 워커 세션 주의 + 자가점검 항목 추가 (실세션 10개 중 3개가 Orca 워커 디스패치 세션이었음)
  - 스펙 필터 목록 동기화
