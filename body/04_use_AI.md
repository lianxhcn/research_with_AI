# 使用 AI 写论文推介


## 局部翻译、润色

写推文过程中，可能需要将英文内容翻译成中文，或对已有的中文内容进行润色。以下是一些常用的 AI 工具和提示词，帮助你完成翻译和润色工作。

::: {.callout-tip}
### 提示词-简要版

请将以下内容翻译成中文，并进行润色：

{{content}}
:::

::: {.callout-tip}
### 提示词-升级版

请将以下内容翻译成中文，并进行润色。
注意保留原文中的代码块和链接格式。
翻译时要确保语句通顺，符合中文表达习惯。
必要时可以意译，甚至大幅调整语序。

{{content}}
:::

::: {.callout-tip}
### 提示词-中文修改

请修改、润色以下中文内容，确保语句通顺，符合中文表达习惯。
必要时可以意译、增加上下文或转承语句，甚至大幅调整语序。

语言风格：兼顾上下文的同时，使用 lianxh.cn 推文中的语言风格。

{{content}}


## 数学公式识别

识别数学公式的首选工具是 [MathPix](https://mathpix.com/)。

替代工具：[simpletex](https://simpletex.cn)
  - 支持 [在线识别](https://simpletex.cn/ai/latex_ocr)；[本地运行](https://simpletex.cn/download)

如果你没有 MathPix 账号，或不想使用付费版本，可以使用 [DeepSeek](https://deepseek.com/) 或 [ChatGPT](https://chat.openai.com/) 等 AI 工具进行数学公式识别：

1.  **截图**：将需要识别的数学公式或文本截图保存为图片文件。建议使用 [Snipaste](https://www.lianxh.cn/details/1111.html) 等工具进行截图。
2.  **发送图片**：将截图粘贴到 AI 工具的输入框中。
3.  **输入提示词**：根据所使用的 AI 工具，输入相应的提示词。

::: {.callout-tip}
### 提示词
```md
识别图片中的文字，转换成标准的 Markdown 文字。

数学符号和公式使用 $$ 包围；
- 文内公式格式为：$y = f(x)$
- 单行公式格式为：

$$
y = f(x)
$$

随后我会发送一系列待识别的图片给你，请都按此要求识别。
```
:::

详情参见：连小白, 2025, [完美替代 MathPix：我用 ChatGPT、豆包、Kimi 识别数学公式](https://www.lianxh.cn/details/1639.html).

<!-- 
## 参考文献格式化

你可以提供一篇 Blog 或论文的基本信息，如标题、作者、期刊等，AI 工具会自动生成符合 Markdown 格式的参考文献条目。

- 对于学术论文，建议优先使用 [getiref](https://www.lianxh.cn/details/1382.html) 命令获取参考文献格式。
- 对于


### B722-翻译 - 论文推介：实证分析常见错误指南

- Wulff, J. N., Sajons, G. B., Pogrebna, G., Lonati, S., Bastardoz, N., Banks, G. C., & Antonakis, J. (2023). Common methodological mistakes. The Leadership Quarterly, 34(1), 101677. [Link](https://doi.org/10.1016/j.leaqua.2023.101677), [PDF](http://sci-hub.ren/10.1016/j.leaqua.2023.101677), [Google](<https://scholar.google.com/scholar?q=Common methodological mistakes>).

写作要点：
- 第一篇推文：整理 Table 1: Common Issues in Empirical Articles and Suggested Solutions. 我已经整理成 items 形式，并使用 ChatGPT 进行了翻译，你可以酌情调整即可。
  - [Table1-英文版](https://gitee.com/Stata002/StataSX2018/blob/master/sample/B722-Common-mistakes.md) | [Table1-中文版](https://gitee.com/Stata002/StataSX2018/blob/master/sample/B722-Common-mistakes-Chinese.md)
- 第二篇推文：对这篇论文的后半部分进行翻译。这些内容为实证分析中的常见错误都提供了解决方法。你可以借助 ai 的工具进行翻译，我发现一个简单的办法就是你直接把作者原始提供的 pdf 文件的截图给 DeepSeek 或者是 ChatGPT，他就可以一页一页的帮你翻译完了。当然你如果能找到更好的办法，那也行。要注意的是，如果你直接把整个 pdf 传给 ai，他会帮你删掉很多内容。 -->