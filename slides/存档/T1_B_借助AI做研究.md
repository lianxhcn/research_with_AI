---
marp: true
size: 16:9        # 宽版：4:3
paginate: true  
footer: '连享会 &emsp; [lianxh.cn](https://www.lianxh.cn)'
---

<style>
/*一级标题局中*/
section.lead h1 {
  text-align: center; /*其他参数：left, right*/
}
section {
  font-size: 22px;      /* 正文字号 */
}
h1 {
  color: blackyellow;   /* 标题的颜色 */
  /*font-size: 28px; */ /* 标题的字号, 其它标题也可以这样修改 */
}
h2 {
  color: green;
}
h3 {
  color: darkblue;
}
h4 {
  color: brown;
}
/* 右下角添加页码 */
section::after {
  content: attr(data-marpit-pagination) '/' attr(data-marpit-pagination-total); 
}
header,
footer {
  position: absolute;
  left: 50px;
  right: 50px;
  height: 25px;
}
</style>

<!--顶部文字-->
[lianxh.cn](https://www.lianxh.cn/news/46917f1076104.html) 

<br>

<!--封面图片-->
![bg right:56% w:700 brightness:. sepia:50%](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250502000239.png) 


<!--幻灯片标题-->

#### 连享会 · 2025 五一论文班

# Research with AI

<br>
<br>

<!--作者信息-->
[连玉君](https://www.lianxh.cn) (中山大学)
arlionn@163.com

<br>


---

## AI 工具

- [ChatGPT](https://chat.openai.com/chat) - 由 OpenAI 开发的聊天机器人，基于 GPT-3.5 架构。可以用于编写代码、回答问题、生成文本等。
- [ChatGPT Plus](https://openai.com/pricing) - 付费版本的 ChatGPT，提供更快的响应时间和更高的可用性。
- [DeepSeek](https://deepseek.ai/) - 一款基于 AI 的搜索引擎，支持多种语言的搜索和翻译。
- [豆包](https://www.douban.com/) - 一款基于 AI 的社交网络应用，支持多种语言的交流和分享。
- [kimi](https://www.kimi.ai/) - 一款基于 AI 的智能助手，支持多种语言的语音识别和翻译。


## 连玉君的提示词

- <https://github.com/arlionn/UseChatGPT>
- <https://gitee.com/arlionn/UseChatGPT> (码云版)

---

## 理念

### 自然语言编程 vs. 传统编程

- 「自然语言编程」与 Python、C++ 等传统编程本质上都是向计算机发出指令，要求其执行特定操作。
- 区别在于：  
    - 传统编程语言（如 Python、C++）有严格的语法和结构。  
    - 自然语言编程则用人类语言（如中文、英文）描述操作。

---

### 思维方式与沟通能力

- 初学时，自然语言编程似乎更简单。
- 真正发挥其潜力，关键在于**思维方式**和**沟通方式**（如何提问）。
- 学习曲线很陡峭：
  - 知识广度：你要知道很多东西以及他们的关联，才能提出好的问题。
  - 知识深度：基本概念、核心理论、核心算法
  - 逻辑思维：界定问题、拆解问题、追问 (横向 v.s. 纵向)
  - 语言表达：简洁、准确、清晰
---

## 最核心的理念转变

- 提示词 = 自然语言的“代码”
- 写好提示词，就像写好 Python/C++ 代码一样重要。
- 许多高校已开设「提示词工程」课程，「Prompt 工程师」将成为热门职业。

### 推荐学习资料

- [Prompt Engineering Guide](https://www.promptingguide.ai/zh)
- 吴恩达老师的 [ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)

![bg right:50% w:600](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250425003834.png)


--- - --


## 提示词


### Tips
  - 先粗后细 [e.g. 生成讲义](https://chatgpt.com/share/680a54a4-1174-8005-bedc-b101549ad45b) v.s 先细后粗 
  - 顺藤摸瓜-迁移 [e.g. 各种抽样方法](https://chatgpt.com/share/680a57b2-f4d4-8005-b94a-b9c659e08508)
  - 虚构角色 [e.g. 你是一个资深的英文经济学期刊的编辑](https://chatgpt.com/share/67f11fc5-b1a0-8005-b559-c479ffbad641) &rarr; [推文](https://www.lianxh.cn/details/1563.html)

### 收集整理自己的提示词
  - [ChatGPT Prompting Cheat Sheet](https://blog.finxter.com/wp-content/uploads/2023/03/Finxter_Prompting_OpenAI-1.pdf)
  - [The Complete ChatGPT Cheat Sheet 2025!](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1icr5au/the_complete_chatgpt_cheat_sheet_2025/)
  - [Prompt工作手册 - 方法篇](https://zhuanlan.zhihu.com/p/713023937)


--- - --
<!-- backgroundColor: #FFFFF9 -->
## 应用体验 1：AI 伴读理论文献

<br>

- 连玉君, 2025, [如何借助 AI 工具来伴读一篇理论类的论文？](https://www.lianxh.cn/details/1571.html), 连享会 No.1571.
  
  - [ChatGPT提示词 1：伴读一篇理论类的论文](https://chatgpt.com/c/67f8b6cc-9da4-8005-b78d-4c3c03693de0)
  
  - [ChatGPT提示词 2：RD调整成本函数](https://chatgpt.com/share/680a3b68-c180-8005-a2f6-00172b13126f)

--- - --
<!-- backgroundColor: white -->
## 借助 AI 寻找 IV

>Han, S. (2024). Mining Causality: **AI-Assisted Search for Instrumental Variables**. arXiv. [Link](https://doi.org/10.48550/arXiv.2409.14202) (rep), [PDF](https://arxiv.org/pdf/2409.14202.pdf), [Google](<https://scholar.google.com/scholar?q=Mining Causality: AI-Assisted Search for Instrumental Variables (Version 2)>).


### 工具变量法（IVs）与大语言模型

- 工具变量法（IVs）是因果推断的主流实证策略。寻找合适的工具变量依赖于研究者的创造性思维，而论证其有效性（尤其是排除性限制）则常常需要一定的修辞技巧。
- 利用大语言模型（LLMs），可以通过叙事和反事实推理来搜索新的工具变量。其原理类似于人类的研究过程，但 LLMs 能极大加速搜索过程，并探索海量的可能性。
- 本文提出多步骤角色扮演提示策略，有效模拟经济主体的决策逻辑，引导模型处理现实场景。
- 方法已应用于教育回报率、供需关系、同伴效应等经典案例，并扩展至回归/双重差分控制变量及断点设计运行变量的自动化寻找。

---

### AI 寻找 IV 的优势

采用 AI 辅助方法寻找工具变量（IVs）至少有**四大优势**：
- 首先，研究者可以根据具体研究情境，快速而系统地进行搜索。
- 其次，与 AI 工具的互动有助于激发寻找新型工具变量领域的灵感。
- 第三，系统性搜索有助于获得多个工具变量，从而可以通过过度识别检验等统计方法对其有效性进行正式检验。
- 第四，拥有候选工具变量清单有助于提高在实际数据中找到工具变量的概率，或指导数据的构建，包括设计实验以生成工具变量。

--- - --
<!-- backgroundColor: #FFFFF9 -->
## 借助 AI 找 IV：连玉君的实战经验

- [帮我找 20 个 IV](https://chatgpt.com/share/67ded832-79bc-8005-bbdb-7a79ebd755c7)
  
- [寻找 IV 的提示词如何写？](https://chatgpt.com/share/680a60aa-3eb4-8005-9478-42828c78c38a)

--- - --

## 使用 AI 写一篇完整的论文推介

- [Du-2024-EE-中文精要生成过程](https://chatgpt.com/share/6812ec94-a280-8005-9abc-ac0bba09e566)

**核心提示词：** 参见 [连玉君的 Prompts](https://github.com/arlionn/UseChatGPT/blob/main/Prompt/useful_Prompts.md)

> **Prompt 1**:   
> {先上传论文的 PDF 版本给 ChatGPT，然后输入以下提示词：}    
>    
> "写一篇论文推介，介绍附件中的论文。先列个提纲给我。"

---

> **Prompt 2**:   

分批次输出吧
1. 计量模型的证明和详细推导过程可以省略，但要补充简单直白的语言来解释模型和参数的经济含义
2. 把数学符号和公司都采用 Latex 格式来写，以保证输出美观
3. 行内公式采用 `$f=x$` 格式，单行公式采用 `$$f=x$$` 格式
4. 所有括号都用半角模式，中英文混排注意加空格
5. 不要添加如何表情符号
6. 按 '## 1. xxx'，'### 1.1 xxx'，'#### xxx'(不编号) 的等格式来分 Section, Subsection, Subsubsection
7. 参考文献格式：
   - xxx, xxx, xxx. (**2023**). xxx. *Journal of xxx*, 1(1), 1-10. `[Link](https://doi.org/{DOI}), [-PDF-](http://sci-hub.ren/{DOI}), [Google](<https://scholar.google.com/scholar?q={Title of the Paper}>).`
8. 注意：每次生成答案时，都在首行按如下格式添加 label，以便我追问时定位：'mylabel-01'，'mylabel-02'，……


---

> **Prompt 3**:   
>
> 连续输出，中间无需停顿

<br>

> **Prompt 4**:  
> 详细介绍一下 4.4 模型四：部分线性函数系数面板模型（PLFC） 中的模型设定和估计方法 

<br>

> **Prompt 5**:  
> 1. 补充一个 Subsection，添加如下内容：
为没有任何非参数估计基础的读者解释一下 样条基函数（Sieve Estimation）
>2. 再补充一个 subsection，解释一下边际效应的置信区间是如何计算的


--- - --



## 借助大语言模型论述因果关系

Garg, P., & Fetzer, T. (2025). Causal Claims in Economics (Version 1). arXiv. [Link](https://doi.org/10.48550/arXiv.2501.06873) (rep), [PDF](https://arxiv.org/pdf/2501.06873.pdf), [Google](<https://scholar.google.com/scholar?q=Causal Claims in Economics (Version 1)>).


> 官网：<https://www.causal.claims/>

### Here are some common use cases

1.  **Exact Cause and Effect Match**
    -   Example Prompt: "Find papers where fiscal policy causes economic growth."
    -   This search will look for papers that contain the specified cause-effect relationship and return exact matches, if available.

2.  **Cause-only Search**
    -   Example Prompt: "Find papers with 'job mobility' as a cause."
    -   When only a cause is specified, the assistant will return all papers that mention this cause, along with a list of effects associated with it.
