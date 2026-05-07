# CHANGELOG

模板版本记录。新版本写在上方。

## v0.1.1 · 2026-05-07 · 单端化 + 全中文模板

### 变更

- 删除跨端通信目录，Codex 公开包不再预设跨端协作或转交给其他智能体。
- 删除 `.codex/agents/` 占位说明，保持最小可用结构。
- README、AGENTS、skills、assistant 骨架文件改为中文口径。
- 安装说明只保留 `<ASSISTANT_ROOT>` 一个占位符。
- 明确 Codex 版是单端自用：启动加载 + skills + 复盘流程驱动记忆代谢。

### 影响

从本版起，公开仓库面向“只使用 Codex Code 的用户”，本模板不内置额外通信区。

## v0.1.0 · 2026-05-07 · 初版 Codex 公共模板

### 新增

- `.codex/AGENTS.md` 全局指令模板。
- Codex skill 集：`close-node`、`create-project`、`daily-review`、`manage-research-reference`、`new-file`、`week-sync`、`weekly-review`、`write-progress`。
- `assistant/` 知识库骨架：USER、SOUL、长期记忆、专注区、项目区、阅读区、写作区、MEMORY。
- v5 记忆文件：`episodic_inbox.md`、`episodic_memory.md`、`semantic_memory.md`。
- README 安装与自定义说明。

### 说明

- Codex 版不包含自动钩子。
- 启动注入读取 `semantic_memory.md`；episodic 两层通过节点闭合、日复盘、周复盘显式整理。
- 公开模板使用占位路径，不含私人姓名、真实路径或个人记忆条目。