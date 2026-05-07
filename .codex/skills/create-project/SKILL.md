---
name: create-project
description: Create a sustained project container with overview, loading chain, progress area, and optional reference area.
created: 2026-05-07
updated: 2026-05-07
---

# create-project

Use when a new line of work is expected to continue beyond a single exchange.

## Inputs

Confirm:
- project name
- project type: research / engineering / writing / operations / other
- whether the assistant may write inside `<ASSISTANT_ROOT>/01 项目区/`

## Folder Pattern

```
<ASSISTANT_ROOT>/01 项目区/<Project Name>/
├── _overview.md
├── _progress/
└── _reference/        # only when needed
```

## `_overview.md` Minimum Sections

```markdown
---
title: <Project Name>
type: project-overview
created: YYYY-MM-DD
status: active
upstream:
  - ../00.项目区_agent.md
downstream:
  - _progress/
---

# <Project Name>

## 项目定义

## 当前状态

## 加载链

## 推进索引

## 待解问题
```

## Workflow

1. Create the project folder and `_progress/`.
2. Write `_overview.md` with explicit upstream and downstream pointers.
3. If references are needed, use `manage-research-reference`.
4. Add a short entry to the area index or portfolio file when one exists.
5. Add the first task to `<ASSISTANT_ROOT>/00 专注区/_本周.md` only with user authorization.
6. If another assistant owns the shared project area, write a bus package instead of direct files.

## Boundaries

- Do not create a project for a one-off answer.
- Do not invent project conclusions.
- Do not create USER or persona facts from project setup.
