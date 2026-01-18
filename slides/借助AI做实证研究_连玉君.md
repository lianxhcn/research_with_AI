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
  font-size: 36px;      /* 正文字号 */
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
<!-- [lianxh.cn](https://www.lianxh.cn/news/46917f1076104.html)  -->

<br>

<!--封面图片-->
![bg right:54% w:650 brightness:. sepia:40%](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250502000239.png) 

<!-- ![bg right:54% w:650 brightness:. sepia:40%](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250724220541.png) -->

<!--幻灯片标题-->



# Empirical Research with AI

<br>
&#x1F34F; 课件：  

<https://lianxhcn.github.io/research_with_AI>

<br>

<br>

<!--作者信息-->
[连玉君](https://www.lianxh.cn) (中山大学)
arlionn@163.com

<br>

---

-   AI 时代：实证研究模式如何变化？
-   AI 工具如何提升实证研究的效率？
-   AI 工具如何帮助我们更好地思考和解决问题？
  
---

-   实例：
    -   如何用 AI 工具发现好的 IV？
    -   如何用 AI 理解复杂的计量文献？
-   技术：
    -   Stata，R 还是 Python？
    -   Markdown，Github 和 Jupyter Notebook
    -   AI 助力论文复现

--- - --

# 1. AI 时代：实证研究模式如何变化？

--- - --

## 引子：你是干什么的？

![bg left:10% w:30](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250724214545.png)

一位窗帘商人，占据了大部分市场，想再多赚点，便请来一位智者 ……  
> - **商人**：“我该如何提升利润？”  
> - **智者**：“你是做什么的？”  
> - **商人**：“我做漂亮的布艺窗帘。”  

智者笑而不语，抄着手离开了。过了一段时间，商人又请来智者，
> - **商人**：“我该如何提升利润？”  
> - **智者** 沉思片刻，问道：“你是做什么的？”

又隔了一段时间，商人还没有找到答案，便再次请来智者，

智者拉动着漂亮的窗帘，屋内的光线忽明忽暗，商人有些茫然 ……
> - **智者**：“你是做什么的？”

商人恍然大悟！&emsp; &emsp; &emsp; &emsp;   :apple: [ChatGPT 对话过程](https://chatgpt.com/share/6881fd7f-305c-8005-b740-1e509e66ab95)

--- - --

## 思考

&emsp;

- 我为什么要学 Stata / Python / R ?

&emsp;

- 我是做什么的？


--- - --

## 变与不变

- 实证研究和学术研究的本质都没有变
  - 大胆假设，小心求证
  - 多数情况下，「问题」比「方法」更重要
  - 提出问题的过程，就是「思考」的过程，就是不断「假设-逻辑推理(测试)-证伪」的过程

- 研究假设的生成过程变化了
  - AI+：更快地生成假设：提供多种思考视角
  - AI+：更好地理解已有成果：哪里能去，哪里不能去

- 研究方法和工具的变化
  - 写代码 &rarr; 写提示词：数据清洗、研究设计、模型构建
  - 从「单点技能」转向「跨界整合」
  - **短板效应**：增强 v.s. 减弱？

![bg right:40% h:650](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/ai_research_01_napkin.png)


--- - --

## 过去:学习的重心是什么？

- **经典理论与范式**：微观、宏观、计量三大支柱；
- **数学与统计工具**：线性代数、概率论、数理统计、计量经济学；
- **主流软件技能**：Stata、R、Matlab、SAS ……
  
- **文献阅读与论文写作能力**：跟踪一条 literature line，围绕它选题、建模、实证。


--- - --

## AI 时代的变化在哪里？


- **从「单点技能」转向「跨界整合」**
  - 整合数据、模型、算法、文献，并用 AI 协助迁移
  
- **理论与数据的互动方向反转**
  - 从「理论先行 → 实证验证」向「数据先感知 → 模型解释」过渡
- **工具从模型核心转向问题核心**
  - 研究工具 = 解决问题的桥梁，而非目的本身
  - 从「写代码」转向「写提示词」：重点不是命令语法，而是能否清晰表达问题、设计流程、定位输出
  - 工具： [ChatGPT](https://chat.openai.com/)、[Causal.Claims](https://www.causal.claims/)、[DeepSeek](https://www.deepseek.com/)、[PaperQA](https://github.com/rocketlaunchr/paperqa)
  - 工具：agents 


---

# AI 工具如何提升实证研究的效率？

- Korinek, A. (2023). Generative AI for Economic Research: Use Cases and Implications for Economists. Journal of Economic Literature, 61(4), 1281–1317.   
  
  [Link](https://doi.org/10.1257/jel.20231736) (rep), [PDF](https://genaiforecon.org/JEL-2023-1736_published.pdf), [-PDF2-](../refs/Korinek_2023_Generative_AI_for_Economic_Research_Use_Cases_and_Implications_for_Economists.pdf)    
  
  [Appendix](https://www.aeaweb.org/doi/10.1257/jel.20231736.appx), [Google](<https://scholar.google.com/scholar?q=Generative AI for Economic Research: Use Cases and Implications for Economists>).   
  
  [作者主页-Tips-AI](https://genaiforecon.org/get-started.html)

---

![w:900](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250725161812.png)

---

![w:900](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250725162052.png)


--- - --

## 搭建 AI 辅助代码环境
- Anaconda + VScode 环境配置
  - 详情：DS with Python，[Chapter 6](https://book.lianxh.cn/ds/body/01_1_install-Python-Anocanda.html) | [Chapter 7](https://book.lianxh.cn/ds/body/01_2_install_FAQs.html)

- 基于提示词的编程和数据分析

- Stata+Python：Jupyter Notebook

---

## AI 工具

- [ChatGPT](https://chat.openai.com/chat) - 由 OpenAI 开发的聊天机器人，基于 GPT-3.5 架构。可以用于编写代码、回答问题、生成文本等。
- [ChatGPT Plus](https://openai.com/pricing) - 付费版本的 ChatGPT，提供更快的响应时间和更高的可用性。
- [DeepSeek](https://deepseek.ai/) - 一款基于 AI 的搜索引擎，支持多种语言的搜索和翻译。
- [豆包](https://www.douban.com/) - 一款基于 AI 的社交网络应用，支持多种语言的交流和分享。
- [kimi](https://www.kimi.ai/) - 一款基于 AI 的智能助手，支持多种语言的语音识别和翻译。

- **其它/高级/多模态**：[杨阳 - 生成式人工智能专题](https://www.lianxh.cn/AIR.html)

---

# 理念

### 自然语言编程 vs. 传统编程

- 「自然语言编程」与 Python、C++ 等传统编程本质上都是向计算机发出指令，要求其执行特定操作。
- 区别在于：  
    - 传统编程语言（如 Python、C++）有严格的语法和结构。  
    - 自然语言编程则用人类语言（如中文、英文）描述操作。


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

- [推文 · 提示词](https://www.lianxh.cn/search.html?s=%E6%8F%90%E7%A4%BA%E8%AF%8D)

- 连玉君的提示词：<https://github.com/arlionn/UseChatGPT>
  - 你可以 Fork 这个仓库

- 应用实例：[连玉君 - Empirical Research with AI](https://lianxhcn.github.io/research_with_AI/)

---

## 大模型的各种应用

> [Google 学术 - LLM and Applications](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Survey++Large+Language+Models+for&btnG=)

![w:800](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20251104143353.png)


---

## 大模型在金融领域的应用

Nie, Y., Kong, Y., Dong, X., Mulvey, J. M., Poor, H. V., Wen, Q., & Zohren, S. (2024). A Survey of Large Language Models for Financial Applications: Progress, Prospects and Challenges (Version 1). arXiv. [Link](https://doi.org/10.48550/arXiv.2406.11903) (rep), [PDF](https://arxiv.org/pdf/2406.11903.pdf), [Google](<https://scholar.google.com/scholar?q=A Survey of Large Language Models for Financial Applications: Progress, Prospects and Challenges (Version 1)>).

![w:800](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/LLM-Finance-survey-01.png)

---

## FinMem: LLM 交易代理

Yu, Y., Li, H., Chen, Z., Jiang, Y., Li, Y., Suchow, J. W., Zhang, D., & Khashanah, K. (2025). FinMem: A Performance-Enhanced LLM Trading Agent With Layered Memory and Character Design. IEEE Transactions on Big Data, 1–18. [Link](https://doi.org/10.1109/TBDATA.2025.3593370), [PDF](https://ojs.aaai.org/index.php/AAAI-SS/article/download/31290/33450/35346), [Google](<https://scholar.google.com/scholar?q=FinMem: A Performance-Enhanced LLM Trading Agent With Layered Memory and Character Design>).

--- 

## 多模态

![20251104144139](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20251104144139.png)

---

## 多模态 JF

> Borgschulte, M., Guenzel, M., Liu, C., & Malmendier, U. (2025). CEO Stress, Aging, and Death. The Journal of Finance. Portico. [Link](https://doi.org/10.1111/jofi.13497) (rep), [PDF](https://repec.iza.org/dp16366.pdf), [Google](<https://scholar.google.com/scholar?q=CEO Stress, Aging, and Death. The Journal of Finance>).

![w:700](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20251104144309.png)

--- 

## 多模态 信息披露

> Boulland, R., Bourveau, T., & Breuer, M. (2025). Company Websites: A New Measure of Disclosure. Journal of Accounting Research. Portico. [Link](https://doi.org/10.1111/1475-679X.70007), [PDF](https://file-lianxh.oss-cn-shenzhen.aliyuncs.com/Refs/2025-08-Yang/JAR-BOULLAND-Company-Websites.pdf), [Google](<https://scholar.google.com/scholar?q=Company Websites: A New Measure of Disclosure. Journal of Accounting Research>).

![w:800](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20251104150825.png)

---

<center>

# [Empirical Research with AI](https://lianxhcn.github.io/research_with_AI/)

</center>