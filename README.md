# claude-md

Central, version-controlled home of my global Claude Code instructions.

## How it works

The instructions live in `global-instructions.md`. Claude Code doesn't
auto-load that filename, so inside this repo it is a plain text file, not
active instructions.

`~/.claude/CLAUDE.md` contains a single import line that pulls it in for
every session, in every project:

    @~/code/r0nny8000/claude-md/global-instructions.md

Why this layout and not a symlink or `claudeMdExcludes`: see
`docs/adr/0001-central-instructions-via-import.md`.

## Setup on a new machine

1. Clone this repo to `~/code/r0nny8000/claude-md`.
2. Write the import line into `~/.claude/CLAUDE.md`:

       printf '@~/code/r0nny8000/claude-md/global-instructions.md\n' > ~/.claude/CLAUDE.md

3. Start a new Claude Code session and run `/memory`. It should list
   `global-instructions.md` under User instructions.

## Editing

- Edit `global-instructions.md` and commit. Changes apply from the next new
  session.
- Don't put the global instructions, or an import of them, into a
  `CLAUDE.md`, `CLAUDE.local.md` or `AGENTS.md` here. They would load twice.
  The repo's `CLAUDE.md` holds repo-specific rules only (ADR 0002).

## history/

Backup copies of Claude Code config files, so they can be restored if the
originals get lost.

| File                    | Original                  |
| ----------------------- | ------------------------- |
| `history/settings.json` | `~/.claude/settings.json` |

To update a copy, copy the original over it and commit. To restore, copy it
back.

This repo is public: check a copy for secrets before committing it. The rule
is in `CLAUDE.md`.

## Limitations

- Cowork desktop sessions skip user-scope imports that point outside the
  working directory, so these instructions don't load there.
