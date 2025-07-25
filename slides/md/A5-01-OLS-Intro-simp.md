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
#header: lianxh.cn
#header: '[连享会](https://www.lianxh.cn)'

### ------------------- 页脚 (备选的用 '#' 注释掉)
footer: '连享会&nbsp;|&nbsp;[lianxh.cn](https://www.lianxh.cn)&nbsp;|&nbsp;[B站](https://space.bilibili.com/546535876)&nbsp;|&nbsp;[课程](https://www.lianxh.cn/KC.html)'
#footer: '![20230202003318](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20230202003318.png)'
---

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
  font-size: 20px; 
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
  content: attr(data-marpit-pagination) '/' attr(data-marpit-pagination-total); 
}
header,
footer {
  position: absolute;
  left: 50px;
  right: 50px;
  height: 25px;
}
section footer{
    margin-left: 10px !important;
}

/* 这个设置适合于所有的背景图片*/
section figure{
    margin-right: 10px !important;
}

/* 这个设置适合于左侧的背景图片 */
section figure:first-child{
    margin-left: -10px !important;
}
</style>

<!-- backgroundColor: #FFFFF9 -->


<!--顶部文字-->
[lianxh.cn](https://www.lianxh.cn/news/46917f1076104.html) 

<br>

<!--封面图片-->
<!-- ![bg right:50% w:400 brightness:. sepia:50%](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20220722114227.png)  -->

![bg right:50% brightness:. sepia:50% w:580](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/%E5%9B%BE%E7%89%872_20191213104808.png)

<!--幻灯片标题-->
# 线性回归分析 (1)

- 条件期望函数 CEF 
- 基本假设
- 估计方法
- 系数含义
- SE

<br>

<!--作者信息-->
[连玉君](https://www.lianxh.cn) (中山大学)
arlionn@163.com

<br>

<!-- 
Notes: 
1. 选中一段文本，按快捷键 'Ctrl+/' 可以将其注释掉；再次操作可以解除 
2. header, footer 后面的文本需要用单引号引起来，否则会有语法错误
3. '#size: 16:9' 不能写为 'size:16:9'，即 'size:' 后要有一个空格
-->


--- - --
<!-- backgroundColor: white -->
### 参考资料
  - Hansen B E . 2021. **Econometrics**. Princeton University Press. [Data and Contents](https://www.ssc.wisc.edu/~bhansen/econometrics/), [PDF](https://www.ssc.wisc.edu/~bhansen/econometrics/Econometrics.pdf), chap 2-5 &#x1F34E; 
  - Rubinstein, Y. 2016, Slides, [The Regression Tool](https://yonarubinstein.files.wordpress.com/2016/07/the-regression-tool1.pdf)
  - Chapter 2, Linear Models for Continuous Data, [PDF](https://data.princeton.edu/wws509/notes/c2.pdf), PDF 讲义
  - James, G., D. Witten, T. Hastie, R. Tibshirani. An introduction to statistical learning[M]. Springer, 2013. [PDF](https://link.springer.com/content/pdf/10.1007/978-1-0716-1418-1.pdf)
  - Stewart, B., 2020. Simple Linear Regression, [Slides](https://scholar.princeton.edu/sites/default/files/bstewart/files/lecture5_handout2020.pdf)
  - Causal Inference for The Brave and True, [-Link-](https://matheusfacure.github.io/python-causality-handbook), 从因果推断的角度进行解释，尤其是控制变量的选
--- - --
## 计量模型的设定思路：${\color{red}{f(\cdot)}}$ —— 模型设定形式

![w:900](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20221209091907.png)


--- - --

### 核心思想

- 从 $y$ 的分布特征入手
  
- 确定分析的重点：均值，中位数，还是尾部、波动率、取值区间？

- 设定 $y = f(x, \beta)$ 的函数形式
  - 变量筛选
  - 模型筛选
- 统计推断：**Population** &rarr; **Sample**
  - 估计参数 $\beta$ &rarr; 假设检验
- 应用：解释 / 因果推断 / 预测 / 可视化

--- - --
<!-- backgroundColor: #C1CDCD -->

# 1. 线性模型与 OLS 估计

- 模型设定
- 条件期望
- OLS 估计

--- - --
<!-- backgroundColor: white -->

## 1.1 条件期望函数 (CEF)

> Mroz, T. A., **1987**, The sensitivity of an empirical model of married women's hours of work to economic and statistical assumptions, **Econometrica**, 55 (4): 765-799. [-Link-](https://doi.org/10.2307/1911029), [-PDF-](https://sci-hub.ren/10.2307/1911029), [PDF2](https://juanmuro.web.uah.es/mroz87.pdf)


![w:700](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/%E5%9B%BE%E7%89%872_20191213104808.png)

--- - --

![bg left:50% w:670](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/gr_OLS_CEF_edu_01_scatter.png)


>条件期望 CEF
$$
\mathbb{E}[Y| X=x]=m(x)
$$
- eg. $\mathbb{E}[Wage| Educ=12]=m(12)$
  - `sum wage if educ==12` 
  - `reg wage if educ==12`
>建模思路：考虑误差

$$
\begin{aligned}
Y &=m(X)+e \\
\mathbb{E}[e| X] &=0 \\
\mathbb{E}\left[e^{2}|X\right] &=\sigma^{2}(X)
\end{aligned}
$$

>实证模型
$$
\mathbb{E}[Wage\,|\,Edu]= m(Edu)
$$



--- - --

![bg left:50% w:670](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/gr_OLS_CEF_edu_02_lfit_qfit.png)

>实证模型
$$
\mathbb{E}[Wage\,|\,Edu]= m(Edu)
$$

>模型设定：

$
(1)\ \  Wage_i = \alpha + \beta Edu_i + e_i
$

$
(2)\ \ Wage_i = \alpha + \beta_1 Edu_i + {\color{red}{\beta_2 Edu_i^2}} + e_i
$

$
(3)\ \ {\color{red}{\text{ln}}}(Wage_i) = \alpha + \beta Edu_i + e_i
$

$
(4)\ \ Wage_i = \alpha + \beta Edu_i + {\color{red}{\gamma D + \theta D\!\times\!Edu_i}} + e_i
$
&emsp;&emsp;  其中，$D = \mathbf{1}(Edu\!>\!16)$

:dog: 切记，上述模型分析的都是 **条件期望** (CEF)。

:cat: 扩展：条件概率、条件中位数、条件分位数

<!--  
--- - --

### CEF 和 线性回归

Regression estimates provide a valuable baseline for almost all empirical research because regression is tightly linked to the CEF, a natural summary of empirical relationships.
Three reasons why vector of population regression coefficients of interest:
(1) The Linear CEF Theorem: If the CEF is linear, the population regression function is it. (limited empirical relevance, special cases only)
(2) The Best Linear Predictor Theorem: The function $X_{i}^{\prime} \beta$ is the best linear predictor of $Y$ given $X$, in a MMSE sense.
(3) The Regression CEF Theorem: The function $X_{i}^{\prime} \beta$ provides the MMSE linear approximation to $E\left[Y_{i} \mid X_{i}\right]$
- Angrist and Pischkes tavourıte way to motivate regression, to extent distribution of Y focus of interest (rather than individual prediction).

--- - --


## replication
> Fan, Y., J. Yi, J. Zhang, **2021**, Rising intergenerational income persistence in china, **American Economic Journal: Economic Policy**, 13 (1): 202-230. [-Link-](https://doi.org/10.1257/pol.20170097), [-PDF-](https://sci-hub.ren/10.1257/pol.20170097), [PDF2](https://www.aeaweb.org/doi/10.1257/pol.20170097.appx), [Replication](https://doi.org/10.3886/E110861V1)

- $ln(y)$，工资弹性估计
- 交乘项、固定效应

This paper documents an increasing intergenerational income persistence in China since economic reforms were introduced in 1979 . The intergenerational income elasticity increases from $0.390$ for the 1970-1980 birth cohort to $0.442$ for the 1981-1988 birth cohort; this increase is more evident among urban and coastal residents than rural and inland residents. We also explore how changes in intergenerational income persistence is correlated with market reforms, economic development, and policy changes.


--- - --

> Goldberg, J., **2016**, Kwacha gonna do? Experimental evidence about labor supply in rural malawi, **American Economic Journal: Applied Economics**, 8 (1): 129-149. [-Link-](https://doi.org/10.1257/app.20130369), [-PDF-](https://sci-hub.ren/10.1257/app.20130369), [Replication](http://doi.org/10.3886/E116331V1)

I use a field experiment to estimate the wage elasticity of employment in the day labor market in rural Malawi. Once a week for 12 consecutive weeks, I make job offers for a workfare-type program to 529 adults. The daily wage varies from the tenth to the ninetieth percentile of the wage distribution, and individuals are entitled to work a maximum of one day per week. In this context (the low agricultural season), 74 percent of individuals worked at the lowest wage, and consequently the estimated labor supply elasticity is low (0.15), regardless of observable characteristics.

--- - --

- 重点参考：
  - Hastie - 2021 书配套 Slides, Linear Regression. [-Link-](https://hastie.su.domains/lectures.htm), [-PDF-](https://hastie.su.domains/MOOC-Slides/linear_regression.pdf) 
- [Wartoon - 很全面](https://finance.wharton.upenn.edu/~mrrobert/resources/Teaching/CorpFinPhD/Linear-Regression-Slides.pdf)
- [MIT - 稳健性检验-GLM-Lasso 简介](https://www.mit.edu/~6.s085/notes/lecture4.pdf)
- [听清楚](https://github.com/skranz/empecon/blob/main/slides/pdf_handout/ee_3.pdf)


--- - --

## Learn how to run and read regression
- Mechanics: how to estimate the intercept and slope?
- Properties: when are these good estimates?
- Uncertainty: how will the OLS estimator behave in repeated samples?
- Testing: can we assess the plausibility of no relationship $\left(\beta_{1}=0\right)$ ?
- Interpretation: how do we interpret our estimates?

-->

<!-- --- - --

## Regression as a prediction algorithm
- Denote by $\mathbf{X}$ the design matrix. This is the matrix on which we will project $\mathbf{y}$.
- In other words we have an input matrix $\mathbf{X}$ with dimensions $n \times p$ and an output vector $\mathbf{y}$ with dimensions $n \times 1$.
$$
\mathbf{X}=\left(\begin{array}{cccc}
X_{11} & X_{12} & \ldots & X_{1 p} \\
X_{21} & X_{22} & \ldots & X_{2 p} \\
\vdots & \vdots & \vdots & \vdots \\
X_{n 1} & X_{n 2} & \ldots & X_{n p}
\end{array}\right)_{n \times p}
$$
- The $X_{j i}$ denotes the value of characteristic $j$ for individual $i$. -->

--- - --
### 矩阵表示 
- **Example** 假设我们收集到了两个解释变量的数据: `education` 和 `age`，则 $X$ 矩阵定义为：
$$
\mathbf{X}=\left(\begin{array}{cccc}
1 & \text { education }_{1} & \text { age }_{1} & \text { age }_{p}^{2} \\
\vdots & \vdots & \vdots & \vdots \\
1 & \text { education }_{n} & \text { age }_{n} & \text { age }_{n}^{2}
\end{array}\right)_{n \times 4}
$$

- 模型写法：
  $$
  \mathbf{y} = \mathbf{X}\mathbf{\beta} + \mathbf{e}
  $$



--- - --

## 1.2 线性回归模型：假设条件

<br>

> $y_{i}=x_{i}^{\prime} \beta+e_{i}, \quad i=1, \ldots, n$ 
&emsp; &emsp; $x_{i}$ 和 $\beta$ 均为 $k \times 1$ 维；&emsp; 参数个数为： $K=k+1$ &ensp;$\left(\beta\right.$ and $\left.\sigma^{2}\right)$



  - **A1： 参数线性假设。**
  
    - $y = a+ x\beta_1 + z\beta_2 + ({\color{red}{x\times z}})\theta + u$
    - $y = a+ x\beta_1 + {\color{red}{z^{\beta_2}}} + u$ &emsp; NLS：[**[R]** `nl`](https://www.stata.com/manuals/rnl.pdf) 
  - **A2： 随机抽样假设。**
    - 否则，便会存在自选择 ([`etregress`](https://www.stata.com/manuals/teetregress.pdf)) 或样本选择偏误 ([`heckman`](https://www.stata.com/manuals/rheckman.pdf))  
  - **A3：外生性假设。** $\mathbb{E}\left(e_{i} \mid x_{i}\right)=0 \ \Longrightarrow \ \mathbb{E}\left(e_{i}\right)=0$ 
  - **A4：同方差假设。** $\mathbb{E}\left(e_{i}^{2}\right)=\sigma^{2}$

--- - --

## 1.3 最小二乘法

- 模型设定：&emsp; &emsp; $\qquad y_{i} = \alpha + x_{i} \beta + e_{i}$

- 最小化残差平方和 (**RSS**)：
$$RSS(\beta)=\sum_{i=1}^{N}\left(y_{i}-\alpha - x_{i} \beta\right)^{2}$$

- 估计值：
$$\widehat{\alpha} = E(y\,|\, x=0) = \bar{y}\,|\, x=0$$

$$\widehat{\beta} = \frac{\sum_{i=1}^{N} (x_i - \bar{x}) (y_i - \bar{y})}{\sum_{i=1}^{N} (x_i - \bar{x})^2}
$$

&emsp; &emsp; 其中，$\bar{x}$ 和 $\bar{y}$ 分别是 $x$ 和 $y$ 的样本均值。
- 拟合值: $\qquad \widehat{y}_{i} = \hat{\alpha} + x_{i} \hat{\beta}$
- 残差：$\quad\quad\,\,\widehat{e}_i = y_i -\widehat{y}_i$ 

![bg right:55% w:600](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/gr_OLS_sum_of_squares.png)

--- - --

### 矩阵表示 
- 模型设定：
$$\mathbf{y} = \mathbf{X}\mathbf{\beta} + \mathbf{e}$$

- 残差平方和：
$$
R S S(\beta)=(\mathbf{y}-\mathbf{X} \beta)^{\prime}(\mathbf{y}-\mathbf{x} \beta)


$$
- 对 $\beta$ 求一阶偏导数:
$$
\frac{\partial \mathrm{RSS}}{\partial \beta}=-2 \mathbf{X}^{\prime}(\mathbf{y}-\mathbf{X} \beta) = 0
$$

- 求解得到 $\beta$ :
$$
\widehat{\beta}=\left(\mathbf{X}^{\prime} \mathbf{X}\right)^{-1} \mathbf{X}^{\prime} \mathbf{y}
$$

- 残差向量：
$$\widehat{\mathbf{e}} = \mathbf{y} - \mathbf{X}\widehat{\mathbf{\beta}}$$


--- - --

## 1.4 拟合值和残差

<br>

![bg right:70% w:700](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20221230115142.png)


> **Stata dofile**:   
> [点击查看](https://gitee.com/arlionn/PX/wikis/SlidesDofiles/A4_OLS_R1_reg_Fig2_v2.md) 


--- - --
<!-- backgroundColor: white -->

### 拟合值和残差 - 实现

<br>

![bg right:50% w:700](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/gr_OLS_CEF_edu_03_lfit.png)

```stata
. webuse "mroz.dta", clear

. reg wage educ  

. predict wage_hat    // 拟合值
. predict e_hat       // 残差

. scatterfit wage educ  // 散点+拟合线


. regfit  // 拟合方程

  wage = -2.74 + 0.52*educ
         (0.62) (0.05)
  N = 421, R2 = 0.22, adj-R2 = 0.21
```

--- - --

### 残差方差估计 $\hat{\sigma}^2$
$$\qquad y_{i} = \alpha + x_{i} \beta + e_{i}$$

<br>

$$
\hat{\sigma}^2 = \frac{RSS}{n - k}
$$

  $$
  RSS = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = \sum_{i=1}^{n} \hat{e}_i^2
  $$
- $y_i$ 是观察值，$\hat{y}_i$ 是拟合值，$\hat{e}_i$ 是残差。
- **$n$** 是样本量，**$k$** 是回归模型中的参数个数 (包括截距项)。

#### 为什么除以 $n - k$？

模型拟合了 $k$ 个参数（包括截距项），因此自由度减去 $k$，以避免过度拟合。此时，残差方差 $\hat{\sigma}^2$ 是对总体残差方差的无偏估计。

```stata
webuse "mroz.dta", clear
eststo m1: reg lwage educ
eststo m2: reg lwage educ exper 

esttab m1 m2, scalar(N r2 rss) nogap 
```

![bg right:38% w:450](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250107092536.png)


--- - --

## 1.5 二元线性回归的可视化解释

![bg right:40% w:500](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/Fig_OLS_superPlanent_01.png)

> Source: [Hastie-2021](https://hastie.su.domains/MOOC-Slides/linear_regression.pdf)，[3D-vedio](https://www.youtube.com/watch?v=JaMgi4XBjo8)

二元线性回归中，用两个自变量 $X_1$ 和 $X_2$ 来预测因变量 $Y$：

$$
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \varepsilon \quad (1)
$$

<!-- - $\beta_0$ 是截距，表示当 $X_1$ 和 $X_2$ 都为 0 时的预测值。
- $\beta_1$ 和 $\beta_2$ 分别是 $X_1$ 和 $X_2$ 的回归系数，表示每个自变量对 $Y$ 的影响。
- $\epsilon$ 是误差项。 -->

> 可视化解释： 

- 在三维空间中，自变量 $X_1$, $X_2$ 是坐标平面，因变量 $Y$ 是垂直轴
- **超平面** 是拟合的模型，即所有预测值 $\hat{Y}$ 组成的平面。
- **红点** 是数据点，**垂直线** 表示实际值 $Y$ 与预测值 $\hat{Y}$ 的残差。

> 线 &rarr; 平面

给定 $\hat{\beta}_0 = 10$，$\hat{\beta}_1 = 0.5$，$\hat{\beta}_2 = 2$，当 $X_1 = 3$ 时，(1) 式变为：

$$
Y = 10 + 0.5 \times 3 + 2 X_2 + \varepsilon = 11.5 + 2 X_2 + \varepsilon 
$$

相当于，在 $X_1 = 3$ 的位置，沿着平行于 $X_2$ 的方向，垂直于 $\{X_1, X_2\}$ 的平面切一刀，与超平面的相交线。

超平面就是有多组这样的切线构成的。

--- - --
<!-- backgroundColor: #C1CDCD -->

# 2. OLS 估计的性质

OLS 回归模型的统计推断主要集中在参数的显著性检验和模型的整体拟合度。

### OLS 估计量的性质

OLS 估计量具有以下几个重要性质：
- **无偏性（Unbiasedness）**：$E(\hat{\beta}) = \beta$。
- **一致性（Consistency）**：随着样本量趋向无穷大，$\hat{\beta}$ 会收敛于真实值 $\beta$。
  - $\widehat{\beta} \stackrel{p}{\longrightarrow} \beta$ 或 $\widehat{\beta}=\beta+o_{p}(1)$
  
- **最小方差线性无偏估计（BLUE）**：在满足一定条件下，OLS 是最优的线性无偏估计量。

--- - --
<!-- backgroundColor: white -->

## 2.1 估计量的无偏性 [codes](https://gitee.com/arlionn/graph/wikis/dofiles/OLS_unbiased_simulation_v2)

- 单次估计具有随机性 (原因？)，但估计很多次，如 $K=1000$ 次，取它们的均值，$E[\widehat{\beta}]$，可以很大程度上消除随机误差的影响
- 这个均值应该接近真实值：$E[\widehat{\beta}]={\beta}_0$

**MC 模拟分析**
- **S1:** 随机生成一个包含 $N=5000$ 个观察值的样本 (视为 “总体”，Population), 记为 $S_{0}$ 。
  - 数据生成过程: $y=10+0.5 x+e$, 
  - $x$ 和 $e$ 均来自标准正态分布, 彼此独立。
- **S2:** 从 $S_{0}$ 中随机抽取 $n=50$ 个观察值, 形成一组抽样样本 (Sample), 
  - 执行 OLS 估计, 记录 $\widehat{\beta}$ 和 $\operatorname{se}(\widehat{\beta})$
- **S3:** 重复第二步 $K= 1000$ 次 (右图取 $K=10$ 次)，得到 $\widehat{\boldsymbol{\beta}}_j = \{\widehat{\beta}_1, \widehat{\beta}_2, \cdots, \widehat{\beta}_K\}$。

![bg right:50% w:700](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/OLS_unbias_scatter_B10.png)
--- - --

## 2.2 估计量的一致性  [codes](https://gitee.com/arlionn/graph/wikis/dofiles/OLS-consistent-simulation)

**估计量的一致性**：当样本数 $n \rightarrow \infty$ 时, 估计值无限接近于真实值。   
表示为 $\widehat{\beta} \stackrel{p}{\longrightarrow} \beta$ 或 $\widehat{\beta}=\beta+o_{p}(1)$

**MC 模拟分析：**
- **S1**. 随机生成一个包含 $N=100000$ 的总体样本, 记为 $S_{0}$ 。数据生成过程：$y=10+0.5 x+e$, 其 中, $x$ 和 $e$ 均来自标准正态分布, 彼此独立。
- **S2**. 从 $S_{0}$ 中随机抽取 $n=10$ 个观察值, 视为一组抽样样本 (sample), 对其执行 OLS 估计, 记录 $\widehat{\beta}$ 和 $\operatorname{se}(\widehat{\beta})$ 。
- **S3**. 重复第二步, 但每次抽取的样本数 $n$ 不断增加，$n=10, 20, ..., 30000$。

![bg right:55% w:650](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/OLS_consis_b_se.png)




--- - --
<!-- backgroundColor: #BDFFF9 -->

# 3. 系数的标准误

- 同方差假设下的 SE
- 异方差稳健型的 SE
- 聚类调整后的 SE

--- - --
<!-- backgroundColor: white -->



> Source: 刘潍嘉, 2023, [Stata：线性回归、OLS与标准误](https://www.lianxh.cn/details/1277.html)

## 3.1 回顾

考虑以下线性模型 (矩阵形式) ，并假设所有经典 LR 假设成立：

$$
y=X \beta+e, \quad E(Xe) = 0
$$

OLS 估计量 $\hat{\beta}$ 为：

$$
\hat{\beta}_{O L S}=\left(X^{\prime} X\right)^{-1} X^{\prime} y
$$

估计值 $\hat{\beta}$ 和真实 $\beta$ 之间的关系：

$$
\begin{aligned}
\hat{\beta}_{O L S} & =\left(X^{\prime} X\right)^{-1} X^{\prime}(X \beta+e) \\
& =\left(X^{\prime} X\right)^{-1} X^{\prime} X \beta+\left(X^{\prime} X\right)^{-1} X^{\prime} e \\
& =\beta+\left(X^{\prime} X\right)^{-1} X^{\prime} e
\end{aligned}
$$

简单地说，如果 $E\left(\left(X^{\prime} X\right)^{-1} X^{\prime} e\right)=0$，那么 $\hat{\beta}$ 是无偏的。


--- - --

## 3.2 我们的估计有多精确?

将 $\operatorname{Var}()$ 应用于方程的两边，可得：

$$
\begin{aligned}
\operatorname{Var}\left(\hat{\beta}_{O L S}\right) &=\operatorname{Var}\left(\beta+\left(X^{\prime} X\right)^{-1} X^{\prime} e\right) \\
\operatorname{Var}\left(\hat{\beta}_{O L S}\right) &= \operatorname{Var}(\beta)+\operatorname{Var}\left(\left(X^{\prime} X\right)^{-1} X^{\prime} e\right)
\end{aligned}
$$

重新写为方差协方差矩阵形式：$Var(\hat{\beta}_{OLS})=Var(\beta)+(X^{\prime}X)^{-1}X^{\prime}Var(e)X(X^{\prime}X)^{-1}$

其中，$Var(e)$ 它是一个 $N×N$ 方差协方差矩阵，将样本中所有观察的信息结合起来：

$$
Var(e)=\begin{pmatrix}\sigma_1^2&\sigma_{1,2}&\sigma_{1,3}&\ldots&\sigma_{1,n}\\\sigma_{1,2}&\sigma_{2}^2&\sigma_{2,3}&\ldots&\sigma_{2,n}\\\sigma_{1,3}&\sigma_{2,3}&\sigma_{3}^2&\ldots&\sigma_{3,n}\\\ldots&\ldots&\ldots&\ldots&\ldots\\\sigma_{1,n}&\sigma_{n,2}&\sigma_{n,3}&\ldots&\sigma_{n}^2\end{pmatrix}
$$

<!-- 如何理解？
- 在截面数据中中，虽然我们每次只能观察到一个样本，但从理论上讲，我们观察到的只是该单位众多可能状态之一。在每一个可能状态中，该单位可能会有不同的 $e_i$ 值。因此，如果我们能够看到所有这些状态，就有可能获得单位自身不可观测的方差 $e_i^2$，以及与其他单位的相关性 $\sigma_i^2$。 -->

我们可以做一个变形，用 $Ω$ 替换 $Var(e)$，这样我们就得到了更传统的公式 (**三明治**公式)：

$$
Var(\hat{\beta}_{OLS})=(X^{\prime}X)^{-1}X^{\prime}{\Omega}X(X^{\prime}X)^{-1}
$$

对 $Var(e)$ 施加不同的假设条件，将得到的不同类型的标准误。


--- - --


## 3.3 同方差标准误

- **同方差**：$\sigma_i^2 =\sigma_j^2=\sigma^2$。影响单位 $i$ 的不可观测的误差 $e$ 与影响单位 $j$ 的不可观测误差是完全独立的。
- **无相关性**：$\sigma_{ij} =0 \, (i\neq j)$。对于不可观测的误差，其大小或变化在所有个体中都是一样的。

这将简化矩阵 $Ω$ 为:

$$
\Omega_0
=\begin{pmatrix}\sigma_1^2&\sigma_{1,2}&\sigma_{1,3}&\ldots&\sigma_{1,n}\\\sigma_{1,2}&\sigma_{2}^2&\sigma_{2,3}&\ldots&\sigma_{2,n}\\\sigma_{1,3}&\sigma_{2,3}&\sigma_{3}^2&\ldots&\sigma_{3,n}\\\ldots&\ldots&\ldots&\ldots&\ldots\\\sigma_{1,n}&\sigma_{n,2}&\sigma_{n,3}&\ldots&\sigma_{n}^2\end{pmatrix}
=
\begin{pmatrix}\sigma^2&0&0&\ldots&0\\0&\sigma^2&0&\ldots&0\\0&0&\sigma^2&\ldots&0\\\ldots&\ldots&\ldots&\ldots&\ldots\\0&0&0&\ldots&\sigma^2\end{pmatrix}=\sigma^2I(N)
$$

当然，这也将系数 $\beta$ 的方差-协方差简化为：

$$
Var(\hat{\beta}_{OLS})_0=(X^{\prime}X)^{-1}X^{\prime}\sigma^2I(N)X(X^{\prime}X)^{-1}=\sigma^2(X^{\prime}X)^{-1}
$$


--- - --
<!-- backgroundColor: white -->
#### 同方差图示
#### $\operatorname{Var}\left(u_{i} | \mathbf{X}\right)=\sigma^{2}$

<br>

$
V[\mathbf{u} | \mathbf{X}]=\left[\begin{array}{cccc}
\sigma^{2} & 0  & \ldots & 0 \\
0 & \sigma^{2}  & \ldots & 0 \\
& & \vdots & \\
0 & 0 & \ldots & \sigma^{2}
\end{array}\right] =\sigma^{2} \mathbf{I}
$

<!-- ![bg right:47% w:580](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/Fig_OLS_error_homo_01.png) -->

![bg right:65% w:600](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/OLS-var-beta-homo-001.png)


--- - --
<!-- backgroundColor: white -->

#### $\operatorname{Var}[\widehat{\boldsymbol{\beta}} \mid \mathbf{X}] = \sigma^{2}\left(\mathbf{X}^{\prime} \mathbf{X}\right)^{-1}$ 的含义

<!-- - **OLS** 的系数估计值为：$\widehat{\boldsymbol{\beta}}=\left(\mathbf{X}^{\prime} \mathbf{X}\right)^{-1}\mathbf{X}^{\prime}\mathbf{y}$。只要 $E(\mathbf{X}^{\prime}\mathbf{\varepsilon})=0$，$\widehat{\boldsymbol{\beta}}$ 就是 $\beta$ 的无偏估计。
- 方差为：$\operatorname{Var}\,[\widehat{\boldsymbol{\beta}} \mid \mathbf{X}] = \sigma^{2}\left(\mathbf{X}^{\prime} \mathbf{X}\right)^{-1}$ -->

在 $\sigma^2$ 相同的情况下，

$\operatorname{Var}(\mathbf{X})=\left(\mathbf{X}^{\prime} \mathbf{X}\right)$ 越大，   

$\operatorname{Var}\,[\widehat{\boldsymbol{\beta}} \mid \mathbf{X}]$ 越小，系数的估计越准确  

> 在线模拟 OLS 的性质  &#x1F449;  [点击](https://econometricsbysimulation.shinyapps.io/OLS-App/), [推文](https://www.lianxh.cn/news/d4fd7a262be49.html)

```stata
*-simulation 
clear
set obs 20
set seed 135 
gen u  = rnormal()
gen x1 = rnormal(0,0.5)
gen x2 = rnormal(0,2)
gen y1 = 2 + 0.6*x1 + u
gen y2 = 2 + 0.6*x2 + u

twoway (scatter y1 x1, mcolor(blue)  ms(+)) ///
       (scatter y2 x2, mcolor(green) ms(oh)) ///
       (lfitci  y1 x1, clcolor(blue)  fcolor(blue%20)) ///
       (lfitci  y2 x2, clcolor(green) fcolor(green%20))
```

![bg right:57% w:700](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/Fig_OLS_se_beta_03.png)


--- - --


## 3.4 异方差稳健标准误

- 保留 **无相关性**：$\sigma_{ij} =0 \, (i\neq j)$ 假设；
- 放松 **同方差**：$\sigma_i^2 =\sigma_j^2=\sigma^2$ 假设，此时 $\sigma_i^2\neq\sigma_j^2$。


这并不意味着在每个个体的方差都不相同，只是它们可能不同。此时，$Ω$ 矩阵可以简化为：

$$
\Omega_1 =
\begin{pmatrix}
\sigma_1^2 & 0 & 0 & \ldots & 0 \\
0 & \sigma_2^2 & 0 & \ldots & 0 \\
0 & 0 & \sigma_3^2 & \ldots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \ldots & \sigma_n^2
\end{pmatrix}
$$


![bg right:45% w:600 OLS-var-beta-het-002](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/OLS-var-beta-het-002.png)


--- - --
<!-- backgroundColor: white -->

### Example: $\operatorname{Var}\left(u_{i} \mid \mathbf{X}\right)=\sigma_{{\color{red}{i}}}^{2}$ Heteroskedasticity

<br>

<br>

![w:700](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20221230100410.png)

![bg right:50% w:600](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/gr_OLS_CEF_edu_03_lfit.png)


--- - --

## 3.5 一维聚类标准误

- 假设 1：允许 **组内相关**：$\sigma_{i,j}\neq 0 \, \, \, \text{if}\,\, g(i)=g(j)$；但组间不相关
- 假设 2：允许 **异方差**：$\sigma_i^2\neq\sigma_j^2$。


例子：

- 家庭成员之间：生活习惯、家风等的存在，导致他们的不可观测变量会有相关性；
- 同学之间：同伴效应、学校的教学风格等，导致……；
- 同一个行业的公司；同一家公司的各个年度；……

此时，$Ω$ 矩阵是 **分块对角矩阵**，主对角线上的分块元素不为零 $(\sum_{j} \neq 0)$，对角线以外的所有元素都为零：

$$
\Omega_2=\left(\begin{array}{ccccc}
\sigma_1^2 & \sigma_{1,2} & 0 & \ldots & 0 \\
\sigma_{1,2} & \sigma_2^2 & 0 & \ldots & 0 \\
0 & 0 & \sigma_3^2 & \ldots & \sigma_{3, n} \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & \sigma_{3, n} & \ldots & \sigma_n^2
\end{array}\right)=\left(\begin{array}{cc}
\Sigma_1 & 0 \\
0 & \Sigma_2
\end{array}\right)
$$

- 具体计算方法参见：[Stata：聚类调整后的标准误-Cluster-SE](https://www.lianxh.cn/details/155.html)


--- - --

![w:900](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/gr_OLS_cluster_SE_1way_combine.png)


> 图中蓝色的方块表示我们允许同一组或聚类中的观察值之间存在一些非零相关性。这意味着，我们也允许主对角线上的所有元素不为零，这就是为什么聚类标准误差也对异方差性具有稳健性。


--- - --

## 3.6 二维聚类标准误差

个体之间的关联可能有多个来源

- 多重社会角色：家庭成员 + 学生：`reghdfe y x, cluster(family class)`
- 一家公司会与其行业竞争对手有关联；也会与其同属于一个城市的其他公司有关联
  - `reghdfe ROE Lev, cluster(industry city)`

**数学表述：** 定义函数 $g_h()$，它表示在集合 $h$ (聚类变量) 中一个个体属于哪个群体，如果 $i$ 和 $j$ 没有以任何方式连接 (基于聚类变量)，则 $gg(i,j)$ 的值为零，否则为 1。如果 $gg(i,j)=0$，则 $\sigma_{ij}=0$。

$$
gg(i,j)=0 \;\; \text{~if~} \forall h:g_h(i)\neq g_h(j) \;\; \text{and~1~otherwise}
$$

因此，$Ω$ 矩阵将不再是块对角线，因为只有主对角线 (和块对角线) 之外的元素将不为零。

$$
\Omega_3=\begin{pmatrix}\sigma_1^2&\sigma_{1,2}&0&\ldots&\sigma_{1,n}\\\sigma_{1,2}&\sigma_2^2&\sigma_{2,3}&\ldots&0\\0&\sigma_{2,3}&\sigma_3^2&\ldots&\sigma_{3,n}\\\cdots&\cdots&\cdots&\cdots&\cdots\\\sigma_{1,n}&0&\sigma_{3,n}&\ldots&\sigma_n^2
\end{pmatrix}
$$

--- - --

![w:800](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/gr_OLS_cluster_SE_2way.png)

> 由于是二维聚类，阴影块会有重叠。


--- - --
<!-- backgroundColor: #FFFFF9 -->

## 3.7 Stata 实操

```stata
  sysuse "nlsw88.dta", clear
  global x "age ttl_exp  union collgrad"

  //去除缺失值；以保证样本数一致
  qui reg wage $x i.industry i.occupation
  keep if e(sample) 
  
  reg wage $x            // 同方差
    est store m1
  reg wage $x, robust    // 异方差
    est store m2  
  *- 一维 clustered S.E.
  reg wage $x, vce(cluster industry) 
    est store m3
  *- 二维 clustered S.E.
  reghdfe wage $x, noabsorb ///
    cluster(industry occupation)
    est store m4
  
*-对比
local m  "m1 m2 m3 m4"
local mt "OLS Robust Clus1 Clus2"
esttab `m', mtitle(`mt') s(N r2)    ///
  b(%4.3f) se(%6.4f) brackets nogap ///
  star(* 0.1 ** 0.05 *** 0.01) 
```

![bg right:50% w:620](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250107181700.png)

--- - --

## 3.8 聚类标准误常见问题 (1)

> Q1： 什么时候需要使用聚类调整？

- 如果 **抽样过程** 和 **分配机制** 都没有进行过聚类，即完全针对个体进行随机抽样，则无需进行聚类调整 (Abadie et al., 2017)。

> Q2: 一维聚类和二维聚类如何选择？二维聚类一定比一维聚类更优吗？

- 更稳健的标准误会降低统计推断的偏差，但同时也会使方差增大，使结果更加不显著，增大犯第二类错误的概率 (Thompson, 2011)。因此，如何在二者之间进行权衡、选择何种聚类方式则应当根据具体的数据结构和逻辑来进行判断。

> Q3：在哪个层面上进行聚类？

- 理论分析。你认为干扰项里包括哪些因素，这些因素如何引起观察值之间的关联？
- 以模型中维度最广的虚拟变量为准。

> Q4: 进行聚类调整后， t 值达到了大样本条件下的临界值，但 p 值却未达到相应的显著性水平，这是何种原因？如 t 值为 1.67，但 p 值却大于 0.1 。

- 由于计算 p 值的公式中其中一个参数为自由度，而聚类调整会影响到模型的自由度，故而会影响到最终计算得到的 p 值。

--- - --

## 3.8 聚类标准误常见问题 (2)

> Q5： Fixed Effect 和 cluster 的区别何在？如果控制了企业固定效应，还需要在企业层面进行了聚类标准误调整吗？。

- 企业固定效应是控制了企业不随时间变化的特征，而企业层面的 cluster 调整则是认为误差项在企业层面存在相关性。

> Q6： 聚类稳健标准误回归中，聚类只有20个，对结果是否有影响？聚类是否要不少于 50 时，使用聚类稳健标准误才有效？

- 是这样的。否则聚类标准误无效。详见 [Problem with small number of clusters using reghdfe and vce suboptions](https://www.lianxh.cn/details/statalist.org/forums/forum/general-stata-discussion/general/1487985-problem-with-small-number-of-clusters-using-reghdfe-and-vce-suboptions)、[How misleading are clustered SEs in designs with few clusters?](https://declaredesign.org/blog/2018-10-16-few-clusters.html)、[Beware of studies with a small number of clusters](https://blogs.worldbank.org/impactevaluations/beware-of-studies-with-a-small-number-of-clusters)。

> Q7：二维 cluster 修正标准误，是不是只在固定效应中使用？

- 随机效应和混合效应模型也可以使用，详见 `vcemway` 命令。

> Q8： 为什么换了 cluster 对象，系数也变了？

- 无论对标准误作何处理，该变的只有标准误，系数是不该变。如果发现调整 cluster 对象系数改变，很可能是样本发生改变。如 cluster(id) 和 cluster(industry) 不同的话，和可能是 id 或 industry 存在缺失值。

--- - --

## 参考资料
- 总览：[连享会 - 标准误](https://www.lianxh.cn/search.html?s=%E6%A0%87%E5%87%86%E8%AF%AF)
- 杨鑫, 秦利宾, 连玉君, 2020, [Stata：聚类调整后的标准误-Cluster-SE](https://www.lianxh.cn/details/155.html), 连享会 No.155.
- 刘潍嘉, 2023, [Stata：线性回归、OLS与标准误](https://www.lianxh.cn/details/1277.html), 连享会 No.1277.

- [Stata：标准误！标准误！](https://www.lianxh.cn/news/e365187a50dc3.html)
- [Stata：聚类标准误的纠结](https://www.lianxh.cn/news/c9dbc1acea75a.html)
- [Stata：聚类调整后的标准误-Cluster-SE](https://www.lianxh.cn/news/a7a8e613b2699.html) 
- [Stata：面板聚类标准误-自动确定最优聚类层级和数量-xtregcluster](https://www.lianxh.cn/news/31be9ab09c5ff.html)
- [倍分法(DID)的标准误：不能忽略空间相关性](https://www.lianxh.cn/news/08f4a7d5ddb4f.html)


--- - --

### cluster SE 参考文献 
- De Chaisemartin, C., & Ramirez-Cuellar, J. (2024). At What Level Should One Cluster Standard Errors in Paired and Small-Strata Experiments? (Version 10). arXiv. [Link](https://doi.org/10.48550/arXiv.1906.00288) (rep), [PDF](https://arxiv.org/pdf/1906.00288.pdf), [Google](<https://scholar.google.com/scholar?q=At What Level Should One Cluster Standard Errors in Paired and Small-Strata Experiments? (Version 10)>).
- Abadie, A., Athey, S., Imbens, G. W., & Wooldridge, J. M. (2023). When Should You Adjust Standard Errors for Clustering? The Quarterly Journal of Economics, 138(1), 1–35. [Link](https://doi.org/10.1093/qje/qjac038) (rep), [PDF](https://watermark.silverchair.com/qjac038.pdf?token=AQECAHi208BE49Ooan9kkhW_Ercy7Dm3ZL_9Cf3qfKAc485ysgAAA0wwggNIBgkqhkiG9w0BBwagggM5MIIDNQIBADCCAy4GCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMijDzL_V-up7VijuCAgEQgIIC_3tVupQGsy_ODJ-LNpZd1fvZ8xGLHUJzknohJ3aAwH9JZOw7h36cwsBzCGapnR6G754K3Ai4wScc9w82qsoc2PbRZQqQdd2A1tZNIg6gFwtQ6yJpRosqs-hnZ3-jwFv4vEwdWwxKePzhtl6H7p91YO0Yk8gKP5qzpi2VZhU6OVzBfz8cnGNp_cfGLTAlWxGQsmseGYbgMaWEDtrIRtyfIV8CppLLxgllT5nDcmB2P1k7c1h75o0dNjLyTRLOufEFo_QzxUUmHEETTVDKLXHDbgyykPF6FECWol6Yx5T5QhTJi-DXeQ08j0pUfHsWTTwIrEL82m60bMPi4IDplo-Cltmey07NJTwP1W6WMryI9Iz5AhgYGYHn-Z9wXEPliLoRXgIiX7RO0M-R1wnN_8SMukcdKtW1rKcKVhYp978P32v-Gi62AiVbLEFteNuyXXwARLcmaEEoVxx_7qnmsj8FlW0mIYTYBauPKPE7wA1D83yKHY8A8ghKBbp-74q655drE7ct5i6Ucx_97UyukcmJtZJdV1SzOOiQEKperSnrWfW6-CVFsd5sI5c0XElgz0AzO8NqoivKL9ld-SXzmulvHqUvb0Rmdu7zRQSydxOj7GZgUvoHGsTQWlPH8AP9nxlGi4TxC5sp6pR0kr4O2512RIYRf9ay9whq5bazknLBk-S0LZEbtHQ24tjknFPQIOR9E2u6wbjvk5909thi9RWYutYmw8nv-jTF0jrgWfXdPYxE8gvp_7q4pt6CLyKhAq-EN_GpWiUmqQLBqEH1wbvjBKQosHCbj6BXyS6brZc976T04QVc5If2juaRpO2T8-UXEjVPUdvnpRe8wYBot6l8hAKsYC8jryV2og2XvR8RvU0pytHKPnA0AHEAuiPAWo7MTKE_z7pAD96v-Be1ruDKp4vaCmDwvrdhm-AR1T67NUHnpd8js_4DQY9gMnYffPFvGBsDeL5xK0uccRhQzI-jtDTi-ES7omW7dvf9uAWa3Dq7YQAVm8i3Zi7n1--PJQMc), [Google](<https://scholar.google.com/scholar?q=When Should You Adjust Standard Errors for Clustering>). 
- Cameron, A. C., J. B. Gelbach, D. L. Miller, **2011**, Robust inference with multiway clustering, **Journal of Business & Economic Statistics**, 29 (2): 238-249. [-Link-](https://doi.org/10.1198/jbes.2010.07136), [-PDF-](https://sci-hub.ren/10.1198/jbes.2010.07136), [-wp2009-](http://faculty.econ.ucdavis.edu/faculty/cameron/research/JBESpaper2009version.pdf)
- Cameron, C. A., D. L. Miller, **2015**, A practitioner’s guide to cluster-robust inference, **Journal of Human Resources**, 50 (2): 317-372. [-Link-](https://doi.org/10.3368/jhr.50.2.317), [-PDF-](https://sci-hub.ren/10.3368/jhr.50.2.317)
- Correia, S. **2017**. `reghdfe`, Linear Models with High-Dimensional Fixed Effects: An Efficient and Feasible Estimator. Working Paper. [-PDF-](http://scorreia.com/research/hdfe.pdf), [Examples](http://scorreia.com/software/reghdfe/), [Slides](https://www.stata.com/meeting/chicago16/slides/chicago16_correia.pdf)
- Correia, S. 2015. Singletons, cluster-robust standard errors and fixed effects: A bad mix. [-PDF-](http://scorreia.com/research/singletons.pdf)
- Gu, A., H. I. Yoo, **2019**, `vcemway`: A one-stop solution for robust inference with multiway clustering, **Stata Journal**, 19 (4): 900-912. [-Link-](https://doi.org/10.1177/1536867x19893637), [-PDF-](https://sci-hub.ren/10.1177/1536867x19893637). 
- MacKinnon, J. G., M. D. Webb, **2020**, When and how to deal with clustered errors in regression models, **Working paper**. [PDF](https://www.econ.queensu.ca/sites/econ.queensu.ca/files/wpaper/qed_wp_1421.pdf)
- MacKinnon, J. G., **2019**, How cluster-robust inference is changing applied econometrics, **Canadian Journal of Economics/Revue canadienne d'économique**, 52 (3): 851-881. [-Link-](https://doi.org/https://doi.org/10.1111/caje.12388), [-PDF-](https://sci-hub.ren/https://doi.org/10.1111/caje.12388), [Replication](https://onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1111%2Fcaje.12388&file=caje12388-sup-0001.zip)



--- - --

<!-- backgroundColor: #C1CDCD -->

# 4. 假设检验


--- - --
<!-- backgroundColor: white -->

## 4.1 t 检验：单个系数显著性检验

- **模型：** $y = \alpha + \beta x + e$
- **原假设（$H_0$）**: $\beta = 0$

$$
t = \frac{\hat{\beta}}{SE(\hat{\beta})} \sim t_{n-k-1}
$$

- **示例**：假设 $\hat{\beta} = 2.5$，标准误差 $SE(\hat{\beta}) = 1.2$，则

$$
t = \frac{\hat{\beta}}{SE(\hat{\beta})} = \frac{2.5}{1.2} \approx 2.08
$$

接着，使用 t 分布表或计算 p-value，假设 p-value = 0.04。

#### 直观解释

- $p = 0.04$ 表示，在 $H_0$ 成立的情况下，观察到 $\hat{\beta} = 2.5$ 或更极端的值出现的概率只有 $4\%$。由于这个概率小于预设的显著性水平 ($0.05$)，我们拒绝 $H_0$，认为 $x$ 对 $y$ 有显著影响。

![bg right:45% w:550](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/gr_OLS_t_distribution.png)


--- - --

## 4.2 区别：t 值和 z 值 (1)

Stata 中，有些命令报告 t 值，有些则报告 z 值：

```stata
. webuse "mroz.dta", clear

. regress wage educ, noheader 
-----------------------------------------
  wage |   Coeff     S.E.    t     P>|t| 
-------+---------------------------------
  educ |   0.495    0.066   7.51   0.000 
 _cons |  -2.092    0.848  -2.47   0.014 
-----------------------------------------
```

```stata
. ivregress gmm wage educ, noheader 
-----------------------------------------
       |           Robust
  wage |   Coeff     S.E.    z     P>|z| 
-------+---------------------------------
  educ |   0.495    0.067   7.35   0.000 
 _cons |  -2.092    0.822  -2.54   0.011 
-----------------------------------------
(no endogenous regressors)
```

![bg right:50% w:600](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/gr_OLS_t-value_z-value.png)

--- - --

## t 值和 z 值 (2)

- t 值：小样本估计和推断，如 `regress`
- z 值：基于大样本的推断，如 `ivregress`, `probit` 等基于 GMM 或 MLE 估计方法的命令。
- 通常无需进行区分，都可视为 $N(0, 1)$

> 解释：  

- 当 $N-k>30$ 时，$t(N-k)$ 的分布趋近于 $N(0,1)$。
- 多数情况下，$(N-k) \gg 30$。
- 因此，无论 Stata 报告的是 $t$ 值还是 $z$ 值，在日常分析中，我们都可以用 $1.96$ 作为 $5\%$ 显著水平的临界值作为判断标准。
- 你甚至可以粗略估算一下 $t = \frac{\hat{\beta}}{SE(\hat{\beta})}$，只要 $|\,t\,|$ 大于 $2$ (近似等于 $1.96$)，就可以认为 $\hat{\beta}$ 在 $5\%$ 水平上显著。

--- - --

## 4.3 F 检验：同时检验多个约束条件
>  $$H_{0}: \beta_{1}=0, \beta_{2}=0, \beta_{3}=0$$

  - 估计非受限模型 &emsp;  $
    y=\beta_{0}+\beta_{1} x_{1}+\beta_{2} x_{2}+\ldots+\beta_{k} x_{k}+u
    $ &emsp; &rarr;&emsp;  $SSR_{U}$
  - 估计受限模型 &emsp;&emsp; $
    y=\beta_{0}+\beta_{4} x_{4}+\beta_{5} x_{5}+\ldots+\beta_{k} x_{k}+u
    $ &emsp; &rarr;&emsp;  $SSR_{R}$
  - 计算 $F$-统计量 ($q=$ 约束条件的个数，$k$ 无约束模型中的参数个数)
    $$
    F=\frac{\left(S S R_{R}-S S R_{U}\right) / q}{S S R_{U} /(n-k-1)}     \sim F_{q, n-k-1}
    $$


```stata
. sysuse "nlsw88.dta", clear
. reg wage i.race hours age 
. testparm i.race

 ( 1)  2.race = 0
 ( 2)  3.race = 0
       F(  2,  2237) = 12.85
            Prob > F =  0.0000
```


--- - --


## 4.4 系数估计的 95% 置信区间 (1)

> **$95\%\, CI$ 公式**：   

$$
\hat{\beta} \pm t_{\alpha/2, \, df} \cdot SE(\hat{\beta})
$$
- $t_{\alpha/2, \, df}$ 是 t 分布的临界值，取决于显著性水平 $\alpha$ 和回归模型的自由度 $df$。对于 95% 置信区间，通常 $t_{\alpha/2} \approx 1.96$ （大样本时）。
$$
\hat{\beta} \pm z_{\alpha/2} \cdot SE(\hat{\beta}) 
$$
- $z_{\alpha/2}$ 是标准正态分布（z 分布）下，显著性水平为 $\alpha$ 时的临界值。对于 95% 置信区间，$\alpha = 0.05$，对应的 $z_{\alpha/2} = 1.96$。

> **简单记忆** ：

$$
\hat{\beta} \pm 1.96 \cdot SE(\hat{\beta})
$$

![bg right:50% w:600](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250107004547.png)

--- - --

## 4.4 系数估计的 95% 置信区间 (2)

```stata
  webuse "mroz.dta", clear

  reg wage educ 
  
  coefplot, xline(0, lp(dash)) ///
            nolabel            ///
            scheme(tufte) 
```

![bg right:55% w:700](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/gr_OLS_95CI_coefplot.png)


--- - --

## 4.5 拟合值 $\hat{y}_i$ 的 95% 置信区间

<br>

$$
\hat{y}_i \pm t_{\alpha/2, \, df} \cdot SE(\hat{y}_i)
$$

<br>

- $\hat{y}_i$ 是第 $i$ 个观测的拟合值 (预测值)。
- $SE(\hat{y}_i)$ 是第 $i$ 个拟合值的标准误差：
  $$SE(\hat{y}_i) = \sqrt{ \hat{\sigma}^2 \left( X(X'X)^{-1}X' \right)_{ii} }$$

<br>

```stata
sysuse "auto.dta", clear

scatterfit mpg weight,  ///
    ci by(foreign)      ///
    leginside xysize(1) ///
    scheme(tufte)
```

![bg right:55% w:600](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/gr_OLS_CI95_yhat.png)




--- - --
<!-- backgroundColor: #FFFFF9 -->

# 5. 模型评价

- $R^{2}$, $\bar{R}^{2}$
- $MSPE$
- $F$ 统计量



--- - --
<!-- backgroundColor: white -->

<!-- ![bg left:35% w:400](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/Fig_OLS_R2_03.png) -->

## 5.1 $R^{2}$ - 拟合优度

$$
\mathbf{Y} = \mathbf{X}\widehat{\boldsymbol{\beta}} + \widehat{\mathbf{\varepsilon}} \quad \Longrightarrow \quad \operatorname{Var}(\mathbf{Y})=\operatorname{Var}(\mathbf{X}\widehat{\boldsymbol{\beta}}) + \operatorname{Var}(\widehat{\mathbf{\varepsilon}})
$$  

<center>

![w:400](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/R2_divide_into_x1_x2_v1.png)

</center>

$$y_{i}-\bar{y}=\underbrace{\left(\widehat{y}_{i}-\bar{y}\right)}_{\text {模型解释部分}}+\underbrace{\left(y_{i}-\widehat{y}_{i}\right)}_{\text {模型无法解释部分}}$$

$$\underbrace{\sum_{i}\left(y_{i}-\bar{y}\right)^{2}}_{\mathrm{SS}_{\text {total }}}=\underbrace{\sum_{i}\left(\widehat{y}_{i}-\bar{y}\right)^{2}}_{\mathrm{SS}_{\text {model }}}+\underbrace{\sum_{i}\left(y_{i}-\widehat{y}_{i}\right)^{2}}_{\mathrm{SS}_{\text {error }}}$$

--- - --

<!-- 残差 (Residuals): $\widehat{e}_i = y_{i}-\widehat{y}_{i}$ ([Source](https://www.mit.edu/~6.s085/notes/lecture3.pdf)) -->

#### $R^{2}$
$$
R^{2}=\frac{MSS}{TSS}=1-\frac{ESS}{TSS}
$$

#### adj-$R^{2}$
$$
R_{a d j}^2=1-\frac{\left(1-R^2\right)(n-1)}{n-k-1}
$$

<br>

#### $R^{2}$：另一种定义方式

 $$R^{2}=[\operatorname{Corr}(y, \widehat{y})]^{2}$$

- $\rho$ (`\rho`) 的首字母是 $R$。
- 当 $y=f(x;\beta)$ 是非线性设定时，这种 $R^{2}$ 的定义方式很有用。 


--- - --
## 5.2 关于 $R^2$ 几点说明

- 只有模型中包含常数项时，才能保证 $0 \leq R^{2} \leq 1$
  - **adj-**$R^{2}$ 有可能小于 0，eg., `reg y x i.id i.year`
- $R^{2}$ 并不是统计检验量，无法用于检验某个预定的假设。  
   $R^{2}$ 只是一个统计指标 (index)，可以用于对比嵌套和非嵌套模型的优劣。:apple: 
- 两个被解释变量不同的模型，它们的 $R^2$ 不可直接比较
- 数据类型
  - 截面数据的 $R^{2}$ 通常都不高
  - 时间序列数据的 $R^{2}$ 通常都很高

- 经验判断和对比：已前期相关文献为对比基准

--- - --
### 要清楚你的 $R^{2}$ 中的 MSS 到底是什么

**Model 1：** $y_i = x_i\beta + \theta_j + u_i$ 
- $j=1,2\dots J$ 表示行业分类


![OLS-R2-001 w:600](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/OLS-R2-001.png)

&emsp;

**Model 2：** $y_i-\bar{y}_j = (x_i-\bar{x}_j)\beta  + (u_i-\bar{u}_j)$ 

![w:380](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/R2_divide_into_x1_x2_no_x2.png)

--- - --

```stata
sysuse "nlsw88.dta", clear
drop if industry==.

eststo m1: regress wage hours 
eststo m2: regress wage hours ib0.industry
eststo m3: reghdfe wage hours, absorb(industry)
eststo m4: areg    wage hours, absorb(industry)

bysort industry: center wage hours, prefix(C_)
eststo m5: reg C_wage C_hours

esttab m1 m2 m3 m4 m5, drop(*.industry) ///
    nogap scalars(N r2) sfmt(%4.3f)
```
```stata
--------------------------------------------------------------------
             (1)          (2)         (3)         (4)         (5)   
            wage         wage        wage        wage      C_wage   
--------------------------------------------------------------------
hours     0.0865***    0.0724***   0.0724***   0.0724***            
          (7.53)       (6.30)      (6.30)      (6.30)               
C_hours                                                    0.0724***
                                                           (6.32)   
_cons      4.569***     6.359***    5.097***    5.097***  0.00547   
         (10.27)      (10.45)     (11.50)     (11.50)      (0.05)   
--------------------------------------------------------------------
N           2228         2228        2228        2228        2228   
r2         0.025        0.080       0.080       0.080       0.018   
--------------------------------------------------------------------
```

--- - --

## 5.2 其他统计量

- **MSE:** mean squared error - 均方误差: 
   $$MSE = \frac{\sum_{i}\left(y_{i} - \widehat{y}_i\right)^{2}}{n}$$
- **RMSE:**$=\sqrt{\text{MSE}}$ - 均方根误差
- **MAE:** mean absolute error - 平均绝对误差 (对离群值和数值较大的误差项不敏感): 
  $$ MAE = \frac{\sum_{i}\left|y_{i} - \widehat{y}_i\right|}{n}$$

- **F 统计量**：F 检验用于检验除了常数项以外的所有回归系数是否同时为零。F 统计量的计算公式为：

$$
F = \frac{(TSS - RSS)/k}{RSS/(n-k-1)}
$$

  其中，$k$ 是回归模型中的自变量个数，$N$ 是样本大小。



--- - --
<!-- backgroundColor: #C1CDCD -->

# 6. FWL 定理

## (Frisch-Waugh-Lovell therom)

--- - --

<!-- backgroundColor: #FFFFF9 -->

## 6.1 简介

- FWL 定理由 Frisch and Waugh (1933) 和 Lovell (1963) 提出
  - 它阐释了 OLS 回归的一个重要性质，为理解多元回归的系数含义，估计高维固定效应提供了重要的理论基础。
  - Davidson and MacKinnon ([1993](http://qed.econ.queensu.ca/pub/dm-book/EIE-davidson-mackinnon-2021.pdf), 19-24) 以及 Davidson and MacKinnon ([2004](http://qed.econ.queensu.ca/pub/faculty/mackinnon/econ850/), [PDF](http://qed.econ.queensu.ca/ETM/ETM-davidson-mackinnon-2021.pdf), pp. 62–75, [Slides](http://qed.econ.queensu.ca/pub/faculty/mackinnon/econ850/slides/econ850-slides-h03.pdf)) 对此进行非常细致的介绍。
- **应用：**
  - 在 Stata 中，`reghdfe` 等处理高维固定效应的命令基本原理便是 FWL 定理
  - 在 `ivreg2`, `lasso2` 等命令中经常出现的 `partial()` 选项也基于 FWL 定理
  - 用于可视化展示多元回归结果的部分回归图命令 `avplot`, `reganat`, `avciplot`, `avciplots`, `binscatter` 等也都基于 FWL 定理。

- **Stata 实操**
  - Filoso, V., **2013**, Regression Anatomy, **Stata Journal**, 13(1): 92–106. [-PDF-](https://journals.sagepub.com/doi/pdf/10.1177/1536867X1301300107)
  - [图示线性回归系数：Frisch-Waugh定理与部分回归图](https://www.lianxh.cn/news/e346db1a68211.html)
  - [多元回归系数：我们都解释错了？](https://www.lianxh.cn/news/22f1f266f5868.html)


--- - --
<!-- backgroundColor: white -->

### 如何控制 x2 的影响？

![bg left:40% w:400](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/OLS-venn-01.png)

![w:400](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/OLS-venn-02.png)

--- - --

$Y=X_1 {\color{red}{\beta_1}} + X_2 \beta_2 + u$ $\ \ \Leftrightarrow$ $\ \ \tilde{Y}= \tilde{X}_1 {\color{red}{\beta_1}} + v$

![](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/Lianxh_装饰黄线.png)

`reg Y X2` 
`predict eY, res` &rarr; $\ \ \ \tilde{Y} = A + {\color{blue}{B}}$

`reg X1 X2` 
`predict eX1, res` &rarr; $\tilde{X}_1 = F + {\color{blue}{B}}$
![](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/Lianxh_装饰黄线.png)

`reg eY eX1` &rarr; `dis _b[eX1]` = ${\color{red}{\widehat{\beta}_1}}$ &rarr; ${\color{blue}{B}}$

![bg left:40% w:400](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/OLS-venn-01.png)



--- - --

#### 如果只需要估计系数

$$Y=X_1 {\color{red}{\beta_1}} + X_2 \beta_2 + u \ \ {\color{blue}{\Leftrightarrow}} \ \ Y= \tilde{X}_1 {\color{red}{\beta_1}} + v$$

- 事实上，只需从 $X_1$ 中去除  (partial out) $X_2$ 的影响，得到 $\tilde{X}_1$，进而用 $Y$ 对 $\tilde{X}_1$ 进行回归即可。即，如下回归都是等价的：
  
  - `reg` $\tilde{Y}$ on $\tilde{X}_1$
  - `reg` ${Y}$ on $\tilde{X}_1$
  - `reg` ${Y}$ on ${X}_1, {X}_2$

![bg left:40% w:400](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/OLS-venn-01.png)

--- - --

![bg left:35% w:350](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/OLS-venn-01.png)

### 遗漏变量偏误
- **真实模型：** $Y=X_1 {\color{red}{\beta_1}} + X_2 \beta_2 + u$
- &#x2753; 如果不控制 $x_2$，即 
  - `reg Y X1` $\iff$ $Y = X_1\theta_1 + \underbrace{{\color{red}{\varepsilon}}}_{X_2\beta_2+u}$
  - $\widehat{\theta}_1 \neq \beta_1$

--- - --
<!-- backgroundColor: #FFFFF9 -->
## 6.2 FWL 应用 1: 常数项的作用

<br>

![bg left:50% w:600](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/FWL_NoConstant.png)

> **包含常数项：**
- $E(Y_{i})= m_i = \boldsymbol{1} {\color{red}{\alpha}} + X_{i} {\color{blue}{\beta}}$
- $E(Y_{i}|X=0)= {\color{red}{\alpha}}$
  - $E(Y_{i}|X=0.5)= {\color{red}{\alpha}} + 0.5\beta$

<br>

> 不**包含常数项：**
- $E(Y_{i})= m_i = X_{i} {\color{blue}{\beta}}$
- $E(Y_{i}|X=0)= 0$

--- - --

### FWL 应用 1：常数项的作用 (1) - FWL 视角


<br>

$Y_{i}=\boldsymbol{1} {\color{red}{\alpha}} + X_{i} {\color{blue}{\beta}} + u_{i}$

$\bar{Y} = \boldsymbol{1} {\color{red}{\alpha}} + \bar{X} {\color{blue}{\beta}} + \bar{u}$

$\Longrightarrow$

$Y_{i} - \bar{Y} =  (X_{i}-\bar{X}) {\color{blue}{\beta}} + (u_{i}-\bar{u})$

#### Stata 实操

- `reg Y` &rarr; `predict eY, res` &emsp; $\widehat{e}_{Yi} = Y_i - \bar{Y}$ &emsp; (Note: $\bar{Y} = (1/N)\sum_i^N Y_i$)
- `reg X` &rarr; `predict eX, res` &emsp; $\widehat{e}_{Xi} = X_i - \bar{X}$

- &#x1F34E;  `reg eY eX` $\iff$ `reg y X`

![bg left:40% w:750](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/FWL_DeConstant.png)

<br>

> [Codes](https://gitee.com/arlionn/graph/wikis/dofiles/OLS_FWL_constant?sort_id=13200673)

--- - --
### 常数项的作用
- $x$ 和 $y$ 的量纲不一致问题
- 吸收 $x$ 或 $y$ 的缩放 $(x \to x/c)$ 或平移 $(x \to x-c)$ 产生的影响，以保证统计推断 ($t$ 值不受影响)
- 保证模型的 $R^2 \in [0,1]$，否则可能出现 $R^2<0$ 或 $R^2>1$ 的情况。
- 在 DID 和 RDD 分析中，常数项本身就有明确的经济含义

![](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/Lianxh_装饰黄线.png)

Note: 平移 $(x \to x-c)$ 在 RDD 和交互项设定中非常必要，参见 
 - [交乘项的中心化问题](https://www.lianxh.cn/news/454644a5b7e3b.html) 
 - [Stata+R：一文读懂精确断点回归-RDD](https://www.lianxh.cn/news/96fb6b7e847e1.html)
 - [Stata：断点回归RDD简明教程](https://www.lianxh.cn/news/789f031b0c110.html)

--- - --

## 6.3 FWL 应用 2: 虚拟变量

<br>

![bg left:45% w:720](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/FWL_Dummy_a01.png)


```stata
      y     x   M    F   cons  
   ---------------------------   
    5.7   1.6   0    1      1  
    6.4   1.4   0    1      1  
    9.3   2.0   1    0      1  
    9.0   1.4   1    0      1  
    9.3   1.7   1    0      1 
```

### 包含常数项
$y_{i} = \alpha_1 + {\color{blue}{\gamma}}\,M_{i} + \beta x_{i} + u_{i}$

$E[y_{i}\,|\,M=0] = \alpha_1 \quad\ \  +  \beta x_{i} + u_{i}$
$E[y_{i}\,|\,M=1] = \underbrace{\alpha_1 + {\color{blue}{\gamma}}}_{\alpha_2} + \beta x_{i} + u_{i}$

> [Stata Codes](https://gitee.com/arlionn/graph/wikis/dofiles/FWL_dummy_variable)

--- - --
<!-- backgroundColor: #FFFFF9 -->

### 不包含常数项

<br>

![bg left:45% w:720](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/FWL_Dummy_a01.png)

```stata
      y     x   M    F   cons  
   ---------------------------   
    5.7   1.6   0    1      1  
    6.4   1.4   0    1      1  
    9.3   2.0   1    0      1  
    9.0   1.4   1    0      1  
    9.3   1.7   1    0      1 
```
$y_{i} = \alpha_1 M_{i} + \alpha_2 F_{i} + \beta x_{i} + u_{i}$

$E[y_{i}\,|\,M=1] =  \alpha_1 + \beta x_{i} + u_{i}$
$E[y_{i}\,|\,F=1]\ = \alpha_2 + \beta x_{i} + u_{i}$

&#x1F34F; $y_{gi} = \alpha_g + \beta x_{gi} + u_{gi}\ (g=1,2)$

--- - --
<!-- backgroundColor: #FFFFF9 -->

![bg left:40% w:680](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/FWL_Dummy_a01.png)


```stata
. eststo m1: reg y M x
. eststo m2: reg y M F x, noconstant
. esttab m1 m2, nogap compress 

------------------------------------
                 (1)          (2)   
------------------------------------
x              0.458***     0.458***
              (5.71)       (5.71)   
M              3.105***     8.212***
             (33.58)      (72.51)   
F                           5.107***
                          (47.03)   
_cons          5.107***             
             (47.03)                
------------------------------------
N                 40           40   
------------------------------------
```

--- - --

<!-- backgroundColor: #FFFFF9 -->
### FWL 视角：动图展示
![bg left:50% w:640](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/OLS_Animation_of_Control_01.gif)

$Y_{i} = \alpha + \beta X_{i} + {\color{blue}{\gamma}}\,W_{i} + u_{i}$

$W_i=\{0,1\}$

- $W=0$: 
  - $Y_{i} = \alpha + \beta X_{i} + u_{i}$
- $W=1$: 
  - $Y_{i} = \alpha+{\color{blue}{\gamma}} + \beta X_{i} + u_{i}$

> Source: [NickCH-K](https://github.com/NickCH-K) &rarr; [causalgraphs](https://nickchk.com/causalgraphs.html) &rarr; [github](https://github.com/NickCH-K/causalgraphs)

--- - --

<!-- backgroundColor: #FFFFF9 -->
### FWL 视角
```stata
   g    i     y     x     D0   D1  
 ---------------------------------   
   1    1    5.7   1.6     0    1   
   1    2    6.4   1.4     0    1   
 ---------------------------------  
   2    1    9.3   2.0     1    0   
   2    2    9.0   1.4     1    0   
   2    3    9.3   1.7     1    0   
```

$(1)\quad Y_{gi} = {\color{blue}{\gamma_g}}D_g + \beta X_{gi} + u_{gi}, \quad g=1,2$ 

$(2)\quad Y_{gi}-\bar{Y}_g = \beta (X_{gi}-\bar{X}_g) + (u_{gi}-\bar{u}_g), \quad \text{de-mean within group}$

#### Stata 实例
```stata
sysuse "auto.dta", clear

reg mpg weight foreign                         // (1)

bysort foreign: center mpg weight, prefix(c_)  
reg c_mpg  c_weight                            // (2) 手动

reghdfe mpg weight, absorb(foreign)            // (2) 更简洁
```


--- - --
<!-- backgroundColor: white -->

## 6.4 FWL 应用 3: 固定效应模型 (FE)


**原始数据:** 

$$
\begin{aligned}
y_{it} &= \alpha_i + x_{it}\beta + \varepsilon_{it} \\
& = \sum_i^N \alpha_i D_i + x_{it}\beta + \varepsilon_{it}
\end{aligned}
$$

**组内去心 (De-meaned):** 

$$
y_{it} -\bar{y}_i \\
= (x_{it}-\bar{x}_i)\beta + (\varepsilon_{it}-\bar{\varepsilon}_i)
$$

![bg left:55% w:680](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/Fig_OLS_FE_01.png)

<br>

#### FE：de-meaned 正式表述
$$
\begin{aligned}
y_{i t} &=x_{i t} \beta+ {\color{red}{\alpha_{i}}}+\varepsilon_{i t} \qquad (1) \\
\bar{y}_{i} &=\bar{x}_{i} \beta+{\color{red}{\alpha_{i}}}+\bar{\varepsilon}_{i} \\
\left(y_{i t}-\bar{y}_{i}\right) &=\left(x_{i t}-\bar{x}\right) \beta+\left({\color{red}{\alpha_{i}}}-{\color{red}{\alpha_{i}}}\right)+\left(\varepsilon_{i t}-\bar{\varepsilon}_{i}\right) \\
\ddot{y}_{i t} &=\ddot{x}_{i t} \beta+\ddot{\varepsilon}_{i t} \qquad\qquad\ (2)
\end{aligned}
$$

> [Stata Codes](https://gitee.com/arlionn/graph/wikis/dofiles/FWL_FE_scatter)


--- - --
<!-- backgroundColor: #C1CDCD -->
## 6.5 常用模型设定

--- - --
<!-- backgroundColor: white -->
### 几种典型设定 - 1
$$Y=X_1 {\color{red}{\beta_1}} + X_2 \beta_2 + u \quad{\color{blue}{\Leftrightarrow}} \quad \tilde{Y}= \tilde{X}_1 {\color{red}{\beta_1}} + v$$

- $\bf{X_2} = \bf{1}$，去除样本均值 &emsp; `reg y x`
  
- ${\bf{X_2}} = Trend_t$，去除时间趋势
  - `reg y x  c.year`
- ${\bf{X}}_{{\bf{2}}it} = \alpha_i = \sum_1^N \alpha_i D_i$，去除个体效应
  - `reg y x i.id` 
  - `xtreg y x, fe`
  - `reghdfe y x, absorb(id)`
- ${\bf{X}}_{{\bf{2}}it} = \lambda_t= \sum_1^T \lambda_t D_t$，去除时间效应 
  - `reg y x i.year` 
  - `areg y x, absorb(year)`
  - `reghdfe y x, absorb(year)`



--- - --

### 几种典型设定 - 2

$$Y=X_1 {\color{red}{\beta_1}} + X_2 \beta_2 + u \quad{\color{blue}{\Leftrightarrow}} \quad \tilde{Y}= \tilde{X}_1 {\color{red}{\beta_1}} + v$$

- ${\bf{X}}_{{\bf{2}}it} = \alpha_i + \lambda_t$，双向固定效应 &rarr; DID
  - `. reghdfe y x, absorb(id year)`
  - `. xtreg y x i.year, fe`
- ${\bf{X}}_{{\bf{2}}sjit} = \alpha_s + \alpha_j + \alpha_i + \lambda_t$，多维固定效应
  - `. reghdfe y x1 x2, absorb(province industry firm year)`

- ${\bf{X}}_{{\bf{2}}jt} = Ind_j + \lambda_t + Ind_j\times \lambda_t$，交互固定效应 
  - `. reghdfe y x, absorb(industry year industry#year)`

- 变系数模型：$Y_{it} = X_{it} {\color{red}{\beta_{t}}} + Z_{it} {\color{blue}{\theta_{i}}} + u$
  - `. reghdfe y c.x#i.year c.z#i.id Controls, absorb(id year) cluster(id year)`

--- - --
<!-- backgroundColor: #FFFFF9 -->

<center>

## 连享会  &#x1F34E; 

### [lianxh.cn](https://www.lianxh.cn)

</center>