# Scout: Reddit (Worker A)

담당 소스: Reddit (r/ClaudeAI, r/LocalLLaMA, r/ChatGPTCoding, r/cursor, r/ExperiencedDevs).
기준선 대조: research/candidates.md · RUBRIC.md · workstyle-overseas.md · workstyle-baseline.md.

---

## ⛔ 접근 한계 (정직 기록 — 전체 소스 차단)

**Reddit은 이 세션에서 사용 가능한 모든 경로로 접근 불가.** 개별 스레드 스킵이 아니라
소스 전체가 막혔다. 3가지 경로를 모두 시도했고 근거는 아래와 같다.

| 시도 경로 | 결과 | 증거 |
|--|--|--|
| **WebFetch** (`reddit.com`, `old.reddit.com`, `*.json` API) | 차단 | `"Claude Code is unable to fetch from www.reddit.com"` / `old.reddit.com` 동일 |
| **WebSearch** (`allowed_domains:["reddit.com"]`) | 차단 | `400 The following domains are not accessible to our user agent: ['reddit.com']` → Reddit이 Anthropic 크롤러를 robots로 차단 (support.anthropic.com/…/8896518) |
| **WebSearch** (도메인 무필터, reddit 지향 쿼리 6회) | reddit URL 0건 | 반환 링크 전부 dev.to/substack/github — reddit이 인덱스에서 제외됨(위 robots 차단 결과) |
| **브라우저 (claude-in-chrome)** | 연결 안 됨 | `"Browser extension is not connected"` — 확장 미설치/미로그인 |

즉 **(a) 직접 fetch 차단 + (b) 검색 인덱스 제외 + (c) 브라우저 미연결**의 삼중 차단.
Reddit 원문 스레드·댓글을 단 한 건도 열람할 수 없었다.

### 왜 secondary 요약을 넣지 않았나
검색에서 Reddit 내용을 재인용한 2차 출처(dev.to·Substack 글, "creator of Claude Code
Boris Cherny의 워크플로우" 등)는 다수 나왔다. 그러나:
- RUBRIC 철칙 **"링크 없는 주장 금지(실데이터 강제)"** — Reddit 원문을 못 읽는 상태에서
  reddit 링크를 다는 것은 실데이터 위반, 블로거 요약을 reddit 발견으로 세탁하는 것도 오염.
- Boris Cherny 팁은 애초에 Reddit이 아니라 인터뷰/공식 계열이며, 기준선 `patterns/05-anthropic`
  범위와 겹침 → Reddit 스카우트 산출물에 넣을 근거 아님.
- RUBRIC 순도 우선(동점·애매하면 기각) 원칙에 따라 **날조·세탁 대신 공백을 택함.**

---

## 본 표 (RUBRIC 상 2개 이상 통과 후보)

| 인물/핸들 | 출처 링크 | 방식 1~3개(재현 가능한 절차) | 기준선에 이미 있음? | 신규 패턴 후보 | RUBRIC 채점 |
|--|--|--|--|--|--|
| _(없음 — 소스 전체 차단으로 원문 열람 0건)_ | — | — | — | — | — |

---

## 기각 / 미수집 (사유 한 줄)

| 항목 | 사유 |
|--|--|
| Reddit 전체 (r/ClaudeAI, r/LocalLLaMA, r/ChatGPTCoding, r/cursor, r/ExperiencedDevs) | 3중 접근 차단(fetch 차단 + 검색 인덱스 제외 + 브라우저 미연결) → 원문 열람 0건, 실데이터 확보 불가 |
| 2차 출처의 Reddit 요약(dev.to/Substack) | 원문 링크 검증 불가 → "링크 없는 주장 금지" 위반, 순도 우선 미수집 |

---

## 코디네이터 조치 요청 (재수집 조건)

Reddit robots 차단은 브라우저 경로와 무관한 하드 팩트지만, **브라우저 확장(claude-in-chrome)이
연결되면** 로그인 세션으로 Reddit 스레드 직접 열람이 가능해 이 소스를 실제로 채굴할 수 있다.
- 재시도하려면: 사용자 Chrome에 Claude 확장 설치·로그인 후 이 태스크를 브라우저 활성 상태로 재디스패치.
- 그전까지 Reddit 소스는 **수집 0건**으로 기록한다. (지어내지 않음.)
