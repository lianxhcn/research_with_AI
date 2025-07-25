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
footer: '连享会&nbsp;|&nbsp;[lianxh.cn](https://www.lianxh.cn)&nbsp;|&nbsp;[Bilibili](https://space.bilibili.com/546535876)'
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
![bg right:50% w:400 brightness:. sepia:50%](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20220722114227.png) 

<!--幻灯片标题-->
# 02 - Stata 数据处理 

> 数据导入  
> 生成新变量  
> 描述性统计   
> 类别变量 / 因子变量  
> 离群值  

<br>

<!--作者信息-->
[连玉君](https://www.lianxh.cn) (中山大学)
arlionn@163.com

<br>


--- - --



<!-- backgroundColor: #C1CDCD -->

<br>

> &#x1F449;  Stata 命令：  
> `. lianxh 数据处理 ` 


<br>


- 专题：[Stata教程](https://www.lianxh.cn/blogs/17.html)
- 专题：[数据处理](https://www.lianxh.cn/blogs/25.html)
- 专题：[面板数据](https://www.lianxh.cn/blogs/20.html)




--- - --
<!-- backgroundColor: #FFFFF9 -->
## 1. 导入数据
```stata
 help sysuse           // Stata 自带数据
      sysuse dir, all  // 数据列表

 help webuse           // 电子手册数据
 help dta_manuals      // 数据列表

 help use              // 导入 Stata 格式数据

 help import excel     // 导入 Excel 格式数据
 help import delimited // 导入 csv, txt 格式数据

 help bcuse          
 help lxhuse
```

<font color=black size=5>

- `bcuse` Wooldrige 教科书数据，[数据列表](http://fmwww.bc.edu/ec-p/data/wooldridge/datasets.list.html)
- `lxhuse` [lianxh.cn](https://www.lianxh.cn) 推文范例数据，[数据列表](https://gitee.com/lianxh/data/tree/master/data01)

</font> 

--- - --

### 1.1 导入 Stata 格式的数据 (1)：sysuse 和 webuse

> `help sysuse`， `help webuse`

<font color=black size=5>

- 调入 Stata 自带数据集
  ```stata
  sysuse "auto.dta", clear
  sysuse "nlsw88.dta", clear
  ```
  - :apple: 有哪些？ `sysuse dir`
  - :cat: 在哪里？【base】文件夹中：**D:\stata17\ado\base\a**，**D:\stata17\ado\base\n**

- 调入 Stata 手册中的范例数据集
  ```stata
  webuse lifeexp, clear 
  use "https://www.stata-press.com/data/r17/lifeexp" //等价
  ```` 
  - :apple: 有哪些？ &ensp;  `help dta_manuals` &ensp; HTML：[stata-press.com/data](https://www.stata-press.com/data/r17/) 

</font>

--- - --

### 1.2 导入 Stata 格式的数据 (2)：use 

![w:850](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20221228164918.png)
- 从工作路径下调入部分数据
  ```stata
  cd "D:/data"
  use price weight if rep78<4 "auto.dta", clear
  ```
- 声明完整路径，调入非工作路径中的数据
  ```stata
  use "E:/mydata/women.dta", clear
  ``` 
- 调入网络数据：
  ```stata
  use "https://gitee.com/arlionn/data/raw/master/data01/mroz.dta", clear
  ``` 

- 其它命令：`bcuse`, `lxhuse`





--- - --

### 1.3 导入 Excel 格式的数据

> `help import excel` &emsp; [**[D]** import excel](https://www.stata.com/manuals/dimportexcel.pdf) 

![20221228171844](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20221228171844.png)

```stata
 help import      // 导入 Excel, csv, txt 格式的数据

 import excel data.xls, firstrow clear

 import excel "D:/data.xlsx", sheet(Sheet1) firstrow clear

 import excel "D:/data.xlsx", cellrange(A1:A10) firstrow clear
```


--- - --

### 1.3 导入 Excel 格式的数据：超大 Excel 文档

<br>

> [Stata数据处理：超大Excel文档如何读入？](https://www.lianxh.cn/news/798d66e2c0acc.html)

<br>

- **方法1**：先执行 `set excelxlsxlargefile on` 命令
  ```stata
  . set excelxlsxlargefile on
  . import excel     "E:\data\个股回报率.xlsx", sheet("Sheet1") firstrow
  ```
- **方法2**：把 Excel 文档另存为 `.csv` 或 `txt` 文档，然后再用 `import delimited` 命令导入 ([**[D]** import delimited](https://www.stata.com/manuals/dimportdelimited.pdf))
  ```stata
  . import delimited "E:\data\个股回报率.csv", encoding(UTF-8) clear
  . import delimited "E:\data\个股回报率.txt", encoding(GB18030) clear
  ```

<br>

--- - --

### 1.4 导入 csv 和 txt 格式的数据

这类数据本身仍然是以「表格 (sheet)」形式存储的，因为两列之间是用 **Tab** 键分隔的。注意：不是若干个空格

> `help import delimited` &emsp; [**[D]** import delimited](https://www.stata.com/manuals/dimportdelimited.pdf)   
> `help insheet` 旧版命令，但语法简洁


```stata
*-下载一份 CSV 格式的数据到当前工作路径
  copy "https://www.stata.com/examples/auto.csv" "auto.csv" // CSV

*-方法 1 
  import delimited "auto.csv", clear

*-方法 2
  insheet "auto.csv", clear
```



--- - --

### 1.5 扩展阅读

<font color=black size=5>

- 专题：[数据处理](https://www.lianxh.cn/blogs/25.html)
  - [Stata数据处理：物价指数-(CPI)-的导入和转换](https://www.lianxh.cn/news/c7eb4207e1d7d.html)
  - [Stata数据处理：FRED数据导入问题的解决方案](https://www.lianxh.cn/news/b7b1ec1c5b9c2.html)
  - [Stata数据处理：import-fred-命令导入联邦储备经济数据库-FRED](https://www.lianxh.cn/news/e5d916ccf8d52.html)
  - [multimport : 一次性导入并合并多个文件](https://www.lianxh.cn/news/e2764903951c6.html) 
- 专题：[Stata教程](https://www.lianxh.cn/blogs/17.html)
  - [Stata-Python交互-9：将python数据导入Stata](https://www.lianxh.cn/news/929a3cc22307b.html)
  - [Stata-Python交互-8：将Stata数据导入Python](https://www.lianxh.cn/news/17c9d76816839.html)
  - [Stata+Python：导入超大Excel文档的新思路-以国泰安为例](https://www.lianxh.cn/news/9be05177a8978.html)



</font> 


--- - --
<!-- backgroundColor: #C1CDCD -->
## 2. 基本语法、运算符和函数

<br>

- [**[U]** Language syntax](https://www.stata.com/manuals/u11.pdf#u11Languagesyntax) Stata 基本命令的语法规则 (务必认真研读)  
  - `help language`
- [**[U]** Functions and expressions](https://www.stata.com/manuals/u13.pdf#u13.2Operators) 函数和表达式
  - `help operators`  
  - `help function`
  - `help expression`
- [**[D]** gen](https://www.stata.com/manuals/dgenerate.pdf) 变量生成和函数 &emsp; `help gen`
- [**[D]** egen](https://www.stata.com/manuals/degen.pdf) 大量扩展函数 &emsp; `help egen`

--- - --
<!-- backgroundColor: #FFFFF9 -->
## 运算符、生成新变量
```stata
sysuse "auto.dta", clear

gen wei2len = weight/length
gen lnPrice = ln(price)

gen bad = (rep78>=4 & rep78!=.)
bysort foreign: egen sd_price = sd(price)

regress  mpg  price  weight##weight  i.foreign  i.foreign#weight
```

![](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20220623172830.png)

--- - --
<!-- backgroundColor: #F1CDCD -->

# 因子变量和时序变量

<br>

- 因子变量 `reg wage hours i.race i.industry i.industry#c.year`
- 时序变量 `reg D.wage D.hours D.L.(z1 z2 z3)`

<br>

> [`help fvvarlist`](https://www.stata.com/manuals/u11.pdf#u11.4.3Factorvariables)

<br>

>[`help varlist`](https://www.stata.com/manuals/u11.pdf#u11.4varnameandvarlists)


--- - --

<!-- backgroundColor: white -->

### 因子变量

<br>

> 详情：[Stata：因子变量全攻略](https://www.lianxh.cn/news/314564eb6d725.html) &emsp; 帮助：[`help fvvarlist`](https://www.stata.com/manuals/u11.pdf#u11.4.3Factorvariables)；[`help varlist`](https://www.stata.com/manuals/u11.pdf#u11.4varnameandvarlists)


| 符号 | 含义 | 实例 |
| :--- | :--- | :--- | 
| `i.` | 标示为类别变量 | `reg y x i.id i.year` &rarr; $y_{it} = {\color{red}{a_i}} + {\color{red}{\lambda_t}} + x_{it}\beta + u_{it}$|
| `c.` | 标示为连续变量 | `reg y x c.year` &rarr; $y_{it} = x_{it}\beta + {\color{red}{Trend_t}} + u_{it}$ | 
| `o.` | 略去某个类别或变量 | | 
| `#` | 交乘项 | `reg y D x i.D#c.x` &rarr; <br>$\quad y_i = a + D_i\beta_1 + x_i\beta_2 + D_i x_i \gamma + u_i$ <br> `reg y x c.x#i.year` &rarr; $y_{it}=a+x_{it}\beta_{\color{red}{t}} + u_{it}$ |
| `##` | 两个变量及其交乘项  | `reg y x##z` &rarr; $y_i=a+x_i\beta_1+z_i\beta_2 + x_iz_i\beta_3 + u_i$|

--- - --

```stata
clear
input group   x
        1     30
        1     50
        2     40
        2     60
        2     80
        3     70
end 
```
```stata
. list group i.group i.group#c.x, clean  

              1.     2.     3.  1.group#  2.group#  3.group#
   group  group  group  group       c.x       c.x       c.x 
1.     1      1      0      0        30         0         0 
2.     1      1      0      0        50         0         0 
3.     2      0      1      0         0        40         0 
4.     2      0      1      0         0        60         0 
5.     2      0      1      0         0        80         0 
6.     3      0      0      1         0         0        70
```

--- - --

![bg left:25% w:260](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20220701091100.png)

```stata
. reg x i.group, noheader 

--------------------------------------------------
     x | Coefficient  Std. err.      t    P>|t|   
-------+------------------------------------------
 group |
    2  |     20.000     16.667     1.20   0.316   
    3  |     30.000     22.361     1.34   0.272   
       |
 _cons |     40.000     12.910     3.10   0.053   
--------------------------------------------------


. regfit

x =  40.00 + 0.00*1b.group + 20.00*2.group + 30.00*3.group
    (12.91) (0.00)          (16.67)         (22.36)
     N = 6, R2 = 0.43, adj-R2 = 0.05
```

--- - --

## 因子变量：设定基准组的运算符及含义

| 基准组运算符 | 含义 |
| :--- | :--- |
| `ib#.x` | 使用*作为基准组，*为变量中其中一类的值 |
| `ib(#*).x` | 使用变量值中的第*位排序的值所对应的类别作为基准组 |
| `ib(first).x` | 使用变量的最小值所对应的类别作为基准组 (该项为 Stata 默认选项) |
| `ib (last).x` | 使用变量的最大值所对应的类别作为基准组 |
| `ib( freq).x` | 使用变量值的频数最大的类别作为基准组 |
| `ibn.x` | 不设基准组 |

--- - --

### 例 1：种族与工资

模型设定：$Wage_i = \alpha + black_i\beta_1 + hours_i\beta_2 + black_i \times hours_i {\color{red}{\beta_3}} + u_i$

```stata
. sysuse "nlsw88.dta", clear

*-传统方法
. gen black=1
. replace black=0 if race!=2
. gen black_x_hours = black*hours
. reg wage black hours black_x_hours

*-因子变量法
. reg wage 2.race c.hours 2.race#c.hours
. reg wage 2.race##c.hours //与上一行等价

------------------------------------------------------------------------------
        wage | Coefficient  Std. err.      t    P>|t|     [95% conf. interval]
-------------+----------------------------------------------------------------
        race |
      Black  |     -1.619      1.266    -1.28   0.201       -4.101       0.864
       hours |      0.089      0.012     7.24   0.000        0.065       0.113
race#c.hours |
      Black  |      0.007      0.033     0.22   0.827       -0.057       0.071
       _cons |      4.810      0.474    10.14   0.000        3.880       5.741
------------------------------------------------------------------------------
```

--- - --

模型设定：$Wage_i = \alpha + B_i\beta_1 + h_i\beta_2 + B_i \times h_i {\color{red}{\beta_3}} + {\color{blue}{h_i^2\beta_4 + B_i\times h_i^2\beta_5}} + u_i$

```stata
. sysuse "nlsw88.dta", clear

. reg wage 2.race##c.hours##c.hours

-------------------------------------------------------------------
                wage |          Coeff       SE        t     P>|t|  
---------------------+---------------------------------------------
                race |
              Black  |         -3.461      2.274    -1.52   0.128  
               hours |          0.133      0.044     3.03   0.002  
                     |
        race#c.hours |
              Black  |          0.123      0.127     0.97   0.331  
                     |
     c.hours#c.hours |         -0.001      0.001    -1.05   0.296  
                     |
race#c.hours#c.hours |
              Black  |         -0.002      0.002    -0.95   0.344  
                     |
               _cons |          4.165      0.778     5.35   0.000  
-------------------------------------------------------------------
```

--- - --
<!-- backgroundColor: #FFFFF9 -->
## 时序变量的表示
帮助：[`help varlist`](https://www.stata.com/manuals/u11.pdf#u11.4varnameandvarlists)；[`help tsvarlist`](https://www.stata.com/manuals/u11.pdf#u11.4.4Time-seriesvarlists)
&#x1F34F; `reg y L.y L(0/2).x D.L.z` ${\color{red}{\rightarrow\ \ }}$  $\small y_t = a + \rho y_{t-1} + \sum_{s=0}^3 \theta_s x_{t-s} + \Delta z_{t-1} + u_t$

<br>

$$\footnotesize
\begin{array}{lll}
\text { Operator } & \text {Meaning } & \\
\hline 
\texttt { L.x } &  x_{t-1} & \text{1-period lag} \\
\texttt { L2.x } &  x_{t-2} & \text{2-period lag} \\
\ldots & \\
\texttt { F.x } &  x_{t+1} & \text{1-period lead} \\
\texttt { F2. } &  x_{t+2} & \text{ 2-period lead } \\
\ldots & \\
\texttt { D. } & \Delta x_t \ \ = x_{t}-x_{t-1} & \text {first difference } \\
\texttt { D2. } & \Delta^2 x_t = (x_{t}-x_{t-1})-\left(x_{t-1}-x_{t-2}\right) & \text{difference of difference} \\
\ldots & \\
\texttt { L(0/2).x } & x_{t}, x_{t-1}, x_{t-2} & \text {sevaral variables} \\
\texttt { L.D.x } & \Delta x_{t-1} & \text {can be nested} \\
\end{array}
$$

--- - --
<!-- backgroundColor: #e6e6fa -->
```stata
. use "https://www.stata-press.com/data/r17/gxmpl1", clear
. format gnp cpi %5.1f

. list year  L(1/3).(gnp cpi)  D.cpi, clean

                   L.      L2.      L3.      L.     L2.     L3.    D. 
       year      gnp      gnp      gnp     cpi     cpi     cpi   cpi  
 ---------------------------------------------------------------------
  1.   1989        .        .        .       .       .       .     .  
  2.   1990   5837.9        .        .   124.0       .       .   6.7  
  3.   1991   6026.3   5837.9        .   130.7   124.0       .   5.5  
  4.   1992   6367.4   6026.3   5837.9   136.2   130.7   124.0   4.1  
  5.   1993   6689.3   6367.4   6026.3   140.3   136.2   130.7   4.2  
  6.   1994   7098.4   6689.3   6367.4   144.5   140.3   136.2   3.7  
  7.   1995   7433.4   7098.4   6689.3   148.2   144.5   140.3   4.2  
  8.   1996   7851.9   7433.4   7098.4   152.4   148.2   144.5   4.5 
```

--- - --

```stata
. use "https://www.stata-press.com/data/r17/invest2", clear
. keep if time<=5&company<=2
. format invest market %4.1f
. list company time invest L(1/2).invest market D1.market

     +--------------------------------------------------------------+
     |                                L.      L2.                 D.|
     | company   time   invest   invest   invest   market    market |
     |--------------------------------------------------------------|
  1. |       1      1    317.6        .        .   3078.5         . |
  2. |       1      2    391.8    317.6        .   4661.7    1583.2 |
  3. |       1      3    410.6    391.8    317.6   5387.1     725.4 |
  4. |       1      4    257.7    410.6    391.8   2792.2   -2594.9 |
  5. |       1      5    330.8    257.7    410.6   4313.2    1521.0 |
     |--------------------------------------------------------------|
  6. |       2      1     40.3        .        .    417.5         . |
  7. |       2      2     72.8     40.3        .    837.8     420.3 |
  8. |       2      3     66.3     72.8     40.3    883.9      46.1 |
  9. |       2      4     51.6     66.3     72.8    437.9    -446.0 |
 10. |       2      5     52.4     51.6     66.3    679.7     241.8 |
     +--------------------------------------------------------------+

```




--- - --
<!-- backgroundColor: #C1CDCD -->

# 数据合并

--- - --
<!-- backgroundColor: white -->
### 数据合并: merge and append 

<br>

> **Source**: Lembcke, 2010, LSE Lectures. [PDF](https://personal.lse.ac.uk/lembcke/ecStata/2010/MResStataNotesOct2010PartA.pdf)


```stata
. use DataLeft, clear
. merge CTRY YEAR 1:1 using DataRight
```

![bg right:60% w:700](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20221110232954.png)

```stata
. use DataL, clear
. merge YEAR m:1 using DataR
```

--- - --
<!-- backgroundColor: #F1CDCD -->
## 数据的长宽转换 long <--> wide


<font color=black size=5>

- 专题：[数据处理](https://www.lianxh.cn/blogs/25.html)
  - [Stata：宽数据到长数据的转换-tolong](https://www.lianxh.cn/news/2d280cdccbe19.html)
  - [Stata数据处理：纵横长宽转换-reshape命令一文读懂！（下）-sreshape-fastreshape-xpose](https://www.lianxh.cn/news/4496d980350ea.html)
  - [Stata数据处理：纵横长宽转换-reshape命令一文读懂！（上）](https://www.lianxh.cn/news/5cc1220a0ea6f.html)
  - [Stata数据处理：纵横长宽转换-reshape的兄弟-gather和spread.md](https://www.lianxh.cn/news/264d23c9fda53.html)
  - [Stata数据处理：快速转换Wind数据-reshapewind](https://www.lianxh.cn/news/abac8de37fd18.html) 

</font> 


--- - --
<!-- backgroundColor: #FFFFF9 -->
```stata
           long
        +------------+                  wide
        | i  j   var |                 +----------------+
        |------------|                 | i   var1  var2 |
        | 1  1   4.1 |     reshape     |----------------|
        | 1  2   4.5 |   <--------->   | 1    4.1   4.5 |
        | 2  1   3.3 |                 | 2    3.3   3.0 |
        | 2  2   3.0 |                 +----------------+
        +------------+

       // long --> wide:

                                            j 旧变量名称
                                           /
                reshape wide year, i(i) j(j)

      //  wide --> long:

                reshape long stub, i(i) j(j)
                                           \
                                            j 新变量名称
```
--- - --

```stata
. reshape long inc ue, i(id) j(year)  //Note: [1] sex 不发生变化，无需转换
                                      //      [2] j() 选项中填写新的变量名称
```

![w:800](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20220630150958.png)


--- - --
### Frames 数据框
- [Stata：如何同时对多个数据框操作-frame](https://www.lianxh.cn/news/3d7f99828eda9.html)
- Stata manual, PDF - [introduction to frames](https://www.stata.com/manuals/dframesintro.pdf)
- [Data frames: multiple datasets in memory](https://www.stata.com/features/overview/multiple-datasets-in-memory/)，[视频讲解](https://www.youtube.com/watch?v=oaju5zTnXe8)

![stata-intro-Frame-002](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/stata-intro-Frame-002.png)


--- - --
<!-- backgroundColor: pink -->
## 离群值

- 界定
  
- 识别
- 应对


![bg right:70% w:750](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20221209092609.png)

--- - --
<!-- backgroundColor: white -->
<br>


![bg left:71% w:890](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/Anscombe1973_Figs.png)


<font color=black size=5>

> Source: [Anscombe, 1973, p.17](https://www.sjsu.edu/faculty/gerstman/StatPrimer/anscombe1973.pdf)

</font> 

--- - --
<!-- backgroundColor: white -->
### 离群值：应对方法

- $x$ &rarr; $ln(x)$
- 截尾处理 (Trimming)
- 缩尾处理 (Winsoring) 
- 离散化和标准化

  - [winsor2：离群值和异常值的缩尾处理](https://www.lianxh.cn/news/29b1139efd0bb.html)
  - [Stata：离群值！离群值？离群值！](https://www.lianxh.cn/news/6fd920ed55bf0.html)

--- - --

### 离群值：log 转换
![w:900](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/gr_Hist_wage_lnw.png)

--- - --

#### 缩尾 v.s 截尾

![w:900](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/trim_winsor_001.png)


--- - --
<!-- backgroundColor: white -->
### 离群值：离散化和标准化

<br>

> 您的家庭年收入？ &emsp;   5, 10, 100, 200, ……, 700
  - 离散化：连续变量 &rarr; 序别变量 / 虚拟变量
  
  - 标准化：$(0, +\infty)$ &rarr; $(-\infty,+\infty)$ &emsp;  $x_i^{s} = (x_i-\bar{x})/sd(x)\sim N(0,1)$
  - 限定范围：$(0, +\infty)$ &rarr; $(0,1)$ &emsp;  $x_i^{r} = (x_{max}-{x}_i)/x_{max}$

<br>

> 一年中交通违法的次数？去医院的次数？

<br>


--- - --
<!-- backgroundColor: #C1CDCD -->
## 缺失值 (略)
- 模式
- 缺失机制
- 补漏/补救 方法


--- - --
<!-- backgroundColor: white -->
### 缺失值：模式
- 单一模式 (Univariate Pattern)：缺失值均属于同一个变量
- 单调模式 (Monotone Pattern)：面板数据中被调查对象退出调查且后续不再返回
- 一般模式 (General Pattern)：缺失值在数据集中随机发生
  
<center>  

![20221209095150](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20221209095150.png)

--- - --
### 缺失值：机制 
- MCAR：完全随机缺失数据 (Missing Completely at Random)
  - 数据缺失的概率与数据集中的任何数据均无关；
- MAR：随机缺失数据 (Missing at Random)
  - 变量 $\small Y$ 数据缺失的概率与模型中其他变量相关，但与变量 $\small Y$ 本身无关；
- MNAR：非随机缺失数据 (Missing Not at Random)
  - 变量 $\small Y$ 数据缺失的概率即使在控制其他变量以后，仍与 $\small Y$ 本身有关。
--- - --
### 缺失值：机制 - 例子

![bg right:65% w:620](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20221209095906.png)


--- - --
### 缺失值：应对方法

#### M1：直接删除法

直接删除法中最常用的方法为成列删除和成对删除：

- 成列删除 (Listwise Deletion, Complete-Case Analysis)：删除所有存在缺失值的个体；
- 成对删除 (Pairwise Deletion, Available-Case Analysis)：只删除需要用到的变量存在缺失值的个体。

直接删除法简单、易操作，但是它们要求缺失数据是「完全随机缺失数据 (MCAR)」，否则会产生明显的偏误。此外，即使缺失数据满足 MCAR 条件，直接删除法会造成数据的浪费，大大削弱分析的效能 (reduce power)。

--- - --
### 缺失值：应对方法
#### M2：单一插补法

单一插补 (Single Imputation) 名称的由来是因为这些方法为每个缺失的数据点生成一个单一的替换值，与多重插补 (Multiple Imputation) 是不同的。多重插补是创建数据集的多个副本，并对每个副本使用不同的估计方法来估算缺失值。

- 算术平均插补法 (Arithmetic Mean Imputation)；
- 回归插补法 (Regression Imputation)；
- 随机回归插补法 (Stochastic Regression Imputation)。
- eg. 小朋友的身高 (Mum: 170cm, Dad: 175cm, Gogo: 171cm)

--- - --
### 缺失值：应对方法-多重插补法 

![20221209123549](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20221209123549.png)


<font color=black size=5>

Source: [Gabriella, 2021, S-in-M](https://onlinelibrary.wiley.com/doi/10.1002/sim.9231)

</font> 

--- - --

![20221209123704](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20221209123704.png)

<font color=black size=5>

Source: [Gabriella, 2021, S-in-M](https://onlinelibrary.wiley.com/doi/10.1002/sim.9231)

</font> 

--- - --

#### M3：多重插补法
- **插补阶段** (Imputation Phase)：创建数据集的 m 个副本，每个副本中包含对缺失值的不同估计；
- **分析阶段** (Analysis Phase)：将分析模型拟合到 m 个数据集中；
- **汇集阶段** (Pooling Phase)：使用 Rubin 法则将 m 组结果汇集成一个结果。

--- - --
<!-- backgroundColor: #FFFFF9 -->

### Missing Data Workshop  —— 模拟和实操代码

> Source: <https://www.trentonmize.com/teaching/miss>

<!-- > 已下载：D:\Lec\data-missing-outlier\refs\Mize-2019-missing-data -->

- [Slides](https://drive.google.com/open?id=1wbbC7TtQOoqY9EAIr_9ETd_IYfK59fbP)
- [Example Stata and R Code](https://drive.google.com/open?id=1EM9ix_Lo7Wnra0F5qadpK8lTrYD0CZkC)
- [Replication Files (Stata)](https://drive.google.com/open?id=1oiJNcUkTRxMKSK0eKLO5b9yIhW6-UCP6)

--- - --
<!-- backgroundColor: white -->
### 缺失值：扩展阅读

<font color=black size=5>

- 专题：[数据处理](https://www.lianxh.cn/blogs/25.html)
  - [Stata数据处理：缺失值填充-autofill-carryforward](https://www.lianxh.cn/news/965e1b0e58b76.html)
  - [Stata：fillmissing-缺失值填充-数值和文字的前后填充！](https://www.lianxh.cn/news/b89837b74ffcc.html)
  - [Stata数据处理：缺失值与多重补漏分析（一）](https://www.lianxh.cn/news/716da36e2cb70.html)
  - [Stata数据处理：缺失值与多重补漏分析（二）](https://www.lianxh.cn/news/c3e8128be3072.html)
  - [Stata数据处理：缺失值与多重补漏分析（三）](https://www.lianxh.cn/news/3b79ea976a27e.html)
  - [Stata：缺失值与多重补漏-misstable-D204](https://www.lianxh.cn/news/b8c80b65442ca.html)
  - [缺失值能否用零代替？-L117](https://www.lianxh.cn/news/0b6ffec361094.html)
  - [Stata：让缺失值一览无余](https://www.lianxh.cn/news/32c1992b13963.html)
  - [Stata缺失值专题：多重补漏分析](https://www.lianxh.cn/news/45e165baf163e.html)
  - [Stata：缺失值的填充和补漏](https://www.lianxh.cn/news/4404052e7b336.html)
- 专题：[面板数据](https://www.lianxh.cn/blogs/20.html)
  - [Stata：面板数据缺失值与多重补漏分析-twofold](https://www.lianxh.cn/news/77d0d450a3024.html)

</font> 



--- - --
<!-- backgroundColor: #C1CDCD -->

## Stata 数据处理：推文

&#x1F34F; Stata 命令：

```stata
. lianxh 数据处理 面板 
```

--- - --
<!-- backgroundColor: #FFFFF9 -->
### 推文：Stata 数据处理 (1)

- 专题：[Stata教程](https://www.lianxh.cn/blogs/17.html)
  - [普林斯顿Stata教程(一) - Stata数据处理](https://www.lianxh.cn/news/c98db865ea7fb.html)
- 专题：
  - [Stata数据处理：数据框使用教程](https://www.lianxh.cn/news/ea9890df3b47d.html)
  - [Stata数据处理：将字符变量编码为数值变量-encoder](https://www.lianxh.cn/news/9e4d009c25018.html)
  - [Stata数据处理：一文搞定CEIC数据库](https://www.lianxh.cn/news/0e5b28707f559.html)
  - [Stata数据处理：清洗中国城市建设统计年鉴](https://www.lianxh.cn/news/fb87f725952e8.html)
  - [Stata数据处理：清洗CFPS数据库](https://www.lianxh.cn/news/2916ae8363459.html)
  - [CFPS数据处理：少儿代答库与成人库匹配](https://www.lianxh.cn/news/22c7cd3ccacc1.html)
  
--- - --

### 推文：Stata 数据处理 (2)
  - [Stata数据处理：批量处理被保护的年鉴数据-dxls-txls](https://www.lianxh.cn/news/6f1b8057418de.html)
  - [Stata数据处理：缺失值与多重补漏分析（一）](https://www.lianxh.cn/news/716da36e2cb70.html)
  - [Stata数据处理：缺失值与多重补漏分析（二）](https://www.lianxh.cn/news/c3e8128be3072.html)
  - [Stata数据处理：缺失值与多重补漏分析（三）](https://www.lianxh.cn/news/3b79ea976a27e.html)
  - [Stata数据处理：一文读懂微观数据库清理（上）](https://www.lianxh.cn/news/f0ea677dfb682.html)
  - [Stata数据处理：一文读懂微观数据库清理（下）](https://www.lianxh.cn/news/cb05be5a4dc6e.html)
  - [Stata数据处理：iebaltab和ieddtab命令介绍-T208](https://www.lianxh.cn/news/f7112283137be.html)
  - [Stata数据处理：超大Excel文档如何读入](https://www.lianxh.cn/news/798d66e2c0acc.html)
  
--- - --

### 推文：Stata 数据处理 (3)
  - [滚动吧统计量！Stata数据处理](https://www.lianxh.cn/news/08bfff06551c4.html)
  - [Stata数据处理：各种求和方式一览](https://www.lianxh.cn/news/3ce33ba6750a7.html)
  - [Stata数据处理：字符型日期变量的转换](https://www.lianxh.cn/news/e19cec1139a11.html)
  - [Stata数据处理：统计组内非重复值个数](https://www.lianxh.cn/news/3f5d25925cd54.html)
  - [Stata数据处理：赫芬达尔指数-(hhi5)-命令介绍](https://www.lianxh.cn/news/b426fbef84f81.html)
  - [Stata数据处理：面板数据的填充和补漏](https://www.lianxh.cn/news/c2febe0f3530a.html)
  - [Stata数据处理：xtbalance-非平衡面板之转换](https://www.lianxh.cn/news/0146f8d3b2861.html)
  - [Stata 权重设定-fweight-pweight](https://www.lianxh.cn/news/4dbc40eb41c3d.html)



--- - --

<center>

## 连享会  &#x1F34E; 

### [lianxh.cn](https://www.lianxh.cn)


