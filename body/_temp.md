

### 博文解读：概率匹配与 Kelly 策略-Python 代码

> [ChatGPT 对话过程](https://chatgpt.com/c/684a20e7-19cc-8005-b1ca-8eb20d29afed)

我看到了一篇很有意思的 Blog：[Probability matching and Kelly betting](https://reasonabledeviations.com/2022/01/10/probability-matching-kelly/)。作者介绍了概率匹配和 Kelly 策略的故事，提醒我们现实决策和自然演化中的“理性”，远不是单一的最大化期望值。更广义的理性关注风险、分布、长期增长以及群体的生存。

里面有很多我不太理解的新概念，作者并未给出详细的解释。同时，我还想了解如何用 Python 代码实现这些概念。于是我将这篇 Blog 的内容和我的问题提供给了 ChatGPT，并与它进行了讨论。最终，我让它帮我输出了一篇 5000 字的推文 ([初稿](https://github.com/arlionn/lianxhta/blob/main/sample/B817-Probability-Matching-and-Kelly-Criterion.md))。

::: {.callout-tip}
### 提示词

> **Prompt** 1:   

帮我解读一些这篇文章的核心观点：
https://reasonabledeviations.com/2022/01/10/probability-matching-kelly/

> **Prompt** 2:  

这个在研究中有何用？在哪些领域，这里提到的概念很重要？

> **Prompt** 3:  

详细介绍一下 Kelly 策略

> **Prompt** 4:  

目的：python 实现代码

帮我设计一组 Python 代码，以便与 https://reasonabledeviations.com/2022/01/10/probability-matching-kelly/ 文中介绍的内容相配合。我想写一篇中文推文，把你给我的 Python 代码与这篇文章的内容结合起来，增加趣味性，也便于读者理解。

> **Prompt** 5:  

用户使用这些函数时，能否自行调节参数，甚至进行动态互动演示？

> **Prompt** 6:   

能否把上述讨论内容整合成一篇完整的推文。主内容包括：

https://reasonabledeviations.com/2022/01/10/probability-matching-kelly/ 的中文翻译 (可以适当意译，以符合中文表述习惯)；

1. 在合适的位置嵌入 Python 代码和解释性文字。 
2. 预留图片插入位置，我随后运行完代码后插入图片。 
3. 其它你认为必要的扩充。 

- 字数：中文字符不少于 10000 字
- 输出：直接连续输出，可以分多次输出
- 格式：不要添加表情符号；章节顺序编号：## 1. xxx;  ### 2.1 xxx
:::

