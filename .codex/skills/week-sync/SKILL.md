---
name: week-sync
description: Startup synchronization for current week, recent work, and continuity checks.
created: 2026-05-07
updated: 2026-05-07
---

# week-sync

Use during startup after the required files have been read.

## Two Modes

| Day | Mode | Scope |
|---|---|---|
| Monday-Thursday | light sync | current week tasks, recent progress, active blockers |
| Friday-Sunday | deep sync | current week tasks, diff against progress records, review readiness |

## Workflow

1. Read `<ASSISTANT_ROOT>/00 专注区/_本周.md`.
2. Check whether active tasks still match recent project progress.
3. Read only the project overview/progress files needed for currently active tasks.
4. If today is Friday-Sunday, check whether weekly-review has enough material:
   - completed outputs
   - unresolved questions
   - memory candidates
   - archive needs
5. Report the current breakpoint in ordinary language.

## Continuity Check

If the current user request clearly continues an unfinished item, load that item's project chain before answering.

## Boundaries

- Do not run a full weekly review unless asked or scheduled.
- Do not rewrite `_本周.md` during startup without user authorization.
- Do not scan the entire assistant root by default.
