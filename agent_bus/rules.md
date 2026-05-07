---
title: agent_bus rules
type: bus-rules
created: 2026-05-07
status: template
---

# agent_bus Rules

The bus is an optional append-only handoff channel between agents.

## Rules

- Append only; do not edit another agent's prior message.
- Use timestamps.
- State sender, recipient, context, files, and requested action.
- If there is a conflict, append a conflict note instead of rewriting history.
- Do not place private secrets or credentials here.

## Entry Template

```markdown
## YYYY-MM-DD HH:mm · from <agent> to <agent/user>

- Context:
- Files:
- Summary:
- Requested action:
- Open questions:
```
