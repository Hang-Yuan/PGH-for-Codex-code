---
name: close-node
description: Close a work node by updating progress, pointers, memory candidates, and optional bus handoff.
created: 2026-05-07
updated: 2026-05-07
---

# close-node

Use when a discussion, subproblem, implementation task, or decision has clearly closed.

## Load Chain

- Upstream: `AGENTS.md §Behavior Routing`, user request, or model judgment.
- Peers: `write-progress`, `new-file`, `daily-review`, `weekly-review`.
- Optional handoff: `<AGENT_BUS_ROOT>/agent_bus.md`.

## Authorization Route

If the user explicitly authorizes direct project writes, update project files. Otherwise, write a concise handoff package to the bus or present it to the user.

Identity files, destructive edits, and replacement of established project conclusions remain C-level.

## Workflow

1. Locate the project and node. If ambiguous, ask before writing.
2. Decide whether the node produced a project conclusion, a progress-only record, a memory signal, or a handoff item.
3. If a project conclusion changed, update the project main document or draft the exact proposed insertion.
4. Use `write-progress` to append the process record under `_progress/` when the node adds reasoning, decisions, or next questions.
5. Check loading-chain pointers in touched Markdown files. New files must go through `new-file`.
6. Scan the closed node for memory signals:
   - fresh, one-off calibration -> `episodic_inbox.md`
   - repeated or already clustered 1-3 star schema -> `episodic_memory.md`
   - stable 4-6 star schema -> only through `weekly-review` or explicit approval
7. Update `_本周.md` only when the user authorized shared status maintenance or the repository is single-agent.
8. If multi-agent coordination exists, append a bus summary:
   - mode: direct write / handoff
   - project and node
   - files touched or proposed
   - closed decisions
   - open questions
   - next action

## Boundaries

- Do not replace `daily-review` or `weekly-review`.
- Do not batch-decay memory pools.
- Do not silently edit USER, persona, or another agent's private files.
- Do not treat a one-off observation as identity.
