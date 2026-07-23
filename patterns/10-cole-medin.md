# 10 — Cole Medin

> 출처: YouTube "Context Engineering is the New Vibe Coding" (https://www.youtube.com/watch?v=Egeuql3Lrzg) + 원문 repo https://github.com/coleam00/context-engineering-intro.
> AI 에듀케이터, 컨텍스트 엔지니어링 전도사. 루브릭: 원문 상(repo에 커맨드·템플릿 verbatim) / 원리 상 / 워크플로우 상 / 결과물 중 = 상 3, 입장.
> 검증 근거: 영상=워크플로우, 연동 공개 repo=복붙 프롬프트. PRP 커맨드 2종·INITIAL 템플릿 그대로 공개.

---

## PRP 생성→실행 2커맨드 파이프라인 (prp-generate-execute)
- **단계:** 리서치위임
- **언제:** 한 기능을 계획-실행 2단계로 자산화하고, 실행 단계에 검증루프를 내장하고 싶을 때.
- **Bad:** "이 기능 만들어줘" (한 번에 계획+구현을 뭉뚱그림).
- **Good:** `INITIAL.md`에 요구를 적고(4섹션 고정: FEATURE / EXAMPLES / DOCUMENTATION / OTHER CONSIDERATIONS) → `/generate-prp INITIAL.md` (리서치+문서수집+구현 청사진 PRP 생성) → `/execute-prp PRPs/<feature>.md` (컨텍스트 로드→계획→구현→**검증 게이트 통과할 때까지 반복**).
- **왜:** 계획(generate)과 실행(execute)을 재사용 슬래시 커맨드 2개로 분리·자산화하면 매번 즉흥 지시가 아니라 버전관리되는 파이프라인이 된다. execute 커맨드에 검증루프를 내장해 자가 수렴시킨다. [[self-converging-loop-delegation]]을 커맨드로 굳힌 형태.
- **출처:** Cole Medin — https://github.com/coleam00/context-engineering-intro

## examples 폴더로 패턴 프라이밍 (examples-folder-priming)
- **단계:** 컨텍스트주입
- **언제:** 구현이 따라야 할 코드 관례·스타일이 있을 때, 말로 설명하는 대신 실물로 보여주고 싶을 때.
- **Bad:** "우리 코드 스타일에 맞춰서 짜줘." (스타일을 말로만 지시)
- **Good:** `examples/` 폴더에 따라야 할 코드 패턴을 미리 넣어두고 참조시킨다 — "more examples = better implementations."
- **왜:** 모델은 서술된 규칙보다 실제 예시를 훨씬 잘 모방한다. 관례를 실물 코드로 프라이밍하면 출력이 프로젝트 결에 붙는다. [[learn-from-reference]]의 코드-내부판.
- **출처:** Cole Medin — https://github.com/coleam00/context-engineering-intro
