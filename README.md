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
- Don't add a file named `CLAUDE.md`, `CLAUDE.local.md` or `AGENTS.md` here,
  and don't pick "Project instructions" in `/memory` in this repo. Any of
  those would load as instructions again.

## Limitations

- Cowork desktop sessions skip user-scope imports that point outside the
  working directory, so these instructions don't load there.
