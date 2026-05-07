---
name: daily-review
description: End-of-conversation review: close missed nodes, consume inbox signals, update progress, and prepare handoff.
created: 2026-05-07
updated: 2026-05-07
---

# daily-review

Use when the user asks to summarize, hand off, end the day, or close the current conversation.

## Output Rule

Speak naturally. Do not print internal step labels unless the user asks for an audit trail.

## Pre-Write Rule

Before appending to any log or memory file, read the target file and follow its local template. If the file has no template, append a compact dated entry.

## Workflow

1. Determine logical date:
   - current hour < 06:00 -> previous day
   - otherwise -> current day
2. Scan the conversation for:
   - completed work
   - unresolved questions
   - missed close-node opportunities
   - fresh memory calibration signals
   - project progress that needs a durable record
3. If a work node closed and was not processed, use `close-node` or draft a handoff package.
4. Consume `MEMORY/episodic_inbox.md`:
   - merge duplicates
   - archive expired low-value items
   - promote repeated candidates into `episodic_memory.md`
5. Update `MEMORY/MEMORY_LOG.md` only for memory metabolism.
6. Update `ITERATION_LOG.md` only for architecture, skill, or protocol changes.
7. If multi-agent coordination is active, append bus handoff:
   - what was done
   - files touched
   - proposed shared-truth updates
   - unresolved decisions
8. Give the user a brief, useful close-out.

## Memory Policy

- L0 `episodic_inbox`: lightweight, recent, mostly forgotten.
- L1 `episodic_memory`: 1-3 star candidates.
- L2 `semantic_memory`: 4-6 star startup schema, normally updated by `weekly-review`.
- L3 identity: USER / persona / skills, always C-level.

## Boundaries

- Do not write identity files during daily-review unless explicitly authorized.
- Do not produce a full weekly review unless requested or scheduled.
- Do not duplicate project conclusions already written in a project main document.
