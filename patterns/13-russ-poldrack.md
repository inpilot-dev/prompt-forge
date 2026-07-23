# 13 — Russ Poldrack

> 출처: russpoldrack.substack.com — "Workflows for agentic coding" (https://russpoldrack.substack.com/p/workflows-for-agentic-coding-and).
> 신경과학자(스탠퍼드), 오픈소스 `parcelextract` 저자. 루브릭: 원문 상(PRD/PLANNING/TASKS 생성 프롬프트 verbatim) / 원리 중 / 워크플로우 상 / 결과물 상 = 상 3, 입장.
> 검증 근거: `parcelextract` 모듈 실제 산출 + GPU 가속 실패를 정직 기록.

---

## PRD 체이닝 — 문서를 다음 문서의 재료로 (prd-document-chaining)
- **단계:** PRD
- **언제:** 프로젝트를 스펙-드리븐으로 시작할 때, 문서들을 손으로 쓰지 않고 연쇄 생성하되 일관성을 유지하고 싶을 때.
- **Bad:** "이 프로젝트 계획 좀 세워줘." (단발 요청)
- **Good:** "Help me create a Project Requirement Document (PRD) for a Python module called parcelextract that…" → 이어서 "Based on the attached CLAUDE.md and PRD.md files, create a **PLANNING.md**…" → "…create a **TASKS.md** with tasks divided into milestones." (PRD→CLAUDE.md→PLANNING→TASKS→SCRATCHPAD 5파일 척추).
- **왜:** 앞 문서를 다음 문서 생성의 **첨부 재료**로 넘기면 문서 사슬이 서로 정합하게 컴파일된다. 각 단계가 이전 단계를 근거로 삼아 표류를 막는다. [[compile-developer-ready-spec]]·[[specs-as-source-of-truth]]와 같은 계열.
- **출처:** Russ Poldrack — https://russpoldrack.substack.com/p/workflows-for-agentic-coding-and

## 50% 컨텍스트 리프레시 임계값 (context-refresh-threshold)
- **단계:** 컨텍스트주입
- **언제:** 긴 세션에서 언제 새 세션으로 갈아탈지 감이 아니라 수치로 정하고 싶을 때.
- **Bad:** "느려지면 그때 새로 시작하지 뭐." (감으로 판단)
- **Good:** `/context`로 사용률 감시 → **절반 넘으면** `/freshstart` 커스텀 커맨드로 새 세션 온보딩 → 마일스톤 끝에서 `/summ`+commit.
- **왜:** 컨텍스트 리프레시를 수치 임계값(50%)에 걸어 열화 전에 선제적으로 리셋한다. 감이 아니라 계기판으로 관리. [[session-reonboarding]]에 트리거 조건을 수치화해 붙인 형태.
- **출처:** Russ Poldrack — https://russpoldrack.substack.com/p/workflows-for-agentic-coding-and

## 정직한 실패 경계 명시 (honest-failure-boundary)
- **단계:** 스코핑
- **언제:** 무엇을 에이전트에 맡길지 정할 때, 잘 되는 영역과 안 되는 영역을 미리 긋고 싶을 때.
- **Bad:** "AI가 알아서 다 해주겠지." (경계 없이 전부 위임)
- **Good:** 경계를 명시 — "vibe coding은 잘 문서화된 흔한 문제에만 성공한다. GPU 가속 같은 신규 알고리즘은 도메인 전문성이 필요하고 실패한다"를 스코핑 기준으로 삼음.
- **왜:** 잘 되는 영역(문서 풍부·흔한 문제)과 안 되는 영역(신규 알고리즘·희소 도메인)을 미리 구분하면 헛된 위임과 그로 인한 슬롯 낭비를 막는다. 스코핑을 능력 한계에 맞춰 재보정. [[scoping-recalibration]]의 도메인판.
- **출처:** Russ Poldrack — https://russpoldrack.substack.com/p/workflows-for-agentic-coding-and
