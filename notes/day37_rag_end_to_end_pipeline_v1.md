# Day 37 — RAG End-to-End Pipeline v1

## 1. 为什么要做 end-to-end pipeline v1

前几天你分别学了：
- ingestion
- chunking
- embedding
- index construction

如果只停留在模块理解阶段，你会有一种错觉：

> “我都懂了，RAG 应该已经会了。”

但真正的工程学习必须跨过一个门槛：

> **把分散模块真的连成一条能跑通的最小系统。**

这就是 Day 37 的意义。

v1 的目标不是最强，而是：
- 跑得通
- 逻辑完整
- 能回答简单问题
- 为后续优化提供底座

---

## 2. v1 的最小系统包含什么

一个最小可运行 RAG pipeline 通常包括：

```text
raw docs
-> ingest
-> chunk
-> embed
-> build index
-> retrieve top-k
-> assemble prompt
-> generate answer
```

Day 37 你最该形成的是系统感：

> **之前学的每个模块，现在终于开始首尾相接。**

---

## 3. 为什么 v1 不追求复杂特性

刚做 v1 时，很多人会很想一口气加：
- reranker
- query rewrite
- citation grounding
- eval
- hybrid retrieval

但如果基础流水线还没真正跑顺，这些复杂模块只会让问题更难定位。

所以 v1 的策略应该是：

> **先跑通，再增强。**

这是非常重要的工程习惯。

---

## 4. v1 最关键的成功标准是什么

不是“答案特别聪明”，而是：

1. 文档能 ingest 进来
2. chunk 能生成
3. embedding 能计算
4. index 能建立
5. query 能检索出合理 top-k
6. prompt 能组装
7. 模型能基于上下文生成答案

如果这 7 步都能稳定跑通，你的 v1 就成功了。

---

## 5. 为什么 Day 37 是 RAG 学习的真正分界线

在 Day 37 之前，你学的是：
- RAG 的零件

在 Day 37 之后，你开始学的是：
- RAG 作为系统如何优化

这两者完全不是一个层级。

所以 Day 37 是从：

> **概念型学习 → 系统型学习**

的分界点。

---

## 6. v1 最常见的失败点

### 1）检索结果看起来不相关
通常可能是：
- chunking 有问题
- embedding 选择不合适
- 数据清洗不到位

### 2）答案不 grounded
可能是：
- prompt 没明确要求基于上下文回答
- top-k 检索质量不够

### 3）上下文太长
可能是：
- chunk 太大
- top-k 太多

### 4）系统能跑，但不好 debug
说明日志和中间结果没保存好。

所以 v1 不只是一个 demo，它也是你发现真实瓶颈的第一面镜子。

---

## 7. v1 为什么要保留中间结果

真实工程里，RAG 最怕“黑盒”。

如果用户问：
- 为什么答案错了？
- 为什么没检索到对的文档？
- 为什么上下文里出现了奇怪内容？

你必须能回溯：
- 读入了哪些文档
- chunk 是怎么切的
- top-k 是什么
- 最终 prompt 是什么

这就是为什么 v1 也最好保留：
- retrieval results
- prompt snapshot
- answer output

---

## 8. v1 和 v2 的关系

你可以把 Day 37 的 v1 理解成：
- “能跑的骨架系统”

而 Day 39–45 的内容会把它逐步升级成：
- hybrid retrieval
- reranking
- query rewrite
- citation grounding
- evaluation

所以 v1 不要嫌它“简陋”，因为：

> **没有 v1，就没有有节制的 v2。**

---

## 9. 今天最该记住的 5 句话

1. **Day 37 的目标不是最强 RAG，而是最小可运行 RAG。**
2. **v1 的价值在于把分散模块真正串起来。**
3. **先跑通，再增强，是 RAG 工程的正确节奏。**
4. **v1 需要保留中间结果，方便 debug。**
5. **v1 是后续所有 retrieval 优化和 eval 的基础。**

---

## 10. 今日任务

### 必做
1. 画出端到端 RAG v1 流程图
2. 写出每一步的输入和输出对象
3. 手动检查至少一轮 top-k retrieval 结果
4. 保存一份最终 prompt 示例

### 你要能回答的问题
1. v1 为什么不追求复杂特性？
2. RAG v1 的最小组成模块有哪些？
3. 为什么保留中间结果很重要？
4. v1 最常见失败点有哪些？
5. 为什么 Day 37 是概念学习到系统学习的分界点？

---

## 11. 一句话总结

> RAG end-to-end pipeline v1 的意义，不在于一开始就做到最好，而在于第一次把 ingestion、chunking、embedding、index、retrieval 和 generation 真正连成一个可运行、可调试、可继续进化的系统骨架。
