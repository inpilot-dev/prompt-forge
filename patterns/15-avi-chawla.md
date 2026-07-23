# 15 — Avi Chawla

> 출처: X @_avichawla (https://x.com/_avichawla/status/2043086745231892982) + 전문 https://www.dailydoseofds.com/p/10-must-use-slash-commands-in-claude-code/.
> AI 엔지니어/에듀케이터(Daily Dose of DS). 루브릭: 원문 중(커맨드 스펙·YAML 프론트매터·`$ARGUMENTS` 구조 공개) / 원리 상(prompt drift 명시) / 워크플로우 상 / 결과물 중 = 상 2, **경계선 입장**. ⚠️튜토리얼/에듀케이터성 — 순도 유의.
> 이식 범위: `/orient`류는 기존 [[session-reonboarding]]과 원리 중복이라 제외. **고유 원리 1개(prompt-drift 방지)만** 채택.

---

## prompt-drift 방지 — 반복 지시를 커맨드로 굳힘 (prompt-drift-prevention)
- **단계:** 컨텍스트주입
- **언제:** 같은 10~15줄 지시(리뷰 기준·커밋 전 점검·테스트 스타일 등)를 매번 기억으로 다시 타이핑하고 있을 때.
- **Bad:** 매 세션 "커밋 전에 디버그문·TODO·하드코딩 시크릿·skip된 테스트 스캔해줘"를 조금씩 다르게 재입력.
- **Good:** 반복 지시를 `.claude/commands/*.md` 슬래시 커맨드로 굳혀 Git 버전관리 — 예 `/preflight`(커밋 전 스캔), `/testmatch`(기존 테스트 관례 학습해 동일 스타일 생성), `/refactor-safe`(public API 시그니처 보존한 채 내부만 리팩터). 매 실행 **동일 문구**.
- **왜:** 반복 지시를 기억으로 재타이핑하면 매번 문구가 조금씩 달라지는 **prompt drift**가 생겨 결과가 흔들린다. 커맨드로 고정하면 케이던스가 일관되고 버전관리로 개선이 누적된다. [[prompt-as-file-template]]에 "표류 방지"라는 *이유*를 명시한 형태.
- **출처:** Avi Chawla (@_avichawla) — https://www.dailydoseofds.com/p/10-must-use-slash-commands-in-claude-code/
