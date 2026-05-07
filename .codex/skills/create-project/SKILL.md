---
name: create-project
description: 新建持续项目：建立项目容器、overview、加载链和推进区。
created: 2026-05-07
updated: 2026-05-07
---

# create-project

当一条新工作会持续推进、需要长期记录时调用。

## 输入确认

先确认：

- 项目名称
- 项目类型：研究 / 工程 / 写作 / 事务 / 其他
- 是否允许写入 `<ASSISTANT_ROOT>/01 项目区/`

## 目录结构

```text
<ASSISTANT_ROOT>/01 项目区/<项目名>/
├── _overview.md
├── _progress/
└── _reference/        # 需要文献时再建
```

## `_overview.md` 最小骨架

```markdown
---
标题: <项目名>
类型: 项目总览
创建日期: YYYY-MM-DD
状态: 进行中
上游:
  - ../00.项目区_agent.md
下游:
  - _progress/
---

# <项目名>

## 项目定义

## 当前状态

## 加载链

## 推进索引

## 待解问题
```

## 流程

1. 建项目文件夹和 `_progress/`。
2. 写 `_overview.md`，明确上游和下游。
3. 若项目需要文献，调用 `manage-research-reference`。
4. 若项目区有总索引，把项目加入索引。
5. 得到用户授权时，把第一条任务写入 `00 专注区/_本周.md`。

## 不做

- 不为一次性问答新建项目。
- 不编造项目结论。
- 不把项目设置写成 USER 或 人格层 事实。