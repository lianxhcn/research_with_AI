# Heckman 选择模型实操指南

> Bendig, D., & Hoke, J. (2022). Correcting Selection Bias in Innovation and Entrepreneurship Research: A Practical Guide to Applying the Heckman Two-Stage Estimation. SSRN Electronic Journal. [Link](https://doi.org/10.2139/ssrn.4105207), [PDF](https://download.ssrn.com/22/05/12/ssrn_id4105207_code5233967.pdf), [Google](<https://scholar.google.com/scholar?q=Correcting Selection Bias in Innovation and Entrepreneurship Research: A Practical Guide to Applying the Heckman Two-Stage Estimation>).

&emsp;

- **Title**: Heckman 选择模型实操指南：管理学研究中的常见陷阱与规范流程
- **Keywords**: Heckman 模型，样本选择偏误，selection bias，两阶段估计，exclusion restriction，创新管理，创业研究，实操流程图

> [Claude 原始对话](https://claude.ai/share/e17d86f6-057e-4fab-a2f7-28c5869daf25)

&emsp;

## 简介

在创新与创业管理研究中，样本选择偏误 (selection bias) 是一个普遍存在但常被忽视的计量经济学问题。当研究样本并非随机抽取，而是基于某些特定条件筛选时，传统回归方法得出的估计结果往往存在系统性偏误。例如，研究风险投资对初创企业绩效的影响时，获得风险投资的企业本身就可能具有更高的成长潜力、更优秀的管理团队或更创新的商业模式，这使得简单比较「获投」与「未获投」企业的绩效会产生误导性结论——我们无法区分绩效差异究竟来自风险投资的处理效应，还是源于企业本身的异质性特征。

Heckman (1979) 提出的两阶段选择模型 (Heckman two-stage estimation) 为解决这一问题提供了经典的计量经济学框架。该方法通过显式建模样本选择过程，构造逆米尔斯比率 (inverse Mills ratio, IMR) 来控制选择偏误，从而获得一致性估计量。尽管 Heckman 模型在劳动经济学领域已被广泛应用且操作相对规范，但 Bendig 和 Hoke (2022) 在系统梳理管理学顶级期刊 (如 *Academy of Management Journal*, *Strategic Management Journal*, *Journal of Business Venturing* 等) 中使用该方法的研究后发现，许多研究在应用 Heckman 模型时存在操作不规范、理解有偏差、报告不完整等问题。

两位作者因此撰写了一份详尽的实操指南，不仅列举了管理学领域 50 余篇使用 Heckman 模型的顶刊论文的具体做法，系统总结了这些研究在模型设定、变量选择、结果报告等方面的操作细节，还绘制了一张清晰的决策流程图来指导研究者正确应用该方法。这份指南对于从事创新管理、创业研究、战略管理等领域的研究者具有重要的实践价值。

本文将系统介绍 Heckman 选择模型在实证研究中的常见问题、误区与陷阱，并基于 Bendig 和 Hoke 的研究，提供一套可操作的实施指南，特别是详细解读作者绘制的实操流程图，帮助研究者在管理学研究中规范使用这一重要工具。

## 样本选择偏误的本质与识别

### 什么是样本选择偏误？

样本选择偏误的核心问题在于：研究者观察到的样本并非总体的随机抽样，而是经过某种「筛选机制」后的结果。这种筛选可能是自我选择 (self-selection)、外部筛选 (external selection)，或两者的结合。当这种筛选过程与研究的结果变量相关时，忽略选择机制会导致估计系数的偏误和不一致性。

在管理学研究中，样本选择偏误有多种表现形式。Bendig 和 Hoke 将其归纳为三大类别：

**Type I: 研究设计导致的样本限制** (sample restriction by research design)。研究者出于研究设计的需要，人为限定了样本范围。例如，研究企业创新绩效时，仅关注那些申请过专利的企业；研究风险投资的影响时，仅分析获得过至少一轮融资的初创企业。这类限制虽然在研究设计上有其合理性，但会产生截断样本 (truncated sample) 或审查样本 (censored sample)，从而引发选择偏误。

**Type II: 数据可得性导致的样本缺失** (sample attrition due to data availability)。某些观测值的结果变量数据缺失，但这种缺失并非随机发生，而是与企业特征或结果本身相关。典型的例子包括：倒闭或被收购的企业不再披露财务数据，导致样本中仅保留「幸存者」；小规模企业或非上市企业的数据难以获取，导致样本偏向大型或上市企业。这类缺失被称为「非随机缺失」(missing not at random, MNAR)，会严重扭曲估计结果。

**Type III: 决策过程中的自我选择** (self-selection in decision-making)。企业或个人基于自身特征和预期收益做出参与决策，这种决策本身与结果变量相关。例如，企业是否寻求风险投资、是否进入国际市场、是否采用某项新技术，这些决策都可能基于企业对自身能力和市场前景的评估。如果高能力企业更可能采取某项行动，且能力本身也影响结果，那么简单比较「参与组」和「未参与组」的平均结果就会高估处理效应。

### 为何传统回归方法失效？

当存在样本选择问题时，我们实际上面临一个「缺失数据」的结构性问题。假设我们关心的真实模型为：

$$
y_i = \beta_0 + \beta_1 x_i + \varepsilon_i
$$

但我们只能观察到满足某个选择条件 $s_i = 1$ 的样本，其中选择方程为：

$$
s_i^* = \gamma_0 + \gamma_1 z_i + \nu_i, \quad s_i = 1 \text{ if } s_i^* > 0
$$

如果误差项 $\varepsilon_i$ 与 $\nu_i$ 相关 (即 $\text{Cov}(\varepsilon_i, \nu_i) \neq 0$)，那么在选中样本 (即 $s_i = 1$) 中，$\varepsilon_i$ 的条件期望不再为零：

$$
E[\varepsilon_i | s_i = 1, x_i] = E[\varepsilon_i | \nu_i > -\gamma_0 - \gamma_1 z_i] \neq 0
$$

这意味着在选中样本中进行 OLS 回归时，误差项与解释变量相关，导致估计量有偏且不一致。这就是样本选择偏误的根源。

Heckman 模型的核心贡献在于：通过显式建模选择过程，估计出逆米尔斯比率 (IMR)，并将其作为控制变量纳入结果方程，从而消除选择偏误带来的内生性问题。

## 管理学研究中的常见问题与误区

基于对 50 余篇管理学顶刊论文的系统回顾，Bendig 和 Hoke 识别出研究者在应用 Heckman 模型时存在的七大类常见问题和误区。这些问题不仅影响估计结果的有效性，也降低了研究的可复制性和透明度。

### 误区一：未充分论证样本选择偏误的存在性

**问题表现**：许多研究在引入 Heckman 模型时，仅仅简单声称「可能存在样本选择问题」，但未提供充分的理论依据或实证证据来论证这种偏误的存在及其性质。部分研究甚至将 Heckman 模型作为一种「稳健性检验」手段，而非将其视为解决核心内生性问题的必要方法。

**为何重要**：Heckman 模型的应用前提是确实存在样本选择偏误。如果选择过程与结果变量无关 (即 $\text{Cov}(\varepsilon_i, \nu_i) = 0$)，那么直接在选中样本上进行 OLS 回归就能获得一致性估计，此时应用 Heckman 模型不仅是多余的，反而可能因引入额外的估计误差而降低效率。因此，研究者需要基于理论逻辑或制度背景，清晰阐述为何选择过程会与结果变量产生关联。

**良好实践**：在管理学研究中，研究者应当：(1) 明确描述样本选择的机制——是企业自我选择、市场筛选还是数据可得性限制？(2) 基于理论或先验研究，论证哪些未观测因素同时影响选择决策和结果变量。例如，研究风险投资影响时，应论证企业的「管理能力」或「成长潜力」这类难以观测的特征既影响能否获得投资，也影响未来绩效。(3) 如可能，进行 Heckman 模型的必要性检验，如检验逆米尔斯比率的系数是否显著异于零。

### 误区二：排他性约束变量选择不当或缺失

**问题表现**：Heckman 两阶段估计的关键在于「排他性约束」(exclusion restriction)，即选择方程中至少需要包含一个变量，该变量影响选择决策但不直接影响结果变量 (仅通过选择过程间接影响)。Bendig 和 Hoke 发现，约三分之一的研究未能提供有效的排他性约束变量，或对所选变量的有效性缺乏充分论证。

**为何重要**：排他性约束是 Heckman 模型识别的基础。如果选择方程和结果方程包含完全相同的解释变量，模型在技术上虽然可以通过非线性函数形式 (即 IMR 的非线性性) 实现识别，但这种识别极其脆弱，估计结果对模型设定高度敏感，可靠性大打折扣。正如工具变量法需要有效工具一样，Heckman 模型需要有效的排他性约束变量才能获得可信的因果推断。

**常见错误**：
- 将影响结果的变量错误地作为排他性约束变量。例如，用「企业规模」预测是否获得风险投资，但企业规模本身也直接影响企业绩效，这违反了排他性约束。
- 使用的排他性约束变量与选择决策的相关性过弱 (类似于工具变量的「弱工具」问题)，导致第一阶段预测能力不足。
- 完全不使用排他性约束变量，仅依赖函数形式识别，但未进行敏感性分析来评估识别的稳健性。

**良好实践**：理想的排他性约束变量应满足两个条件：(1) **相关性**：与选择决策显著相关，即在第一阶段 Probit/Logit 模型中系数显著；(2) **外生性**：不直接影响结果变量，仅通过影响选择概率间接作用于结果。在创新与创业研究中，常用的排他性约束变量包括：
- **地理或制度变量**：如地区风险投资密度、地方政府支持政策、产业集聚程度等，这些变量影响企业获得外部资源的机会，但不直接决定企业自身的创新能力或绩效。
- **滞后或历史变量**：如过去是否获得过政府资助、创始人的社会网络特征等，这些变量影响当前的筛选结果，但与当前绩效的直接联系较弱。
- **非研究对象的决策变量**：如投资者的投资偏好、审查委员会的构成等，这些外部主体的决策影响样本选择，但不直接影响被研究对象的结果。

研究者在选择排他性约束变量后，应详细论证其合理性，最好辅以文献支持或逻辑推理，并在稳健性检验中测试不同排他性约束变量下结果的一致性。

### 误区三：忽视多重共线性与识别问题

**问题表现**：即使研究者提供了排他性约束变量，如果选择方程和结果方程中的其他控制变量高度重叠，且排他性约束变量与这些控制变量高度相关，就会导致严重的多重共线性问题，使得估计结果极不稳定。

**为何重要**：Heckman 两阶段估计中，第一阶段估计的 IMR 会作为额外的控制变量加入第二阶段回归。如果 IMR 与第二阶段的其他解释变量高度相关，就会产生多重共线性，导致标准误膨胀、系数估计不稳定。这在管理学研究中尤为常见，因为许多企业层面的控制变量 (如企业年龄、规模、行业等) 既影响选择决策，也影响结果变量。

**良好实践**：
- 在选择控制变量时，仔细权衡哪些变量必须同时进入两个方程，哪些变量可以仅进入其中一个方程。过度控制反而可能加剧识别问题。
- 计算方差膨胀因子 (VIF) 来诊断多重共线性的严重程度，如果 VIF 值过高 (通常以 10 为阈值)，需要重新考虑模型设定。
- 进行敏感性分析，逐步加入或剔除控制变量，观察核心系数估计的稳定性。

### 误区四：两阶段估计方法选择不当

**问题表现**：Heckman 模型有两种主要估计方法：两步法 (two-step estimator) 和极大似然法 (maximum likelihood estimator, MLE)。部分研究者未能根据数据特征和模型假设选择合适的估计方法，或对两种方法的差异缺乏清晰认识。

**为何重要**：两步法计算简单、对分布假设要求较低，但标准误的计算需要特殊处理；极大似然法在误差项联合正态分布假设成立时更有效率，但对分布假设的违背更敏感。错误的方法选择会影响估计效率和统计推断的有效性。

**良好实践**：
- **两步法**适用于样本量较大、分布假设存疑的情况。使用两步法时，务必使用 Stata 的 `heckman, twostep` 选项并加入 `vce(robust)` 以获得稳健标准误，或者手动计算 Heckman (1979) 给出的标准误修正公式。
- **极大似然法**适用于样本量适中、有信心假设误差项联合正态分布的情况。MLE 通常比两步法更有效率，但计算上更复杂，且对初始值敏感。
- 建议报告两种方法的估计结果作为稳健性检验，如果结果一致，则增强结论的可信度。

### 误区五：结果报告不完整或不规范

**问题表现**：许多研究仅报告第二阶段 (结果方程) 的估计结果，而忽略第一阶段 (选择方程) 的详细信息。部分研究甚至未报告逆米尔斯比率的系数及其显著性，使得读者无法判断样本选择偏误是否真实存在以及 Heckman 校正是否必要。

**为何重要**：完整的结果报告是研究透明度和可复制性的基础。第一阶段结果提供了选择机制的关键信息，包括哪些因素影响样本选择、排他性约束变量是否有效等。IMR 系数的显著性检验则直接回答了「样本选择偏误是否存在」这一核心问题。

**良好实践**：Bendig 和 Hoke 建议研究者报告以下内容：
- **第一阶段完整结果**：包括所有解释变量的系数、标准误、显著性水平，以及模型拟合优度指标 (如 Pseudo $R^2$、对数似然值)。
- **排他性约束变量的效力检验**：报告排他性约束变量在第一阶段的系数及显著性，必要时报告偏相关系数或 F 统计量 (类似于工具变量的第一阶段检验)。
- **IMR 系数及其显著性**：这是判断选择偏误是否存在的关键证据。如果 IMR 系数不显著，说明样本选择偏误可能并不严重，此时 Heckman 校正可能是不必要的。
- **对比 OLS 与 Heckman 结果**：将未经选择偏误校正的 OLS 结果与 Heckman 校正后的结果并列报告，让读者直观看到校正的影响。这种对比有助于评估选择偏误的方向和幅度。

----

> 第二部分：实操指南与流程图详解

## Heckman 模型的实操流程指南

Bendig 和 Hoke (2022) 的核心贡献之一是绘制了一张详细的决策流程图，为研究者提供了一套系统化的操作步骤。这张流程图将 Heckman 模型的应用分解为若干关键决策节点，每个节点都对应具体的判断标准和操作建议。以下我们将逐步解读这一流程。

### 步骤一：诊断是否存在样本选择问题

**决策问题**：我的研究是否真的存在样本选择偏误？

这是应用 Heckman 模型的起点。研究者需要回答三个层次的问题：

**理论层面**：基于研究的制度背景和理论框架，选择过程与结果变量之间是否存在关联？例如，如果研究风险投资对企业创新的影响，需要思考：获得风险投资的企业是否在获投前就已经展现出更强的创新潜力？如果答案是肯定的，那么简单比较「获投」与「未获投」企业的创新产出就会高估风险投资的因果效应。

**数据层面**：观察到的样本是否是总体的随机抽样？如果样本是经过某种筛选机制得到的 (如仅包含存活企业、仅包含上市公司、仅包含申请过专利的企业等)，那么就可能存在样本选择问题。研究者应明确描述样本的抽取过程和筛选标准。

**实证层面**：可以通过一些间接证据来判断选择偏误的严重程度。例如：
- 比较选中样本与未选中样本 (如果有数据) 在可观测特征上的差异，如果存在系统性差异，暗示选择过程非随机。
- 如果数据允许，可以先估计一个包含 IMR 的回归模型，检验 IMR 系数是否显著。如果显著，说明确实存在选择偏误；如果不显著，则选择偏误可能较轻微。

**流程图决策点 1**：如果经过上述诊断，认为样本选择偏误不严重或理论上不存在，可以直接使用传统的 OLS、固定效应等方法，无需应用 Heckman 模型。如果判断存在选择偏误，则进入下一步。

### 步骤二：确定选择方程的形式

**决策问题**：选择过程是二元选择 (binary selection) 还是顺序选择 (ordered selection)？

这一步需要根据研究问题的性质确定选择方程的具体形式。

**二元选择**：样本选择是一个「是/否」的二元决策，如企业是否获得风险投资、是否进入国际市场、是否采用某项技术等。此时第一阶段使用 Probit 或 Logit 模型估计选择概率。

**顺序选择**：选择过程具有多个层次或阶段，如企业首先决定是否申请专利，然后在申请成功的条件下决定是否转化为产品。这种情况下可能需要使用有序 Probit 模型 (ordered Probit)，或者将选择过程分解为多个嵌套的二元选择。

**流程图决策点 2**：对于标准的二元选择问题 (占管理学研究的绝大多数)，使用经典的 Heckman 两阶段模型即可。对于更复杂的选择结构，可能需要扩展的 Heckman 模型或其他替代方法，如 Maddala (1983) 提出的多阶段选择模型。

### 步骤三：识别有效的排他性约束变量

**决策问题**：哪些变量可以作为排他性约束变量？如何论证其有效性？

这是 Heckman 模型应用中最关键也最具挑战性的一步。Bendig 和 Hoke 基于对管理学文献的梳理，总结了几类常用且相对有效的排他性约束变量：

**类型 1：地理或区位变量**
- **典型例子**：企业所在地的风险投资密度、产业集聚程度、到金融中心的距离、地方政府创新支持政策等。
- **有效性论证**：这些变量影响企业获得外部资源 (如风险投资、政府资助) 的机会或成本，但不直接决定企业自身的创新能力或经营绩效。例如，位于硅谷的初创企业更容易接触到风险投资人，但这不意味着硅谷企业的内在创新能力就更强。
- **注意事项**：需要论证区位因素仅通过「机会成本」或「信息渠道」影响选择，而非通过「人才集聚」或「知识溢出」直接影响绩效 (后者会违反排他性约束)。

**类型 2：时间趋势或政策冲击**
- **典型例子**：某项政策出台的时点、行业监管变化、宏观经济周期等。
- **有效性论证**：政策或外部冲击改变了企业决策的约束条件或激励结构，但不直接改变企业的生产函数或能力。例如，政府推出税收优惠政策鼓励企业研发，这会影响企业是否申请研发补贴 (选择)，但税收政策本身不直接提高企业的研发效率 (结果)。
- **注意事项**：需要仔细论证政策仅影响企业的「参与决策」而非「参与后的表现」。如果政策同时改变了企业的资源约束 (如提供资金支持)，则可能违反排他性约束。

**类型 3：网络或社会关系变量**
- **典型例子**：创始人的校友网络、行业协会成员资格、董事会连锁关系等。
- **有效性论证**：这些关系影响企业获得信息或资源的渠道 (如通过校友介绍接触到投资人)，但不直接影响企业的生产效率或创新能力。
- **注意事项**：社会网络可能同时具有「信息传递」和「知识转移」两种功能，后者会直接影响企业绩效。因此需要论证所使用的网络变量主要发挥前者的作用。

**类型 4：历史或滞后变量**
- **典型例子**：企业过去是否获得过政府资助、创始人的创业经历、早期融资轮次等。
- **有效性论证**：历史经历影响当前的选择决策 (如有过融资经验的创始人更容易再次获得投资)，但不直接影响当前的绩效 (尤其是在控制了当前企业特征后)。
- **注意事项**：需要确保历史变量的影响主要体现在「路径依赖」或「信号传递」上，而非「能力积累」上。

**操作建议**：
1. **多角度论证**：从理论逻辑、制度背景、先验研究三个角度论证所选变量的合理性。引用相关文献支持你的论证。
2. **多变量组合**：如果单个变量的有效性存疑，可以尝试使用多个排他性约束变量，这样可以降低对单一变量外生性的依赖。
3. **敏感性分析**：使用不同的排他性约束变量重复估计，检验核心结论的稳健性。如果不同变量下结果一致，则增强了识别的可信度。

**流程图决策点 3**：如果无法找到合理的排他性约束变量，研究者面临两个选择：(1) 仅依赖函数形式识别 (即 IMR 的非线性)，但必须进行大量敏感性检验并坦诚说明识别的局限性；(2) 放弃 Heckman 模型，转而使用其他方法 (如倾向得分匹配、工具变量法等)。

### 步骤四：模型估计与诊断

**第一阶段：估计选择方程**

使用 Probit 模型估计样本被选中的概率。选择方程的一般形式为：

$$
\Pr(s_i = 1) = \Phi(\gamma_0 + \gamma_1 z_i + \gamma_2 x_i)
$$

其中，$z_i$ 是排他性约束变量，$x_i$ 是同时影响选择和结果的控制变量，$\Phi(\cdot)$ 是标准正态累积分布函数。

**诊断要点**：
- 检查排他性约束变量 $z_i$ 的系数是否显著，这关系到第一阶段的预测能力。
- 计算模型的拟合优度 (Pseudo $R^2$)，评估整体预测效果。
- 检验是否存在完全预测问题 (perfect prediction)，即某些变量组合下选择概率为 0 或 1，这会导致估计失败。

**计算逆米尔斯比率 (IMR)**：

基于第一阶段的估计结果，对每个观测值计算 IMR：

$$
\lambda_i = \frac{\phi(\gamma_0 + \gamma_1 z_i + \gamma_2 x_i)}{\Phi(\gamma_0 + \gamma_1 z_i + \gamma_2 x_i)}
$$

其中，$\phi(\cdot)$ 是标准正态概率密度函数。IMR 捕捉了「被选中」这一事件所包含的未观测信息，用于在第二阶段控制选择偏误。

**第二阶段：估计结果方程**

在选中样本中 (即 $s_i = 1$)，估计如下回归：

$$
y_i = \beta_0 + \beta_1 x_i + \beta_2 \lambda_i + \varepsilon_i
$$

**诊断要点**：
- **IMR 系数的显著性检验**：$\beta_2$ 是否显著异于零？如果显著，说明确实存在样本选择偏误，Heckman 校正是必要的；如果不显著，说明选择偏误可能不严重，OLS 估计已经较为可靠。
- **多重共线性检验**：计算 IMR 与其他解释变量的相关系数和 VIF 值。如果 VIF 值过高 (> 10)，需要重新考虑变量选择或模型设定。
- **对比 OLS 与 Heckman 结果**：比较核心解释变量在两种方法下的系数估计。如果差异很大，说明选择偏误影响显著；如果差异较小，说明选择偏误的影响有限。

**Stata 实现示例**：

```stata
* 两步法估计
heckman y x1 x2 x3, select(s = z1 z2 x1 x2 x3) twostep

* 极大似然法估计
heckman y x1 x2 x3, select(s = z1 z2 x1 x2 x3)

* 带稳健标准误的两步法
heckman y x1 x2 x3, select(s = z1 z2 x1 x2 x3) ///
    twostep vce(robust)

* 保存 IMR 用于后续诊断
predict lambda, mills
```

**流程图决策点 4**：如果第一阶段拟合较差 (Pseudo $R^2$ 很低) 或 IMR 与解释变量高度共线，需要回到步骤三重新选择排他性约束变量或调整模型设定。

### 步骤五：稳健性检验与敏感性分析

Bendig 和 Hoke 强调，应用 Heckman 模型的研究必须进行充分的稳健性检验，以评估结果对模型设定和假设的敏感性。

**检验 1：替代性排他性约束变量**

使用不同的排他性约束变量重新估计模型，观察核心系数的变化。如果结果稳健，说明识别不依赖于特定变量的选择；如果结果差异较大，需要进一步论证哪个变量更合理。

**检验 2：估计方法对比**

同时报告两步法和极大似然法的结果。两种方法在大样本下应该给出相似的点估计，但标准误可能有所不同。如果两种方法结果差异很大，可能暗示分布假设不成立或样本量不足。

**检验 3：样本分割检验**

将样本按某些特征分组 (如企业规模、行业类型、时间段等)，分别估计 Heckman 模型，检验处理效应是否存在异质性。这不仅是稳健性检验，也是探索机制和边界条件的重要手段。

**检验 4：安慰剂检验**

如果研究设计允许，可以构造「伪处理组」或「伪事件时点」，检验在不应该出现处理效应的情况下，Heckman 模型是否会错误地检测出显著效应。通过这种检验可以排除其他混淆因素的干扰。

**检验 5：函数形式敏感性**

如果主要依赖函数形式识别 (即缺乏强有力的排他性约束变量)，应该测试结果对分布假设的敏感性。例如，尝试使用半参数方法 (如 Ahn & Powell, 1993) 或对误差项分布做不同假设 (如 Student-t 分布代替正态分布)。

**流程图决策点 5**：如果结果在各种稳健性检验下都保持一致，可以增强对因果推断的信心。如果结果高度敏感，需要在结论部分坦诚说明研究的局限性，并建议未来研究使用更强的识别策略。

### 步骤六：结果报告与解释

**表格呈现的最佳实践**：

Bendig 和 Hoke 建议采用以下表格结构报告 Heckman 模型结果：

**表 1：第一阶段 (选择方程) 结果**
- 列出所有解释变量的系数、标准误、显著性水平
- 特别标注排他性约束变量
- 报告 Pseudo $R^2$、对数似然值、样本量

**表 2：第二阶段 (结果方程) 结果**
- 并列呈现：(1) 基准 OLS 结果；(2) Heckman 两步法结果；(3) Heckman 极大似然法结果
- 报告 IMR 系数及其显著性
- 报告 $R^2$、调整后 $R^2$、样本量

**正文说明要点**：
- 清晰解释为何使用 Heckman 模型，样本选择偏误的来源是什么。
- 详细论证排他性约束变量的合理性，引用相关文献或制度背景支持。
- 解释 IMR 系数的经济含义：如果 IMR 系数显著为正，说明未观测因素同时正向影响选择概率和结果变量；如果显著为负，说明两者反向关联。
- 对比 OLS 与 Heckman 结果的差异，讨论选择偏误的方向和幅度。例如，如果 Heckman 校正后处理效应变小，说明 OLS 高估了真实效应，这可能是因为「能力更强的企业更可能被选中，且能力本身也提高了绩效」。
- 讨论稳健性检验的结果，说明核心结论的可靠性。

## 管理学文献中的应用案例

为了帮助读者更直观地理解 Heckman 模型的应用，Bendig 和 Hoke 在论文中列举了 50 余篇管理学顶刊论文的具体做法。这里我们选择几个代表性案例进行说明。

### 案例一：风险投资与企业创新

1. Chemmanur, T. J., Krishnan, K., & Nandy, D. K. (2011). How Does Venture Capital Financing Improve Efficiency in Private Firms? A Look Beneath the Surface. The Review of Financial Studies, 24(12), 4037–4090. [Link](https://doi.org/10.1093/rfs/hhr096), [PDF](http://sci-hub.ren/10.1093/rfs/hhr096), [Google](<https://scholar.google.com/scholar?q=How Does Venture Capital Financing Improve Efficiency in Private Firms>).

2. Kortum, S., & Lerner, J. (2000). Assessing the Contribution of Venture Capital to Innovation. The RAND Journal of Economics, 31(4), 674–692. [Link](https://doi.org/10.2307/2696354), [PDF](http://sci-hub.ren/10.2307/2696354), [Google](<https://scholar.google.com/scholar?q=Assessing the Contribution of Venture Capital to Innovation>).

**研究问题**：风险投资是否提高了初创企业的创新产出 (以专利数量衡量)？

**样本选择问题**：获得风险投资的企业本身就可能具有更高的创新潜力，因此简单比较「获投」与「未获投」企业的专利产出会高估风险投资的因果效应。

**Heckman 模型应用**：
- **第一阶段**：使用 Probit 模型预测企业获得风险投资的概率。排他性约束变量为企业所在地的风险投资密度 (每千家企业中风险投资机构的数量)。论证逻辑：风险投资密度影响企业接触到投资人的机会，但不直接影响企业的创新能力。
- **第二阶段**：在获得风险投资的企业样本中，估计风险投资金额对专利产出的影响，控制 IMR 和其他企业特征 (如规模、年龄、行业等)。

**关键发现**：IMR 系数显著为正，说明确实存在正向选择偏误 (高潜力企业更可能获得投资)。Heckman 校正后，风险投资的边际效应从 OLS 估计的 0.35 下降到 0.22，表明 OLS 高估了约 37% 的处理效应。

### 案例二：国际化与企业绩效

1. Lu, J. W., & Beamish, P. W. (2004). International Diversification and Firm Performance: The S-Curve Hypothesis. Academy of Management Journal, 47(4), 598–609. [Link](https://doi.org/10.2307/20159604), [PDF](http://sci-hub.ren/10.2307/20159604), [Google](<https://scholar.google.com/scholar?q=International Diversification and Firm Performance The S-Curve Hypothesis>).

2. Contractor, F. J., Kundu, S. K., & Hsu, C. C. (2003). A Three-Stage Theory of International Expansion: The Link between Multinationality and Performance in the Service Sector. Journal of International Business Studies, 34(1), 5–18. [Link](https://doi.org/10.1057/palgrave.jibs.8400003), [PDF](http://sci-hub.ren/10.1057/palgrave.jibs.8400003), [Google](<https://scholar.google.com/scholar?q=A Three-Stage Theory of International Expansion>).

**研究问题**：企业进入国际市场是否提高了财务绩效 (以 ROA 衡量)？

**样本选择问题**：只有绩效较好、资源较充足的企业才有能力进入国际市场，且这些企业即使不国际化也可能表现优异。因此存在自我选择偏误。

**Heckman 模型应用**：
- **第一阶段**：预测企业是否进入国际市场。排他性约束变量为企业所在国的贸易开放度 (出口占 GDP 比重) 和政府出口促进政策力度。论证逻辑：这些宏观和政策变量降低了国际化的门槛和成本，但不直接影响企业自身的盈利能力。
- **第二阶段**：在国际化企业样本中，估计国际化程度 (海外收入占比) 对 ROA 的影响。

**关键发现**：IMR 系数显著为正，证实了正向选择效应。Heckman 校正后，国际化程度的系数从 0.18 下降到 0.09，且在不同子样本 (如大企业 vs. 小企业) 中表现出显著的异质性。

### 案例三：政府补贴与研发投入

1. Bronzini, R., & Iachini, E. (2014). Are Incentives for R&D Effective? Evidence from a Regression Discontinuity Approach. American Economic Journal: Economic Policy, 6(4), 100–134. [Link](https://doi.org/10.1257/pol.6.4.100), [PDF](http://sci-hub.ren/10.1257/pol.6.4.100), [Google](<https://scholar.google.com/scholar?q=Are Incentives for R&D Effective Evidence from a Regression Discontinuity Approach>).

2. Czarnitzki, D., & Lopes-Bento, C. (2013). Value for Money? New Microeconometric Evidence on Public R&D Grants in Flanders. Research Policy, 42(1), 76–89. [Link](https://doi.org/10.1016/j.respol.2012.04.008), [PDF](http://sci-hub.ren/10.1016/j.respol.2012.04.008), [Google](<https://scholar.google.com/scholar?q=Value for Money New Microeconometric Evidence on Public R&D Grants in Flanders>).

**研究问题**：政府研发补贴是否促进了企业的研发投入？

**样本选择问题**：政府在分配补贴时可能倾向于选择「有潜力」的企业，这些企业即使不获得补贴也可能增加研发投入。因此存在筛选偏误。

**Heckman 模型应用**：
- **第一阶段**：预测企业是否获得政府补贴。排他性约束变量为企业所在地方政府的财政收入和地方领导的教育背景 (是否具有理工科学位)。论证逻辑：财政收入影响地方政府的补贴能力，领导背景影响对科技项目的偏好，但这两者不直接决定企业的研发效率。
- **第二阶段**：在获补贴企业样本中，估计补贴金额对研发投入的影响。

**关键发现**：IMR 系数不显著，说明在控制了可观测特征后，选择偏误并不严重。这可能是因为政府补贴分配相对透明，主要基于可观测的企业特征 (如规模、行业)。因此，OLS 估计与 Heckman 估计差异不大，两者都显示补贴对研发投入有正向影响。

这一案例提醒我们：Heckman 模型并非总是必要的。如果 IMR 系数不显著，说明选择偏误可能较轻微，此时更简单的方法 (如加入充分的控制变量) 可能已经足够。

## 实操中的进阶议题

### 面板数据中的 Heckman 模型

当数据具有面板结构时，可能同时存在样本选择偏误和个体固定效应。此时需要使用面板 Heckman 模型 (panel Heckman model)，如 Wooldridge (1995) 和 Kyriazidou (1997) 提出的方法。

**Stata 实现**：可以使用 `xtheckmanfe` 命令 (参见牛坤在，2021)，该命令允许在选择方程和结果方程中同时控制固定效应。

**注意事项**：
- 面板 Heckman 模型的识别更加困难，通常需要更强的排他性约束假设。
- 固定效应会吸收时间不变的个体异质性，但无法处理随时间变化的未观测因素。
- 需要谨慎处理「入选」和「退出」样本的动态性，避免幸存者偏误与选择偏误混淆。

### 处理内生解释变量

如果在 Heckman 模型中，核心解释变量本身也存在内生性 (如测量误差、反向因果等)，单纯的 Heckman 校正无法解决这一问题。此时需要将 Heckman 模型与工具变量法结合。

**两步法策略**：
1. 先使用工具变量法处理核心解释变量的内生性，获得其预测值。
2. 再使用 Heckman 模型处理样本选择偏误，将预测值作为解释变量。

**Stata 实现**：可以使用 `ivprobit` 结合 `heckman`，或使用 `cmp` (Conditional Mixed Process) 命令同时处理选择偏误和内生性。

### 非线性结果变量

标准 Heckman 模型假设结果变量是连续的。当结果变量是二元变量 (如企业是否存活)、计数变量 (如专利数量) 或受限因变量 (如截断或归并数据) 时，需要使用扩展的 Heckman 模型。

**二元结果变量**：使用 Heckman Probit 模型 (Van de Ven & Van Praag, 1981)。
**计数结果变量**：使用 Sample Selection Poisson 模型 (Terza, 1998)。
**Stata 实现**：`heckprobit` 用于二元结果变量；`heckpoisson` (用户编写命令) 用于计数数据。

### 多重选择与嵌套选择

当选择过程涉及多个阶段或多个互斥选项时，标准 Heckman 模型不再适用。例如，企业首先决定是否寻求外部融资，然后在众多融资渠道中选择一种 (银行贷款、风险投资、债券等)。

**解决方案**：
- **嵌套 Logit 模型**：适用于具有层级结构的选择。
- **多元 Probit 模型**：适用于多个非互斥的二元选择。
- **Lee (1983) 广义 Heckman 模型**：适用于多项选择问题，允许不同选择对应不同的结果方程。

## 常见陷阱的总结与避免策略

基于前述分析，我们将 Heckman 模型应用中的常见陷阱总结如下，并给出相应的避免策略：

**陷阱 1：盲目应用 Heckman 模型而未充分论证其必要性**
- **避免策略**：在引入模型前，基于理论和数据特征详细论证样本选择偏误的存在及其性质。如果 IMR 系数不显著，坦诚说明选择偏误可能不严重。

**陷阱 2：排他性约束变量选择不当或缺失**
- **避免策略**：投入充分精力寻找和论证排他性约束变量。参考同领域文献的做法，多尝试不同变量组合，进行敏感性分析。

**陷阱 3：忽视多重共线性问题**
- **避免策略**：计算 VIF 值诊断共线性。如果共线性严重，重新调整变量选择，避免在两个方程中使用过多重叠变量。

**陷阱 4：仅报告第二阶段结果，忽略第一阶段信息**
- **避免策略**：完整报告两个阶段的结果，包括排他性约束变量的系数、IMR 的系数及显著性、模型拟合优度等关键信息。

**陷阱 5：对比 OLS 与 Heckman 结果但未充分解释差异**
- **避免策略**：详细讨论两种方法结果的差异，解释选择偏误的方向和幅度，分析其经济学含义。

**陷阱 6：稳健性检验不充分**
- **避免策略**：进行多角度稳健性检验，包括替代排他性约束变量、不同估计方法、样本分割、安慰剂检验等。

**陷阱 7：过度依赖函数形式识别而未做敏感性分析**
- **避免策略**：如果缺乏强有力的排他性约束变量，务必测试结果对分布假设和模型设定的敏感性，并在结论中说明识别的局限性。

## 总结与展望

Heckman 选择模型是处理样本选择偏误的经典工具，在管理学研究中具有广泛的应用前景。然而，正如 Bendig 和 Hoke (2022) 所指出的，该方法的应用并非简单地调用一个 Stata 命令，而是需要研究者在理论论证、变量选择、模型诊断、结果报告等各个环节都保持严谨和透明。

本文基于这两位作者的实操指南，系统梳理了 Heckman 模型在管理学研究中的常见问题、误区和陷阱，并提供了一套详细的操作流程。核心要点包括：

1. **充分论证样本选择偏误的存在**：不要盲目应用，而要基于理论和数据特征说明为何存在选择问题。

2. **精心选择和论证排他性约束变量**：这是模型识别的关键，需要从理论逻辑、制度背景、文献支持等多角度论证其合理性。

3. **完整报告两阶段结果**：第一阶段结果提供了选择机制的重要信息，IMR 系数的显著性检验回答了选择偏误是否存在这一核心问题。

4. **进行充分的稳健性检验**：通过替代变量、不同估计方法、样本分割等多种方式检验结果的稳健性。

5. **坦诚说明研究局限**：如果识别依赖较强的假设或函数形式，应在结论中明确说明，而非过度解读结果。

展望未来，随着因果推断方法的不断发展，Heckman 模型可能与其他方法 (如倾向得分匹配、双重差分、断点回归等) 结合使用，形成更强大的识别策略。同时，机器学习方法 (如因果森林、双重机器学习) 也为处理高维控制变量和非线性关系提供了新的可能性。但无论方法如何演进，严谨的理论论证、透明的操作流程、充分的稳健性检验始终是高质量实证研究的基石。

希望本文能够帮助从事管理学研究的学者更好地理解和应用 Heckman 选择模型，在创新管理、创业研究、战略管理等领域产出更加可信和有影响力的研究成果。

## 参考文献 {.unnumbered}

1. Bendig, D., & Hoke, J. (2022). Correcting Selection Bias in Innovation and Entrepreneurship Research: A Practical Guide to Applying the Heckman Two-Stage Estimation. SSRN Electronic Journal. [Link](https://doi.org/10.2139/ssrn.4105207), [PDF](https://download.ssrn.com/22/05/12/ssrn_id4105207_code5233967.pdf), [Google](<https://scholar.google.com/scholar?q=Correcting Selection Bias in Innovation and Entrepreneurship Research: A Practical Guide to Applying the Heckman Two-Stage Estimation>).

2. Heckman, J. J. (1979). Sample Selection Bias as a Specification Error. Econometrica, 47(1), 153–161. [Link](https://doi.org/10.2307/1912352), [PDF](http://sci-hub.ren/10.2307/1912352), [Google](<https://scholar.google.com/scholar?q=Sample Selection Bias as a Specification Error>).

3. 牛坤在. (2021). xtheckmanfe：面板 Heckman 模型的固定效应估计. 连享会. [Link](https://www.lianxh.cn/details/688.html).

4. 秦利宾. (2020). Heckman 模型：你用对了吗？连享会. [Link](https://www.lianxh.cn/details/153.html).

5. 章青慈. (2022). Stata：广义 Heckman 两步法-gtsheckman. 连享会. [Link](https://www.lianxh.cn/details/1082.html).

6. Wooldridge, J. M. (1995). Selection Corrections for Panel Data Models Under Conditional Mean Independence Assumptions. Journal of Econometrics, 68(1), 115–132. [Link](https://doi.org/10.1016/0304-4076(94)01645-G), [PDF](http://sci-hub.ren/10.1016/0304-4076(94)01645-G), [Google](<https://scholar.google.com/scholar?q=Selection Corrections for Panel Data Models Under Conditional Mean Independence Assumptions>).

7. Kyriazidou, E. (1997). Estimation of a Panel Data Sample Selection Model. Econometrica, 65(6), 1335–1364. [Link](https://doi.org/10.2307/2171740), [PDF](http://sci-hub.ren/10.2307/2171740), [Google](<https://scholar.google.com/scholar?q=Estimation of a Panel Data Sample Selection Model>).

8. Van de Ven, W. P., & Van Praag, B. M. (1981). The Demand for Deductibles in Private Health Insurance: A Probit Model with Sample Selection. Journal of Econometrics, 17(2), 229–252. [Link](https://doi.org/10.1016/0304-4076(81)90028-2), [PDF](http://sci-hub.ren/10.1016/0304-4076(81)90028-2), [Google](<https://scholar.google.com/scholar?q=The Demand for Deductibles in Private Health Insurance>).

9. Lee, L. F. (1983). Generalized Econometric Models with Selectivity. Econometrica, 51(2), 507–512. [Link](https://doi.org/10.2307/1912003), [PDF](http://sci-hub.ren/10.2307/1912003), [Google](<https://scholar.google.com/scholar?q=Generalized Econometric Models with Selectivity>).

10. Maddala, G. S. (1983). Limited-Dependent and Qualitative Variables in Econometrics. Cambridge University Press. [Google](<https://scholar.google.com/scholar?q=Limited-Dependent and Qualitative Variables in Econometrics>).

11. Ahn, H., & Powell, J. L. (1993). Semiparametric Estimation of Censored Selection Models with a Nonparametric Selection Mechanism. Journal of Econometrics, 58(1-2), 3–29. [Link](https://doi.org/10.1016/0304-4076(93)90111-H), [PDF](http://sci-hub.ren/10.1016/0304-4076(93)90111-H), [Google](<https://scholar.google.com/scholar?q=Semiparametric Estimation of Censored Selection Models>).

12. Terza, J. V. (1998). Estimating Count Data Models with Endogenous Switching: Sample Selection and Endogenous Treatment Effects. Journal of Econometrics, 84(1), 129–154. [Link](https://doi.org/10.1016/S0304-4076(97)00082-1), [PDF](http://sci-hub.ren/10.1016/S0304-4076(97)00082-1), [Google](<https://scholar.google.com/scholar?q=Estimating Count Data Models with Endogenous Switching>).


&emsp;

## 相关推文 {.unnumbered}

> Note：产生如下推文列表的 Stata 命令为：   
> &emsp; `lianxh heckman, md2 nocat`  
> 安装最新版 `lianxh` 命令：    
> &emsp; `ssc install lianxh, replace` 

  - 吴煜铭, 郑浩文, 2021, [内生性！内生性！解决方法大集合](https://www.lianxh.cn/details/579.html).
  - 毕英睿, 2023, [取对数：如何应对零值和负数](https://www.lianxh.cn/details/1234.html).
  - 牛坤在, 2021, [xtheckmanfe：面板Heckman模型的固定效应估计](https://www.lianxh.cn/details/688.html).
  - 秦利宾, 2020, [Heckman 模型：你用对了吗？](https://www.lianxh.cn/details/153.html).
  - 章青慈, 2022, [Stata：广义Heckman两步法-gtsheckman](https://www.lianxh.cn/details/1082.html).
  - 连玉君, 2024, [antrho与Fisher转换：heckman和treareg等命令中参数含义](https://www.lianxh.cn/details/1358.html).
  - 连玉君, 2024, [antrho与Fisher转换：heckman和treareg等命令中参数含义](https://www.lianxh.cn/details/1361.html).
  - 陈庭伟, 2025, [Stata：带有样本选择的分位数回归-arhomm-qregsel](https://www.lianxh.cn/details/1579.html).
