---
### ------------------- 幻灯片还是普通网页
marp: true
#marp: false

### ------------------- 幻灯片尺寸，宽版：4:3
size: 16:9
#size: 4:3

### ------------------- 是否显示页码
paginate: true  
#paginate: false

### ------------------- 页眉 (备选的用 '#' 注释掉)
# header: lianxh.cn
#header: '[连享会](https://www.lianxh.cn)'
#header: '[lianxh.cn](https://www.lianxh.cn/news/46917f1076104.html)'

### ------------------- 页脚 (备选的用 '#' 注释掉)
#footer: 'lianx.cn Marp 模板'
footer: '连享会&nbsp;|&nbsp;[lianxh.cn](https://www.lianxh.cn)&nbsp;|&nbsp;[Video](https://lianxh-class.cn/)'
#footer: '![20230202003318](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20230202003318.png)'
---

<!-- 
Notes: 
1. 选中一段文本，按快捷键 'Ctrl+/' 可以将其注释掉；再次操作可以解除 
2. header, footer 后面的文本需要用单引号引起来，否则会有语法错误
3. '#size: 16:9' 不能写为 'size:16:9'，即 'size:' 后要有一个空格
-->



<!-- Global style: 设置标题字号、颜色 -->
<!-- Global style: 正文字号、颜色 -->
<style>
/*一级标题局中*/
section.lead h1 {
  text-align: center; /*其他参数：left, right*/
  /*使用方法：
  <!-- _class: lead -->
  */
}
section {
  font-size: 22px; 
}
h1 {
  color: blackyellow;
}
h2 {
  color: green;
}
h3 {
  color: darkblue;
}
h4 {
  color: brown;
  /*font-size: 28px; */
}
/* 右下角添加页码 */
section::after {
  /*font-weight: bold; */
  /*text-shadow: 1px 1px 0 #fff; */
/*  content: 'Page ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total); */
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
![bg right:56% brightness:. sepia:50% w:700](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/PSTR_02_c_location.png) 



<!-- backgroundColor: #FFFFF9 -->
# 实证分析可视化  <!--幻灯片标题-->

<br>

##### 连玉君 (中山大学)
arlionn@163.com

<br>

> :dog: 课件：<https://gitee.com/arlionn/graph>


--- - --

## 概要

1. 感受可视化

2. 为何要进行可视化？

3. 一些基本原则

4. 工具和软件

--- - --
<!-- backgroundColor: #C1CDCD -->

# 1. 感受可视化


--- - --
<!-- backgroundColor: #FFFFF9 -->

> 2021 年蒙特卡洛大师赛-八强赛：卢布列夫 v.s. 纳达尔

- 卢布列夫：不断用正拍攻击纳达尔威胁性较低的反拍
- 纳达尔：全身的重心时刻预备着防范卢布列夫可能的下一球对角正拍
- 卢布列夫：运用重复路线打回马枪
- 纳达尔：望球兴叹

![h:400](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20220722113618.png)


--- - --

## 劳动力市场中的性别不平等

> Kleven, Henrik, Camille Landais, and Jakob Egholt Søgaard. 2019. "Children and Gender Inequality: Evidence from Denmark."   
>**American Economic Journal: Applied Economics**, 11 (4): 181-209. [-Link-](https://www.aeaweb.org/articles?id=10.1257/app.20180010), [-PDF-](https://pubs.aeaweb.org/doi/pdfplus/10.1257/app.20180010),[-cited-](https://scholar.google.com/scholar?cites=167605246068571565&as_sdt=2005&sciodt=0,5&hl=en), [-Appendix-](https://www.aeaweb.org/content/file?id=10629), [-Replication-](https://www.openicpsr.org/openicpsr/project/116366/version/V1/view)

- 丹麦的数据，孩子出生对劳动力市场性别不平等的影响。
- 发现：孩子的到来导致了长期的性别差距：工资差距大概 20%。
  - 这种差距在最近的 30-40 年中越来越显著。
  - 这种差距是由每周工作的小时数、参与率以及工资率等造成的。

> 更多顶刊可视化: [论文写作](https://www.lianxh.cn/blogs/31.html) &rarr; [论文中因果推断的经典图形](https://www.lianxh.cn/news/0593e9487d93e.html)

--- - --

<!-- backgroundColor: #FFFFF9 -->

![bg left:45% w:600](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/B208-陈卓然-因果推断经典图形-Kleven2019AEAAEA2.png)

![w:800](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/B208-陈卓然-因果推断经典图形-Kleven2019AEAAEB.png)

--- - --

## 信息技术与一价定律

> Jensen, R., The digital provide: Information (technology), market performance, and welfare in the South Indian fisheries sector. **Quarterly Journal of Economics**, 2007, 122 (3): 879-924. [-Link-](https://academic.oup.com/qje/article/122/3/879/1879540?login=true),[-PDF-](https://sci-hub.mksa.top/10.1162/qjec.122.3.879) [-cited-](https://scholar.google.com/scholar?cites=14479768387379224975&as_sdt=2005&sciodt=0,5&hl=en).

- 信息成本高 &rarr; 套利活动受阻 &rarr; **一价定律** ${\color{red}{??}}$
- 手机 &rarr; 信息技术进步 &rarr; 市场效率提高 &rarr; 社会福利增加
- **Data:** 
  - 印度南部的一个以渔业为主的州: Kerala
  - 1997-2001 年，陆续引入移动手机 &rarr; 海鲜价格波动 
- **发现：** 移动手机引入后，价格波动大幅降低 &rarr; **一价定律** ${\color{blue}{\text{OK}}}$

--- - --

![w:900](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20220626191325.png)

--- - --

![w:900](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20220626191935.png)



--- - --

> Source: [dsbook](http://rafalab.dfci.harvard.edu/dsbook/introduction-to-data-visualization.html)

<center>

![gapminder-dsbook-R](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/gapminder-dsbook-R.gif)

</center>

--- - --

## 动图：多幅图片叠加播放

> 犯罪行为的扩散 / 疾病的传播

<center>

![w:600](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/071632_bb2d5064_1522177.gif)

> Source: ：[连享会：空间计量](https://www.lianxh.cn/blogs/29.html) &rarr; [空间计量溢出效应的动态GIF演示](https://www.lianxh.cn/news/0b822f835c9d5.html)

</center>

--- - --

![bg left:55% w:600](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/Animation-of-DID-01.gif)

$$
\begin{aligned}
Y_{it} &= \alpha + \beta_1 Treat_{it} + \beta_2 After_{it} + \\
&\quad {\color{blue}{\gamma}}\,Treat_{it}\times After_{it} + u_{it}
\end{aligned}
$$


> Source:   
> [NickCH-K](https://github.com/NickCH-K) &rarr; [causalgraphs](https://nickchk.com/causalgraphs.html) &rarr; [github](https://github.com/NickCH-K/causalgraphs)
- 采用动图呈现了常用的因果推断模型的核心思想，包括 IV, DID, FE, RDD, PSM 等



--- - --

<center>

![_data_visualization_definition](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/_data_visualization_definition.gif)

> Source: [Tableau - What Is Data Visualization?](https://www.tableau.com/visualization/what-is-data-visualization)

</center>



--- - --
<!-- backgroundColor: #C1CDCD -->

# 2. 为什要可视化 ？

<!-- 
### 大咖怎么看？

<br>

> A picture is worth a thousand words. —— Barnard (1927)  

> Graphs are essential to good statistical analysis. —— Anscombe (1973)

> The greatest value of a graph is when it forces us to see what we never expected. —— Tukey (1977)

> A picture may be worth a thousand words, but it may take a hundred words to do it. —— Tukey (1986)

> Visualization is critical to data analysis. —— Cleveland (1993) -->

<!-- 
![h:640](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20220630010015.png)
-->

<!-- 
--- - --


##### Table 2. Graphical Analyses in Top Manag Journals (Starr, [2020](https://doi.org/https://doi.org/10.1002/smj.3199), [PDF](http://sci-hub.ren/https://doi.org/10.1002/smj.3199)) 

&\text { Table 2. Graphical Analyses in Top Management Journals } \\
$$
\begin{aligned}

&\begin{array}{lrr}
\hline \textbf { Panel A. Graphs in the manuscripts } & \text { Mean } & N \\ 
\text { Was there a graph at all in the manuscript? } & 46 \% & 100 \\
\text { Was the distribution of a variable graphically shown? } & 2 \% & 100 \\
\text { Was the relationship between } x \text { and } y \text { shown at all? } & 35 \% & 100 \\ \newline
\textbf {Panel B. Graphing the Relationship of Interest } & & \\ 
\text { Was a scatter plot between } x \text { and } y \text { shown? } & 4 \% & 100 \\
\text { Were the fitted values from the estimated model graphed? } & 27 \% & 100 \\
\text { Was the raw data shown, after conditioning out observables? } & 1 \% & 100 \\
\text { Was the relationship between } x \text { and y shown in any other way? } & 10 \% & 100 \\ \newline
\textbf {Panel C. Interaction or Subgroup Analyses } \\
\text { Was there an interaction hypothesis? } & 63 \% & 100 \\
\text { Were the interaction results displayed graphically? } & 49 \% & 63 \\
\text { Were the fitted values for the interaction model graphed? } & 48 \% & 63 \\ \newline
\textbf {Panel D. Outliers and Functional Forms } & & \\
\text { Were any the independent variables of interest continuous? } & 94 \% & 100 \\
\text { How many functional forms were examined for these variables? } & 1.07 & 94 \\
\text { Was sensitivity to outliers explored? } & 18 \% & 94 \\
\hline
\end{array}
\end{aligned}
$$ -->

--- - --

## Why ？
<!-- backgroundColor: #FFFFF9 -->

<br>

- **直观**：快速了解信息
- **视觉冲击力**：印象深刻
- **不得不**：
  - 分布 (密度函数、直方图等)
  - 地图
  - 三维图
- **场景**：Seminar, 会议，答辩，group Pre

--- - --

## Why 01 ： 数据长啥样 ?
- 在正式回归分析之前，务必多做一些描述性统计分析
- 绘制散点图有助于识别如下问题： ([Source: Anscombe, 1973, p.17](https://www.sjsu.edu/faculty/gerstman/StatPrimer/anscombe1973.pdf))

  - $(x, y)$ 的散点基本上处于一条直线上
  - $(x, y)$ 的散点分布于一条平滑的曲线，而非直线上
  - $y$ 集中于某一点，基本上与 $x$ 无关
  - 常规 (幸运) 情形：介于以上几种情形之间
  - 多数点都正常，但有个别 **离群值** 

--- - --

![bg left:71% w:890](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/Anscombe1973_Figs.png)

> Source: [Anscombe, 1973, p.17](https://www.sjsu.edu/faculty/gerstman/StatPrimer/anscombe1973.pdf)

> [Stata codes](https://github.com/arlionn/StataGraph/blob/main/dofiles/Anscombe_1973.do)

<!-- 
--- - --
<-- backgroundColor: #e6e6fa ->
```stata
clear
input x      y1    y2    y3   x4    y4 
     10.0  8.04  9.14  7.46  8.0  6.58 
      8.0  6.95  8.14  6.77  8.0  5.76 
     13.0  7.58  8.74 12.74  8.0  7.71 
      9.0  8.81  8.77  7.11  8.0  8.84 
     11.0  8.33  9.26  7.81  8.0  8.47 
     14.0  9.96  8.10  8.84  8.0  7.04 
      6.0  7.24  6.13  6.08  8.0  5.25 
      4.0  4.26  3.10  5.39 19.0 12.50 
     12.0 10.84  9.13  8.15  8.0  5.56 
      7.0  4.82  7.26  6.42  8.0  7.91 
      5.0  5.68  4.74  5.73  8.0  6.89
end 
label data "Anscombe (1973), The American Statistician, 27(1): 17-21, Table 1"
save "$data/Anscombe1973", replace 
```

--- - --
<-- backgroundColor: #e6e6fa ->
```stata
ssc install cleanplots  // 安装绘图模板
set scheme cleanplots

global opt "legend(off) lc(green*2)"
tw scatter y1 x  || lfit y1 x , $opt xtitle("Fig 1")

graph save "Anscombe1973_1_temp.gph", replace 
tw scatter y2 x  || lfit y2 x , $opt xtitle("Fig 2")

graph save "Anscombe1973_2_temp.gph", replace
tw scatter y3 x  || lfit y3 x , $opt xtitle("Fig 3")

graph save "Anscombe1973_3_temp.gph", replace
tw scatter y4 x4 || lfit y4 x4, $opt xtitle("Fig 4")

graph save "Anscombe1973_4_temp.gph", replace

*-combine
graph combine "Anscombe1973_1_temp.gph" "Anscombe1973_2_temp.gph" ///
              "Anscombe1973_3_temp.gph" "Anscombe1973_4_temp.gph", xcommon ycommon

graph export "$fig/Anscombe1973_Figs.png", replace width(1200)
``` 
-->


--- - --


### 数据可能会骗你

> Source: 黄湘云, [R 语言数据分析实战-介绍](https://bookdown.org/xiangyun/data-analysis-in-action/intro.html)

R 中的 [**datasauRus**](https://github.com/jumpingrivers/datasauRus) 包 内置了一个数据集 **datasaurus\_dozen**，包含 13 个子数据集，它们在均值、标准差等描述性统计量方面十分接近。
<!-- 其中 $\bar{x}, \sigma_x$ 分别代表预测变量 $X$ 的均值和标准差， $\bar{y}, \sigma_y$ 代表响应变量 $Y$ 的均值和标准差，$\beta_0, \beta_1$ 代表回归方程方程式 1的截距和斜率， $R^2$ 代表模型拟合数据的程度。 -->

$$
y=\beta_0+\beta_1 x+\epsilon
$$


--- - --

### 统计和回归结果

![20241227104917](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20241227104917.png)

--- - --

### 可视化结果

![w:500](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20241227104640.png)






--- - --
<!-- backgroundColor: #FFFFF9 -->
## Why 02 ：辅助学习

<br>

> 直观展示变量的分布 
> 
--- - --

### OLS 的无偏性：模拟分析

#### 思路：

- 单次抽样具有随机性 (原因？)
- 然而，如果抽样很多次，如 $\small K=1000$ 次，取它们的均值，$\small E[\hat{\beta}]$，可以很大程度上消除随机误差的影响
- 这个均值应该接近真实值：$\small E[\hat{\beta}]={\beta}_0$

#### MC-DGP 过程：
- **S1:** 随机生成一个包含 $\small N=100000$ 个观察值的样本 (视为 “总体”，Population), 记为 $\small S_{0}$ 。
  - 数据生成过程 (DGP) 为 $\small y=10+0.5 x+e$, 
  - 其中, $x$ 和 $e$ 均来自标准正态分布, 彼此独立。
- **S2:** 从 $S_{0}$ 中随机抽取 $n=50$ 个观察值, 形成一组抽样样本 (Sample), 
  - 执行 OLS 估计, 记录 $\small \widehat{\beta}$ 和 $\small\operatorname{se}(\widehat{\beta})$
  
- **S3:** 重复第二步 $\small K=1000$ 次，得到 $\small \widehat{\boldsymbol{\beta}}_j = \{\widehat{\beta}_1, \widehat{\beta}_2, \cdots, \widehat{\beta}_K\}$。

--- - --

```stata
clear 
set seed 1357
set obs 100000

gen x = rnormal(0,1)
gen y = 10 + 0.5*x + rnormal()
gen b = .
gen b_se = .
local  n = 50 // 每次抽样的样本数
global K = 1000      // 模拟次数
gen id = _n in 1/$K  // 样本序号
forvalues j =1/$K {
   preserve
     qui sample `n', count
     qui reg y x 
   restore
   qui replace    b = _b[x]  in `j'
   qui replace b_se = _se[x] in `j'
   dis "." _c
}

*-图示系数估计值
kdensity b, ///
 xline(0.5, lp(dash) lc(red) noextend)
```

![bg right:55% w:700](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/OLS_unbias_b_density.png)


--- - --

```stata
*-图示 t-value
  gen t = b/b_se

kdensity t,                    ///
  xline(1.96, lp(dash)         ///
        lc(red) noextend)      ///
  normal title(" ")            ///
  legend(order(1 "b_j den"     ///
               2 "Normal den") ///
         ring(0) pos(3))    
```

![bg right:60% w:700](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/OLS_t_value_kden.png)

--- - --
![](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/OLS_unbias_b.png)

--- - --
<!-- backgroundColor: #FFFFF9 -->
### OLS 估计的一致性 - 01

#### 何谓一致性？日久见人心
所谓估计量的「一致性」，是指当样本数 $n \rightarrow \infty$ 时, 估计值无限接近于真实值, 表示为 

$$\widehat{\beta} \stackrel{p}{\longrightarrow} \beta \qquad \text{或} \qquad \widehat{\beta}=\beta+o_{p}(1)$$

#### MC 模拟分析：

1. 随机生成一个包含 $N=$ 100000 个观察值的样本 (视为 “总体”), 记为 $S_{0}$ 。数据生成过程 (DGP) 为 $y=10+0.5 x+e$, 其 中, $x$ 和 $e$ 均来自标准正态分布, 彼此独立。
2. 从 $S_{0}$ 中随机抽取 $n=10$ 个观察值, 视为一组抽样样本 (sample), 执行 OLS 估计, 记录 $\widehat{\beta}$ 和 $\operatorname{se}(\widehat{\beta})$ 。
3. 重复第二步, 但每次抽取的样本数 $n$ 不断增加，$n=10, 20, ..., 30000$。

--- - --
<!-- backgroundColor: #e6e6fa -->
```stata
*-MC，OLS 估计的一致性：
* 随着样本数的增大，OLS 估计值的期望值趋向于真实值，方差趋近于 0
clear 
set seed 13579
set obs 100000

gen x = rnormal(0,1)
gen y = 10 + 0.5*x + rnormal()

gen n = .
gen b = .
gen b_se = .

local j = 1
foreach i of numlist 10(10)1000 1100(100)30000{
   preserve
     qui sample `i', count
     qui reg y x 
   restore
   qui replace    n = e(N)   in `j'
   qui replace    b = _b[x]  in `j'
   qui replace b_se = _se[x] in `j++'
}
```

--- - --

```stata
tw (line b n) (line b_se n), ///
   yline(0.5, lp(dash))   ///
   ylabel(0(0.1)0.8)      ///
   xlabel(10 50 100 400 1000 5000 30000) ///
   xscale(log)            ///
   legend(ring(0) pos(2)) ///
   scheme(tufte)
```

![bg right:50% w:600](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/OLS_consis_b_se.png)


--- - --
<!-- backgroundColor: #FFFFF9 -->
## Why 03 ：参透计量原理

<br>

> 例：何谓固定效应 ？何谓组内去心？

<br>

#### 固定效应模型
$$
\begin{aligned}
y_{i t} &= {\color{red}{\alpha_{i}}}+x_{i t} \beta+\varepsilon_{i t} \\
&=\sum_{i}^{N} \alpha_{i} D_{i}+x_{i t} \beta+\varepsilon_{i t}
\end{aligned}
$$

#### 组内去心

$$y_{it} -\bar{y}_i= (x_{it}-\bar{x}_i)\beta + (\varepsilon_{it}-\bar{\varepsilon}_i)$$

--- - --
<!-- backgroundColor: #FFFFF9 -->
**Raw:** $\quad \qquad\qquad\quad y_{it} = \alpha_i + x_{it}\beta + \varepsilon_{it}$ 
 <!--$D_i = 1\ \text{for firm}\ i$ and $0$ otherwise-->

**De-meaned:** $\quad y_{it} -\bar{y}_i= (x_{it}-\bar{x}_i)\beta + (\varepsilon_{it}-\bar{\varepsilon}_i)$

![w:750](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/Fig_OLS_FE_01.png)

--- - --

### FE：de-meaned 正式表述
$$
\begin{aligned}
y_{i t} &=x_{i t} \beta+ {\color{red}{\alpha_{i}}}+\varepsilon_{i t} \qquad (1) \\
& \, \\
\bar{y}_{i} &=\bar{x}_{i} \beta+{\color{red}{\alpha_{i}}}+\bar{\varepsilon}_{i} \\
& \, \\
\left(y_{i t}-\bar{y}_{i}\right) &=\left(x_{i t}-\bar{x}\right) \beta+\left({\color{red}{\alpha_{i}}}-{\color{red}{\alpha_{i}}}\right)+\left(\varepsilon_{i t}-\bar{\varepsilon}_{i}\right) \\
& \, \\
\ddot{y}_{i t} &=\ddot{x}_{i t} \beta+\ddot{\varepsilon}_{i t} \qquad\qquad\ (2)
\end{aligned}
$$

> (1) 式和 (2) 式中 $\small \beta$ 的 OLS 估计是等价的

--- - --
<!-- backgroundColor: #e6e6fa -->
#### 数据生成过程 (DGP)
```stata
clear
set obs 60
set seed 13599

egen id= seq(), from(1) to(3) block(20)
bysort id : gen t = _n + 1990

gen x1 = 3*rnormal() 
gen  e = 1*rnormal()
gen y = .

gen     x = x1 + 0
replace x = x1 + 4 if 1.id
replace x = x1 - 5 if 3.id

replace y = 6  + 0.4*x + e if id==1
replace y = 10 + 0.4*x + e if id==2
replace y = 15 + 0.4*x + e if id==3

bysort id: center y x, prefix(c_)  // De-mean

save "FWL_sim_data_FE", replace 
```

--- - --
#### 绘图1：手动
```stata
use "FWL_sim_data_FE", clear
#delimit ;
  twoway (scatter y x     if id==1, mcolor(green) msymbol(+)) 
         (scatter y x     if id==2, mc(red)  ms(oh))
         (scatter y x     if id==3, mc(blue) ms(dh))
         (lfit    y x,    lcolor(purple) lw(*1.5))    
         (lfit    y x     if id==1, lc(gray) lw(*1))
         (lfit    y x     if id==2, lc(gray) lw(*1))
         (lfit    y x     if id==3, lc(gray) lw(*1))
         (scatter c_y c_x if id==1, mcolor(green) msymbol(+)) 
         (scatter c_y c_x if id==2, mc(red)  ms(oh))
         (scatter c_y c_x if id==3, mc(blue) ms(dh))
         (lfit    c_y c_x,lcolor(purple) lw(*1.5))    
         (lfit    c_y c_x if id==1, lc(gray) lw(*1))
         (lfit    c_y c_x if id==2, lc(gray) lw(*1))
         (lfit    c_y c_x if id==3, lc(gray) lw(*1))
         , 
         yline(5, lp(longdash) lc(blue*1.5%30))
         ylabel(,angle(0))
         text(15.5 9.4 "Raw") text( 4 8.8   "De-mean")
         legend(off)  ;
#delimit cr
```

--- - --

#### 绘图 2：使用 `binscatter2` 命令

```stata
  use "FWL_sim_data_FE", clear

  global legend "legend(ring(0) pos(2) col(1))"
  global scheme "scheme(white_tableau)"
  global scheme "scheme(tufte)"
  
  binscatter2 y x, n(60) by(id)            /// // Raw
              $legend $scheme  

  binscatter2 y x, n(60) by(id) absorb(id) /// // De-mean
              $legend $scheme
```

--- - --
- $y_{it} = \alpha_i + x_{it}\beta + \varepsilon_{it}$&ensp;命令：`binscatter2 y x, by(id)` (左图)
- $\tilde{y}_{it} = y_{it} - \bar{y}_{i.} + {\color{red}{\bar{\!{\bar{y}}}_{..}}}$ &emsp; 命令：`binscatter2 y x, by(id) absorb(id)` (右图)
- $\ddot{y}_{it} = y_{it} - \bar{y}_{i.}$ &emsp;&emsp; &emsp; 命令：`binscatter2 y x, by(id) absorb(id) noaddmean` (未呈现)
  
![h:500](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20220703002127.png)


--- - --
<!-- backgroundColor: #FFFFF9 -->
## Why 04：其它原因

- 实时展示和监控 (股市、交通、气象)
- 多维度、多层次展示信息
- 发现新规律
- ……

--- - --
<!-- backgroundColor: #FFFFF9 -->
## 挑战

<br>

- 数据量大 &rarr; 可视化不容易做 &rarr; `binscatter` **分仓散点图**
  
- 变量很多，存在异质性影响，如何「控制其他变量」？ &rarr; **FWL 定理**
- 要有设计师的视角和思路 &rarr; 工具箱 + 好想法

<br>

--- - --
<!-- backgroundColor: #C1CDCD -->

# 3. 可视化的一些基本原则

1. 要有清晰的目标
2. 准确传达信息
3. 不要扭曲事实
4. 确保有可比性 
5. 选择合适的图形种类


--- - --
<!-- backgroundColor: #FFFFF9 -->

## 原则 1：要有清晰的目标

- 听众是谁？(知识背景、关注点)
- 想要达到何种目标？

<center>

![w:800](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/dv_different_reader.png)

</center>

--- - --

> 可视化与 $t$-检验、回归分析等相辅相成

- **直方图/点图/密度函数图**：呈现一维连续变量的分布特征
- **条形图**：比较一维分类数据
- **散点图/分仓散点图**：显示变量 $Y$ 和 $X$ 的之间的相关性，分组特征
- **马赛克图**：显示分类 $Y$ 和 $X$ 的关联（或缺乏关联）
- **QQ 图**：比较两个连续分布、分布的尾部特征、结构变化等

<!--  Some scientific purposes: (Note close connections to $t$-tests, regression etc)
- Histogram/dotchart/beeswarm plot: summarize 1D continuous data
- Barchart: compare 1D categorical data
- Scatterplots: show association of continuous $Y$ and $X$ (or lack of association)
- Mosaic plots: show association of categorical $Y$ and $X$ (or lack of association)
- QQ plots: compare two continuous distributions; talk about the shift, spread, heavy tails, light tails etc
-->

> Source: Rice, K., 2021, Communicating using graphics, [Slides](https://faculty.washington.edu/kenrice/HowToGraph2021.pdf)

--- - --

## 原则 2：准确传达信息

#### Bad 

```stata
sysuse "nlsw88.dta"
graph dot wage,   ///
   over(industry) ///
   over(collgrad)    
```


![bg right:60% w:720](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/gr_graph_dot_wage_ind_01.png)

--- - --

#### Better (Q: 如何进一步优化？)

```stata
separate wage, by(collgrad)

#d ;
graph dot (mean) wage0 
          (mean) wage1
   , 
   over(industry) 
   subtitle("hourly wage ($)") 
   legend(
     order  
     (1 "College" 2 "NonColl") 
      ring(0) pos(5) row(2) box);
#d cr
```

![bg right:60% w:720](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/gr_graph_dot_wage_ind_02.png)


--- - --

## Example

<br>

![bg right:60% w:720](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20241221230447.png)

> Source: [Kwon](https://doi.org/10.1257/aer.20220621) et al. ([2024](https://www.nber.org/system/files/working_papers/w32002/w32002.pdf), [AER](https://www.aeaweb.org/doi/10.1257/aer.20220621.appx), [Rep](https://doi.org/10.3886/E197985V1)), Figure IA3.   
   
> 注：此图展示了美国一级行业中，按资产排名前 1% 的企业占总企业资产的比例变化。红色空心菱形表示 2010 年代相较于 1970 年代的比例，蓝色实心圆点表示 1970 年代相较于 1930 年代的比例。行业按照 1970 年代至 2010 年代间的变化幅度排序。
<!-- > Kwon, Spencer Y., Yueran Ma, and Kaspar Zimmermann. **2024**. \"100 Years of Rising Corporate Concentration.\" American Economic Review, 114 (7): 2111–40. DOI: 10.1257/aer.20220621 [Link](https://doi.org/10.1257/aer.20220621), [PDF](https://www.nber.org/system/files/working_papers/w32002/w32002.pdf), [-Replication-](https://doi.org/10.3886/E197985V1), [-Appendix-](https://www.aeaweb.org/doi/10.1257/aer.20220621.appx), [Google](https://scholar.google.com/scholar?q=100%20Years%20of%20Rising%20Corporate%20Concentration) -->

--- - --

## 原则 3：不要扭曲事实


--- - --

## 原则 4：确保有可比性 - 坐标的使用 (1) - bad

<br>

![20241120174656](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20241120174656.png)

--- - --

## 原则 4：确保有可比性 - 坐标的使用 (2) - better

<br>

![20241120174735](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20241120174735.png)

--- - --

## 原则 4：确保有可比性 - 颜色的使用

![20241120174241](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20241120174241.png)

> Source: Rice, K., 2021, Communicating using graphics, [Slides](https://faculty.washington.edu/kenrice/HowToGraph2021.pdf)

--- - --

- [查验颜色对比度](https://webaim.org/resources/contrastchecker/)

- Stata: [绘图模版](https://www.lianxh.cn/search.html?s=%E6%A8%A1%E6%9D%BF)，[配色](https://journals.sagepub.com/doi/pdf/10.1177/1536867X1801800402)
  - Jann, B. (2018). Color Palettes for Stata Graphics. The Stata Journal, 18(4), 765–785. [Link](https://journals.sagepub.com/doi/10.1177/1536867X1801800402), [PDF](https://journals.sagepub.com/doi/pdf/10.1177/1536867X1801800402), [Google](<https://scholar.google.com/scholar?q=Color Palettes for Stata Graphics>).
- R: [R 配色](https://r-graph-gallery.com/38-rcolorbrewers-palettes.html), []() &rarr; [Example](https://colorbrewer2.org/#type=sequential&scheme=Reds&n=3)

--- - --

### 原则 5：选择合适的图形种类

<center>

![h:300](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20241120223638.png)

![h:300](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20241120223800.png)

</center>

--- - --

### 原则 6：简洁-直奔主题

<center>

![h:500](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20241120224122.png)

</center>

> Source: [6 Tips for Creating Effective Data Visualizations](https://blog.csgsolutions.com/6-tips-for-creating-effective-data-visualizations)

--- - --

### 建议：黑白和彩色模式兼顾

<br>

<br>

![bg right:60% w:720](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20241221232333.png)

> Source: [Kwon](https://doi.org/10.1257/aer.20220621) et al. ([2024](https://www.nber.org/system/files/working_papers/w32002/w32002.pdf), [AER](https://www.aeaweb.org/doi/10.1257/aer.20220621.appx), [Rep](https://doi.org/10.3886/E197985V1)), Figure IA12.   
   

--- - --
<!-- backgroundColor: #C1CDCD -->

# 4. 可视化工具

---
<!-- backgroundColor: #FFFFF9 -->

## 4.1 编程工具

<br>

- Python 
- R
- Stata
- Matlab
- ……

---

### Stata

- **适合人群**：学术研究。

- **图表类型**：[**[G-2]** graph](https://www.stata.com/manuals/g-2graph.pdf)
  - `twoway`：生成散点图、折线图等基础图表。[**[G-2]** graph twoway](https://www.stata.com/manuals/g-2graphtwoway.pdf)
  - `histogram`, `kdensity`：直方图，密度函数等 [**[G-2]** graph other](https://www.stata.com/manuals/g-2graphother.pdf)
  - `graph bar/pie`：生成条形图和饼图 [**[G-2]** graph twoway](https://www.stata.com/manuals/g-2graphtwoway.pdf)
  - `marginsplot`：交乘项、非线性关系的边际效应可视化
  - `coefplot`：回归结果可视化
  - 选项：[**[G-3]** twoway options](https://www.stata.com/manuals/g-3twoway_options.pdf)
  - [Stata 绘图：推文合集](https://www.lianxh.cn/search.html?s=%E7%BB%98%E5%9B%BE)
- Books
  - **Mitchell M. N.** (2021). *Interpreting and Visualizing Regression Models Using Stata* (2nd ed.). Stata Press. [Link](https://www.stata.com/bookstore/interpreting-visualizing-regression-models/). [-Online preview-](https://www.stata-press.com/books/preview/ivrm-preview.pdf). 
  - **Mitchell M. N.** (2022). *A Visual Guide to Stata Graphics* (4th ed.). Stata Press. [Link](https://www.stata.com/bookstore/visual-guide-to-stata-graphics/). [-PDF-](https://ia800308.us.archive.org/33/items/a-visual-guide-to-stata-graphics-2022/A%20Visual%20Guide%20to%20Stata%20Graphics%20%282022%29.pdf). 
--- - --

### Python

- **适合人群**：熟悉编程的用户，尤其是数据科学家和工程师。

- **主要库**：
  - **[Matplotlib](https://matplotlib.org/)**：功能强大但语法复杂，适合基础绘图和高度定制。
  - **[Seaborn](https://seaborn.pydata.org/)**：基于 Matplotlib，简化了统计学可视化，适合数据探索性分析。
  - **[Plotly](https://plotly.com/python/)**：支持交互式图表，特别适合仪表盘和动态可视化。
  - **[Bokeh](https://bokeh.org/)**：适合交互式可视化，支持大规模数据集的实时处理。
  - **[Altair](https://altair-viz.github.io/)**：基于 Vega-Lite 的高级可视化库，语法简洁，适合快速生成高质量图表。

---

### R

- **适合人群**：统计学家和需要进行复杂统计可视化的研究者。
- [Top R Graph Examples](https://r-graph-gallery.com/best-r-chart-examples.html)
- **主要库**：[The best R packages for data visualization](https://r-graph-gallery.com/best-dataviz-packages.html)
  - **[ggplot2](https://ggplot2.tidyverse.org/)**：基于图层语法的可视化工具，功能全面，尤其适合科研论文和报告。
  - **[tidyplots](https://github.com/jbengler/tidyplots_paper/tree/master)**：未来替代 `ggplot2` 的绘图包，语法简洁，功能强大。[PDF](https://www.biorxiv.org/content/10.1101/2024.11.08.621836v1.full.pdf)  
  - **[Shiny](https://shiny.rstudio.com/)**：支持构建交互式 Web 应用，可用于动态可视化结果展示。
  - **[plotly](https://plotly.com/r/)**：为 R 提供交互式图表支持，适合仪表盘和动态可视化。
  - **[lattice](https://cran.r-project.org/web/packages/lattice/index.html)**：基于公式语法的可视化工具，适合高维数据展示。
  - **[highcharter](https://jkunst.com/highcharter/)**：基于 Highcharts 的 R 接口，适合创建高度交互的图表。
  - **[DT](https://rstudio.github.io/DT/)**：基于 DataTables 的 R 包，用于创建交互式表格展示数据。
  - **[leaflet](https://rstudio.github.io/leaflet/)**：用于创建交互式地图，可与地理数据可视化结合。

--- - --
### R - Books
- **${\color{red}{R4DS}}$** | **Wickham H.**, and G. Grolemund. 2023. **R for Data Science**. O’Reilly Media. [在线阅读](https://www.tidyverse.org/blog/2023/07/r4ds-2e/)，[Solutions](https://mine-cetinkaya-rundel.github.io/r4ds-solutions/)
- **Wickham H.**, D. Navarro, & T. L. Pedersen (2016). *ggplot2: Elegant Graphics for Data Analysis* (3rd ed.). Springer. [Link](https://doi.org/10.1007/978-3-319-24277-4). [-Online read-](https://ggplot2-book.org/), [-GitHub-](https://github.com/hadley/ggplot2-book).
- Claus O. Wilke (2019). *Fundamentals of Data Visualization: A Primer on Making Informative and Compelling Figures*. O'Reilly Media. ISBN: 978-1-492-03108-6. [-Online read-](https://clauswilke.com/dataviz/), [-GitHub-](https://github.com/clauswilke/dataviz). 介绍了各种学术类图形的绘制方法，R 代码。例举了各类「urgly/Bad」图形的范例，以便我们知道如何绘制干净、漂亮的图形。

---

## 4.2 可视化-专业软件

### Tableau：[https://www.tableau.com](https://www.tableau.com)

- **优点**：直观拖拽操作、支持复杂交互、连接多种数据源。
- **适用场景**：企业报告、仪表盘设计、商业数据展示。
- **交互功能**：支持过滤器、下钻分析。



### Power BI：[https://powerbi.microsoft.com/](https://powerbi.microsoft.com/)

- **优点**：与微软生态深度集成，适合 Excel 用户。
- **适用场景**：企业业务分析、动态报告生成。
- **功能特色**：强大的数据建模能力，支持实时数据流。


---

## 4.3 在线工具

### Datawrapper

- **特点**：无需编程，操作简单，适合快速生成新闻级可视化
- 官网：[https://www.datawrapper.de/](https://www.datawrapper.de/)

### Flourish

- **特点**：丰富的交互图表，动态可视化、嵌入网页展示。
- 官网：[https://flourish.studio/](https://flourish.studio/)，[Examples](https://flourish.studio/examples/)

### GIS 专用工具

- **ArcGIS**：地理信息系统，适合复杂地图绘制。
  - 官网：[https://www.esri.com/en-us/arcgis/products/index](https://www.esri.com/en-us/arcgis/products/index)
- **QGIS**：开源替代，适合预算有限的项目，[https://qgis.org/zh_Hans/site/](https://qgis.org/zh_Hans/site/)



---

## 选择建议

- **交互性需求**：选择 Tableau、Power BI 或 Plotly。
- **科研需求**：优先选择 ggplot2、Matplotlib 或 Stata。
- **快速制图**：Flourish 或 Datawrapper。



--- - --
<!-- backgroundColor: #C1CDCD -->


# 5. 借助 AI 绘图

- 工具
  - ChatGPT：<https://chatgpt.com/>
  - Kimi Chat: <https://kimi.moonshot.cn/chat>

- 例子
  - 例 1：[用 ChatGPT 绘制密度函数图](https://chatgpt.com/share/7ed51dad-8a35-4e82-bf9b-092ca1631f52)

  - 例 2：[绘制面板平滑转换模型的转换函数](https://github.com/arlionn/UseChatGPT/blob/main/Examples/Stata_graph_PSTR_trans_function.md)

--- - --
<!-- backgroundColor: #FFFFF9 -->
#### 例 1：用 ChatGPT 绘制密度函数图

> :cat: [原始对话](https://chatgpt.com/share/7ed51dad-8a35-4e82-bf9b-092ca1631f52)

![](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20240630014852.png)

--- - --

#### **例 2：** 绘制面板平滑转换模型的转换函数

> :cat: [原始对话](https://github.com/arlionn/UseChatGPT/blob/main/Examples/Stata_graph_PSTR_trans_function.md)

<br>

$$
y_{it}=\mu_i+\beta_0'x_{it}+\beta_1'x_{it}\cdot g(q_{it};\gamma,c)+u_{it}  \quad(1)
$$

转换函数：
$$
g(q_{it};\gamma,c) = \frac{1}{1+\exp\left[-\gamma(q_{it}-c)\right]} \quad (2)
$$

### 速度参数
- 当 $\gamma = 0$ 时，$g(q_{it};\gamma,c) = 0.5$，模型为线性模型，无状态转换。
- 当 $\gamma \to \infty$ 时，$g(q_{it};\gamma,c)$ 迅速从状态 1 转换到状态 2，类似于跳跃，与 Hansen (1999) 的面板门槛模型相似。
- 当 $\gamma = 0.3$ 和 $\gamma = 1$ 时，表示状态转换的平滑程度。

--- - --

![](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/PSTR_01_gamma.png)


--- - --

![](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/PSTR_02_c_location.png)


--- - --
<!-- backgroundColor: white -->

<center>

# 谢&emsp; 谢

<br>
<br>

## 连享会 


### [lianxh.cn](https://www.lianxh.cn)

</center>
