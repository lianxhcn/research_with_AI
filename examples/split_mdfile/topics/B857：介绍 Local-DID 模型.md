# B857：介绍 Local-DID 模型

> [github-lpdid](https://github.com/friosavila/lpdid)

- Markdown 文档生成建议：
  - 复制网页内容 &rarr; 贴入 Typora 编辑器，按 **Ctrl+/** 即可呈现 Markdown 文本。
  - 数学公式：可以用 [simpletex](https://simpletex.cn/) 软件扫描获取。

## 简介 LP-DiD

- Dube, A., D. Girardi, O. Jorda, A. M. Taylor, **2023**, A local projections approach to difference-in-differences event studies. [PDF](https://www.frbsf.org/wp-content/uploads/sites/4/wp2023-12.pdf), [Replication](https://github.com/danielegirardi/lpdid), [-cited-](https://scholar.google.com/scholar?cites=2002525239519188943&as_sdt=2005&sciodt=0,5&hl=zh-CN)

Dube, Girardi, Jorda' and Taylor (2023) propose a local projections approach to difference-in-differences event studies - LP-DiD.

This repository contains two STATA do files that implement the LP-DiD estimator in simulated datasets. 

Both examples illustrate the case of binary, staggered and absorbing treatment, when only not yet treated units are used as controls. 

- `LP_DiD_examplefile.do` uses a simulated dataset similar to the Montecarlo simulations presented in Dube, Girardi, Jorda' and Taylor (2023). 

- `lpdid_test.do` applies LP-DiD in a simulated dataset from Borusyak (2021).
