
# B813：渐进DID的五种估计方法对比

> **作者：** xxx (xxx大学)    
> **邮箱：** <xxx@163.com> 

&emsp;

> **Source:** Wing, C., Yozwiak, M., Hollingsworth, A., Freedman, S., & Simon, K. (2024). Designing Difference-in-Difference Studies with Staggered Treatment Adoption: Key Concepts and Practical Guidelines. Annual Review of Public Health, 45(1), 485–505. [Link](https://doi.org/10.1146/annurev-publhealth-061022-050825), [PDF](https://www.annualreviews.org/docserver/fulltext/publhealth/45/1/annurev-publhealth-061022-050825.pdf?expires=1752678753&id=id&accname=guest&checksum=345B1C3C23D23EC0D6A9B385A91F2513), [Google](<https://scholar.google.com/scholar?q=Designing Difference-in-Difference Studies with Staggered Treatment Adoption: Key Concepts and Practical Guidelines>), [github-replication](https://github.com/hollina/arph-did-example)

&emsp;

- **Title**: 渐进式双重差分（DID）研究设计
- **Keywords**: 双重差分，渐进式，因果推断，政策评估

&emsp; 

## 1. 简介：渐进 DID 的综述  

在公共卫生、经济学、社会学等实证研究领域，我们经常需要回答“一项政策或干预是否有效”这类核心问题。比如：“新的医保支付方式是否降低了患者的住院费用？”“社区戒烟干预是否减少了吸烟率？”要回答这些问题，关键在于准确识别“处理”（政策/干预）与“结果”之间的因果关系，而双重差分（Difference-in-Difference, DID）方法正是实现这一目标的常用工具。  

DID方法的优势在于，它能通过对比“处理组”和“对照组”在“处理前后”的变化，有效剔除不随时间变化的组间差异（如地区固有医疗水平）和不随组变化的时间趋势（如全社会健康意识提升），从而分离出处理的净效应。但现实中的政策实施往往不是“一刀切”——比如，我国的“家庭医生签约服务”可能在2019年先在浙江试点，2021年推广到江苏，2023年再扩展到安徽，而部分省份至今未推行。这种“交错式处理实施”（不同群体在不同时间接受处理）的场景极为普遍。  

更复杂的是，处理效果往往“因人而异”：早期试点的浙江可能因经验积累，效果随时间增强；而后期推广的安徽可能因基础条件不同，效果较弱。这种“处理效应异质性”与“交错式实施”结合时，传统的分析方法就可能“失灵”。Wing等人2024年发表在《Annual Review of Public Health》的论文《Designing Difference-in-Difference Studies with Staggered Treatment Adoption: Key Concepts and Practical Guidelines》，正是针对这一问题，系统揭示了传统方法的局限，介绍了稳健的新方法，并给出了“手把手”的实操指南。  

对于初涉因果推断的博士生和青年学者，这篇论文的价值怎么强调都不为过：它不仅能帮你避免方法误用导致的“结论翻车”，更能让你的研究设计经得起顶级期刊审稿人的推敲。接下来，我们就一步步拆解这篇论文的核心内容，确保你读完就能上手应用。  


## 2. 核心概念：打好基础才能走远路  

### 2.1 双重差分（DID）：从“简单对比”到“因果推断”  
DID的逻辑可以用一个生活化的例子理解：假设你想知道“每天运动是否能减重”。你找了两组人，一组开始运动（处理组），一组不运动（对照组）。  
- 处理组运动前体重60kg，运动后55kg（变化-5kg）；  
- 对照组同期从62kg变为61kg（变化-1kg）；  
- 那么运动的净效应就是-5kg - (-1kg) = -4kg，即运动使体重减少4kg。  

用公式表示就是：  

$$
\text{处理效应} = \underbrace{(\text{处理组后} - \text{处理组前})}_{\text{处理组自身变化}} - \underbrace{(\text{对照组后} - \text{对照组前})}_{\text{对照组自然变化}}
$$
  

这个简单的“2×2 DID”（2组、2时间点）是所有DID方法的基础，但现实研究往往更复杂——当处理在不同时间点实施时，“处理组”和“对照组”的界限会变得模糊。  


### 2.2 交错式处理实施（Staggered Treatment Adoption）：现实中的“分批推行”  
交错式处理实施指处理不是在同一时间点覆盖所有研究单元，而是“分批生效”。比如：  
- 公共卫生领域：甲县2018年推行“高血压规范化管理”，乙县2020年推行，丙县2022年推行，丁县未推行；  
- 教育领域：A校2019年引入“在线教学平台”，B校2021年引入，C校未引入。  

这种场景下，“处理前”和“处理后”的划分因组而异：对甲县来说，2018年前是“前”，2018年后是“后”；对乙县来说，“前”是2020年前，“后”是2020年后。更棘手的是，某一时期的“对照组”可能在后期变成“处理组”（如乙县在2018-2019年是甲县的对照组，但2020年后成为处理组）。  


### 2.3 处理效应异质性（Heterogeneous Treatment Effects）：效果“因时因地而异”  
处理效应异质性指处理效果在不同维度存在差异，常见类型包括：  
- **时间异质性**：处理效果随实施时间变化。比如，“HPV疫苗接种”第1年保护率90%，第5年降至70%；  
- **群体异质性**：不同群体效果不同。比如，“戒烟干预”在高学历群体中效果更好；  
- **实施时间异质性**：早期实施组与晚期实施组效果不同。正如论文中模拟的“磺胺类药物”例子：1930年实施的地区，死亡率每年下降7.5人/10万；1940年实施的地区下降5人/10万；1945年实施的地区下降2.5人/10万。  

这三种异质性本身并不可怕，但当它们与“交错式实施”结合时，传统方法就可能得出错误结论——这正是论文要解决的核心问题。  


## 3. 传统方法的“陷阱”：双向固定效应模型（TWFE）为何会“骗人”？  
在很长一段时间里，研究者分析面板数据时，习惯用“双向固定效应模型（TWFE）”估计DID效应。其模型形式为：  

$$
Y_{ist} = \beta \cdot D_{ist} + \alpha_s + \gamma_t + \epsilon_{ist}
$$
  
其中， $Y_{ist}$是个体i在组s、时间t的结果（如死亡率）， $D_{ist}$是处理变量（1=接受处理，0=未接受）， $\alpha_s$是“组固定效应”（控制地区固有差异）， $\gamma_t$是“时间固定效应”（控制共同时间趋势）， $\epsilon_{ist}$是随机误差。  

看似完美的模型，在交错式实施和异质性并存时，却可能“翻车”。  


### 3.1 “子实验”视角：揭露TWFE的偏误根源  
论文提出一个关键视角：**任何交错式处理设计都是多个“2×2 DID子实验”的组合**。以甲县（2018）、乙县（2020）、丁县（未实施）为例，可拆分为：  
- 子实验1：甲县（处理组）vs 乙县+丁县（2018年前未实施，对照组），对比2017-2019年变化；  
- 子实验2：乙县（处理组）vs 丁县（2020年前未实施，对照组），对比2019-2021年变化。  

理想情况下，所有子实验都应使用“干净对照组”（从未实施或尚未实施的组）。但TWFE模型会自动纳入“有毒子实验”：比如，用“已实施处理的甲县”作为“乙县2020年处理”的对照组。此时甲县的时间趋势已受处理影响（如死亡率持续下降），不再是“干净”的对照，导致乙县的处理效应估计偏误。  


### 3.2 数学推导：偏误来自“早期处理组的效应变化”  
论文通过严谨推导证明，当处理效应随时间变化时，TWFE的估计值会包含一个“偏误项”。以“晚期处理组（A_s=a）”对比“早期处理组（A_s=b < a）”为例：  

$$
\text{TWFE偏误项} = E\left[\beta_{ist}(b)_{\text{处理后}} - \beta_{ist}(b)_{\text{处理前}}\right]
$$
  
即偏误源于“早期处理组自身的效应变化”。比如，甲县（2018年处理）的效应逐年增强（第1年降5人，第3年降10人），当乙县（2020年处理）以甲县为对照时，TWFE会错误地将甲县的“持续改善”归因于乙县的“处理无效”。  


### 3.3 模拟案例：TWFE如何得出“磺胺类药物有害”的荒谬结论？  
论文的磺胺类药物模拟数据清晰展示了这一问题：  
- 真实情况：早期处理组（1930）死亡率每年降7.5人，中期（1940）降5人，晚期（1945）降2.5人，从未处理组不变；  
- TWFE估计结果：却显示“磺胺类药物使死亡率上升5.1人/10万”（p=0.03），与事实完全相反。  

原因是TWFE赋予了“1940年组vs1930年组”这一“有毒比较”18%的权重——1930年组的死亡率下降早已是药物的持续效应，而非“自然趋势”，TWFE却将其当作“对照趋势”，最终得出错误结论。  


## 4. 稳健方法工具箱：6种“避坑”方法详解  
针对TWFE的局限，论文在Table 1中系统对比了6种稳健方法。以下结合“控烟政策与肺癌发病率”的例子，详解每种方法的原理、操作、适用场景和结果解读。  


### 4.1 Stacked DID（堆叠DID）：“拆分-净化-合并”三步法  

#### 原理  
将每个“处理实施事件”视为独立子实验，仅纳入“干净对照组”（子实验窗口内未受处理的组），再将所有子实验数据“堆叠”（纵向拼接）后回归。  

#### 操作步骤  
1. **拆分子实验**：例如，将浙江2019年控烟、江苏2021年控烟各视为一个子实验；  
2. **定义窗口**：为每个子实验设定统一的“事件时间窗口”（如处理前3年至处理后5年）；  
3. **筛选对照组**：子实验1（浙江2019）的对照组只能是“2019年前未控烟的江苏、安徽、未实施省份”；  
4. **堆叠数据**：将所有子实验的“组-时间-结果”数据纵向拼接；  
5. **回归估计**：用TWFE模型（控制“子实验-组”固定效应和“子实验-事件时间”固定效应）估计平均效应：  

$$
Y_{ised} = \sum_{b=-\kappa_{\text{pre}}}^{\kappa_{\text{post}}} \beta_b (D_{sd} \times 1[e=b]) + a_{sd} + b_{de} + \epsilon_{ised}
$$
  
其中， $e$是事件时间（如处理后第1年 $e=1$）， $a_{sd}$是子实验-组固定效应， $b_{de}$是子实验-事件时间固定效应。  

#### 适用场景  
- 处理实施时间分散（如跨度5年以上）；  
- 存在“从未实施处理”的组（如部分省份始终未控烟）；  
- 需一个“单一汇总效应”（如政策平均使肺癌发病率下降X%）。  

#### 结果解读  
若 $\beta_{\text{post}}$（处理后平均效应）为-8，则说明在所有子实验中，控烟政策平均使肺癌发病率下降8人/10万。论文的磺胺类药物例子中，堆叠DID估计的效应与真实值几乎一致（见图2b）。  

#### 工具推荐  
- 代码：可参考论文GitHub仓库的示例：<https://github.com/hollina/arph-did-example>；  
- 软件：Stata的`stackedev`命令、R的`dplyr`包（用于数据堆叠）。  


### 4.2 Callaway & Sant’Anna方法：“细分效应+灵活聚合”  
#### 原理  
先估计“组-时间平均处理效应（group-time ATT）”——即每个组在每个时间点的处理效应（如浙江2020年的效应、江苏2022年的效应），再根据研究需求聚合（如“所有组处理后第1年的平均效应”）。  

#### 操作步骤  
1. **定义对照组**：可选“从未处理组”或“尚未处理组”（推荐后者，样本量更大）；  
2. **估计组-时间ATT**：对每个组s（处理时间 $A_s=a$）和时间t，计算：  

$$
ATT(a,t) = E[Y_{ist}(a) - Y_{ist}(0) | A_s=a]
$$
  
即组s在时间t接受处理的平均效应；  
3. **聚合效应**：例如，按“事件时间”聚合（处理后k年的平均效应）：  

$$
\delta_q = \sum_a ATT(a, a+q) \times \text{权重}_a
$$
  
其中权重可按组样本量分配。  

#### 适用场景  
- 想分析“动态效应”（如控烟政策后1年、3年、5年的效果差异）；  
- 需对比不同实施时间组的效应（如浙江vs江苏的效果差异）。  

#### 结果解读  
- 若“处理后第1年 $\delta_1=-5$”“第3年 $\delta_3=-12$”，说明政策效果随时间增强；  
- 可绘制“事件研究图”（横轴为事件时间，纵轴为ATT），直观展示效应动态变化。  

#### 工具推荐  
- 软件：R的`did`包、Stata的`cysdid`命令；  
- 参考：论文GitHub仓库提供了该方法的实现代码。  


### 4.3 Gardner方法（两阶段DID）：“先净化趋势，再算效应”  
#### 原理  
分两阶段控制“组-时间趋势”，避免趋势差异被误判为处理效应：  
1. **第一阶段**：仅用“未受处理的样本”（如始终未控烟的省份）估计组固定效应和时间固定效应，得到“纯净趋势”；  
2. **第二阶段**：用所有样本，控制第一阶段的趋势，再估计处理效应。  

#### 操作步骤  
1. **筛选未处理样本**：如丁县（始终未控烟）的所有年份数据；  
2. **估计纯净趋势**：对未处理样本回归 $Y_{ist} = \alpha_s + \gamma_t + \epsilon_{ist}$，得到 $\hat{\alpha}_s$和 $\hat{\gamma}_t$；  
3. **估计处理效应**：对全样本回归 $Y_{ist} = \beta D_{ist} + \hat{\alpha}_s + \hat{\gamma}_t + \epsilon_{ist}$， $\beta$即为净效应。  

#### 适用场景  
- 未处理样本量大（如多数省份暂未控烟）；  
- 担心“处理组与对照组的固有趋势差异”干扰结果（如浙江原本肺癌发病率下降就比其他省份快）。  

#### 结果解读  
 $\beta$ 直接反映“净处理效应”，不受组间固有趋势差异的影响。例如，若 $\beta=-6$，说明排除固有趋势后，控烟政策仍使肺癌发病率下降6人/10万。  


### 4.4 Sun & Abraham方法：“饱和模型”捕捉细节  
#### 原理  
通过“交互项饱和”避免平均效应偏误：为每个组和每个时间点设置单独的交互项，单独估计效应后再聚合。  

#### 操作步骤  
1. **构建饱和模型**：纳入“组×时间”交互项，控制组固定效应和时间固定效应：  

$$
Y_{ist} = \sum_{s,t} \beta_{st} (1[s=s'] \times 1[t=t']) + \alpha_s + \gamma_t + \epsilon_{ist}
$$
  
2. **提取处理后效应**：仅关注处理组在处理后的 $\beta_{st}$（即组s在处理后时间t的效应）；  
3. **聚合**：按事件时间或日历时间合并效应（如处理后各年的平均效应）。  

#### 适用场景  
- 处理效应异质性极强（如城乡、贫富地区效果差异悬殊）；  
- 需精确识别“某类群体在特定时间的效应”（如贫困地区控烟后第2年的效应）。  


### 4.5 Wooldridge方法：“简单回归+灵活聚合”  
#### 原理  
用简单的OLS或固定效应模型直接估计“组-时间ATT”，支持灵活聚合，且允许纳入时间不变的协变量（如地区医疗资源）。  

#### 操作步骤  
1. **估计组-时间ATT**：通过 pooled OLS 回归：  

$$
Y_{ist} = \sum_{a,t} \beta_{a,t} (1[A_s=a] \times 1[t=t]) + \alpha_s + \gamma_t + X_{ist}\gamma + \epsilon_{ist}
$$
  
其中 $X_{ist}$是时间不变协变量（如是否有三甲医院）；  
2. **聚合效应**：可按“实施时间”“地区类型”等维度合并（如早期实施组的平均效应）。  

#### 适用场景  
- 初学者想兼顾“操作简单”和“结果细分”；  
- 需控制地区固有特征（如医疗资源）对政策效果的影响。  


### 4.6 de Chaisemartin & D’Haultfoeuille方法：“聚焦变化瞬间”  
#### 原理  
仅对比“处理状态刚变化的组”与“同期状态不变的组”，聚焦“政策实施瞬间”的效应，避免长期趋势干扰。  

#### 操作步骤  
1. **识别“变化组”与“不变组”**：例如，2021年江苏刚实施控烟（变化组），同期浙江已实施、丁县未实施（不变组）；  
2. **估计效应**：对比变化组与不变组在“变化前后”的结果差异，得到短期效应：  

$$
\text{效应} = (\text{变化组后} - \text{变化组前}) - (\text{不变组后} - \text{不变组前})
$$
  
3. **聚合所有变化瞬间的效应**，得到平均短期效应。  

#### 适用场景  
- 评估“短期效应”（如控烟政策实施后6个月的效果）；  
- 处理可能“时开时关”（如疫情期间的封锁政策反复实施）。  


### 4.7 方法选择“决策树”  
1. 若需“简单易操作+单一汇总效应”：选**Stacked DID**；  
2. 若需“动态效应分析+事件研究图”：选**Callaway & Sant’Anna**；  
3. 若未处理样本多+担心“趋势混淆”：选**Gardner**；  
4. 若效应异质性极强+需“精准细分”：选**Sun & Abraham**。  


## 5. 实操指南：从“数据准备”到“结果发表”的5步流程  
论文的Section 5提供了可直接落地的操作建议，以下结合“控烟政策”例子，详解每一步的具体操作。  


### 5.1 探索原始数据：画对图，心中有数  
**核心目的**：直观判断是否存在“交错实施”“效应异质性”和“预趋势”，为后续方法选择打基础。  

**具体操作**：  
1. **分组**：按“处理实施时间”将样本分为“早期组”（如浙江2019）、“晚期组”（如江苏2021）、“从未处理组”（如丁县）；  
2. **绘趋势图**：用折线图展示各组结果变量（如肺癌发病率）的时间趋势（横轴为年份，纵轴为发病率），用不同颜色区分组（参考论文图1）；  
3. **关键观察**：  
   - 处理前：各组趋势是否平行？（若早期组与从未处理组在2019年前趋势差异大，说明共同趋势假设可能不成立）；  
   - 处理后：处理组是否与对照组出现“分离趋势”？（如浙江2019年后下降更快，提示政策可能有效）；  
   - 异质性：早期组与晚期组的处理后趋势是否不同？（如浙江下降幅度大于江苏，说明存在实施时间异质性）。  

**工具推荐**：  
- 软件：Excel（插入折线图）、R（`ggplot2`包）、Stata（`twoway line`命令）；  
- 技巧：在图中标注“处理实施时间点”（如浙江2019年处画竖线），更直观。  


### 5.2 评估偏误风险：判断TWFE是否“可用”  
**核心目的**：量化传统TWFE的偏误程度，决定是否需要改用新方法。  

**具体操作**：  
1. **分析处理实施分布**：  
   - 若80%的组在1-2年内实施（如2020-2021年），TWFE偏误可能较小；  
   - 若实施时间跨度超过5年（如2018-2023年），偏误风险高。  
2. **用Goodman-Bacon分解诊断**：  
   - 工具：R的`bacondecomp`包、Stata的`bacon`命令；  
   - 输出：分解TWFE估计值为三类比较的加权平均：  
     - 处理组vs从未处理组（干净比较）；  
     - 早期组vs晚期组（干净比较）；  
     - 晚期组vs早期组（有毒比较）；  
   - 判断标准：若“有毒比较”的权重超过20%（如论文例子中为18%），强烈建议放弃TWFE。  
3. **检验效应异质性**：  
   - 方法：对不同实施时间组分别跑DID，若效应差异显著（如浙江降10人，江苏降3人），说明异质性强。  


### 5.3 选择并实施方法：“对号入座”写代码  
**核心目的**：根据数据特征选择合适方法，并完成基础分析。  

**以Stacked DID为例的操作细节**：  
1. **设定事件窗口**：如“处理前2年至处理后3年”（平衡数据，避免窗口过短/过长）；  
2. **构建子实验**：  
   - 子实验1（浙江2019）：纳入浙江（处理组）、2019年前未实施的江苏/安徽/丁县（对照组），时间范围2017-2022；  
   - 子实验2（江苏2021）：纳入江苏（处理组）、2021年前未实施的安徽/丁县（对照组），时间范围2019-2024；  
3. **堆叠数据**：用`rbind`（R）或`append`（Stata）纵向拼接子实验数据；  
4. **回归估计**：控制“子实验-组”和“子实验-事件时间”固定效应，代码参考论文GitHub仓库。  

**以Callaway & Sant’Anna为例的操作细节**：  
1. 定义处理时间变量（如`treat_year`：浙江=2019，江苏=2021，丁县=∞）；  
2. 用`did`包估计组-时间ATT：`att_gt = att_gt(yname="lung_cancer", tname="year", idname="province", gname="treat_year", data=data)`；  
3. 按事件时间聚合：`agg_effects = aggregate(att_gt, type="dynamic")`；  
4. 绘图：`plot(agg_effects)`得到事件研究图。  


### 5.4 交叉验证：用多种方法“互相印证”  
**核心目的**：避免单一方法的“固有局限”，增强结果可信度。  

**具体操作**：  
1. **至少用两种方法**：例如“Stacked DID”+“Callaway & Sant’Anna”，若两者结果方向一致（如均显示肺癌发病率下降5%-8%），则结论更可靠；  
2. **对比TWFE与稳健方法**：若TWFE结果与新方法差异大（如TWFE为-2，新方法为-7），需在论文中说明TWFE的偏误来源（参考论文图2b的对比）；  
3. **敏感性检验**：  
   - 改变控制组：仅用“从未处理组”vs包含“尚未处理组”；  
   - 调整窗口：事件窗口从“前2后3”改为“前3后2”，看结果是否稳定。  


### 5.5 稳健性检验：堵住“漏洞”，让审稿人无话可说  
**核心目的**：排除“预趋势”“遗漏变量”等替代性解释。  

**关键检验**：  
1. **预趋势检验**：  
   - 方法：在事件研究中加入“处理前系数”（如处理前1年、前2年），若系数接近0且不显著，说明满足“无预期假设”；  
   - 进阶：用Roth（2022）的方法计算“可检测的最小预趋势”，证明样本量足够拒绝“显著预趋势”。  
2. **安慰剂检验**：  
   - 方法：随机分配“虚假处理时间”（如将浙江的处理时间随机改为2017或2021），重复估计1000次，若真实效应远大于虚假效应的95%分位数，则结果可靠。  
3. **异质性分析**：  
   - 按“地区特征”分组（如城乡、收入水平），探讨效应差异的原因（如高收入地区效果更好，可能与医疗资源相关）。  


## 6. 总结与展望：初学者最该记住的“3个核心”  

1. **“交错+异质性”是“雷区”**：当政策分批实施且效果不同时，TWFE可能“撒谎”，务必用新方法验证；  
2. **“干净控制组”是“底线”**：任何稳健方法的核心都是避免用“已受处理的组”作对照，Stacked DID和Callaway & Sant’Anna是新手友好的“首选”；  
3. **“画图+诊断+验证”是“标配”**：永远从数据可视化开始，用Goodman-Bacon分解评估偏误，再用多种方法交叉验证——这是写出“无方法硬伤”论文的关键。  

这篇论文的价值不仅在于提供“工具”，更在于传递一种“研究思维”：因果推断的核心是“设计”而非“模型”。对于博士生和青年学者，掌握这些方法能让研究设计更严谨，结论更有说服力——而这正是在顶级期刊发表论文的“敲门砖”。  

最后提醒：论文的 [GitHub仓库](https://github.com/hollina/arph-did-example) 提供了模拟数据和代码，建议下载后“边跑代码边理解”，这是最快的上手方式！  

## 参考文献


==连老师修改建议：== 这部分内容是豆包自动生成的，还需要检查一下。如有必要，可以使用 [getiref 命令](https://www.lianxh.cn/details/1382.html) 自动生成，并根据 google 学术的结果补充 PDF 链接，working paper 版本也可以。  

1. Athey, S., & Imbens, G. W. (2022). Design-based analysis in Difference-In-Differences settings with staggered adoption. *Journal of Econometrics*, 226(1), 62–79. [Link](https://doi.org/10.1016/j.jeconom.2021.09.002), [PDF]（需从期刊数据库获取，如ScienceDirect等）, [Google](https://scholar.google.com/scholar?q=Design-based+analysis+in+Difference-In-Differences+settings+with+staggered+adoption+Athey+Imbens)
2. Borusyak, K., Jaravel, X., & Spiess, J. (2022). Revisiting event study designs: robust and efficient estimation. arXiv:2108.12419v2 [econ.EM]. [Link](https://arxiv.org/abs/2108.12419v2), [PDF](https://arxiv.org/pdf/2108.12419v2.pdf), [Google](https://scholar.google.com/scholar?q=Revisiting+event+study+designs%3A+robust+and+efficient+estimation+Borusyak+Jaravel+Spiess)
3. Caetano, C., Callaway, B., Payne, S., & Rodrigues, H. S. (2022). Difference in differences with time-varying covariates. arXiv:2202.02903 [econ]. [Link](https://arxiv.org/abs/2202.02903), [PDF](https://arxiv.org/pdf/2202.02903.pdf), [Google](https://scholar.google.com/scholar?q=Difference+in+differences+with+time-varying+covariates+Caetano+Callaway+Payne+Rodrigues)
4. Callaway, B., & Sant’Anna, P. H. C. (2021). Difference-in-Differences with multiple time periods. *Journal of Econometrics*, 225(2), 200–230. [Link](https://doi.org/10.1016/j.jeconom.2021.01.004), [PDF]（需从期刊数据库获取，如ScienceDirect等）, [Google](https://scholar.google.com/scholar?q=Difference-in-Differences+with+multiple+time+periods+Callaway+Sant%27Anna)
5. Cengiz, D., Dube, A., Lindner, A., & Zipperer, B. (2019). The effect of minimum wages on low-wage jobs. *The Quarterly Journal of Economics*, 134(3), 1405–1454. [Link](https://doi.org/10.1093/qje/qjz019), [PDF]（需从期刊数据库获取，如Oxford Academic等）, [Google](https://scholar.google.com/scholar?q=The+effect+of+minimum+wages+on+low-wage+jobs+Cengiz+Dube+Lindner+Zipperer)
6. Deshpande, M., & Li, Y. (2019). Who is screened out? Application costs and the targeting of disability programs. *American Economic Journal: Economic Policy*, 11(4), 213–248. [Link](https://doi.org/10.1257/pol.20170412), [PDF]（需从期刊数据库获取，如American Economic Association等）, [Google](https://scholar.google.com/scholar?q=Who+is+screened+out%3F+Application+costs+and+the+targeting+of+disability+programs+Deshpande+Li)
7. Dube, A., Girardi, D., Jordà, S., & Taylor, A. M. (2023). A local projections approach to difference-in-differences event studies. NBER Working Paper No. 31184. [Link](https://www.nber.org/papers/w31184), [PDF](https://www.nber.org/system/files/working_papers/w31184/w31184.pdf), [Google](https://scholar.google.com/scholar?q=A+local+projections+approach+to+difference-in-differences+event+studies+Dube+Girardi+Jord%C3%A0+Taylor)
8. Gardner, J. (2022). Two-stage differences in differences. arXiv:2207.05943 [econ]. [Link](https://arxiv.org/abs/2207.05943), [PDF](https://arxiv.org/pdf/2207.05943.pdf), [Google](https://scholar.google.com/scholar?q=Two-stage+differences+in+differences+Gardner)
9. Goodman-Bacon, A. (2018). Difference-in-differences with variation in treatment timing. NBER Working Paper No. 25018. [Link](https://www.nber.org/papers/w25018), [PDF](https://www.nber.org/system/files/working_papers/w25018/w25018.pdf), [Google](https://scholar.google.com/scholar?q=Difference-in-differences+with+variation+in+treatment+timing+Goodman-Bacon)
10. Goodman-Bacon, A. (2021). Difference-in-differences with variation in treatment timing. *Journal of Econometrics*, 225(2), 254–277. [Link](https://doi.org/10.1016/j.jeconom.2021.01.003), [PDF]（需从期刊数据库获取，如ScienceDirect等）, [Google](https://scholar.google.com/scholar?q=Difference-in-differences+with+variation+in+treatment+timing+Goodman-Bacon)
11. Han, X. (2018). Difference-in-differences with multiple time periods and heterogeneous treatment effects. Unpublished manuscript.（因未找到更多信息，按现有信息列出，实际引用时若有更多出版信息应补充完整）[Google](https://scholar.google.com/scholar?q=Difference-in-differences+with+multiple+time+periods+and+heterogeneous+treatment+effects+Han)
12. Hull, J. (2018). Difference-in-differences with heterogeneous treatment effects: A nonparametric identification and estimation approach. Unpublished manuscript.（因未找到更多信息，按现有信息列出，实际引用时若有更多出版信息应补充完整）[Google](https://scholar.google.com/scholar?q=Difference-in-differences+with+heterogeneous+treatment+effects%3A+A+nonparametric+identification+and+estimation+approach+Hull)
13. Imai, K., Kim, D., & Wang, M. (2018). Robust inference in difference-in-differences models: A synthesis of recent developments. Unpublished manuscript.（因未找到更多信息，按现有信息列出，实际引用时若有更多出版信息应补充完整）[Google](https://scholar.google.com/scholar?q=Robust+inference+in+difference-in-differences+models%3A+A+synthesis+of+recent+developments+Imai+Kim+Wang)
14. Shahn, Z., Dukes, O., Richardson, D., Tchetgen, E., & Robins, J. (2023). Structural nested mean models under parallel trends assumptions. arXiv:2204.10291 [stat.ME]. [Link](https://arxiv.org/abs/2204.10291), [PDF](https://arxiv.org/pdf/2204.10291.pdf), [Google](https://scholar.google.com/scholar?q=Structural+nested+mean+models+under+parallel+trends+assumptions+Shahn+Dukes+Richardson+Tchetgen+Robins)
15. Sun, L., & Abraham, S. (2021). Estimating dynamic treatment effects in event studies with heterogeneous treatment effects. *Journal of Econometrics*, 225(2), 175–199. [Link](https://doi.org/10.1016/j.jeconom.2021.01.002), [PDF]（需从期刊数据库获取，如ScienceDirect等）, [Google](https://scholar.google.com/scholar?q=Estimating+dynamic+treatment+effects+in+event+studies+with+heterogeneous+treatment+effects+Sun+Abraham)
16. Wooldridge, J. M. (2005). Fixed-effects and related estimators for correlated random-coefficient and treatment-effect panel data models. *Review of Economics and Statistics*, 87(2), 385–390. [Link](https://doi.org/10.1162/rest.87.2.385), [PDF]（需从期刊数据库获取，如MIT Press Journals等）, [Google](https://scholar.google.com/scholar?q=Fixed-effects+and+related+estimators+for+correlated+random-coefficient+and+treatment-effect+panel+data+models+Wooldridge)
17. Wooldridge, J. M. (2021). Two-way fixed effects, the two-way Mundlak regression, and difference-in-differences estimators. Working Paper, Michigan State University, East Lansing. [Google](https://scholar.google.com/scholar?q=Two-way+fixed+effects%2C+the+two-way+Mundlak+regression%2C+and+difference-in-differences+estimators+Wooldridge) 


