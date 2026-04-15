# Day 38 — RAG Prototype v1 README and Failure Cases

## 1. 为什么 README 和 failure cases 也是工程产出

很多人做项目时有个习惯：
- 只关心代码能不能跑
- 不关心 README
- 不记录失败案例

但真实工程里，一个没有文档、没有失败记录的项目，很快就会变成：
- 未来的你都看不懂
- 别人无法复现
- 问题无法系统优化

所以 Day 38 的重点不是“写文档”这么简单，而是：

> **把 RAG v1 从个人实验，变成可解释、可复现、可迭代的项目。**

---

## 2. README 真正在做什么

好的 README 不是摆设，而是在回答这些问题：
- 这个项目做什么？
- 为什么要做？
- 系统结构是什么？
- 怎么运行？
- 输入输出是什么？
- 已知限制是什么？

如果没有 README，项目对外几乎就是不可读的。

所以 Day 38 的关键认识是：

> **README 是系统设计的文字界面。**

---

## 3. failure cases 为什么必须记录

RAG 系统天然容易失败，因为它不是一个模型，而是一串模块：
- ingestion 可能脏
- chunking 可能切坏
- embedding 可能不对齐
- retrieval 可能召回错
- prompt assembly 可能压坏上下文
- generation 可能幻觉

如果你不记录失败案例，你就只能模糊地说：
- “效果一般”
- “有时候不太对”

这对工程优化几乎没有帮助。

failure case 的作用是：

> **把模糊失败，变成可定位、可分析、可改进的问题。**

---

## 4. 什么样的 failure case 值得记录

至少值得记录这几类：

### 1）检索失败
用户问得对，但 top-k 没召回到相关 chunk。

### 2）检索对了，回答还错
说明 generation / prompt grounding 可能有问题。

### 3）citation 不清楚
说明 chunking / metadata / prompt 可能有问题。

### 4）上下文太长或重复太多
说明 chunking / top-k 策略有问题。

这些失败案例会变成后续 v2 升级的直接线索。

---

## 5. README 和 failure cases 的关系

README 讲的是：
- 系统理想上应该怎么工作

failure cases 讲的是：
- 系统现实中是怎么失败的

这两个东西放在一起，项目才真实。

也就是说：
- README 提供结构化说明
- failure cases 提供边界与问题空间

这是从“demo”走向“工程项目”的标志。

---

## 6. Day 38 为什么是 v1 的收口日

Day 37 把系统跑起来。

Day 38 要做的是把它收口：
- 文档化
- 失败显式化
- 为 v2 铺路

如果 Day 37 是“把机器装起来”，
那 Day 38 就是：

> **给机器贴上说明书，并标出它现在最容易坏的地方。**

---

## 7. 今天最该记住的 5 句话

1. **README 不是装饰，而是项目的文字界面。**
2. **failure cases 是系统优化的起点。**
3. **不记录失败，就无法系统改进 RAG。**
4. **README 讲理想工作流，failure cases 讲真实边界。**
5. **Day 38 是把 v1 从实验收口成项目的关键一步。**

---

## 8. 今日任务

### 必做
1. 写 README：目标、结构、运行方式、限制
2. 至少记录 3 个 failure cases
3. 每个 failure case 写出可能原因
4. 写出这些 failure 如何引出 v2 的改进方向

### 你要能回答的问题
1. 为什么 README 也是工程产出？
2. failure case 为什么比“效果一般”更有价值？
3. 哪几类失败最值得记录？
4. README 和 failure case 分别解决什么问题？
5. 为什么 Day 38 是 v1 的收口日？

---

## 9. 一句话总结

> RAG Prototype v1 的 README 和 failure cases，不是附属文档，而是把一个能跑的原型系统转化成可复现、可诊断、可迭代工程项目的关键组成部分。
