# PGH for Codex Code

一个给 Codex / Codex Code 使用的持久化工作系统模板。它把 Codex 的身份、用户档案、项目加载链、周工作流和 v5 默认遗忘记忆架构放进一套可复制的 Markdown 骨架里。

> 最新版本见 [CHANGELOG.md](./CHANGELOG.md)。

## 这是什么

Codex 很擅长写代码、审查、重构和本地工具调用，但新会话默认不会自动拥有一套长期知识库。这个系统做的是：把长期上下文外置成文件，让 Codex 每次启动时沿加载链读取，需要记录时按 skill 写入。

核心能力：

- **Codex 原生启动序列**：通过 `.codex/AGENTS.md` 规定启动读取顺序。
- **v5 默认遗忘记忆架构**：`episodic_inbox -> episodic_memory -> semantic_memory -> 身份层`。
- **项目加载链**：每个长期文件都写清楚上游、下游和同级联动，避免 Codex 靠硬记目录结构。
- **周工作循环**：本周任务、项目推进、节点闭合、日复盘、周复盘。
- **单端自用**：不包含跨端通信层，不预设把内容交给另一个智能体处理。
- **公开模板**：不含私人姓名、真实路径或个人记忆条目。

## 目录结构

```text
codex-code-harness/
├── .codex/
│   ├── AGENTS.md
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
├── CHANGELOG.md
├── LICENSE
└── README.md
```

## Codex 版的运行方式

这版不依赖自动钩子。Codex 通过三件事运行：

1. `.codex/AGENTS.md` 规定全局行为和启动加载。
2. `.codex/skills/` 承接节点闭合、项目推进、日复盘、周复盘等流程。
3. `assistant/` 保存长期知识库和记忆候选池。

因此 `episodic_inbox.md` 不会自动逐消息写入；它由 Codex 在节点闭合、日复盘或明确记忆整理时写入。这样更适合 Codex 当前的使用方式，也更容易部署到公开仓库。

## 记忆架构

| 层级 | 文件 | 存什么 | 启动注入 |
|---|---|---|---|
| L0 情景收件箱 | `assistant/MEMORY/episodic_inbox.md` | 新鲜校准信号 | 否 |
| L1 情景记忆 | `assistant/MEMORY/episodic_memory.md` | 1-3 星情境级模式 | 否 |
| L2 语义记忆 | `assistant/MEMORY/semantic_memory.md` | 4-6 星启动注入模式 | 是 |
| L3 身份层 | `assistant/USER`、`assistant/SOUL`、`.codex/skills` | 稳定身份与行为程序 | 是 / 触发时 |

默认动作是遗忘。一次性观察不应直接写成身份层；只有复现、稳定、有证据的模式才能逐级上行。

## 安装

1. 把 `.codex/AGENTS.md` 复制到 Codex 全局指令位置，通常是：

   ```text
   ~/.codex/AGENTS.md
   ```

   也可以按需要改成项目内 `AGENTS.md`。

2. 把 `.codex/skills/*` 复制到 Codex 技能 目录：

   ```text
   ~/.codex/skills/
   ```

3. 把 `assistant/` 放到你想保存长期知识库的位置。

4. 全局搜索并替换占位符：

   ```text
   <ASSISTANT_ROOT> -> 你的 assistant 文件夹路径
   ```

5. 按自己的情况填写：

   - `assistant/USER/USER.md`
   - `assistant/SOUL/persona/persona_SOUL.md`
   - `assistant/长期记忆.md`
   - `assistant/00 专注区/_本周.md`

6. 启动新的 Codex 会话。Codex 应按启动序列读取身份层、USER、语义记忆、当前处境和本周任务。

## 自定义

- 在 `persona_SOUL.md` 里定义 Codex 的名字、语气和工作风格。
- 在 `USER/` 下维护稳定用户档案。
- 在 `01 项目区/` 下建立持续项目。
- 在 `.codex/skills/` 下新增自己的工作流 skill。
- 按需要调整记忆阈值，例如 semantic 启动注入条数、episodic 保留时间、周复盘升降规则。

## 设计原则

- **加载链，而不是硬记忆**：文件自己声明上游和下游。
- **单一权威源**：每条信息只在一个地方定义，其他地方只放摘要和指针。
- **默认遗忘**：低置信号自然消失，高价值信号复现后才上行。
- **身份层需确认**：USER、SOUL、skill 的稳定改动必须经过明确授权。
- **过程与结论分离**：项目主文档放稳定结论，`_progress/` 放推理路径。

## 许可

MIT。见 [LICENSE](./LICENSE)。