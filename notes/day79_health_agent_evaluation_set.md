# Day 79 — Health Agent Evaluation Set

## 1. 为什么 Health Agent 一定要有专门的 evaluation set

到了 Health Agent 2.0 这一步，系统已经不再是普通 RAG demo 了。

它涉及：
- 多路 retrieval
- 时间线问题
- 医疗实体问题
- 关系推理问题
- grounding / citation

如果你还只靠“随便问几个问题看看”，那几乎不可能判断系统是否真的可用。

所以 Day 79 的核心是：

> **给 Health Agent 建一套真正贴合任务结构的评估集合。**

---

## 2. 为什么 Health Agent 的 eval 比普通 RAG 更难

普通 RAG 可能更多关注：
- 找到相关文档
- 回答是否正确

但 Health Agent 的复杂性更高，因为问题类型差异很大：
- summary
- timeline
- meds
- labs
- relation queries

也就是说，系统不是只在回答“是什么”，而且还在回答：
- 怎么变的
- 它和什么有关
- 哪项指标异常
- 药物和疾病之间有什么关系

这说明 Day 79 的 eval 不能只是通用问答集合，而必须反映：

> **医疗场景中的任务结构差异。**

---

## 3. evaluation set 至少要覆盖哪些 query 类型

一个最小有意义的 Health Agent eval set，至少应覆盖：

### 1）Summary
例如：
- 总结最近一次就诊
- 总结近期病情变化

### 2）Timeline
例如：
- HbA1c 过去一年如何变化
- 哪些症状是最近新增的

### 3）Medications
例如：
- 当前药物有哪些
- 哪次就诊开始调整药物

### 4）Labs
例如：
- 最近异常指标有哪些
- 哪些实验室值持续恶化

### 5）Relations
例如：
- 某药物对应什么疾病
- 某指标变化是否与药物调整相关

这些 query 类型正好对应前面设计的多路 retrieval。

---

## 4. 为什么 query type 标注很重要

在 Health Agent 里，题目不只是“一个问题”，它还属于某一类任务。

如果没有 query type 标注，你就很难分析：
- 系统到底在哪类问题上弱
- dense retrieval 是否只擅长 summary 类问题
- timeline retrieval 是否真的对时间类问题有帮助
- graph retrieval 是否真的改善 relation 类问题

所以 query type 标注的意义是：

> **让 evaluation 不只是给总分，而是能按能力维度拆开看。**

---

## 5. 为什么 Health Agent eval 特别需要 reference evidence

在医疗场景中，仅仅有 reference answer 还不够。

更有价值的是：
- reference answer
- supporting evidence
- source visit / document / date

原因很简单：
- 答案也许看起来对
- 但如果依据错了，系统仍然不可信

所以 Day 79 的 eval set 理想情况下最好包含：
- question
- query_type
- reference_answer
- supporting_evidence
- preferred_retrieval_path（可选）

这样才能更好地评估 grounding。

---

## 6. Day 79 和 Day 77 / Day 80 的关系

Day 79 不是孤立的一天。

### Day 77
你设计了多路 retrieval

### Day 79
你用 evaluation set 检验这些设计是否真的有用

### Day 80
你进一步建立 observability，看系统在线行为

所以 Day 79 是连接“设计假设”和“可验证结果”的关键节点。

---

## 7. 为什么 Health Agent 的 eval set 同时也是安全护栏

医疗场景里，eval set 不只是为了提升分数，更是为了降低风险。

因为它可以帮助你提早发现：
- 哪类问题经常答错
- 哪些场景 citation 不稳
- 哪些 retrieval path 容易失效
- 哪些 query 需要更保守处理

所以评估集不仅是优化工具，也是：

> **系统边界识别工具。**

---

## 8. 今天最该记住的 5 句话

1. **Health Agent 必须有贴合医疗任务结构的专门评估集。**
2. **summary、timeline、meds、labs、relations 至少都应覆盖。**
3. **query type 标注能让你按能力维度分析系统强弱。**
4. **医疗 eval 特别需要 reference evidence，而不只是 reference answer。**
5. **Day 79 的 eval set 同时是优化工具和安全护栏。**

---

## 9. 今日任务

### 必做
1. 为 5 类 query type 各写若干示例题
2. 给每题补 reference answer
3. 尽量补 supporting evidence / date / source
4. 写一句：为什么 Health Agent eval 比普通 RAG eval 更难

### 你要能回答的问题
1. 为什么 Health Agent 一定要有专门 eval set？
2. 至少要覆盖哪些 query 类型？
3. query type 标注为什么重要？
4. 为什么医疗 eval 更强调 supporting evidence？
5. Day 79 为什么是系统安全护栏的一部分？

---

## 10. 一句话总结

> Health Agent Evaluation Set 的本质，是围绕医疗场景中最核心的总结、时间线、药物、化验和关系查询构建一套带有答案和证据基准的测试集合，用来验证系统能力、发现风险边界并指导后续优化。
