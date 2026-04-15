# Day 78 — Evidence Panel Design

## 1. 为什么 Health Agent 必须有 evidence panel

如果你在医疗场景里只给用户一个答案，而没有任何证据界面，那么即使答案语言很流畅，系统仍然会显得非常不可信。

因为用户真正需要知道的是：
- 这句话根据哪条记录得出？
- 来自哪次就诊？
- 对应哪份化验单？
- 这结论是不是系统自己猜的？

所以 Day 78 的重点不是 UI 漂不漂亮，而是：

> **如何把答案背后的证据暴露给用户。**

---

## 2. evidence panel 在解决什么问题

evidence panel 的作用包括：
- 提供可验证来源
- 展示引用片段
- 暴露证据不足处
- 帮助用户建立信任
- 帮助系统调试错误

也就是说，它不仅是用户体验组件，更是：

> **grounding 的可视化载体。**

---

## 3. 为什么 evidence panel 对医疗场景尤其关键

医疗场景和普通问答最大的不同之一是：
- 错误成本高
- 用户对结论验证需求更强
- 时间线和来源上下文非常重要

一个“答案看起来像对的”系统是不够的。

用户需要：
- 来源
- 原文片段
- 时间信息
- 文档类型

所以在 Health Agent 里，evidence panel 几乎是系统可信度的一部分，而不是装饰。

---

## 4. evidence panel 应该展示什么

一个最小可用 evidence panel 至少应该展示：
- 引用片段本身
- 文档来源
- 日期 / 时间
- retrieval path（dense / graph / timeline）
- 与回答的对应关系

这很重要，因为“只给一个链接”通常还不够。

你真正想做的是：

> **让用户不需要重新搜索，就能看见答案所依据的证据。**

---

## 5. evidence panel 为什么也有工程价值

它不只是服务用户，也服务开发者。

因为一旦回答出错，evidence panel 能帮助你判断：
- retrieval 找错了？
- citation 对错了？
- 模型超出了证据范围？
- 哪一类 retrieval path 更可靠？

所以 evidence panel 也是一种 debug interface。

这说明它同时连接了：
- 用户信任
- 系统可解释性
- 工程调试能力

---

## 6. 为什么 Day 78 是“grounding 走向产品形态”的一天

前面你已经学过 citation grounding。

但 citation grounding 还只是系统内部能力。

Day 78 的重点是把它变成：
- 用户能看见
- 用户能理解
- 用户能利用的产品界面能力

也就是说，这一天是在完成一次转换：

> **从内部 grounding 机制，走向外部 evidence experience。**

---

## 7. 今天最该记住的 5 句话

1. **Health Agent 没有 evidence panel，就很难真正可信。**
2. **evidence panel 是 grounding 的可视化载体。**
3. **在医疗场景里，来源、时间和原文片段都很关键。**
4. **evidence panel 既服务用户信任，也服务工程调试。**
5. **Day 78 标志着 grounding 开始进入产品形态。**

---

## 8. 今日任务

### 必做
1. 设计 evidence panel 至少应展示的 5 个字段
2. 画一个最小 evidence UI 草图
3. 写出 panel 如何帮助定位 retrieval / generation 问题
4. 写一句：为什么医疗系统特别需要 evidence panel

### 你要能回答的问题
1. 为什么 Health Agent 必须有 evidence panel？
2. evidence panel 到底在解决什么问题？
3. 它为什么对医疗场景尤其关键？
4. evidence panel 至少该展示什么？
5. Day 78 为什么是 grounding 走向产品形态？

---

## 9. 一句话总结

> Evidence Panel Design 的本质，是把 Health Agent 的 citation grounding 能力转化为用户可见、可验证、可调试的证据界面，从而让系统不仅会回答，而且能清楚展示“为什么这样回答”。 
