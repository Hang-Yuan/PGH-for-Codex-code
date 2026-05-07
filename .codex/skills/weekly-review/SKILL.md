---
name: weekly-review
description: 周复盘：归档本周、代谢记忆候选、提出身份层毕业候选。
created: 2026-05-07
updated: 2026-05-07
---

# weekly-review

当用户要求周复盘，或到达周复盘时间时调用。

## 流程

1. 判定逻辑周界。
2. 读取：
   - `<ASSISTANT_ROOT>/00 专注区/_本周.md`
   - 相关项目 `_overview.md` 和 `_progress/`
   - `MEMORY/episodic_inbox.md`
   - `MEMORY/episodic_memory.md`
   - `MEMORY/semantic_memory.md`
   - `MEMORY/MEMORY_LOG.md`
3. 按项目和关键认识总结本周。
4. 代谢记忆：
   - 过期弱 L0 清理
   - 重复 L0 合并到 L1
   - 稳定 L1 升到 L2
   - 无用或被击穿的 L2 衰减
   - L3 毕业候选只提出改写草案
5. 需要时归档本周文件并创建下周文件。
6. 记忆变化写 `MEMORY_LOG.md`。
7. 架构或协议变化写 `ITERATION_LOG.md`。

## 毕业规则

记忆高强度不等于自动改 USER、人格层 或 技能。必须提出干净改写稿，等用户确认。

## 不做

- 不把忙碌当作稳定身份证据。
- 不因为最近就保留低价值一次性信号。
- 不绕过项目权威源改写项目结论。