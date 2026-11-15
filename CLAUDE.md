# Instructions

## Language

- German is my native language; English is what I work in and want to improve. Default to English, even when I write in German. Mixed German and English is welcome — follow my lead when I switch.

## Validation

- Verify before asserting. Before stating that a function, file, flag, or config value exists, confirm it by reading the file, running the command, or checking current docs.
- Name what you checked and where. If you couldn't verify, say so explicitly — never present unverified information as established.

## Recommendations

- Flag problems, inconsistencies, and better approaches with real consequences — correctness, maintainability, or a decision I'd regret. Never re-raise a suggestion I declined or passed over.
- When a task is done and only polish remains, say so and stop.
- Phrase every recommendation as a decisive action — Do X, not Consider X. Rank by what's expensive to change later, highest first, and mark each high, medium, or low. Drop low-impact items unless I ask for a thorough pass.

## Decisions and Response Format

- Make it easy to see and decide: structured output over walls of text.
- Present comparisons, differences, and lists of changes as a table whenever a side-by-side beats prose — in chat replies too, not just files.
- For a rough proportion or trend, add a simple inline text bar. For an actual chart — pie, line, bar — write an SVG file I can open. Terminals can't render charts inline.
- Present all recommendations first as one batch I can approve with a single yes, then ask open decisions separately — never mix the two.
- Ask decisions with AskUserQuestion so I can pick rather than type, batching related ones into one call. Plain text only when the answer is genuinely free-form.

## Planning

- Work from goals and a checklist, not step-by-step instructions: restate the goal, then track work as a task list you tick off.
- Before starting, state how we'll know the result is right — a passing test for code, or an explicit acceptance criterion otherwise. Make it the checklist's final item.
- For anything beyond a one-sentence diff, write the plan — goal, files, risks, tests, checklist — and wait for my approval before editing. Skip planning when the change fits in one sentence.
- For larger features, put the plan in a file so it survives context resets and I can edit it first.

## Testing

- Work test-first for code. Before fixing a bug, reproduce it, then capture that as a failing test. Before a feature, write a test that defines done. Done means the test goes green, not before.
- Never make a test pass by weakening, skipping, or deleting it. If a test is genuinely outdated or conflicts with a new feature, stop and flag it — change or remove it only with my approval, never silently.

## Code Changes

- Write code for the next human or agent to read. Favor clear, obvious solutions over clever or compact ones: no features beyond what was asked, no abstractions for single-use code, no configurability or error handling nobody requested. If shorter code is harder to follow, keep it readable.
- Comment only to capture the why — the reasoning, trade-off, or constraint behind a non-obvious decision. Never narrate what the code already shows.
- Surgical edits: touch only what the task requires. Don't improve adjacent code, comments, or formatting, and don't refactor what isn't broken.
- Clean up after yourself: remove unused imports, variables, and functions your work orphaned, plus scratch artifacts like test tickets or temp files. Leave others' dead code alone — mention it, don't delete it.

## Decision Memory

- Preserve the reasoning behind decisions, not just the change.
- Significant decision — architecture, direction, an approach chosen over a rejected one — gets an Architecture Decision Record: one file per decision under `docs/adr/` with context, alternatives, rationale. No separate skill needed.
- Smaller decision with a non-obvious why: put the reasoning in the Git commit message — why, not just what.
- Before the first file edit, or when a decision worth recording is made, check the scaffolding exists — Git, `docs/adr/`, a README. If something's missing, offer to set it up; do it yourself when it's safe and obvious, ask first when it isn't.
- Keep each kind of record in its place: a backlog item under `docs/backlog/` is what's still to do; an ADR under `docs/adr/` is the why behind a decision already made; the README is what the project is and how to run it; the Git commit message carries the why behind a smaller change. CLAUDE.md holds only durable instructions — how to work, not what the project is.

## Backlog

- Track outstanding work as a backlog: one Markdown file per task under `docs/backlog/`, with a short YAML header for status, priority, and acceptance criteria.
- When a task is done, delete its file. Record completion in the Git commit message — the file stays recoverable in history, so no archive folder is needed.

## Markdown & Documents

- Before editing a file without a safety net — Word, markdown, plain text outside a repo — make it reversible first: if it's under version control, rely on that; if not, check for Git and offer to put it under version control; only if neither works, make a timestamped backup. Then edit in small, reviewable steps.
- When rewriting or summarizing, preserve meaning first: keep every fact, qualifier, and key term, and when unsure whether a detail matters, keep it. Trim only genuine redundancy. If I ask for shorter than the content safely allows, show me the trade-off instead of silently dropping something.
- Importance depends on my purpose, which isn't in the text. If I ask for a summary without saying what it's for — and the document is long or consequential — ask who it's for and what it should enable. For short or low-stakes text, just summarize.
- The raw file should read cleanly in a plain text editor, not just rendered. Use tables for overviews and comparisons, column-aligned — pad cells so pipes line up and dashes fill the column, no compact tables. Avoid bold; the asterisks only clutter the raw text.

## Python & Tooling

- Prefer Python for scripts, skills, hooks, and automation.
- Use `python`, not `python3`.
- Use `uv` as package manager — `uv pip install`, `uv run`.
- Use `pytest` as the testing framework.
- Global Python versions are managed via `pyenv`.

