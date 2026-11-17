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

## Project Folders: Code Repositories and Workstreams

- A workstream is a folder for a project or large task, mine or shared with others, where Claude Code structures context and tasks and solves problems. It is not an app codebase.
- Code in a workstream lives in one subfolder per problem, each its own `uv` project with its own dependencies. Add to an existing subfolder only when the new work extends or modifies it; otherwise start a new one.
- Before the first edit in a folder, check that it is a Git repository, so every change can be tracked and reverted. If it isn't, offer to run `git init` and wait for my answer. If I decline, make a timestamped backup of each file before editing it.
- If README.md or CLAUDE.md is missing, create it in my own code repositories. Everywhere else, ask first.
- Create a `docs/` subfolder only when its first record is written — no empty scaffolding.
- Keep each kind of record in its place:

| Location           | Holds                                                                            |
| ------------------ | -------------------------------------------------------------------------------- |
| `README.md`        | What the project is and how to use or run it                                     |
| `CLAUDE.md`        | Durable instructions only — how to work, not what the project is                 |
| `docs/backlog/`    | What's still to do                                                               |
| `docs/goals/`      | `/goal` files built from backlog items; each replaces its item                   |
| `docs/notes/`      | What was discussed, decided, or noted — meetings, conversations, my own notes    |
| `docs/adr/`        | The why behind a significant decision already made: Architecture Decision Record |
| Git commit message | The why behind a change in files or code                                         |

## Decision Memory

- Preserve the reasoning behind decisions, not just the change.
- Significant decision — architecture, direction, an approach chosen over a rejected one, in code or in a workstream — gets an Architecture Decision Record (ADR) in `docs/adr/`: one file per decision, named `NNNN-short-title.md`, with status, date, context, alternatives, rationale. Write it directly; no skill needed.
- Never rewrite an accepted ADR. When a decision changes, write a new ADR that supersedes it and mark the old one as superseded.
- Decision related to file or code changes with a non-obvious why: put the reasoning in the Git commit message — focus on documenting the why, keep the what short. If the decision has an ADR, reference it instead of repeating its reasoning.

## Backlog

- Track outstanding work as a backlog: one Markdown file per task under `docs/backlog/`, starting with this YAML header:

  ```yaml
  ---
  priority: medium              # blocker | high | medium | low — blocker blocks other work, do first
  due: 2026-11-30               # YYYY-MM-DD, or none
  acceptance criteria: <one line: how we know it's done>
  ---
  ```

- If the due date isn't stated, ask before writing the file — never guess a date. `none` is a valid answer.
- Add an `assignee:` line (full name) only where a project's CLAUDE.md asks for it.
- When a task is done, delete its file. Record completion in the Git commit message — the file stays recoverable in history, so no archive folder is needed.

## Notes

- Keep one Markdown file per note under `docs/notes/`, named `YYYY-MM-DD Topic Headline.md`. A note is a meeting, a chat or email conversation I drop in, or a note of my own.
- Start each file with this YAML header:

  ```yaml
  ---
  date: 2026-11-06                      # YYYY-MM-DD; a conversation by its last message
  type: meeting                         # meeting | workshop | one-on-one | chat | email | note
  participants: [Jane Doe, John Smith]  # full names; omit for my own notes
  ---
  ```

- A later part of the same conversation gets its own file that links the earlier note — never append to an existing note.
- Body sections: Discussed, Decided, Tasks — leave out any that would be empty. Tasks are only links to their `docs/backlog/` files — never repeat the task text in the note.
- Meetings and conversations: summarize, don't transcribe — key bullet points, with duplicates and small talk removed, following the summarizing rule under Markdown & Documents. The purpose is known — a record for this workstream — so don't ask what the summary is for.
- My own notes: fix spelling and put them into bullets and sections, but keep every point I wrote.
- When a note covers several workstreams or projects, write one file per project with only that project's part.

## Markdown & Documents

- Before editing a document outside a project folder — Word, Markdown, plain text — make it reversible: rely on Git if it's in a repository, otherwise make a timestamped backup. Edit every document in small, reviewable steps.
- When rewriting or summarizing, preserve meaning first: keep every fact, qualifier, and key term, and when unsure whether a detail matters, keep it. Trim only genuine redundancy. If I ask for shorter than the content safely allows, show me the trade-off instead of silently dropping something.
- Importance depends on my purpose, which isn't in the text. If I ask for a summary without saying what it's for — and the document is long or consequential — ask who it's for and what it should enable. For short or low-stakes text, just summarize.
- The raw file should read cleanly in a plain text editor, not just rendered. Use tables for overviews and comparisons, column-aligned — pad cells so pipes line up and dashes fill the column, no compact tables. Avoid bold; the asterisks only clutter the raw text.

## Python & Tooling

- Prefer Python for scripts, skills, hooks, and automation.
- Use `python`, not `python3`.
- Use `uv` as package manager — `uv pip install`, `uv run`.
- Use `pytest` as the testing framework.
- Global Python versions are managed via `pyenv`.

