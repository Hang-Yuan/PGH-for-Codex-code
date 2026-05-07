---
标题: ITERATION_LOG
类型: 迭代日志
创建日期: 2026-05-07
状态: 活动
上游:
  - .codex/AGENTS.md
下游: []
---

# ITERATION_LOG

架构、协议、技能、文件结构变化写在这里。记忆代谢写入 `MEMORY/MEMORY_LOG.md`。

## 条目模板

```markdown
## vX.Y.Z · YYYY-MM-DD · 标题

### 摘要

### 详情

### 影响

### 同步建议
```

---

## v0.1.1 · 2026-05-07 · 单端化 + 全中文模板

### 摘要

Codex 公共模板改为单端自用结构，并完成中文化。

### 详情

- 删除跨端通信目录。
- 删除额外 agent 占位区。
- README、AGENTS、skills、assistant 骨架统一中文口径。
- 安装占位符只保留 `<ASSISTANT_ROOT>`。

### 影响

使用者只需要 Codex 和本地 assistant 知识库即可运行本模板。

### 同步建议

旧版用户可直接删除跨端通信目录，并替换 `.codex/AGENTS.md` 与 `.codex/skills/`。

## v0.1.0 · 2026-05-07 · 初版 Codex 公共模板

### 摘要

建立 Codex 原生的预测性记忆和项目工作流模板。

### 详情

- 新增 `.codex/AGENTS.md`。
- 新增八个技能：close-node、create-project、daily-review、manage-research-reference、new-file、week-sync、weekly-review、write-progress。
- 新增 assistant 知识库骨架。
- 新增 v5 默认遗忘记忆层。

### 影响

使用者可以基于本模板建立自己的 Codex 长期工作系统。

### 同步建议

安装前替换 `<ASSISTANT_ROOT>`。