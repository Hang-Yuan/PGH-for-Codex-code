---
name: new-file
description: Ensure every new Markdown file under the assistant root has a clear loading chain and ownership boundary.
created: 2026-05-07
updated: 2026-05-07
---

# new-file

Use whenever creating a Markdown file under `<ASSISTANT_ROOT>`.

## Goal

Make the new file discoverable. Every durable file should state:
- who loads it
- what it governs
- which sibling files it should be checked with

## Frontmatter Template

```yaml
---
title: <title>
type: <area/project/progress/reference/memory/user/persona>
created: YYYY-MM-DD
status: active
upstream:
  - <file that loads this file>
downstream:
  - <files or folders governed by this file>
peers:
  - <sibling files to check together>
---
```

## Workflow

1. Identify the parent area or project.
2. Add frontmatter with upstream, downstream, and peers.
3. Add a short `## 加载链` section if frontmatter is not enough.
4. Update the parent index, `_overview.md`, or area agent only when this file should be discoverable from there.
5. If the file is temporary or scratch-only, mark it as temporary and do not add it to durable loading chains.

## Boundaries

- This skill does not decide whether a file should exist.
- Do not add broad pointers that make every file load every other file.
- Do not write identity facts into a new file unless the user authorized identity-layer changes.
