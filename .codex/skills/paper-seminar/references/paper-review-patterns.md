# Graduate Paper Review Pattern

Use this file only as distilled process knowledge from graduate-level paper review materials. Do not bundle source PDFs or quote their prose.

## Common Seminar Arc

1. Title slide
   - Paper title, authors, venue/year, citation count when useful, presenter, date.
2. Contents
   - Usually 4-6 sections.
3. Introduction / Background
   - Define task and motivation before details.
   - Explain why the problem is practically or scientifically important.
4. Prior work / Preliminaries
   - Introduce only concepts required to understand the new paper.
   - Build vocabulary: task setting, data shape, metrics, model family, notation.
5. Methodology
   - Show pipeline or architecture first.
   - Then explain each component, objective/loss, training path, inference path.
6. Experiments
   - Dataset, baselines, metrics, main table.
   - Then ablation, sensitivity, qualitative examples, or case study.
7. Discussion / Conclusion
   - Restate the contribution, when it works, why it works, where it may fail.
   - Add presenter opinion, unresolved questions, and future directions.

## Reading Tactics

Read for a teachable chain, not for page order:

1. Claim: identify the one-sentence claim.
2. Gap: identify what previous methods cannot do.
3. Mechanism: identify the smallest mechanism that explains the improvement.
4. Evidence: identify the table/figure proving the claim.
5. Weakness: identify assumptions, missing baselines, fragile metrics, and failure cases.
6. Transfer: decide how this idea could apply to the user's research area.

When writing seminar material, make the first 20% of the document reduce confusion: task definition, why naive baselines fail, and what the paper changes.

## Structure By Paper Type

### Single Method Paper

Use:

- Problem and prior limitation.
- Core idea.
- Architecture/pipeline figure.
- Loss/objective and algorithm.
- Main experiments.
- Ablations and failure cases.

Do not over-explain every module equally. Spend time where the paper differs from prior work.

### Survey, Series, Or Multi-Paper Review

Use:

- Research lineage.
- Comparison table of papers.
- Shared problem.
- How each paper fixes the previous limitation.
- Final synthesis: what changed in the field.

This is common for model-family talks such as foundation model series or GraphRAG series.

### Time-Series Paper

Emphasize:

- Data shape: univariate/multivariate, windowing, horizon, channel count.
- Train/test split and leakage risk.
- Forecasting/anomaly/classification setting.
- Metrics and why each metric can mislead.
- Distribution shift, timestamp use, stationarity, seasonality, drift.
- Inference-time cost and online/offline constraints.

### Anomaly/OOD Paper

Emphasize:

- Is anomaly data used during training?
- Detection vs localization vs segmentation.
- Zero-shot/few-shot/supervised setting.
- Normal-only assumption and contamination risk.
- AUROC, AUPR, FPR95, AUPRO, pixel-level vs image-level metrics.
- Qualitative failures; anomaly papers need visual evidence.

### LLM/RAG/Reasoning Paper

Emphasize:

- Pipeline: corpus, indexing, retrieval, generation, verifier/judge.
- What is learned vs prompted vs retrieved.
- Evaluation data construction and leakage risk.
- Cost/latency/token budget.
- Failure modes: hallucination, retrieval miss, judge bias, benchmark saturation.
- Examples where the method changes the answer.

### Vision/Multimodal Paper

Emphasize:

- Backbone, pretraining data, frozen vs fine-tuned modules.
- Feature resolution and representation alignment.
- Task compatibility: classification, dense prediction, segmentation, grounding, VQA.
- Qualitative figures before metric tables when they clarify the task.
- Dataset/domain gap and annotation assumptions.

### Theory/Architecture Paper

Emphasize:

- Notation table.
- Minimal toy example.
- Theorem/guarantee in plain language.
- Complexity and scaling.
- What the architecture can express that a baseline cannot.

## Presenter Behavior

During Q&A:

- Answer from the paper first, then from interpretation.
- If uncertain, say which page/figure/table leaves ambiguity.
- Convert equations to verbal steps before manipulating symbols.
- Use a concrete example when the user asks "왜?" or "무슨 뜻?".
- Record clarified answers in `seminar.md` so Notion export includes the final understanding.
