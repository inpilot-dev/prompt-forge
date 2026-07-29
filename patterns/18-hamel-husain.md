# 18 — Hamel Husain

> 출처: hamel.dev — "Using LLM-as-a-Judge For Evaluation: A Complete Guide" (https://hamel.dev/blog/posts/llm-judge/)
> + "LLM Evals: Everything You Need to Know (FAQ)" (https://hamel.dev/blog/posts/evals-faq/ — 2025-05 게시, 2026-07 갱신).
> ex-GitHub ML 엔지니어, 30여 개 회사의 LLM 평가 체계 구축 컨설턴트. 루브릭: 원문 상(판정기 프롬프트 템플릿 골격이 복붙 가능하게 공개) / 원리 상(왜 척도가 무너지고 이진이 버티는지) / 워크플로우 상(비평 섀도잉 7단계) / 결과물 중(Honeycomb Query Assistant 실사례이나 산출물은 서술 중심) = 상 3, 입장.
> 이식 범위 메모: "채점기를 먼저 만들라"([[build-grader-first]])·"심사 취향을 명시"([[judge-taste-explicit]])·"기준 자체를 갱신"([[update-the-rubric-itself]])은 기존 패턴과 동일해 제외. **판정기를 어떻게 설계·검수하느냐**에 해당하는 4개만 이식.

---

## 판정은 이진으로, 척도 금지 (binary-verdict-not-scale)
- **단계:** 검증기
- **언제:** 산출물 품질을 에이전트에게 채점시킬 때. 여러 항목을 점수로 매기게 하고 싶을 때.
- **Bad:** "정확성·유용성·톤을 각각 1~5점으로 평가해줘." (척도 채점)
- **Good:** 질문을 하나로 줄이고 답을 두 개로 줄인다 — "Did the AI achieve the desired outcome?" → **pass / fail**. 항목을 여러 개 보고 싶으면 점수 축을 늘리지 말고 **이진 질문을 여러 개** 만든다.
- **왜:** "If your evaluations consist of a bunch of metrics that LLMs score on a 1-5 scale (or any other scale), you're doing it wrong." 척도는 눈금 사이 차이가 정의되지 않아 채점자(사람이든 모델이든)마다 다르게 해석되고, **애매한 사례가 전부 중간값으로 숨는다**. 이진은 불확실성을 숨길 곳을 없애서 "무엇이 진짜 중요한가"를 강제로 정의하게 만들고, 라벨링 속도도 빨라진다. 장황하게 써서 점수를 올리는 편법도 통하지 않는다.
- **출처:** Hamel Husain — https://hamel.dev/blog/posts/llm-judge/ , https://hamel.dev/blog/posts/evals-faq/

## 비평 먼저, 판정 나중 (critique-before-verdict)
- **단계:** 검증기
- **언제:** 판정기 프롬프트를 짤 때. 모델이 "좋습니다/통과"만 뱉고 근거가 없을 때.
- **Bad:** "이 결과물 통과인지 아닌지 알려줘." (판정만 요구 → 근거가 사후 정당화로 붙거나 아예 없음)
- **Good:** 출력 순서를 프롬프트에 명시한다 — "For the following query, first write a detailed critique explaining your reasoning, **then** provide a pass/fail judgment in the same format as above." 판정기 템플릿 골격:

  ```
  You are a {domain} evaluator with advanced capabilities to judge
  if a {artifact} is good or not. You understand the nuances of
  {domain-specific knowledge}.

  Here is information about {domain}:
  {{domain_info}}

  Here are some guidelines for evaluating {artifact}:
  {{guidelines}}

  Example evaluations:
  {{few-shot examples — 입력 / 산출물 / 비평+판정}}

  For the following {artifact}, first write a detailed critique
  explaining your reasoning, then provide a pass/fail judgment.
  ```
- **왜:** 판정을 먼저 내놓게 하면 이후 문장은 그 판정을 방어하는 글이 된다. 비평을 먼저 쓰게 하면 판정이 **자기 근거의 결과**로 나오고, 사람이 판정기를 신뢰할지 결정할 때 읽을 것이 남는다. 또 이 비평이 다음 패턴의 재료가 된다.
- **출처:** Hamel Husain — https://hamel.dev/blog/posts/llm-judge/

## 전문가 비평을 few-shot 재료로 승격 (expert-critique-as-fewshot)
- **단계:** 검증기
- **언제:** 판정기가 내 취향·도메인 기준과 어긋날 때. 판정 기준을 말로 다 설명하기 어려울 때.
- **Bad:** "우리 도메인에선 이런 게 중요해" 하고 기준을 계속 말로 덧붙이기.
- **Good:** **비평 섀도잉(critique shadowing)** — ① 판단이 곧 성공 기준인 *한 명*의 도메인 전문가를 정한다(위원회 금지) ② 기능·시나리오·페르소나를 고루 덮는 데이터셋을 만든다 ③ 전문가가 각 사례에 pass/fail + **왜 그런지 비평**을 단다 ④ 드러난 오류를 고치고 ③으로 되돌아간다 ⑤ 이 비평들을 그대로 판정기 프롬프트의 few-shot 예시로 넣는다. 비평을 쓸 때는 "The critique should be detailed enough so that you can use it in a few-shot prompt for a LLM judge" — 새로 합류한 사람이 읽고 이해할 정도로 쓰고, 너무 짧게 쓰지 않는다. few-shot 예시에는 평가할 때 실제로 본 정보(사용자 메타데이터·시스템 정보 등)를 **같이** 넣는다.
- **왜:** 기준을 규칙 목록으로 옮겨 적으면 항상 새는 부분이 생긴다. 판정 사례 + 이유를 통째로 주면 모델이 규칙이 아니라 **판단의 결**을 흡수한다. 부수 효과로, 사람이 비평을 쓰는 동안 정작 고쳐야 할 제품 결함이 먼저 드러난다(④). [[learn-from-reference]]가 스타일을 예시로 학습시키는 것이라면, 이건 *심사 기준*을 예시로 학습시키는 것.
- **출처:** Hamel Husain — https://hamel.dev/blog/posts/llm-judge/

## 판정기 자체를 검수한다 (judge-alignment-check)
- **단계:** 검증기
- **언제:** 판정기를 만들어 자동 채점을 돌리기 시작할 때. "AI가 통과라니까 통과겠지"로 넘어가려 할 때.
- **Bad:** 판정기를 만들자마자 전체 파이프라인에 붙이고 통과율을 지표로 삼기.
- **Good:** 판정기를 **검수 대상**으로 취급한다 — 사람이 라벨링한 사례 일부를 **홀드아웃**으로 빼두고, 판정기가 그 사람 라벨과 얼마나 일치하는지(True Positive / True Negative rate)를 측정해 "수용 가능한 일치"에 도달할 때까지 프롬프트를 고친다. 처음엔 비용 최적화 말고 가장 강한 모델로 시작한다. 그 다음 실패 사례를 오픈 코딩→분류(taxonomy)로 묶어 반복되는 실패 유형에는 **전용 판정기**를 따로 붙인다.
- **왜:** 채점기는 도구가 아니라 **또 하나의 측정 장치**다. 검수 안 된 판정기를 붙이면 잘못된 통과율을 근거로 제품을 튜닝하게 되어 오류가 증폭된다. 사람 라벨과의 일치율은 판정기가 언제 믿을 만한지를 알려주는 유일한 숫자다. [[update-the-rubric-itself]]가 기준을 고치는 루프라면, 이건 기준을 **집행하는 장치**를 교정하는 루프다.
- **출처:** Hamel Husain — https://hamel.dev/blog/posts/evals-faq/ , https://hamel.dev/blog/posts/llm-judge/
