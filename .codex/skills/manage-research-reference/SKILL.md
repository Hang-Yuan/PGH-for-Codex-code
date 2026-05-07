---
name: manage-research-reference
description: Create and maintain project reference records for research-heavy projects.
created: 2026-05-07
updated: 2026-05-07
---

# manage-research-reference

Use when a project first needs literature tracking or when new references should be added.

## Folder Pattern

```
<project>/_reference/
└── 文献记录.md
```

## Reference Record Template

```markdown
## YYYY-MM-DD · Short Title

- Citation:
- Link / DOI:
- Type:
- Status: unread / skimmed / read / used
- Relevance:
- Key claims:
- Notes:
```

## Workflow

1. Confirm the project and whether `_reference/` already exists.
2. Create `_reference/文献记录.md` if missing.
3. Add the reference entry using structured metadata.
4. In project prose, cite only short inline references such as `(Author, Year)` and point to `_reference/文献记录.md` for detail.
5. Update `_overview.md` loading chain if `_reference/` becomes part of the project workflow.

## Boundaries

- Do not fabricate bibliographic metadata.
- For current or high-stakes claims, verify through primary sources.
- Do not mix long reading notes into the project main document.
