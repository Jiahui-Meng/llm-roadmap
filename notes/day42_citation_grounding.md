# Day 42 — Citation Grounding

## 1. 为什么 citation grounding 是 RAG 的关键升级

很多系统会说自己是 RAG，但实际用户体验可能只是：
- 回答看起来像是“基于资料”
- 但用户看不到依据
- 也无法验证答案到底来自哪里

这时系统仍然存在很大问题：

> **它可能只是把资料塞进 prompt，然后生成一段看起来很像真的答案。**

citation grounding 的意义就在于：

> **让答案和证据建立明确、可追踪的连接。**

---

## 2. grounding 到底在解决什么问题

grounding 解决的不是“让答案更长”或者“让模型更会引用”，而是：
- 降低 unsupported claims
- 让用户能验证来源
- 暴露 retrieval 失败
- 提高系统可审计性

也就是说，它把 RAG 从：
- “可能参考了文档”

变成：
- “这句话具体对应哪段证据”

这两者差别非常大。

---

## 3. 为什么 citation 对信任特别重要

在很多场景中，用户真正想要的不是“更像人说的话”，而是：
- 这结论哪来的？
- 这句话是不是有依据？
- 我能不能自己点开看看？

尤其在：
- 医疗
- 法律
- 金融
- 企业知识库

这些高风险场景中，citation 几乎不是可选项，而是必要项。

所以 Day 42 的关键认识是：

> **grounded answer 和 fluent answer 不是一回事。**

---

## 4. citation grounding 如何影响系统设计

一旦你决定做 citation，前面很多模块都要配合：
- chunking 要更注意证据边界
- metadata 要保留来源信息
- retrieval 要尽量返回可引用单元
- prompt assembly 要把引用信息带进去
- generation 要输出 citation marker

这说明 citation grounding 不是后处理小功能，而是：

> **反向塑造整个 RAG pipeline 的设计约束。**

---

## 5. citation grounding 的常见失败方式

### 1）有 citation，但对不上内容
说明引用只是装饰，没真正 grounding。

### 2）citation 太粗
引用的是整篇文档，用户仍然找不到具体证据。

### 3）citation 很碎
一个回答跨很多小 chunk，用户体验差。

### 4）模型有引用，但结论超出证据范围
这是典型 hallucination + fake grounding。

所以不能因为“有 [1][2][3]” 就默认系统真的 grounded 了。

---

## 6. 为什么 citation grounding 和 eval 强相关

citation 做出来以后，你就可以更明确地评估：
- 答案是否被支持
- citation 是否正确对应证据
- 是否有 unsupported claim
- retrieval 是否真的提供了足够证据

也就是说，citation grounding 不仅改善用户体验，也提升系统可测性。

这正是 Day 43–44 eval / ablation 的前置条件之一。

---

## 7. Day 42 的本质：把文档从“背景材料”变成“证据”

这个转变非常关键。

如果没有 grounding：
- 文档只是 prompt 里的背景上下文

有了 grounding：
- 文档变成了证据对象
- 每条回答都可以映射回证据

所以 Day 42 真正代表的是：

> **RAG 从“参考文档式生成”进化到“证据驱动式生成”。**

---

## 8. 今天最该记住的 5 句话

1. **citation grounding 的核心是让答案和证据建立明确连接。**
2. **有 citation 不等于真的 grounded。**
3. **grounding 会反向影响 chunking、metadata、retrieval 和 prompt 设计。**
4. **citation 对高风险场景的信任建立尤其关键。**
5. **grounding 让 RAG 更可验证，也更可评估。**

---

## 9. 今日任务

### 必做
1. 写出 grounded answer 和 fluent answer 的区别
2. 列出 3 种 citation 可能失败的方式
3. 画出 citation grounding 对前面 pipeline 的依赖关系
4. 思考：为什么 citation 对医疗 / 法律系统尤其重要？

### 你要能回答的问题
1. citation grounding 到底在解决什么问题？
2. 为什么 citation 不只是后处理功能？
3. “有 citation”为什么不一定等于真的 grounded？
4. 它为什么和 eval 强相关？
5. Day 42 为什么代表 RAG 设计的一次跃迁？

---

## 10. 一句话总结

> Citation grounding 的本质，是把 RAG 中被检索到的文档从“模型参考过的背景材料”升级为“用户可以验证的明确证据”，从而让系统更可信、更可审计、也更可评估。
