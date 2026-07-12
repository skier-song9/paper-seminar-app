# paper-seminar-app

Codex-only skill pack for building Korean graduate-level paper seminar
packages and running evidence-grounded Q&A about them.

This repository targets the [Codex CLI](https://github.com/openai/codex)
skill format (`.codex/skills/<name>/SKILL.md`) exclusively. It is not a
Claude Code plugin and should stay that way.

## Skills

| Skill | Invoke | What it does |
| --- | --- | --- |
| `paper-seminar` | `$paper-seminar` | Takes a paper PDF or arXiv URL, builds `seminars/<short-title>/` with `paper.pdf`, `seminar.md` (Korean), and extracted `figures/`. Offers an optional Notion export at the end. |
| `paper-qa` | `$paper-qa` | Evidence-grounded follow-up Q&A over an existing seminar folder. Every answer cites evidence saved under `QA/`, and finished Q&A is folded back into `seminar.md`. |

`paper-seminar` hands off to `paper-qa` for the Q&A phase, so install both.

## Install

```bash
git clone https://github.com/skier-song9/paper-seminar-app.git
cd paper-seminar-app
./install.sh
```

`install.sh` symlinks each skill into `~/.codex/skills/` (or
`$CODEX_HOME/skills` if set), so `git pull` updates the installed skills in
place. To install manually, copy or symlink the directories under
`.codex/skills/` into `~/.codex/skills/`.

## Usage

In a Codex session:

```text
$paper-seminar https://arxiv.org/abs/1706.03762
```

Output lands under `seminars/` in the current working directory:

```text
seminars/
└── attention-is-all-you-need/
    ├── paper.pdf
    ├── seminar.md
    └── figures/
```

Then ask follow-up questions with `$paper-qa`. When Q&A ends, the skill asks
whether to export the result to Notion; if you accept, it asks for the Notion
page URL to export into.

## Dependencies

Both are optional; the skills degrade gracefully without them.

- **Poppler** (`pdftoppm`) — deterministic page/figure rendering. Without it,
  figure extraction falls back to Codex's PDF preview.
- **pypdf** — folder-name guessing from PDF metadata. Without it, pass
  `--title` to the workspace script (the skill does this automatically).

## Development

```bash
python3 -m unittest discover tests
```

Repo layout:

```text
.codex/skills/
├── paper-seminar/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   ├── references/          # templates, style guide, Notion export procedure
│   └── scripts/prepare_paper_workspace.py
└── paper-qa/
    ├── SKILL.md
    └── agents/openai.yaml
tests/                       # unittest suite for the workspace script
```
