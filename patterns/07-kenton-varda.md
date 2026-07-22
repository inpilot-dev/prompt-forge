# 07 — Kenton Varda

> 출처: Kenton Varda (Cloudflare 수석엔지니어; Google에서 Protocol Buffers v2 오픈소스 릴리스 주도, Cap'n Proto 창시자).
> 프로덕션 라이브러리 `@cloudflare/workers-oauth-provider`(OAuth 2.1, Cloudflare 원격 MCP 인증에 사용)를
> 며칠간 Claude 프롬프팅으로 구현하고, **각 커밋 메시지에 그 diff를 만든 프롬프트 원문을 그대로 넣었다.**
> 커밋 히스토리 = (프롬프트 → 그 프롬프트가 만든 변경) 검증 가능한 로그. 자칭 AI 회의론자였고, AI가 낸 실수(사소한 편집 thrashing, 평문 키 백업 저장, SHA-256 재사용)를 솔직히 공개.
> 채점: 원문 상 / 원리 상 / 워크플로우 상 / 결과물 상 → 상 4개 = 입장.
> (C조사 Worker2 2차 추가분. Simon·Mitchell 등과 겹치지 않는 '보안·감사 가능한 AI 코딩'이 고유 기여.)

---

## 예시 API로 스펙 지정 (spec-by-example-api)
- **단계:** 킥오프
- **언제:** 라이브러리·모듈을 새로 만들 때, 산문으로 요구사항을 나열하기 전에.
- **Bad:** "Write me an OAuth 2 provider library for Cloudflare Workers with token management and client registration."
- **Good:** "We are going to write a TypeScript library that implements the provider side of the OAuth 2 protocol." — 그리고 곧바로 **호출부 예시 코드 블록**을 통째로 붙여 원하는 API 표면을 못박음: `new OAuthProvider({ apiRoute, apiHandler, defaultHandler, authorizeEndpoint, tokenEndpoint, clientRegistrationEndpoint })`, `oauth.parseAuthRequest()`, `oauth.lookupClient()`, `oauth.completeAuthorization()`.
- **왜:** 완성된 사용 예시를 먼저 보여주면 모델이 추측할 API 설계 자유도가 사라지고 사람이 원하는 형태로 수렴한다 — "prompt by example." (01 [[function-signature-spec]]가 함수 1개의 시그니처를 못박는 것이라면, 이건 라이브러리 전체의 *호출부 예시*로 표면을 못박는 상위판.)
- **출처:** 커밋 "Have Claude write an OAuth provider implementation." — https://github.com/cloudflare/workers-oauth-provider/commit/3b2ae809e9256d292079bb15ea9fe49439a0779c

## 프롬프트를 diff와 함께 커밋 (commit-the-prompt)
- **단계:** 검증루프
- **언제:** 감사·재현성·팀 리뷰가 중요한 코드(보안·인프라)를 AI로 생성할 때.
- **Bad:** AI로 코드를 만들고 프롬프트는 버린 채 결과 코드만 커밋한다.
- **Good:** 각 커밋 메시지에 그 diff를 만든 **정확한 프롬프트 원문을 그대로 넣어** 커밋한다 — "Check out the commit history to see how Claude was prompted and what code it produced." 매 커밋 = (프롬프트 → 그 변경) 쌍.
- **왜:** 프롬프트가 곧 코드의 "의도 기록"이 된다. 리뷰어가 무엇을 지시했고 무엇이 생성됐는지 대조·추적할 수 있다. Kenton은 이 투명성 덕에 "not vibe coded — every line reviewed against the RFCs"를 실제로 입증했다. (Harper의 "아티팩트를 파일로 굳혀 커밋"을 *프롬프트 자체*로 확장한 것.)
- **출처:** README 개발 노트 + 전체 커밋 히스토리 — https://github.com/cloudflare/workers-oauth-provider

## 결함 구성을 집어서 교정 (name-the-flawed-construction)
- **단계:** 검증기
- **언제:** 보안·암호 등 도메인 지식이 필요한 코드를 리뷰하며 AI의 그럴듯하지만 틀린 구현을 잡을 때.
- **Bad:** "This encryption doesn't look secure, fix it."
- **Good:** "You used a SHA-256 hash of the token as the key material for wrapping. However, SHA-256 is also how we compute token IDs. With this construction, someone would be able to unwrap the keys using only the token ID." — 무엇이 틀렸는지(같은 SHA-256을 키 유도와 토큰 ID 양쪽에 재사용) + **구체적 공격 경로**를 명시.
- **왜:** AI는 표면적으로 맞는 암호 코드를 자신 있게 생성한다. 리뷰어가 결함의 정확한 메커니즘과 결과를 짚어줘야 올바른 구성으로 수정한다. (그는 Claude가 키/시크릿을 평문 백업으로 저장한 것도 이렇게 잡았다.) 도메인 지식이 사람 쪽에 있을 때의 리뷰 언어.
- **출처:** Neil Madden 분석(암호화 프롬프트·교정 인용) — https://neilmadden.blog/2025/06/06/a-look-at-cloudflares-ai-coded-oauth-library/

## 백업하고 딱 하나만 (back-up-and-do-only-one-thing)
- **단계:** 구현위임
- **언제:** 모델이 간단한 수정에서 헤매며 오히려 코드를 더 망가뜨릴 때.
- **Bad:** 망가진 상태 위에서 "no that's wrong, try again"을 계속 쌓는다.
- **Good:** "No, this last edit made things worse. Let's back up and try again. The only thing you need to do is move the text `export class OAuthProvider {` and the associated doc comment back down so that it appears immediately after the declaration of the ListResult interface. Please don't re-order any of the other declarations." — 이전 실패를 명시적으로 되돌리고, 작업을 단 하나로 축소하며, 건드리지 말 것을 못박음.
- **왜:** 모델이 발산할 때 범위를 최소 단위로 좁히고 불변 조건("나머지는 재정렬 금지")을 주면 thrashing이 멈춘다. (Kenton은 이런 사소한 편집은 "I really could have done this one faster by hand"라며, 언제 손대야 하는지 신호로도 삼았다.) 04 [[narrow-scope-iteration]]과 같은 계열이나, 여기선 *직전 회귀를 명시적으로 되돌리고 + 나머지를 동결*하는 verbatim 커밋 프롬프트가 고유하다.
- **출처:** 커밋 "Ask Claude to fix its bugs." — https://github.com/cloudflare/workers-oauth-provider/commit/9c389439f8c0629f850b03e554c182879c3e4961

## 스키마 문서도 AI에게 맡겨 검증 (delegate-the-schema-doc)
- **단계:** 리서치위임
- **언제:** 구현뿐 아니라 데이터 스키마·API 문서가 1급 산출물로 필요할 때.
- **Bad:** 코드만 AI로 만들고 스토리지 스키마 문서는 사람이 나중에 대충 적는다.
- **Good:** Claude에게 스토리지 스키마 문서 자체를 작성하게 하고(`storage-schema.md`, "Add storage schema by Claude"), 그 문서를 코드와 대조 검토한다 — "the storage schema is carefully designed such that a complete leak of the storage only reveals mundane metadata."
- **왜:** 문서를 모델이 먼저 쓰게 하면 설계 의도가 글로 드러나 코드-문서 불일치를 잡기 쉽고, 스키마의 보안 속성(유출 시 무해성)을 명시적으로 검증할 수 있다. (05 [[delegate-research-to-subagents]]가 조사를 위임한다면, 이건 *1급 문서 산출물*을 위임하고 그 문서를 검증 기준으로 삼는다.)
- **출처:** `storage-schema.md` + README 노트 — https://github.com/cloudflare/workers-oauth-provider/blob/main/storage-schema.md
