# Day 33 — RAG Ingestion Pipeline

## 1. 为什么 ingestion pipeline 很重要

很多人第一次做 RAG，会把注意力全部放在：
- embedding 模型
- 向量数据库
- 检索效果
- prompt 设计

但现实里，RAG 的第一层问题往往不是 retrieval，而是：

> **你的知识到底是怎么进入系统的？**

如果 ingestion 做不好，后面所有环节都会被污染：
- 文档结构丢失
- metadata 缺失
- 脏文本进入索引
- 重复 chunk 太多
- 时间、标题、来源信息丢失

所以 Day 33 的核心不是“再学一个工具”，而是：

> **理解 RAG 的数据入口决定系统上限。**

---

## 2. ingestion pipeline 在做什么

ingestion pipeline 可以理解成：

> 把原始知识源，转成后续 retrieval / generation 可消费的标准化数据结构。

这个流程通常包括：
1. 数据接入
2. 文本提取
3. 清洗与标准化
4. metadata 提取
5. 切块前预处理
6. 写入中间存储或索引前缓存

一句话说：

> ingestion 负责把“外部世界的文档”变成“RAG 系统内部的知识对象”。

---

## 3. 典型输入源有哪些

RAG 的输入远不只是 PDF。

常见输入包括：
- PDF
- HTML 网页
- Markdown 文档
- Wiki 页面
- Word / docx
- 数据库记录
- Notion / Confluence / 飞书文档
- CSV / JSON 结构化记录

不同来源的 ingestion 难点不一样：

### PDF
- 排版复杂
- 可能有页眉页脚污染
- 表格和多栏结构难解析

### HTML
- 导航栏、广告、无关元素很多
- 主体内容提取难

### Markdown / Wiki
- 结构较清晰
- heading 信息很有价值

### 数据库记录
- 字段清晰
- 但跨字段语义要重新组织

---

## 4. 为什么清洗是 ingestion 的核心步骤

很多新手会低估清洗的重要性。

如果清洗不做，常见问题包括：
- chunk 里混入大量重复页脚
- 网页导航文本进入检索
- markdown 噪声符号太多
- OCR 文本断裂
- 多余空格 / 换行导致 embedding 质量下降

清洗的目标不是“文本更好看”，而是：

> **让知识以更可检索、更可阅读、更可引用的形式进入系统。**

---

## 5. metadata 为什么这么重要

很多人一开始只关心正文，但 metadata 在 RAG 里几乎同样关键。

常见 metadata 包括：
- title
- source
- URL
- author
- created_at / updated_at
- section / heading
- page number
- document id
- tags / category

为什么它重要？

### 对 retrieval 有帮助
- 可做 filter
- 可做 rerank 特征
- 可做时间约束

### 对 generation 有帮助
- 可展示 citation
- 可输出来源说明

### 对 evaluation 有帮助
- 可检查答案是否来自正确文档

所以：

> **没有 metadata 的 RAG，通常只能算半成品。**

---

## 6. ingestion pipeline 的输出应该长什么样

理想情况下，ingestion 的输出不应该是“原始文本字符串”，而应该是结构化对象，例如：

```json
{
  "doc_id": "policy-001",
  "title": "RAG System Design",
  "source": "internal_wiki",
  "updated_at": "2026-04-15",
  "content": "...cleaned text...",
  "metadata": {
    "section": "retrieval",
    "url": "https://..."
  }
}
```

这样做的好处是：
- 后续 chunking 更方便
- 索引时 metadata 不会丢
- citation 更容易做
- eval 和 trace 也更清晰

---

## 7. ingestion 和 chunking 的关系

Day 33 和 Day 34 是强相关的。

ingestion 解决的是：
- 文档怎么进入系统
- 怎么清洗
- 怎么保留结构

chunking 解决的是：
- 文档进入系统后，如何切成适合检索的粒度

如果 ingestion 阶段把结构破坏掉了，chunking 阶段就很难补救。

比如：
- heading 丢了
- 段落边界丢了
- 表格被压扁了

那后面 chunk 再怎么切，语义也容易碎。

所以 Day 33 的关键认识是：

> **chunking 效果的上限，受 ingestion 质量强约束。**

---

## 8. ingestion pipeline 的工程视角

在真实系统里，ingestion 不只是一次性脚本，而常常是：
- 可重复运行的 pipeline
- 支持增量更新
- 支持失败重跑
- 支持版本追踪

也就是说，工程上常会关心：
- 新文档如何增量 ingest
- 文档更新后如何重建 chunk
- 文档删除后如何同步删除索引
- ingestion 失败时如何报警 / 重试

所以 ingestion 不是“准备数据的小步骤”，而是：

> **RAG 系统的数据工程骨架。**

---

## 9. 今天最该记住的 5 句话

1. **RAG 的第一层问题不是 retrieval，而是知识如何进入系统。**
2. **ingestion 负责把外部文档转成可检索的结构化对象。**
3. **清洗与 metadata 保留是 ingestion 的核心。**
4. **如果 ingestion 质量差，后面的 chunking 和 retrieval 上限都会下降。**
5. **ingestion pipeline 本质上是 RAG 的数据工程入口。**

---

## 10. 今日任务

### 必做
1. 回看你现有文档样本，列出 3 种不同数据源
2. 写下每种数据源 ingestion 时最可能遇到的噪声问题
3. 设计一个统一的数据对象结构（至少含 content + metadata）
4. 画出 ingestion → chunking → indexing 的前半段数据流

### 你要能回答的问题
1. ingestion pipeline 在 RAG 里到底负责什么？
2. 为什么 metadata 对 RAG 很关键？
3. PDF / HTML / Markdown ingestion 的难点各是什么？
4. ingestion 和 chunking 有什么关系？
5. 为什么 ingestion 是数据工程问题，而不只是预处理问题？

---

## 11. 一句话总结

> RAG ingestion pipeline 的本质，是把外部世界中格式混乱、结构各异的原始文档，转成后续 chunking、indexing、retrieval 和 citation 都能稳定消费的标准化知识对象，它决定了整个系统的数据质量上限。
