---
name: write-progress
description: Record project progress as durable reasoning nodes with clear questions, decisions, and next steps.
created: 2026-05-07
updated: 2026-05-07
---

# write-progress

Use when project work produces reasoning, decisions, attempts, or next questions that should survive the conversation.

## Progress Folder Pattern

```
<project>/_progress/
├── 00_progress_index.md
└── YYYY-MM-DD_short-topic.md
```

## Progress Node Template

```markdown
---
title: <node title>
type: progress
created: YYYY-MM-DD
project: <project name>
upstream:
  - ../_overview.md
peers: []
---

# <node title>

## 问题承接

## 推进

## 结论 / 当前判断

## 新问题

## 下一步
```

## Workflow

1. Locate the project and `_overview.md`.
2. If `_progress/` is missing, create it and add a progress index.
3. Decide whether to append an existing progress file or create a new one.
4. Record the reasoning path, not just the final answer.
5. Use explicit transition markers when useful:
   - `**问题承接**`
   - `**开出**`
   - `**本节收束**`
6. Update `_overview.md` only with stable status and pointers, not full discussion.
7. Update `_本周.md` only when authorized or in single-agent mode.

## Boundaries

- Do not bury stable project conclusions only in progress notes.
- Do not turn every chat message into progress.
- Do not write personal identity facts here; use memory review and identity confirmation.
