# Day 43 — RAG Evaluation Set

## 1. 为什么 RAG 一定要有 evaluation set

很多人做 RAG 时，会靠几次手测来判断效果：
- 随便问几个问题
- 感觉还行
- 就继续往前做

但这种方式有一个大问题：

> **你永远不知道系统是真的变好了，还是只是碰巧答对了。**

这就是为什么 Day 43 要开始构建 evaluation set。

没有 evaluation set，RAG 优化基本上就等于：
- 拍脑袋
- 看感觉
- 随缘比较

这在工程上是非常危险的。

---

## 2. evaluation set 在 RAG 里扮演什么角色

evaluation set 的作用不是“考试”，而是：

> **提供一个稳定、可重复、可比较的测试基线。**

它能帮助你回答：
- 改了 chunking 之后，系统真的更好了吗？
- 换 embedding 后，召回提高了吗？
- 加 reranker 值不值？
- citation grounding 真的更准了吗？

也就是说，eval set 让 RAG 优化从主观经验变成相对客观的比较过程。

---

## 3. 一个好的 RAG evaluation set 应该覆盖什么

好的 eval set 不应该只有一种问题。

至少应该覆盖：
- 直接事实问答
- 需要跨段整合的问题
- 需要时间信息的问题
- 需要关系信息的问题
- 容易混淆的近似问题

还应该覆盖不同难度：
- 简单命中题
- 中等推理题
- 高噪声/高混淆题

这样 eval set 才能真实反映系统边界。

---

## 4. 为什么 RAG eval 比普通 NLP eval 更难

因为 RAG 不是单模型单输出问题。

它至少包含两层：
- retrieval 对不对
- generation 对不对

有时 retrieval 是错的，导致 answer 错。
有时 retrieval 是对的，但 generation 还是错。

这意味着 eval set 不只是看“答案像不像”，还要帮助你定位：
- 问题出在 retrieval 还是 generation

所以 RAG eval 的复杂度天然更高。

---

## 5. eval set 不只是问题列表，还要有 reference

一个好的 eval set 通常至少要包含：
- question
- reference answer
- reference evidence / supporting chunks（如果可能）
- category / query type
- difficulty（可选）

为什么 reference evidence 很重要？

因为这样你不只是在评估“答得像不像”，而是在评估：
- 是否基于正确证据回答
- citation 是否真的对上

---

## 6. evaluation set 和 Day 44 / Day 45 的关系

Day 43 的 eval set 是后面两天的基石。

### Day 44
你会做 ablation

### Day 45
你会打包 RAG v2

如果没有 eval set：
- ablation 无法成立
- v2 的“提升”也无法被证明

所以 Day 43 并不是准备杂活，而是：

> **给后面所有系统优化提供统一测量尺。**

---

## 7. eval set 的工程价值

一个长期维护的 RAG 系统，最怕 regression。

比如：
- 改了 chunking 后，有些题变差了
- 换 embedding 后，某类 query 崩了
- reranker 引入后 latency 上升但收益不明显

如果你有 eval set，就能较早发现这些问题。

这说明 eval set 不只是实验室工具，而是：

> **持续迭代系统的防回退护栏。**

---

## 8. 今天最该记住的 5 句话

1. **没有 evaluation set，RAG 优化就容易沦为拍脑袋。**
2. **eval set 的价值是提供稳定、可重复的比较基线。**
3. **好的 eval set 应覆盖多种 query 类型和难度。**
4. **RAG eval 不只看答案，还要帮助定位 retrieval 与 generation 的问题。**
5. **eval set 是后续 ablation 和系统迭代的基础。**

---

## 9. 今日任务

### 必做
1. 设计至少 5 类 query 类型
2. 为每类 query 写 3–5 个示例题
3. 给每题补 reference answer
4. 如果可以，补一列 reference evidence / source

### 你要能回答的问题
1. 为什么 RAG 一定要有 eval set？
2. 好的 eval set 应覆盖哪些维度？
3. 为什么 RAG eval 比普通问答 eval 更难？
4. reference evidence 为什么有价值？
5. eval set 为什么是系统防回退护栏？

---

## 10. 一句话总结

> RAG evaluation set 的本质，是为系统提供一把稳定、可重复、可分解问题来源的测量尺，让你能真正比较不同 retrieval / generation 方案是否带来了可靠提升。
