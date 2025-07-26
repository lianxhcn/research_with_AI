::: {.callout-tip}
### 提示词

\##-Prompt 1:  

我想根据如下资料 ({text-01}) 写一篇推文。我的读者主要是经管类的博士生和青年老师，他们的主要工作做实证研究。

1. 你觉得这篇推文的主要卖点应该是什么？
2. 推文的思路和结构应该是什么样的？

---

'''{text-01}
# Causal-Copilot

介绍原理，然后使用 [https://causalcopilot.com/](https://causalcopilot.com/) 来做一些测试。 

- github: <https://github.com/Lancelot39/Causal-Copilot>
- [demo-vedio: Causal-Copilot Demo: Tabular Data](https://www.youtube.com/watch?si=3DTT2AlEIcAf-T_E&v=U9-b0ZqqM24&feature=youtu.be)
- [Sample Dataset](https://huggingface.co/Causal-Copilot)

Wang, X., Zhou, K., Wu, W., Singh, H. S., Nan, F., Jin, S., Philip, A., Patnaik, S., Zhu, H., Singh, S., Prashant, P., Shen, Q., & Huang, B. (2025). Causal-Copilot: An Autonomous Causal Analysis Agent (Version 2). arXiv. [Link](https://doi.org/10.48550/arXiv.2504.13263) (rep), [PDF](https://arxiv.org/pdf/2504.13263.pdf), [Google](<https://scholar.google.com/scholar?q=Causal-Copilot: An Autonomous Causal Analysis Agent (Version 2)>). [TeX Source](https://arxiv.org/src/2504.13263)
'''


\##-Prompt 2:   

帮我规划一个写作提纲。

1. 语言朴实，注重为论据提供细节
2. 不要任何表情符号。全文按照 ## 1. title    ### 1.1 sub_title  的结构来编号
3. 注重实操性。我的读者希望看完推文后能上手操作，实现自己的需求。


\##-Prompt 3:

好。
1. 我希望你提供的推文可以按 section 输出，确保每个 section 都有充实的内容。
2. 每个 section 可以先用一段话概括这个 section 针对的问题是什么？要点是什么。然后再开始展开说明。
3. 段落性文字和 items 格式的文本占比 为 2:1 以上，也就说，不要过度使用 items 方式来写推文，总感觉干巴巴的。


\##-Prompt 4:

好

\##-Prompt 5:

将整篇推文汇总成 Markdown 教学文稿。不要删减，只需要把现有答案合并起来，稍作调整即可。

:::