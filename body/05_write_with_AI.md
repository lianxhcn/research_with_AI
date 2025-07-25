# 使用 AI 撰写论文推介

对于初学者而言，精读 Top Journal 的论文，并参考作者提供的数据和代码进行复现是一个非常有效的学习方法。在此过程中，我们可以使用 VScode + Jupyter Notebook 来记录复现过程。虽然 AI 可以大幅提高复现和写作效率，但需要调教有方 (给出清晰的提示词)。

::: {.callout-note}
## 基本步骤

1. **选择 AI 工具**：可以使用 ChatGPT、DeepSeek、豆包等工具。也可以同时使用多个工具，互为补充。
2. **上传论文 PDF 和相关资料**：将论文 PDF 文件贴入 AI 助手对话框。如果你已经写了一些读书笔记，或搜索到了与论文相关的博文、Slides，评论等，也可以一并发给 AI。
3. **撰写提示词**：根据目标读者和内容要求，撰写清晰的提示词，指导 AI 工具生成内容。
4. **生成内容**：使用 AI 工具生成论文推介内容。
5. **编辑和润色**：对 AI 生成的内容进行编辑和润色，确保符合中文表述习惯和格式要求。
:::

## 撰写提示词的建议

**A. 先泛聊**。先使用比较开放的提示词，看看 AI 能否抓住这篇论文的要点，比如，`请简要介绍论文的核心观点`；`论文的主要贡献是什么`；`简要说明文中理论模型的设定思路`；`该文的适用场景是什么？`等；。也可以针对论文中比较棘手的部分进行提问，比如假设的含义、数学公式的解释等。

**B. 再形成提纲**。待上述讨论完成后，先不要急着输出推文内容，而是让 AI 工具先给出一个提纲。然后根据提纲讨论完善后，再进行详细撰写。

