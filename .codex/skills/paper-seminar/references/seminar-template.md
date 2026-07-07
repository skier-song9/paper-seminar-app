# seminar.md Template

Use this structure unless the paper type clearly needs the survey/series variant.

```markdown
# {Paper Title}

## 0. 메타데이터

- 논문:
- 저자 / 소속:
- 학회 / 연도:
- 링크:
- 한 줄 요약:
- 학습 목표:

## 1. 먼저 이렇게 읽으면 된다

- 이 논문을 읽는 순서:
- 먼저 알아야 할 개념:
- 헷갈리기 쉬운 포인트:

## 2. 문제 정의와 배경

### 2.1 Task

### 2.2 왜 중요한가

### 2.3 기존 접근의 한계

## 3. 논문의 핵심 주장

- Claim:
- Contribution:
- Assumption:
- What changes:

## 4. Method

### 4.1 전체 구조

![method](figures/{method-image}.png)

### 4.2 구성 요소별 설명

### 4.3 학습 / 추론 절차

### 4.4 수식과 notation

## 5. Experiments

### 5.1 실험 세팅

- Dataset:
- Baseline:
- Metric:
- Protocol:

### 5.2 Main results

![main-results](figures/{result-image}.png)

### 5.3 Ablation / Analysis

### 5.4 Qualitative examples

## 6. 이 논문에서 진짜 봐야 하는 포인트

- 가장 설득력 있는 근거:
- 가장 약한 근거:
- 재현/적용 시 조심할 점:
- 내 연구에 가져올 수 있는 아이디어:

## 7. 한계와 비판

- 논문이 인정한 한계:
- 이 자료에서 보는 한계:
- 추가로 확인하면 좋은 실험:

## 8. 결론

- 기억할 문장:
- 후속 연구 방향:

## 9. 예상 질문과 답변

### Q1.

A.

## 10. Q&A 기록

사용자와 질의응답하며 새로 명확해진 내용을 여기에 추가한다.
```

For survey/series papers, replace sections 3-5 with:

```markdown
## 3. 연구 흐름 지도

| Paper | Problem | Key idea | Limitation fixed | Remaining issue |
| --- | --- | --- | --- | --- |

## 4. Paper별 핵심

### 4.1 {Paper A}

### 4.2 {Paper B}

## 5. 종합 비교
```
