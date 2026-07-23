# Scout — YouTube (Worker C)

> 담당 소스: **YouTube**. 개발자들이 유튜브 영상(본문·설명란·고정댓글·연동 repo)에서
> 공개한 **본인의 AI 코딩 실제 작업 방식(워크플로우·프롬프트)**만 수집.
> 기준선: candidates.md / RUBRIC.md / workstyle-overseas.md / workstyle-baseline.md.
> 기준선에 이미 있는 인물은 재발굴 안 함 — 아래 3인은 모두 **신규 인물**.
>
> 규칙 준수: 링크 없는 주장 없음. 홍보성·일반론 제외. RUBRIC 상 2개 이상만 본 표.
> ⚠️ 유튜브는 영상 본문의 프롬프트 원문을 텍스트로 재현하기 어려워, 각 인물의
> **영상에 연동된 공개 GitHub repo(프롬프트/커맨드 원문 그대로 공개)**를 원문 근거로 함께 씀.
> 즉 "워크플로우=영상, 복붙 프롬프트=연동 repo" 조합으로 채점.

---

## 본 표 (입장자)

| 인물/핸들 | 출처 링크 | 방식 1~3개 (재현 가능한 절차) | 기준선에 이미 있음? | 신규 패턴 후보 | RUBRIC 채점 |
|--|--|--|--|--|--|
| **Cole Medin** (@ColeMedin) — AI 에듀케이터, 컨텍스트 엔지니어링 전도사 | 영상: "Context Engineering is the New Vibe Coding" https://www.youtube.com/watch?v=Egeuql3Lrzg · X 발표 https://x.com/cole_medin/status/1948792622933315593 · 원문 repo: https://github.com/coleam00/context-engineering-intro | ① **INITIAL.md → `/generate-prp INITIAL.md` → PRP → `/execute-prp PRPs/<feature>.md`** 2단계 커맨드 파이프라인. INITIAL.md는 `FEATURE/EXAMPLES/DOCUMENTATION/OTHER CONSIDERATIONS` 4섹션 고정. generate 단계=리서치+문서수집+구현 청사진 생성, execute 단계=컨텍스트 로드→계획→구현→**검증 게이트 통과할 때까지 반복(validation loop 커맨드에 내장)**. ② **`examples/` 폴더에 따라야 할 코드 패턴을 미리 넣어 프라이밍** ("more examples = better implementations"). ③ 프로젝트 상수는 **CLAUDE.md 전역 규칙**(구조·테스트·스타일·문서 규약)으로 고정. | ❌ 신규 인물 | ✅ **PRP: generate→execute 2커맨드 파이프라인 + execute에 자가 검증루프 내장** (계획→실행 분리를 '재사용 슬래시 커맨드 2개'로 자산화한 게 고유. Alex persistent-context-file·reverse-interview와 구분되는 아티팩트 생성 단계) | 원문 상(repo에 커맨드·템플릿 verbatim 공개) / 원리 상(왜 컨텍스트를 앞단에 몰아넣는가 설명) / 워크플로우 상(6단계 재현) / 결과물 중(repo 예제·데모) → **상 3 = 입장** |
| **IndyDevDan** (disler) — 15년+ 실무, 유튜브 2M+ 뷰, "Agentic Engineering" | 영상: "The One Agent to RULE them ALL" https://www.youtube.com/watch?v=p0mrXfwAbCg · 원문 repo: https://github.com/disler/infinite-agentic-loop (커맨드 원문 `.claude/commands/infinite.md`) · https://github.com/disler/claude-code-is-programmable | ① **Infinite Agentic Loop = 2프롬프트 시스템**: `spec 파일 1개` + `/project:infinite <spec> <out_dir> <count>` 커맨드 1개. 커맨드는 5단계(스펙 분석→출력디렉토리 상태 점검→시작번호·전략 수립→**병렬 서브에이전트 웨이브 배치**→infinite 모드 연속 생성). 각 서브에이전트에 `Spec Context`+`Iteration Assignment(고유 번호)`를 배분, 중복 번호 금지·매 반복 고유값 강제. ② **"progressive sophistication"**: 웨이브가 진행될수록 기본 구현→스펙 경계를 미는 고급 개념으로 정교화(발산형 다변량 생성). ③ **프롬프트/슬래시 커맨드를 '프로그래밍 가능한 자산'으로 버전관리**(claude-code-is-programmable) — 복붙이 아니라 재사용 커맨드. | ❌ 신규 인물 | ✅ **병렬 서브에이전트 웨이브로 "수렴"이 아니라 "발산(N개 고유 변형)" 생성** (실밸 서브에이전트 오케스트레이션은 만점 수렴, Huntley ralph는 단일 기능 반복 — 이건 한 스펙에서 다양한 변형을 병렬 대량 생성하는 반대 방향) | 원문 상(커맨드 `.md` verbatim 공개) / 원리 중(웨이브 정교화 논리) / 워크플로우 상(5단계+커맨드 구문) / 결과물 상(repo·데모) → **상 3 = 입장.** ⚠️ 심화 프레임(Tactical Agentic Coding)은 유료 강의라 미인용 — 무료 repo+영상만 근거 |
| **Matt Pocock** (@mattpocockuk) — TypeScript 에듀케이터(Total TypeScript) | 영상: "Full Walkthrough: Workflow for AI Coding — Matt Pocock" https://www.youtube.com/watch?v=-QFHIoCo-Ko | ① **`grill-me` 스킬을 모든 기능의 1단계로**: 러프 아이디어를 던지면 AI가 **한 번에 한 질문씩** 모호함을 집요하게 캐물어(interview) 스코프가 concrete해질 때까지 반복 → 그 결과를 문서로 굳힘. repo 안에 짧은 CC 프롬프트(스킬)로 상주. ② **"Memento" 규칙 — compact 금지, 항상 `/clear`로 fresh context**: 요약 압축 대신 매번 시스템 프롬프트 상태로 리셋해 **결정론적·반복가능한** 고성능 상태 유지. ③ **구현=Sonnet / 리뷰=Opus, 리뷰는 반드시 fresh context에서**(같은 세션 금지 — "dumb zone" 열화 회피). | ❌ 신규 인물 | ⚠️ **부분 신규**: grill-me는 Alex `reverse-interview`+`session-reonboarding`과 겹침(스킬로 상주·1단계 강제만 추가). 진짜 신규는 **(a) "절대 compact 안 하고 항상 clear" 하드룰**, **(b) 구현/리뷰 모델 역할 분리(Sonnet↔Opus)를 fresh-context 규칙과 결합** | 원문 중(grill-me 프롬프트 전문은 컨퍼런스 발표라 텍스트 재현 확보 실패, 절차는 명확) / 원리 상(Memento·dumb-zone 메커니즘 설명) / 워크플로우 상(준비→실행 루프 재현) / 결과물 상(라이브 데모) → **상 3 = 입장** |

