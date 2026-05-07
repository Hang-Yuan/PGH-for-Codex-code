---
name: weekly-review
description: Weekly review: archive work, metabolize memory candidates, and prepare stable identity changes for approval.
created: 2026-05-07
updated: 2026-05-07
---

# weekly-review

Use when the user asks for a weekly review or when the weekly schedule reaches review time.

## Workflow

1. Determine the logical week boundary.
2. Read:
   - `<ASSISTANT_ROOT>/00 专注区/_本周.md`
   - relevant project `_overview.md` and `_progress/`
   - `MEMORY/episodic_inbox.md`
   - `MEMORY/episodic_memory.md`
   - `MEMORY/semantic_memory.md`
   - `MEMORY/MEMORY_LOG.md`
3. Summarize the week by project and key realization.
4. Metabolize memory:
   - expire weak L0 inbox entries
   - merge repeated L0 into L1
   - promote stable L1 into L2
   - decay unused or contradicted L2
   - prepare L3 graduation candidates for user approval
5. Archive the week file when appropriate and create the next week file.
6. Append `MEMORY_LOG.md` for memory changes.
7. Append `ITERATION_LOG.md` for protocol or structure changes.
8. If multi-agent coordination exists, bus-sync weekly decisions and unresolved items.

## Graduation Rule

Do not directly edit USER, persona, or skill files just because a memory reaches high confidence. Present the clean proposed rewrite and wait for confirmation.

## Boundaries

- Do not treat a busy week as evidence of stable identity.
- Do not keep low-value one-off signals just because they are recent.
- Do not overwrite project conclusions during review without checking project authority files.
