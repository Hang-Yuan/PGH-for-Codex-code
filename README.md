# Codex Code Harness

A public, customizable persistence harness for Codex-style coding agents. It gives Codex a durable workspace: persona, USER profile, project loading chains, weekly workflow, multi-agent handoff, and a v5 default-forget memory system.

> See [CHANGELOG.md](./CHANGELOG.md) for version history and sync notes.

## What This Is

Codex is strong at implementation, review, and local tool use, but a fresh session does not automatically carry a whole personal knowledge system. This harness externalizes that system into Markdown files and Codex skills.

Core capabilities:

- **Codex-native startup loading** through `.codex/AGENTS.md`.
- **v5 default-forget memory**: `episodic_inbox -> episodic_memory -> semantic_memory -> identity`.
- **Project loading chains**: each durable file declares upstream and downstream pointers.
- **Weekly work loop**: focus file, project progress, daily review, weekly review.
- **Optional multi-agent bus** for handoff between Codex and another assistant.
- **Public-safe template**: no private names, real paths, or personal memory entries.

## Architecture

```text
codex-code-harness/
├── .codex/
│   ├── AGENTS.md
│   ├── agents/
│   │   └── README.md
│   └── skills/
│       ├── close-node/
│       ├── create-project/
│       ├── daily-review/
│       ├── manage-research-reference/
│       ├── new-file/
│       ├── week-sync/
│       ├── weekly-review/
│       └── write-progress/
├── assistant/
│   ├── 长期记忆.md
│   ├── ITERATION_LOG.md
│   ├── 00 专注区/
│   │   ├── 00.专注区_agent.md
│   │   ├── _本周.md
│   │   └── _归档/
│   ├── 01 项目区/
│   │   └── 00.项目区_agent.md
│   ├── 02 阅读区/
│   │   └── 00.阅读区_agent.md
│   ├── 03 写作区/
│   │   └── 00.写作区_agent.md
│   ├── MEMORY/
│   │   ├── 00.memory_agent.md
│   │   ├── episodic_inbox.md
│   │   ├── episodic_memory.md
│   │   ├── semantic_memory.md
│   │   ├── MEMORY_LOG.md
│   │   └── _archive/
│   │       └── semantic_archive.md
│   ├── SOUL/persona/
│   │   └── persona_SOUL.md
│   └── USER/
│       ├── USER.md
│       ├── background.md
│       ├── beliefs.md
│       ├── cognition.md
│       └── personality.md
└── agent_bus/
    ├── rules.md
    └── agent_bus.md
```

## Codex vs Hook-Based Harnesses

This package does not rely on Claude Code hooks. Codex uses:

- `AGENTS.md` for global behavior and startup loading;
- Codex skills for durable workflows;
- explicit review flows for memory metabolism;
- optional bus files for cross-agent handoff.

That means `episodic_inbox.md` is not filled by an automatic per-message hook. Codex is instructed to capture signals during `close-node`, `daily-review`, and explicit memory work.

## Memory Model

| Layer | File | Purpose | Startup |
|---|---|---|---|
| L0 episodic inbox | `assistant/MEMORY/episodic_inbox.md` | fresh calibration signals | no |
| L1 episodic memory | `assistant/MEMORY/episodic_memory.md` | 1-3 star situational schema | no |
| L2 semantic memory | `assistant/MEMORY/semantic_memory.md` | 4-6 star startup schema | yes |
| L3 identity | `assistant/USER`, `assistant/SOUL`, `.codex/skills` | stable identity and procedures | yes / triggered |

Default action is forgetting. A one-off observation should not become identity. Stable schema must survive review, evidence, and explicit approval before it becomes L3.

## Installation

1. Copy `.codex/AGENTS.md` to your Codex global instruction location, usually:

   ```text
   ~/.codex/AGENTS.md
   ```

   You can also adapt it as a project-local `AGENTS.md`.

2. Copy `.codex/skills/*` into your Codex skills directory:

   ```text
   ~/.codex/skills/
   ```

3. Put `assistant/` wherever you want your persistent knowledge base to live.

4. Replace placeholders in `.codex/AGENTS.md` and all skill files:

   ```text
   <ASSISTANT_ROOT>  -> your assistant folder
   <AGENT_BUS_ROOT>  -> your bus folder, or remove bus references if unused
   ```

5. Customize:

   - `assistant/USER/USER.md`
   - `assistant/SOUL/persona/persona_SOUL.md`
   - `assistant/长期记忆.md`
   - `assistant/00 专注区/_本周.md`

6. Start a new Codex conversation. The agent should run the startup sequence, load semantic memory, read current focus, and use `week-sync`.

## Customization

- Rename the assistant persona in `persona_SOUL.md`.
- Add USER subfiles if your stable profile grows.
- Add project templates under `assistant/01 项目区/`.
- Add specialized Codex skills under `.codex/skills/<skill-name>/SKILL.md`.
- If your Codex runtime supports persistent agent configs, add them locally and document them in `.codex/agents/README.md`.

## Design Principles

- **Loading chain over memorization**: files point to the next files Codex should read.
- **Single authority source**: do not define the same fact in multiple places.
- **Default forgetting**: low-confidence signals expire unless they recur.
- **Review before identity**: USER, persona, and skills change only after approval.
- **Append-only handoff**: cross-agent coordination uses bus entries rather than rewriting another agent's records.

## License

MIT. See [LICENSE](./LICENSE).
