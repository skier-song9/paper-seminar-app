# Example seminar.md Excerpt

A short excerpt showing the target writing quality. Match this density of
page references, the claim/evidence framing, and the Korean-with-English-terms
style. Do not copy the content; it is illustrative only.

```markdown
# Attention Is All You Need

## 0. 메타데이터

- 논문: Attention Is All You Need
- 저자 / 소속: Vaswani et al. / Google Brain, Google Research
- 학회 / 연도: NeurIPS 2017
- 링크: https://arxiv.org/abs/1706.03762
- 한 줄 요약: recurrence 없이 self-attention만으로 sequence transduction을
  수행하는 Transformer를 제안하고, 번역에서 더 적은 학습 비용으로 SOTA를 달성.
- 학습 목표: attention이 recurrence를 대체할 수 있는 이유와 그 대가(장단점)를
  설명할 수 있다.

## 2. 문제 정의와 배경

### 2.3 기존 접근의 한계

- RNN 계열은 토큰을 순차 처리하므로 학습 시 시퀀스 길이만큼의 순차 연산이
  필요하고, 병렬화가 막힌다 (p.2).
- ConvS2S 같은 convolution 기반 접근은 병렬화는 되지만, 멀리 떨어진 두 위치를
  연결하는 데 필요한 연산 수가 거리에 따라 증가한다 (p.2). Transformer는 이를
  상수 횟수의 연산으로 줄이는 대신, attention-weighted averaging으로 인한
  해상도 손실을 Multi-Head Attention으로 상쇄한다 (p.2).

## 3. 논문의 핵심 주장

- Claim: sequence transduction에 recurrence와 convolution은 필요 없고,
  attention만으로 충분하며 오히려 더 병렬화가 잘 된다.
- Contribution: Transformer 아키텍처, Multi-Head Attention,
  positional encoding 기반의 순서 주입.
- Assumption: 시퀀스 전체를 한 번에 볼 수 있는 메모리 예산
  (self-attention은 길이 n에 대해 O(n²) 메모리, p.6 Table 1).
- What changes: 학습이 순차 연산에서 행렬곱 중심의 병렬 연산으로 바뀐다.

## 6. 이 논문에서 진짜 봐야 하는 포인트

- 가장 설득력 있는 근거: Table 2 (p.8) — WMT14 En-De에서 BLEU 28.4로 기존
  최고 대비 +2.0, 학습 비용은 오히려 낮음. 성능과 비용이 동시에 개선됐다는
  것이 claim을 직접 지지한다.
- 가장 약한 근거: 번역 외 태스크 검증은 constituency parsing 하나뿐 (p.9).
  "attention이면 충분하다"는 일반화된 주장에 비해 태스크 커버리지가 좁다.
- 재현/적용 시 조심할 점: label smoothing, warmup 스케줄 등 학습 레시피가
  성능에 크게 기여하며 (p.7), 아키텍처만 가져오면 재현이 안 될 수 있다.
```
