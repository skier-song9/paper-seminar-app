# paper-seminar-app

Skill pack for building Korean graduate-level paper seminar packages and
running evidence-grounded Q&A about them.

Supports both [Codex CLI](https://github.com/openai/codex) and
[Claude Code](https://claude.com/claude-code). The skills use the shared
Agent Skills format (`SKILL.md`), so a single source tree under
`.codex/skills/` serves both harnesses.

## Skills

| Skill | What it does |
| --- | --- |
| `paper-seminar` | Takes a paper PDF or arXiv URL, builds `seminars/<short-title>/` with `paper.pdf`, `seminar.md` (Korean), and extracted `figures/`. Offers an optional Notion export at the end. |
| `paper-qa` | Evidence-grounded follow-up Q&A over an existing seminar folder. Every answer cites evidence saved under `QA/`, and finished Q&A is folded back into `seminar.md`. |

`paper-seminar` hands off to `paper-qa` for the Q&A phase, so install both.

## Install

```bash
git clone https://github.com/skier-song9/paper-seminar-app.git
cd paper-seminar-app
./install.sh --codex    # ~/.codex/skills (default when no flag is given)
./install.sh --claude   # ~/.claude/skills
```

`install.sh` symlinks each skill into the chosen skills directory
(`$CODEX_HOME` / `$CLAUDE_CONFIG_DIR` override the base directory), so
`git pull` updates the installed skills in place. Run it once per harness to
install into both.

## Usage

Codex:

```text
$paper-seminar https://arxiv.org/abs/1706.03762
```

Claude Code:

```text
/paper-seminar https://arxiv.org/abs/1706.03762
```

Or just ask in plain language ("이 논문으로 세미나 자료 만들어줘") — the skill
triggers on matching requests.

Output lands under `seminars/` in the current working directory:

```text
seminars/
└── attention-is-all-you-need/
    ├── paper.pdf
    ├── seminar.md
    └── figures/
```

Then ask follow-up questions with the `paper-qa` skill. When Q&A ends, the
skill asks whether to export the result to Notion; if you accept, it asks for
the Notion page URL to export into.

## Dependencies

Both are optional; the skills degrade gracefully without them.

- **Poppler** (`pdftoppm`) — deterministic page/figure rendering. Without it,
  figure extraction falls back to the harness's PDF preview.
- **pypdf** — folder-name guessing from PDF metadata. Without it, pass
  `--title` to the workspace script (the skill does this automatically).

## Development

```bash
python3 -m unittest discover tests
```

Repo layout:

```text
.codex/skills/               # single source tree, shared by both harnesses
├── paper-seminar/
│   ├── SKILL.md
│   ├── agents/openai.yaml   # Codex-only UI metadata; Claude ignores it
│   ├── references/          # templates, style guide, Notion export procedure
│   └── scripts/prepare_paper_workspace.py
└── paper-qa/
    ├── SKILL.md
    └── agents/openai.yaml
tests/                       # unittest suite for the workspace script
```
