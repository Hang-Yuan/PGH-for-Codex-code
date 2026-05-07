---
title: ITERATION_LOG
type: iteration-log
created: 2026-05-07
status: active
upstream:
  - .codex/AGENTS.md
downstream: []
---

# ITERATION_LOG

Architecture, protocol, skill, and file-structure changes go here. Memory metabolism belongs in `MEMORY/MEMORY_LOG.md`.

## Entry Template

```markdown
## vX.Y.Z · YYYY-MM-DD · Title

### Summary

### Details

### Impact

### Sync Notes
```

---

## v0.1.0 · 2026-05-07 · initial public Codex harness template

### Summary

Initial public template for a Codex-native predictive memory and workflow harness.

### Details

- Added `.codex/AGENTS.md`.
- Added public skill set: close-node, create-project, daily-review, manage-research-reference, new-file, week-sync, weekly-review, write-progress.
- Added assistant knowledge-base skeleton with v5 default-forget memory layers.
- Added optional append-only agent bus skeleton.

### Impact

Users can install this as a fresh Codex workspace harness, then customize persona, USER, project structure, and memory parameters.

### Sync Notes

Replace `<ASSISTANT_ROOT>` and `<AGENT_BUS_ROOT>` before installation.
