---
name: paper-qa
description: Evidence-grounded Korean Q&A for an existing paper seminar folder. Use when the user wants to ask follow-up questions about a paper already prepared under seminars, clarify ambiguous parts of seminar.md or paper.pdf, create temporary QA evidence, adapt explanations to repeated confusion, and fold Q&A results back into seminar.md.
---

# Paper Q&A

## Input Gate

Identify the target paper folder first. It should look like:

```text
seminars/<short-title>/
├── paper.pdf
├── seminar.md
└── figures/
```

If no target folder is clear, ask the user for the paper folder path and stop.

## Evidence Rule

Create `QA/` under the paper folder at the start:

```text
seminars/<short-title>/QA/
```

Every answer must be grounded in evidence saved in `QA/`. Before answering, save the relevant evidence there, such as:

- `question-log.md`: running Q&A notes.
- `paper-excerpt-pNN.md`: copied/paraphrased paper excerpt with page number.
- `seminar-excerpt.md`: relevant `seminar.md` section.
- `figure-pNN.png`: rendered page or cropped figure/table.
- `scratch.md`: short derivation, toy example, or notation rewrite.

Do not answer from memory alone. If evidence is not yet in `QA/`, create it first. Mention the evidence filename or paper page in the answer.

Reuse existing evidence when it already covers the question: if a file in `QA/` or a section of `seminar.md` answers the question, cite it instead of creating a new evidence file. Create new evidence only when the question needs paper content not yet captured.

Do not use `/tmp`. If temporary files are needed, keep them inside `QA/` and delete them before finishing unless the user asks to preserve `QA/`.

## Answering Flow

1. Read the user question.
2. Add the question to `QA/question-log.md`.
3. Collect minimal evidence into `QA/`.
4. Answer in Korean using `paper.pdf`, `seminar.md`, figures, and `QA/` evidence.
5. If the user asks a similar question again, lower the explanation level:
   - first repeat: fewer terms, more step-by-step wording.
   - second repeat: concrete toy example.
   - third repeat or more: analogy plus tiny numeric/example walkthrough.
6. Add useful clarified notes to `QA/question-log.md`.

Keep answers direct. Technical terms may stay in English when translation harms precision.

## Presenter Behavior

Answer like the seminar presenter:

- Answer from the paper first, then from interpretation, and say which is which.
- If uncertain, say which page/figure/table leaves the ambiguity.
- Convert equations to verbal steps before manipulating symbols.
- Use a concrete example when the user asks "왜?" or "무슨 뜻?".
- Record clarified answers so the final `seminar.md` update reflects the final understanding.

## Seminar Update On Completion

When the user says Q&A is finished:

1. Use `QA/question-log.md` and evidence files to update `seminar.md`.
2. Add explanations to the relevant topic sections when possible. Use `## 10. Q&A 기록` only for content that does not fit elsewhere.
3. Use neutral writing. Do not write phrases like `사용자가 ~~ 개념을 어려워했다`.
4. Remove `QA/` by default.
5. Preserve `QA/` only if the user explicitly asks to keep it.

## Response Grounding

Each answer should make clear which evidence was used, for example:

- `근거: QA/paper-excerpt-p12.md, paper.pdf p.12`
- `근거: QA/figure-p07.png`

If the paper or seminar material does not answer the question, say so and identify the missing evidence.
