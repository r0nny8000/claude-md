# 2. Allow a repo-specific CLAUDE.md

Date: 2026-11-17
Status: Accepted
Amends: 0001

## Context

ADR 0001 renamed the global instructions to `global-instructions.md` so they
would not load twice in this repo. The README turned that into a blanket rule:
no `CLAUDE.md` here at all.

Since then the repo holds `history/` with copies of config files and is
public on GitHub. A rule to check for secrets before committing needs to load
automatically whenever Claude works here.

## Alternatives

| Option                             | Why not chosen                                                   |
| ---------------------------------- | ---------------------------------------------------------------- |
| Rule in README only                | Not auto-loaded; Claude follows it only if it happens to read it |
| Rule in `global-instructions.md`   | Applies to every project, though only this repo needs it         |

## Decision

Allow a `CLAUDE.md` in this repo that holds repo-specific rules only. The
global instructions, or an import of them, still must not go into it, which
keeps 0001's reason intact: nothing loads twice.

## Consequences

- The secret check loads automatically in every session in this repo.
- Repo rules and global rules stay separate, with no overlap to keep in sync.
