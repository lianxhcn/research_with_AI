# B860：Stata 可视化：heatplot-热力图

写一篇推文，介绍 `heatplot` 命令的用法。主要参考资料如下：

- Ben Jann, 2019, [Heat (and hexagon) plots in Stata](https://www.stata.com/meeting/germany19/slides/germany19_Jann.pdf)

## 简介

Stata 模块 `heatplot` 用于绘制热力图和六边形热力图。

`heatplot` 可以基于变量或矩阵生成热力图。常见用法包括：将 X 和 Y 两个变量分箱后，统计每个组合出现的频率，并用颜色深浅来表示（即二维直方图）；也可以在 X 和 Y 的分箱格点上，用颜色梯度展示第三个变量 Z 的平均值，实现三元分布的可视化。此外，还可以直接用颜色梯度展示矩阵内容，比如相关系数矩阵或空间权重矩阵等。

## 安装方法

`heatplot` 是 Stata 中用于绘制热力图的强大工具。推荐通过 SSC 安装，具体步骤如下：

```stata
ssc install heatplot, replace
```

该命令依赖于 `palettes` 包（用于配色方案）以及 `colrspace` 包（Stata 14.2 及以上版本支持颜色空间管理）。请先安装这两个依赖：

```stata
ssc install palettes, replace
ssc install colrspace, replace
```

如果你希望使用 `heatplot` 的 `fast` 选项（加速大数据处理），还需安装 `gtools` 包：

```stata
ssc install gtools, replace
gtools, upgrade
```

此外，也可以直接从 GitHub 获取最新版（可能包含最新功能和修复）：

```stata
net install heatplot, replace from(https://raw.githubusercontent.com/benjann/heatplot/master/)
```

安装完成后，即可在 Stata 中使用 `heatplot` 进行热力图绘制。

## Stata 实操

> 写作说明：

执行 Ben Jann, 2019, [Heat (and hexagon) plots in Stata](https://www.stata.com/meeting/germany19/slides/germany19_Jann.pdf) 中的例子，配上说明文字。

图形模板：`set scheme cleanplots`

### 基本用法

以下是一个简单的 Stata 实操示例，演示如何使用 `heatplot` 绘制热力图：

```stata
. webuse nhanes2, clear
. heatplot weight height
``` 

![](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250708092845.png)

### 附加其他图形

```stata
hexplot weight height, statistic(count) color(plasma) ///
        cut(1(5)@max) keylabels(, range(1)) size ///
        addplot(lpolyci weight height, degree(1) psty(p2) lw(*1.5) ac(%50) alc(%0))
```

![](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250708093036.png)
