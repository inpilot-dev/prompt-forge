# 기준선 2인 — 일하는 방식 (workstyle-baseline)

기준선 출처(커리어해커 알렉스 · 실밸개발자)의 **재현 가능한 작업 방식**만 모은 노트.
프롬프트 패턴이 아니라 "작업 순서·검증 습관·도구 구성·발행 리듬" 중 남이 따라 할 수 있는 것.
근거 URL 없는 항목은 넣지 않는다.

---

## 접근 한계 (정직 기록)

- **실밸개발자**: 유튜브 외 별도 채널(Threads/X/블로그/뉴스레터/링크드인)을 웹검색으로 **찾지 못함**.
  "실밸개발자"는 공개적으로 검색되는 고유 핸들이 아니었다. 기준선 워크스타일 재료는 이미
  `patterns/00-silvally-alex.md`의 39분 영상 17패턴에 담겨 있고, 그 밖의 유튜브 외 원문은 확보 실패.
  → 아래 workstyle은 대부분 **커리어해커 알렉스**의 유튜브 외 채널에서 나온다. 지어내지 않았다.
- 알렉스의 유료/로그인 콘텐츠(패스트캠퍼스 강의 본편, 뉴스레터 유료분)는 접근하지 않았다. 공개 블로그·Threads 범위에서만 작성.

---

## 커리어해커 알렉스 — 재현 가능한 작업 방식

출처 표기: [블로그]=blog.highoutputclub.com, [Threads]=@careerhackeralex

### 작업 순서
1. **문서 먼저, 코드 나중.** 프로젝트를 열면 PRD·README·initialize.md부터 만들어 "문서 기반 기억"을 세운다. 코드는 그 문서 위에서 시작.
   - 근거: https://blog.highoutputclub.com/vibecoding-with-ai-replit-careerhackeralex/
2. **세션마다 문서 재-온보딩.** 세션이 바뀌면 "initialize.md부터 읽고 구조 이해한 다음 ~부터"로 다시 문을 연다. 기억 손실 방지.
   - 근거: 위 블로그 (→ 패턴 `session-reonboarding`)
3. **작은 단위로 순차 구현.** 기능을 잘게 쪼개(예: "MBTI 선택 버튼 UI부터 → 다음은 결과 페이지") 하나씩 요청. "양이 질을 만든다"는 반복 축적.
   - 근거: 위 블로그
4. **정상 작동마다 스냅샷, 실패하면 롤백.** 되는 지점을 체크포인트로 남겨 무한 디버깅을 끊는다.
   - 근거: 위 블로그 (→ 패턴 `checkpoint-rollback`)

### 검증 습관
- **회귀 델타로 디버깅.** "이전까지 됐는데 X 추가 이후 안 돼" 식으로 변경 경계를 줘서 원인 범위를 좁힌다.
  - 근거: 위 블로그 (→ 패턴 `regression-delta-debug`)
- **progress.md로 진행 상황 추적**, 콘솔 로그를 에이전트와 함께 분석.
  - 근거: 위 블로그
- **Human-on-the-loop 검증 단계를 설계**한다 — 사람이 끼는 확인 지점을 워크플로우에 명시적으로 둔다.
  - 근거: https://www.threads.com/@careerhackeralex

### 도구 구성
- **반복 규칙은 CLAUDE.md에 고정.** 브랜드 컬러·폰트·톤 같은 상수를 프로젝트 메모리 파일에 박아 세션 간 일관성 확보.
  - 근거: https://blog.highoutputclub.com/2026-claude-code-for-non-developers/ (→ 패턴 `persistent-context-file`)
- **반복 작업은 스킬로 자산화.** "프롬프트를 복붙·재작성"하는 대신 `/스킬이름` 한 줄로 부른다. 스킬 정의 시 5요소(작업 정의·트리거·규칙·톤·결과물 형태)를 포함하고, 쓰면서 피드백으로 점진 개선.
  - 근거: https://blog.highoutputclub.com/claude-skills-for-non-developers/
- **레퍼런스 첨부로 스타일 학습.** 추상적 "내 톤" 대신 실제 샘플 파일을 재료로 줘 패턴을 역추출시킨다.
  - 근거: https://blog.highoutputclub.com/claude-cowork-use-cases/ (→ 패턴 `learn-from-reference`)

### 발행 리듬 (재현 가능한 퍼블리싱 루틴)
- **주 1회 1-pager**: 하나의 아이디어를 한 장에 담아 X·Threads·LinkedIn에 **동시** 게시.
- **월 2회 에세이** 발행.
- 하나의 소스를 채널별 포맷(링크드인/인스타 카드뉴스/스레드/오픈채팅 홍보글)으로 **팬아웃 변환**해 재활용.
  - 근거: https://www.careerhackeralex.com/ , https://blog.highoutputclub.com/claude-cowork-use-cases/ (→ 패턴 `multichannel-fanout`)

---

## 실밸개발자

- 유튜브 외 채널 미발견(위 접근 한계 참조). 유튜브 39분 영상 기반 작업 방식은 이미
  `patterns/00-silvally-alex.md`에 17패턴으로 이식됨 — 요약하면:
  평가 루브릭을 먼저 역설계 → 서브에이전트 오케스트레이션으로 위임 → "만점 나올 때까지" 자가수렴 루프
  → 사람+에이전트 two-way 검증 → 기준을 계속 상향. (재인용은 해당 파일 참조.)
- 유튜브 밖 원문을 확보하지 못했으므로 여기에 새 workstyle 항목은 추가하지 않는다. (지어내지 않음.)
