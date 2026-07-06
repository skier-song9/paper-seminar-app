---
name: paper-seminar
description: Build a Korean graduate-level paper seminar package from a main paper PDF or arXiv URL. Use when the user asks to study a paper, create seminar.md, prepare paper review materials, extract figures/tables/plots from a paper PDF, run presenter-style Q&A about a paper, or later organize the seminar and Q&A into Notion.
---

# Paper Seminar

## Overview

Create a project folder for one main paper, write `seminar.md`, and act as the seminar presenter during follow-up Q&A. Base the seminar style on graduate-level paper review materials, but do not copy source PDFs or prose.

## Input Gate

If the user did not provide a main paper PDF path/file or arXiv URL, ask for one and stop until it is provided.

Accept:
- Local PDF path.
- arXiv abstract URL, PDF URL, or arXiv id.

If the input title is unclear, infer a short title from the PDF/arXiv metadata. If inference is poor, ask for a short title.

## Required Output

Create one folder named from the input paper short title:

```text
short-title/
├── paper.pdf
├── seminar.md
└── figures/
```

Keep all figure links in `seminar.md` relative, for example `figures/method-p12.png`.

## Workflow

1. Prepare the workspace.
   - Run `scripts/prepare_paper_workspace.py <input> --output <target-dir> --title "<short title>"` when useful.
   - Save the input paper as `paper.pdf`.
   - Create `figures/`.
2. Read the seminar style guide.
   - Read `references/paper-review-patterns.md`.
   - Read `references/seminar-template.md`.
3. Read the paper like a presenter.
   - First pass: title, abstract, intro, contribution list, figures, main tables, conclusion.
   - Second pass: method details, notation, assumptions, training/inference path, experiments, ablations, limitations.
   - Third pass: build the explanation order; do not mirror paper order when a teaching order is clearer.
4. Extract visuals.
   - Select only visuals needed for understanding: task/problem diagram, model/pipeline, algorithm, main result table, ablation, qualitative examples.
   - Prefer Codex's PDF preview when available for visual inspection.
   - For deterministic page capture, use bundled Poppler directly:
     `pdftoppm -png -singlefile -f 7 -l 7 -r 180 paper.pdf figures/paper-p007`.
   - For cropped capture, use Poppler crop flags:
     `pdftoppm -png -singlefile -f 7 -l 7 -r 180 -x 0 -y 0 -W 1200 -H 800 paper.pdf figures/method-p007`.
5. Write `seminar.md` in Korean.
   - Keep technical terms in English when translation hurts precision.
   - Use the structure in `references/seminar-template.md`.
   - Include source page numbers for important claims and every extracted visual.
   - End with expected Q&A and a short list of what still feels uncertain.
6. During Q&A, answer as the seminar presenter.
   - Ground answers in `paper.pdf`, `seminar.md`, and the extracted figures.
   - If the user finds a point ambiguous, restate it with a smaller example, a diagram-level explanation, or equations.
   - Add useful Q&A notes back into the Q&A section of `seminar.md` when the discussion changes the understanding.
7. When Q&A ends, ask whether to organize the result in Notion.
   - If yes, create/update the Notion page from `seminar.md` plus Q&A.
   - Use heading prefixes exactly: heading1 `◾`, heading2 `🔻`, heading3 `🔸`.

## Seminar Quality Bar

Explain the paper around these questions:

- What problem is being solved, and why does it matter?
- What did prior work fail to handle?
- What is the paper's core claim in one sentence?
- What is the mechanism, step by step?
- What assumptions must hold?
- Which experiment most directly supports the claim?
- Which ablation or failure case weakens the claim?
- What should the reader remember after one week?

Skip decorative summaries. Prefer a precise explanation of the actual method, evidence, and limitations.
