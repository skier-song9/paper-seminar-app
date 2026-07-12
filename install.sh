#!/usr/bin/env bash
# Symlink the skills in this repo into a harness skills directory.
#
# Usage:
#   ./install.sh --codex    # install into ~/.codex/skills (default)
#   ./install.sh --claude   # install into ~/.claude/skills
#
# Re-running after `git pull` is safe; existing links are refreshed.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_SRC="$REPO_DIR/.codex/skills"

case "${1:---codex}" in
    --codex)
        SKILLS_DST="${CODEX_HOME:-$HOME/.codex}/skills"
        ;;
    --claude)
        SKILLS_DST="${CLAUDE_CONFIG_DIR:-$HOME/.claude}/skills"
        ;;
    *)
        echo "usage: $0 [--codex | --claude]" >&2
        exit 2
        ;;
esac

mkdir -p "$SKILLS_DST"

for skill_dir in "$SKILLS_SRC"/*/; do
    name="$(basename "$skill_dir")"
    target="$SKILLS_DST/$name"
    if [ -e "$target" ] && [ ! -L "$target" ]; then
        echo "skip: $target exists and is not a symlink; remove it first" >&2
        continue
    fi
    ln -sfn "${skill_dir%/}" "$target"
    echo "linked: $target -> ${skill_dir%/}"
done
