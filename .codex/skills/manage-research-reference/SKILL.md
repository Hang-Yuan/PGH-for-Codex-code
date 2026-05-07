---
name: manage-research-reference
description: 科研或资料密集项目的文献记录管理。
created: 2026-05-07
updated: 2026-05-07
---

# manage-research-reference

当项目首次需要文献记录，或需要追加参考资料时调用。

## 目录结构

```text
<项目>/_reference/
└── 文献记录.md
```

## 文献条目模板

```markdown
## YYYY-MM-DD · 文献短标题

- 引用：
- 链接 / DOI：
- 类型：
- 状态：未读 / 略读 / 已读 / 已使用
- 相关性：
- 关键主张：
- 备注：
```

## 流程

1. 确认项目和 `_reference/` 是否存在。
2. 缺失时创建 `_reference/文献记录.md`。
3. 按结构化字段追加文献。
4. 项目正文只保留简短引用，例如 `(Author, Year)`；细节放在文献记录。
5. 若 `_reference/` 成为项目加载链的一部分，更新 `_overview.md`。

## 不做

- 不编造作者、年份、DOI 或链接。
- 当前事实或高风险主张必须查一手来源。
- 不把长篇读书笔记塞进项目主文档。