---

## 기각 (RUBRIC 상 2개 미만 — 다시 후보로 올리지 말 것)

| 후보 | 기각 사유 |
|--|--|
| **"Spec-Driven Development" 컨퍼런스 토크 다수** (Erik Hanchett/AWS, Anton Arhipov 등 — YouTube) | 원문 하(복붙 프롬프트 없음, 개념 설명 위주) / 원리 중 / 워크플로우 중(GitHub Spec Kit 툴 소개) / 결과물 중 → **상 0~1 = 기각.** 이미 baseline의 계획/실행 분리·Spec 원리와 중복이고 개인 verbatim 프롬프트가 없음. GitHub Spec Kit은 툴이지 개인 노하우가 아님 |
| **Boris Tane — "How I Use Claude Code"** (boristane.com) | 좋은 워크플로우(계획 승인 없이는 코딩 금지 + "implement it all" 재사용 프롬프트)지만 **블로그 글**이라 담당 소스(YouTube) 밖 → 스킵. (Worker B/블로그 담당에게 이관 가치 있음) |
| **"Claude Code 세팅 10선 / 프롬프트 팁 50" 류 요약 영상** | 원문 없음 + 원리 없음 → 상 0. 홍보성·일반론 |

---

## 접근 한계 (정직 기록)
- 유튜브 **영상 본문 내 프롬프트 원문**은 자동 자막·요약으로만 접근 가능해, verbatim 복붙 근거는
  각 인물의 **연동 공개 repo**(Cole=context-engineering-intro, disler=infinite-agentic-loop)에서 확보.
  repo가 없는 인물(Matt Pocock)은 절차만 확인되고 프롬프트 전문 미확보 → 원문 '중'으로 채점.
- IndyDevDan의 핵심 프레임 상당수는 **유료 강의(Tactical Agentic Coding) 게이트** → 인용 안 함.
  무료 repo + 무료 영상 범위에서만 작성.
- 고정 댓글·설명란은 대부분 repo/강의 링크였고, 그 repo를 직접 근거로 사용함.
