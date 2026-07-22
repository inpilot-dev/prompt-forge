# 01 — Simon Willison

> 출처: simonwillison.net — 주로 "Here's how I use LLMs to help me write code" (2025-03-11).
> Django 공동창시자, Datasette·`llm` CLI 제작자. 루브릭 4항목 전부 상.
> 검증 근거: 한 편의 에세이에 복붙 가능한 프롬프트 ~9개 + 전체 빌드 트랜스크립트(Gist) 공개.
> 콜로폰 기능을 17분·$0.61에 GitHub Pages 배포하고 프롬프트 시퀀스 전문 공개.

---

## 옵션 메뉴 리서치 (options-menu-research)
- **단계:** 리서치위임
- **언제:** 어떤 라이브러리/접근을 쓸지 아직 안 정했고, 한 개 정답이 아니라 선택지 지형이 필요할 때.
- **Bad:** "Rust에서 어떤 HTTP 라이브러리 써야 해?"
- **Good:** "what are options for HTTP libraries in Rust? Include usage examples" / "what are some useful drag-and-drop libraries in JavaScript? Build me an artifact demonstrating each one"
- **왜:** 하나의 답을 요구하면 모델이 임의로 하나 골라 밀어붙인다. "options + usage examples"를 요구하면 지형이 펼쳐지고, 실행·검증 가능한 구체 코드가 딸려 나와 내가 직접 고를 수 있다.
- **출처:** Simon Willison, using-llms-for-code — https://simonwillison.net/2025/Mar/11/using-llms-for-code/

## 함수 시그니처 지정 (function-signature-spec)
- **단계:** 구현위임
- **언제:** 구현을 위임하되 인터페이스(입력·출력·타입)는 내가 설계자로 못 박고 싶을 때.
- **Bad:** "URL에서 DB를 크기 제한 걸어서 받는 함수 짜줘."
- **Good:** "Write a Python function that uses asyncio httpx with this signature: `async def download_db(url, max_size_bytes=5 * 1025 * 1025) -> pathlib.Path`" (시그니처를 통째로 지정)
- **왜:** 그의 말 — "I get to act as the function designer, the LLM does the work of building the body to your specification." 시그니처를 고정하면 내가 소유한 스펙에 대고 본문을 리뷰할 수 있다. 인터페이스 설계는 사람, 본문 채우기는 모델.
- **출처:** Simon Willison, using-llms-for-code — https://simonwillison.net/2025/Mar/11/using-llms-for-code/

## 테스트 즉시 후속 (tests-as-followup)
- **단계:** 검증루프
- **언제:** 구현이 나온 직후, 같은 대화 맥락에서 실행 가능한 검증을 붙일 때.
- **Bad:** 테스트 없이 "잘 되는지 봐줘." 또는 검증 스킵.
- **Good:** "Now write me the tests using pytest"
- **왜:** LLM이 쓴 코드는 반드시 실행해서 검증해야 한다(환각 메서드는 실행에서 드러난다). 구현 직후 같은 맥락에서 테스트를 요구하면 바로 돌려볼 검증물이 생긴다. 실행 가능한 샌드박스 툴과 짝을 이룬다.
- **출처:** Simon Willison, using-llms-for-code — https://simonwillison.net/2025/Mar/11/using-llms-for-code/

## 대화형 정정 (conversational-refinement)
- **단계:** 솔루션깎기
- **언제:** 이전 출력이 살짝 어긋났을 때, 처음부터 다시 짜지 않고 그 자리에서 고칠 때.
- **Bad:** "URL 처리가 틀렸어. 고쳐."
- **Good:** "It looks like it just got the start of the URLs, it should be getting the whole URLs which might be to different websites—so just get anything that starts https:// and ends with whitespace or the end of the commit message"
- **왜:** 관찰된 결함 + 교정 규칙을 평문으로 정확히 준다. 유지된 맥락을 활용해 모델이 자기 이전 출력을 패치하게 만든다. "디지털 인턴에게 상세 지시" 프레이밍.
- **출처:** Simon Willison, using-llms-for-code — https://simonwillison.net/2025/Mar/11/using-llms-for-code/

## 산출물 파일·입출력 명시 (named-script-spec)
- **단계:** 스코핑
- **언제:** 단일 구현 작업의 결과물 형태(파일명·입력 소스·출력)를 사전에 못 박을 때.
- **Bad:** "데이터로 HTML 페이지 만드는 거 하나 만들어줘."
- **Good:** "Write me a new script called `build_colophon.py` which looks through that gathered JSON file and builds and saves an HTML page." / "Build a Python script that checks the commit history for each HTML file in turn and extracts any URLs from those commit messages into a list."
- **왜:** 파일명 + 입력 아티팩트 + 구체적 출력을 지정하면 산출물이 스케치가 아니라 바로 떨어뜨릴 수 있는 완성 단위로 나온다. (리서치 병렬용 [[structured-output-spec]]의 단일 구현판.)
- **출처:** Simon Willison, using-llms-for-code — https://simonwillison.net/2025/Mar/11/using-llms-for-code/

## 아키텍처 개요 요청 (architectural-overview)
- **단계:** 컨텍스트주입
- **언제:** 낯선/거대 코드베이스에 손대기 전에 먼저 지형을 파악할 때.
- **Bad:** "이 코드베이스 설명해줘."
- **Good:** (코드베이스 덤프와 함께) "architectural overview as markdown"
- **왜:** 짧은 프레이밍으로 훑기 좋은 구조 요약을 강제하고, 출력 형식("as markdown")을 고정한다. 편집 전에 오리엔테이션을 먼저 얻는다.
- **출처:** Simon Willison, using-llms-for-code — https://simonwillison.net/2025/Mar/11/using-llms-for-code/
