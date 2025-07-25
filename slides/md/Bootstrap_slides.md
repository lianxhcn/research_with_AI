---
marp: true
size: 16:9
paginate: true
---

<!-- Global style -->
<style>
h1 {
  color: darkyellow;
}
h2 {
  color: darkblue;
}
h3 {
  color: green;
}
</style>

<!--封面图片-->
![bg right:50% brightness:. sepia:50% w:500](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20221127233319.png)



<!--底部链接-->
<!-- footer: 连享会 · [推文](https://www.lianxh.cn) &nbsp;  | &nbsp;  lianxh.cn &nbsp; | &nbsp; [Bilibili](https://space.bilibili.com/546535876) &nbsp;| &nbsp; [课程](https://www.lianxh.cn/news/46917f1076104.html)-->

<!--顶部文字-->
#### [${\color{blue}{连享会·课程}}$](https://www.lianxh.cn/news/46917f1076104.html)



<!--幻灯片标题-->
# 再抽样方法 
> ### Resampling methods

<br>

- Bootstrap
- Jackknife 
- Permutation

<br>

<!--作者信息-->
#### [连玉君](https://www.lianxh.cn) (中山大学)
arlionn@163.com

<br>

--- - --

## 参考资料
- Hansen, B.E., Slides, [Bootstrap](https://www.ssc.wisc.edu/~bhansen/706/boot.pdf)
- Wikipedia, [Resampling (statistics)](https://en.wikipedia.org/wiki/Resampling_(statistics))
- Wikipedia, [Bootstrapping (statistics)](https://en.wikipedia.org/wiki/Bootstrapping_(statistics))
- Wikipedia, [Empirical distribution function](https://en.wikipedia.org/wiki/Empirical_distribution_function)
- Wikipedia, [Frequency (statistics)](https://en.wikipedia.org/wiki/Frequency_(statistics))
- [BOOTSTRAP IN NONSTATIONARY AUTOREGRESSION](https://dml.cz/bitstream/handle/10338.dmlcz/135473/Kybernetika_38-2002-4_1.pdf)

--- - --
<!-- backgroundColor: white -->
### 提纲 1

- 基本概念
  - 总体，抽样样本，经验样本
  - 标准差与标准误
  - 分布函数、分位数
- Bootstrap 基本原理
  - Bootstrap 标准误
  - Bootstrap 置信区间
  - Bootstrap 经验 p 值

--- - --
### 提纲 2

- Bootstrap 方法
  - Pair Bootstrap
  - Pamameter Bootstrap
  - Residuals Bootstrap
  - Wild Bootstrap
  - Block Bootstrap

--- - --

## Bootstrap 简史
The bootstrap was 
- published by [Bradley Efron](https://en.wikipedia.org/wiki/Bradley_Efron) in "Bootstrap methods: another look at the jackknife" (1979),[[5\]](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)#cite_note-5)[[6\]](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)#cite_note-6)[[7\]](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)#cite_note-7) inspired by earlier work on the [jackknife](https://en.wikipedia.org/wiki/Jackknife_resampling).[[8\]](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)#cite_note-Quenouille1949-8)[[9\]](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)#cite_note-Tukey1958-9)[[10\]](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)#cite_note-Jaeckel1972-10) 
- Improved estimates of the variance were developed later.[[11\]](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)#cite_note-Bickel1981-11)[[12\]](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)#cite_note-Singh1981-12) 
- A Bayesian extension was developed in 1981.[[13\]](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)#cite_note-Rubin1981-13) 
- The bias-corrected and accelerated (BCa) bootstrap was developed by Efron in 1987,[[14\]](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)#cite_note-BCa-14). 
- The ABC procedure in 1992.[[15\]](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)#cite_note-Diciccio1992-15)

> Source: Wikipedia, [Bootstrapping (statistics)](https://en.wikipedia.org/wiki/Bootstrapping_(statistics))

--- - --

![BS-01-population](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/BS-01-population.png)

--- - --

![BS-02-assum-normal](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/BS-02-assum-normal.png)

--- - --

![BS-03-pop-sample-bsample](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/BS-03-pop-sample-bsample.png)


--- - --

![w:950 BS-Bootstrap-resampling-method-001](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/BS-Bootstrap-resampling-method-002.png)

<!-- > Source: [resampling - Bootstrap](https://analystprep.com/cfa-level-1-exam/quantitative-methods/resampling/) -->

--- - --


![20241215000654](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20241215000654.png)

> Source: <https://datasciencebook.ca/inference.html#bootstrapping>


--- - --


### 参考文献
- Rubin, D. B. (1981). "The Bayesian bootstrap". *Annals of Statistics*, 9, 130.