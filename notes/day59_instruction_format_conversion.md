# Day 59 — Instruction Format Conversion

## 1. 为什么 Day 59 很关键

到了这一步，你已经有了原始数据。

但原始数据并不能直接用于 instruction tuning。

因为模型训练需要的不是“原始记录”，而是：

> **一组清晰定义输入、任务指令和目标输出的训练样本。**

这就是 Day 59 的工作：
- 把原始数据转换成 instruction / input / output 结构
- 让模型清楚知道：你想让我做什么，以及正确答案应该长什么样

所以 Day 59 的本质不是格式整理，而是：

> **把任务定义显式编码进训练数据。**

---

## 2. instruction format 在解决什么问题

instruction tuning 和普通语言建模最大的不同是：

### 普通语言建模
- 主要预测下一个 token

### instruction tuning
- 学的是“在一个明确任务描述下如何输出合适结果”

所以如果格式不好，模型就会学得模糊：
- 到底任务是什么？
- 输入和输出边界在哪里？
- 结果需要什么风格？

这说明 instruction format 不是语法包装，而是：

> **训练目标的显式界面。**

---

## 3. 常见 instruction 格式长什么样

最常见的形式通常是：

```json
{
  "instruction": "...",
  "input": "...",
  "output": "..."
}
```

其中：
- `instruction`：任务说明
- `input`：待处理内容（可为空）
- `output`：目标答案

看起来简单，但真正难点是：
- instruction 写得够不够清楚
- output 风格是否一致
- 数据整体格式是否统一

---

## 4. 为什么 instruction 写法会直接影响训练效果

instruction 不只是“说一句任务名字”。

它实际上在规定：
- 模型应完成什么动作
- 输出要满足什么约束
- 输出风格要不要固定

举例：
- “总结这段内容”
- “从这段文本中抽取技能并用 JSON 返回”

这两种 instruction 对训练结果影响会非常不一样。

所以 Day 59 要特别意识到：

> **instruction 本身就是训练信号的一部分。**

---

## 5. 为什么 output consistency 很重要

如果 output 风格很不稳定，比如：
- 有时是列表
- 有时是长段落
- 有时是 JSON
- 有时中英混杂

模型就很难学到稳定模式。

尤其在 LoRA 小规模微调里，output consistency 比很多人想象中更重要。

因为小数据训练对噪声更敏感。

所以 Day 59 的关键工作之一其实是：

> **让目标输出尽可能风格一致、边界清晰。**

---

## 6. instruction format conversion 为什么不只是技术活

有些人会把这一步当成纯粹脚本转换。

但其实它本质上在回答：
- 我希望模型学会什么行为？
- 我希望它以什么格式回答？
- 我希望它在面对类似输入时形成什么模式？

这说明 Day 59 同时也是一次：

> **任务建模工作。**

不是只改字段名，而是在塑造训练语义。

---

## 7. Day 59 和 Day 60 的关系

Day 60 就要真正开始训练。

如果 Day 59 的格式有问题，Day 60 即使跑起来，也会出现：
- loss 看着正常，但输出风格很乱
- 模型学不到你真正想要的行为
- before/after 差异很难解释

所以 instruction format conversion 是训练前最后一个高杠杆环节。

---

## 8. 今天最该记住的 5 句话

1. **instruction format 不是包装，而是训练目标的显式界面。**
2. **instruction 写法本身会直接影响模型学到什么行为。**
3. **output consistency 对小规模 LoRA 微调尤其关键。**
4. **Day 59 不只是脚本转换，也是任务建模。**
5. **这一步质量会直接决定 Day 60 训练结果是否可解释。**

---

## 9. 今日任务

### 必做
1. 设计一套统一 instruction/input/output 模板
2. 随机抽查 20 条转换后的样本
3. 检查 output 风格是否一致
4. 写出你的 instruction 想显式教给模型什么行为

### 你要能回答的问题
1. 为什么原始数据不能直接拿去做 instruction tuning？
2. instruction format 到底在编码什么？
3. 为什么 instruction 写法会影响训练效果？
4. output consistency 为什么重要？
5. Day 59 和 Day 60 的关系是什么？

---

## 10. 一句话总结

> Instruction format conversion 的本质，是把原始数据重新组织成“任务说明 + 输入 + 目标输出”的训练接口，让模型不仅看到数据内容，也明确学习到你希望它执行的具体行为模式。
