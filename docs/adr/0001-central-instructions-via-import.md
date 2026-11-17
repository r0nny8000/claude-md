# 1. Maintain global instructions centrally via an @import

Date: 2026-11-15
Status: Accepted, amended by 0002

## Context

This repo keeps my global Claude Code instructions under version control.
Claude Code loads every `CLAUDE.md`, `CLAUDE.local.md` and `AGENTS.md` in the
working directory and its ancestors, and loads subdirectory `CLAUDE.md` files
on demand. A file named `CLAUDE.md` here was therefore loaded as project
instructions whenever I worked on it, on top of the identical copy in
`~/.claude/CLAUDE.md`.

## Alternatives

| Option                                 | Why not chosen                                                                                       |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Keep `CLAUDE.md`, add `claudeMdExcludes` | Two copies to sync by hand; correctness depends on a local setting                                   |
| Symlink `~/.claude/CLAUDE.md` to repo  | Edit/Write tools refuse to write through symlinks; Cowork skips a symlinked `~/.claude/CLAUDE.md`    |
| Move file into a subfolder             | Subdirectory `CLAUDE.md` files still load once Claude touches a file there                           |

## Decision

Name the file `global-instructions.md`, a name Claude Code does not
auto-discover. `~/.claude/CLAUDE.md` contains only:

    @~/code/r0nny8000/claude-md/global-instructions.md

User-scope imports load without an approval dialog (source: Claude Code memory
docs, code.claude.com/docs/en/memory).

## Consequences

- One source of truth; edits here take effect in new sessions everywhere.
- Inside this repo the file is plain text, not instructions.
- Cowork desktop sessions skip user-scope imports that point outside the
  session's working directory, so the instructions won't load there.
- The import path is machine-specific; another machine needs the repo cloned
  at the same path or its own one-line `~/.claude/CLAUDE.md`.