- **推文的目的**，比如帮助读者快速了解论文的核心内容，或者提供对某个研究问题的深入分析；
- **读者群体**，比如经济学、计量经济学领域的博士生和青年教师/高年级本科生；
- **风格要求**：比如中文推文风格 (参考 <https://www.lianxh.cn> 的风格)；中文讲义风格 (语言朴实、用语准确) 等。
- **优化提纲**。可以用 `再来一个版本`；或 `再来一个着重介绍 {论文思路/实证方法/因果识别策略} 的版本` 等提示词，来让 AI 工具生成不同风格的内容。你也可以就某个 Section 提出具体要求，细化这个 Section 的提纲。

**C. 分 Section 输出**。对于 2000 字以上的内容，建议分多次输出。每次输出一个 Section，酌情修改和提出新的要求。符合要求后，再让 AI 按照这个风格继续输出后续内容。

- Tip 1：正式输出前，可以使用提示词 `Prompt: 请为每个输出添加 label，方便我后续整理`。这样 AI 工具会在每个 Section 前添加一个 label，比如 `#Sec-1`，`#Sec-2` 等，方便后续修改时引用。
- Tip 2：可以使用提示词 `Prompt: 请酌情标注需要插入原文图表的地方，并给出图形建议`。随后，你可以使用 SniPaste 等软件从原文中截图后插入推文。
- Tip 3：可以要求 AI 使用 `$$` 符号包裹数学公式，方便后续在 Markdown 中渲染；并使用提示词 `请勿添加任何表情符号`，避免 AI 在输出中添加表情符号。


输出文档的提示词有如下几个要点：

1. **写作目的**：说明你希望通过这篇论文推介达到什么目的，比如帮助读者快速了解论文的核心内容，或者提供对某个研究问题的深入分析。
2. **读者群体**：明确你的目标读者是谁，比如经济学、计量经济学领域的研究人员和学生。
3. **格式要求**：说明你希望输出的文档格式，比如需要包含标题、摘要、引言、方法、结果、讨论等部分。
4. **内容要求**：列出你希望 AI 工具覆盖的主要内容，比如论文的主要内容、研究方法、数据来源和主要结论等。
5. **篇幅要求**：如果有特定的篇幅要求，可以在提示词中说明，比如希望生成一篇 5000 字以上的论文推介。你甚至可以要求每个 Section 的字数范围。如果推文中包含图表、公式或代码，可以限定中文字符的字数范围。
6. **分多次输出**。对于 2000 字以上的内容，建议分多次输出。每次输出一个 Section，酌情修改和提出新的要求。符合要求后，再让 AI 按照这个风格继续输出后续内容。 


提示词，说明你的写作目的、读者群体和格式要求等

::: {.callout-tip}
## 提示词：论文推介

我想写一篇论文推介，介绍我传给你的 PDF 论文。具体要求如下：

1. 目标读者：经济学、计量经济学领域的研究人员和学生。
   - 希望能够让他们快速了解这篇论文的核心内容和贡献。  
   - 对于一些复杂的数学公式，可以用比较通俗的语言进行解释。
   - 必要时，可以提供 1-2 个简化版的例子加以说明。
2. 需要介绍论文的主要内容、研究方法、数据来源和主要结论。   
   如果需要插入原文中的图形或表格，请告知我图表编号和插入位置，我会手动添加。
3. 需要包含关键公式和代码的解读。
4. 需要提供参考文献列表。

你先帮我列一个提纲，我们讨论完善后再进行详细撰写。

- 以 Section 为单位输出。

:::

## 实例 1：Wing et al. (2024) 论文推介

Wing, C., Yozwiak, M., Hollingsworth, A., Freedman, S., & Simon, K. (2024). Designing Difference-in-Difference Studies with Staggered Treatment Adoption: Key Concepts and Practical Guidelines. **Annual Review of Public Health**, 45(1), 485–505. [Link](https://doi.org/10.1146/annurev-publhealth-061022-050825), [PDF](https://www.annualreviews.org/docserver/fulltext/publhealth/45/1/annurev-publhealth-061022-050825.pdf?expires=1752678753&id=id&accname=guest&checksum=345B1C3C23D23EC0D6A9B385A91F2513), [Google](<https://scholar.google.com/scholar?q=Designing Difference-in-Difference Studies with Staggered Treatment Adoption: Key Concepts and Practical Guidelines>), [github-replication](https://github.com/hollina/arph-did-example)

这篇论文介绍了五种常用的渐进 DID 的估计方法，作者还在 GitHub 上提供了相关的代码和数据。我采用上文介绍的提示词方法与豆包聊了 20 分钟，最终形成了推文的初稿 (满意度：80%)。

> [豆包对话过程](https://www.doubao.com/thread/w8e524bfc59a644e2))

::: {.callout-tip}
### 提示词 1：概要

# 论文解读：

> Wing, C., Yozwiak, M., Hollingsworth, A., Freedman, S., & Simon, K. (2024). Designing Difference-in-Difference Studies with Staggered Treatment Adoption: Key Concepts and Practical Guidelines. Annual Review of Public Health, 45(1), 485–505. [Link](https://doi.org/10.1146/annurev-publhealth-061022-050825), [PDF](https://www.annualreviews.org/docserver/fulltext/publhealth/45/1/annurev-publhealth-061022-050825.pdf?expires=1752678753&id=id&accname=guest&checksum=345B1C3C23D23EC0D6A9B385A91F2513), [Google](<https://scholar.google.com/scholar?q=Designing Difference-in-Difference Studies with Staggered Treatment Adoption: Key Concepts and Practical Guidelines>).

我想写一篇论文推介，介绍这篇论文。你帮我列个提纲。

包括如下要点：

1. 论文的核心观点和主要结论是什么？
2. 文中介绍了哪些主要方法 (参见 Table 1)？
3. 作者提供了哪些实操建议？参见 Section 5

:::




## 实例 2：FutureHouse.org 平台简介 

> [ChatGPT 对话过程](https://chatgpt.com/share/687d0bfa-d780-8005-a430-6c73ab075087)

[FutureHouse.org](https://futurehouse.org) 平台提供了很多 AI 工具和资源，帮助用户更高效地使用 AI 技术。我浏览了该平台的主页和 Github 仓库后，将我记录的笔记提供给了 ChatGPT，并与它进行了一些讨论。最终，我让它帮我输出了一篇 5000 字的推文。 


## 实例 3：概率匹配与 Kelly 策略-Python 代码

[ChatGPT 对话过程](https://chatgpt.com/c/684a20e7-19cc-8005-b1ca-8eb20d29afed)

我看到了一篇很有意思的 Blog：[Probability matching and Kelly betting](https://reasonabledeviations.com/2022/01/10/probability-matching-kelly/)。作者介绍了概率匹配和 Kelly 策略的故事，提醒我们现实决策和自然演化中的“理性”，远不是单一的最大化期望值。更广义的理性关注风险、分布、长期增长以及群体的生存。

里面有很多我不太理解的新概念，作者并未给出详细的解释。同时，我还想了解如何用 Python 代码实现这些概念。于是我将这篇 Blog 的内容和我的问题提供给了 ChatGPT，并与它进行了讨论。最终，我让它帮我输出了一篇 5000 字的推文 ([初稿](https://github.com/arlionn/lianxhta/blob/main/sample/B817-Probability-Matching-and-Kelly-Criterion.md))。


## 其它借助 AI 完成的推文

- 连小白, 2025, [自动化因果推断助手：Causal-Copilot 简介](https://www.lianxh.cn/details/1643.html), 连享会 No.1643. ([ChatGPT 对话](https://chatgpt.com/share/686c70ed-70d0-8005-bf02-972e9b2b11e8))
