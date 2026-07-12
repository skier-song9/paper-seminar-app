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

Create one folder under `seminars/`, named from the input paper short title:

```text
seminars/
└── short-title/
    ├── paper.pdf
    ├── seminar.md
    └── figures/
```

Keep all figure links in `seminar.md` relative, for example `figures/method-p12.png`.

## Workflow

0. Check tool availability once, before any other step.
   - Run `command -v pdftoppm` to check Poppler. If missing, do not fail: skip
     deterministic page capture and rely on the harness's PDF preview for
     visual inspection, and note in the final report that figure extraction
     was limited.
   - Run `python3 -c "import pypdf"` to check pypdf. If missing, the workspace
     script still works but cannot guess the folder name from the PDF; always
     pass `--title` in that case.
1. Prepare the workspace.
   - Run `scripts/prepare_paper_workspace.py <input> --title "<short title>"` when useful.
   - The script refuses to overwrite an existing `paper.pdf`. Re-run with
     `--force` only when the user confirms replacing the existing folder.
   - Keep the output under `seminars/`.
   - Save the input paper as `paper.pdf`.
   - Create `figures/`.
   - Do not use `/tmp` during skill execution.
   - If temporary files are needed, keep them inside the output paper folder and delete them before finishing.
2. Read the seminar style guide.
   - Read `references/paper-review-patterns.md`.
   - Read `references/seminar-template.md`.
   - Read `references/example-seminar-excerpt.md` and match its writing
     quality: page references on claims, claim/evidence framing, Korean prose
     with English technical terms.
3. Read the paper like a presenter.
   - First pass: title, abstract, intro, contribution list, figures, main tables, conclusion.
   - Second pass: method details, notation, assumptions, training/inference path, experiments, ablations, limitations.
   - Third pass: build the explanation order; do not mirror paper order when a teaching order is clearer.
   - For long papers (roughly 40+ pages, e.g. surveys or model reports), do not
     read linearly in one sweep. After the first pass, split the paper into
     sections from the table of contents, read section by section, and keep
     short running notes per section inside the paper folder. Use the
     survey/series template variant when the paper covers many works.
4. Extract visuals.
   - Select only visuals needed for understanding: task/problem diagram, model/pipeline, algorithm, main result table, ablation, qualitative examples.
   - Prefer the harness's built-in PDF preview when available for visual inspection.
   - For deterministic page capture, use bundled Poppler directly:
     `pdftoppm -png -singlefile -f 7 -l 7 -r 180 paper.pdf figures/paper-p007`.
   - For cropped capture, never guess crop coordinates. Follow this order:
     1. Render the full page first: `pdftoppm -png -singlefile -f 7 -l 7 -r 180 paper.pdf figures/tmp-p007-full`.
     2. Inspect the full-page image to locate the target region.
     3. Compute `-x -y -W -H` in pixels of the rendered image (top-left origin).
     4. Crop: `pdftoppm -png -singlefile -f 7 -l 7 -r 180 -x 0 -y 0 -W 1200 -H 800 paper.pdf figures/method-p007`.
     5. Delete the temporary full-page render unless `seminar.md` links to it.
5. Write `seminar.md` in Korean.
   - Keep technical terms in English when translation hurts precision.
   - Use the structure in `references/seminar-template.md`.
   - Keep template labels exactly: `메타데이터`, `학습 목표`, `이 자료에서 보는 한계`.
   - Include source page numbers for important claims and every extracted visual.
   - End with expected Q&A and a short list of what still feels uncertain.
   - Before reporting completion, remove temporary files from the paper folder, including hidden partial downloads and intermediate render artifacts not referenced by `seminar.md`.
6. Verify the package before reporting completion.
   - Every `figures/...` link in `seminar.md` points to a file that exists.
   - Every extracted visual and every important claim carries a source page
     number (`p.NN`).
   - The template labels `메타데이터`, `학습 목표`, `이 자료에서 보는 한계` are
     present and unchanged.
   - No temporary or unreferenced files remain in the paper folder.
7. During Q&A, use the `paper-qa` skill.
   - Ground answers in `QA/` evidence created under the paper folder.
   - If a point stays ambiguous, restate it with a smaller example, a diagram-level explanation, or equations.
   - Add useful Q&A notes back into `seminar.md` when the discussion changes the understanding.
8. When Q&A ends, offer a Notion export.
   - First ask the user explicitly whether to organize the result in Notion.
     Never start the export without a yes.
   - If yes, ask the user for the Notion page URL to export into, and wait for
     it. Do not guess or search for a page.
   - Then follow `references/notion-export.md` for the export procedure,
     including the no-connector fallback and figure handling.
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
