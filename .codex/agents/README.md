# Codex Agents

Codex sub-agents are runtime-specific. This template does not ship custom agent definitions by default.

Suggested public roles:

- `research-agent`: broad academic retrieval and evidence synthesis
- `general-search-agent`: web and conversation-context search
- `project-agent`: scoped implementation or project-audit worker

If your Codex installation supports persistent agent config files, place them in your local Codex configuration directory and reference them from `AGENTS.md` only after testing.
