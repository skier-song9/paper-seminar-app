# Notion Export Procedure

Follow this file when the user agreed to organize a seminar into Notion.

## Preconditions

1. The user explicitly said yes to a Notion export. If not, stop and ask first.
2. The user provided a Notion page URL. If not, ask for it and wait. The URL
   identifies the parent page the seminar content goes into. Do not guess a
   page, search the workspace, or create a page in an unspecified location.

## Tool Check

Check whether a Notion tool (Notion MCP server or connector) is available in
the current session.

- If available: export directly into the page from the provided URL.
- If not available: use the fallback below. Tell the user why.

## Export Rules

- Source of truth is `seminar.md` plus the Q&A notes already folded into it.
- Map headings with these exact prefixes:
  - heading1: `◾`
  - heading2: `🔻`
  - heading3: `🔸`
- Keep Korean prose and English technical terms exactly as written in
  `seminar.md`. Do not re-summarize during export.
- Keep source page references (`p.NN`) in the exported text.

## Figure Handling

Local images under `figures/` cannot be uploaded through the Notion API as
local files. Handle every image link in `seminar.md` as follows:

1. Replace the image with a short caption line that names the figure and its
   source page, for example: `[그림: method pipeline, paper.pdf p.7]`.
2. Tell the user which figures were replaced with captions so they can attach
   the image files manually in Notion if wanted.
3. Never upload figures to third-party hosting to work around this.

## Fallback Without a Notion Tool

If no Notion tool is available in the session:

1. Create `notion-export.md` next to `seminar.md`, containing the full export
   content with the heading prefixes already applied and figures replaced by
   caption lines.
2. Tell the user the file is ready to paste into the Notion page they gave,
   and that no page was created or modified.

## After Export

- Confirm to the user what was written and where (the page URL or the fallback
  file path).
- Do not delete or modify `seminar.md` during export.
