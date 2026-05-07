# CHANGELOG

Template version history. Newer entries go above older entries.

## v0.1.0 · 2026-05-07 · initial public Codex harness

### Added

- `.codex/AGENTS.md` public global instruction template.
- Codex skill set:
  - `close-node`
  - `create-project`
  - `daily-review`
  - `manage-research-reference`
  - `new-file`
  - `week-sync`
  - `weekly-review`
  - `write-progress`
- `assistant/` knowledge-base skeleton:
  - USER layer
  - persona SOUL layer
  - long-term memory
  - focus / project / reading / writing areas
  - v5 memory files: `episodic_inbox.md`, `episodic_memory.md`, `semantic_memory.md`
- optional `agent_bus/` append-only handoff template.
- README installation and customization guide.

### Notes

- This is Codex-native: it does not include Claude Code hooks.
- Startup injection uses `semantic_memory.md`; episodic layers are reviewed explicitly.
- Public template uses placeholders and contains no private paths or personal memory entries.
