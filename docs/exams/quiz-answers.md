# 课堂小测 答案解析汇总

> **数据来源**：`src/data/` 目录下 JSON 题目数据（2026 年课堂小测，共 134 题）


## 敏捷概述

> 共 17 题

### (1) 在软件项目成功的传统观点中，"不太成功的(Challenged)"项目指的是（）？

- **A**：在开发周期某个时刻被取消的项目
- **B**：按时完成、不超预算且功能符合规格的项目
- **C**：已完成可运行，但超预算、未如期完成、功能少于设计规格的项目
- **D**：需求始终无法确定而长期停滞的项目


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<p><strong>正确率</strong>：96.67%</p>
<blockquote>
<p>根据 Standish Group 的 CHAOS 报告，软件项目分为三类：<strong>成功的（Successful）</strong>——按时、按预算、按规格完成；<strong>不太成功的（Challenged）</strong>——已完成可运行，但超预算、超时、或功能少于原始规格；<strong>失败的（Failed）</strong>——在开发过程中被取消。Challenged 项目占比在传统瀑布模式下常年居高不下，这正是敏捷运动兴起的重要背景。</p>
</blockquote>

</details>

### (2) 敏捷观点认为，评价软件项目是否成功最重要的标准是（）？

- **A**：按时完成且费用不超预算
- **B**：为客户创造价值
- **C**：功能数量符合最初设计规格
- **D**：文档齐全并通过评审


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<p><strong>正确率</strong>：92.67%</p>
<blockquote>
<p>敏捷观点衡量项目成功的首要标准是<strong>为客户创造价值（Customer Value）</strong>。与传统方法关注「按时/按预算/按规格」的三角约束不同，敏捷认为即使偏离计划，只要交付的软件为客户带来实际价值，项目就是成功的。这是价值观层面的根本差异。</p>
</blockquote>

</details>

### (3) 在"价值观—原则—实践"体系中，作为"我们在某种处境中喜欢或不喜欢某事情的根源"的是（）？

- **A**：价值观
- **B**：原则
- **C**：实践
- **D**：工具


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<p><strong>正确率</strong>：99.33%</p>
<blockquote>
<p>在「价值观—原则—实践」体系中，<strong>价值观（Values）</strong>是最根本的层次——它是「我们在某种处境中喜欢或不喜欢某事情的根源」。价值观之上是原则（Principles，价值观的具体化），再之上是实践（Practices，原则的具体执行）。三者构成自上而下的指导体系。</p>
</blockquote>

</details>

### (4) 《敏捷宣言》诞生的时间和地点是（）？

- **A**：1995年，Standish Group 总部
- **B**：2001年，犹他州雪鸟滑雪山庄
- **C**：2011年，精益创业运动的发起地
- **D**：1990年代，ThoughtWorks 公司


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<p><strong>正确率</strong>：95.33%</p>
<blockquote>
<p>《敏捷宣言》由 17 位软件方法论专家于 <strong>2001 年 2 月 11-13 日在犹他州雪鸟（Snowbird）滑雪场</strong>的 The Lodge 酒店签署。这次历史性会议汇集了 XP、Scrum、DSDM、ASD、Crystal、FDD 等「轻量级方法论」的代表，他们最终达成了 4 条价值观和 12 条原则的共识。</p>
</blockquote>

</details>

### (5) 关于《敏捷宣言》中每条"……高于……"两侧的关系，正确的表述是（）？

- **A**：右项毫无价值，应予以抛弃
- **B**：应优先满足右项，再考虑左项
- **C**：左右两项的价值完全相等
- **D**：尽管右项有其价值，但更重视左项的价值


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：D（单选）</p>
<p><strong>正确率</strong>：98.67%</p>
<blockquote>
<p>《敏捷宣言》每条「X 高于 Y」的表述格式的正确理解是：<strong>尽管右项（Y）有其价值，但我们更重视左项（X）的价值</strong>。这不是说右项毫无价值——文档、合同、计划、流程都有其必要性——而是说当二者冲突时，优先选择左项。宣言本身特别注明「while there is value in the items on the right, we value the items on the left more」。</p>
</blockquote>

</details>

### (6) 材料把"设计过程充斥短期、即时的决定，而无完整规划"的典型开发模式称为（）？

- **A**：边写边改(code and fix)
- **B**：迭代式开发
- **C**：计划驱动方法
- **D**：螺旋式开发


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<p><strong>正确率</strong>：97.33%</p>
<blockquote>
<p><strong>Code and Fix（边写边改）</strong>是一种无正式规划的开发模式：设计过程充斥短期的、即时的决定，没有完整的前期规划。这是敏捷方法所反对的原始状态——它既不是工程方法（有规划但缺乏适应），也不是敏捷方法（有适应但缺乏纪律）。</p>
</blockquote>

</details>

### (7) 材料指出，"工程方法(engineering methodologies)"另一个被广泛使用的名称是（）？

- **A**：适应性方法
- **B**：计划驱动方法(plan-driven methodologies)
- **C**：面向人的方法
- **D**：迭代式方法


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<p><strong>正确率</strong>：98.67%</p>
<blockquote>
<p>「工程方法（Engineering Methodologies）」也被广泛称为<strong>计划驱动方法（Plan-Driven Methodologies）</strong>。这类方法强调:先做完整规划 → 按计划执行 → 减少变更。典型代表是瀑布模型。它与敏捷/适应性方法形成方法论谱系的两端。</p>
</blockquote>

</details>

### (8) 文档减少只是表象，敏捷型方法相对工程型方法的两个深层本质特点是（）？

- **A**：步骤更多、规定更严
- **B**：面向过程、拒绝变化
- **C**：预见性的、面向过程的
- **D**：适应性而非预见性的、面向人而非面向过程的


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：D（单选）</p>
<p><strong>正确率</strong>：97.33%</p>
<blockquote>
<p>敏捷方法相对工程方法的两个深层本质特点是：<strong>适应性而非预见性（Adaptive rather than Predictive）</strong>和<strong>面向人而非面向过程（People-oriented rather than Process-oriented）</strong>。文档减少只是表象，根源在于对不确定性和人性的不同假设。</p>
</blockquote>

</details>

### (9) 传统正规方法"将设计与建造分离"的基本思路主要借鉴自（）？

- **A**：制造业的流水线作业
- **B**：泰勒的科学管理
- **C**：土木工程等其他工程领域
- **D**：精益创业方法


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<p><strong>正确率</strong>：88.0%</p>
<blockquote>
<p>传统正规软件工程方法「将设计与建造分离」的基本思路主要借鉴自<strong>土木工程等其他工程领域</strong>。在这些成熟的工程领域中，设计和建造天然是分开的（建筑师画图 → 施工队按图建造），因为后期变更的代价极高。这种思路被软件工程早期照搬，但软件的特殊性（可修改性、不可触摸性）使其不完全适用。</p>
</blockquote>

</details>

### (10) McConnell 指出，在大型软件项目中编码和单元测试所占的比例约为（）？

- **A**：10%
- **B**：15%
- **C**：50%
- **D**：90%


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<p><strong>正确率</strong>：87.33%</p>
<blockquote>
<p>Steve McConnell 在其著作中指出，在大型软件项目中，编码和单元测试仅占项目总工作量的约 <strong>15%</strong>。其他工作包括需求分析、架构设计、集成测试、文档、项目管理等。这一数据常被用来论证「为什么只关注编码效率是不够的」以及「为什么敏捷实践需要覆盖整个价值流」。</p>
</blockquote>

</details>

### (11) Alistair Cockburn 在其论文中提出，软件开发中的"人"是（）？

- **A**：可以自由替换的编程插件
- **B**：与角色相比无关紧要的资源
- **C**：非线性、一阶的部件
- **D**：可被过程完全规范的可预见性部件


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<p><strong>正确率</strong>：90.67%</p>
<blockquote>
<p>Alistair Cockburn 在其著名论文《Characterizing People as Non-Linear, First-Order Components in Software Development》中提出，软件开发中的「人」是<strong>非线性的一阶部件（non-linear, first-order components）</strong>——这意味着：①人不是可预见的、可替换的标准化零件；②人之间的互动产生非线性效应（沟通效果受信任、熟悉度等复杂因素影响）；③因此「过程」和「方法论」必须考虑到人的独特性。</p>
</blockquote>

</details>

### (12) 某团队的程序员说："因为我重视沟通，所以我写了这份1000页的项目文档。"对照材料中的价值观与实践，下列判断最恰当的是（）？

- **A**：写了详尽文档就证明他确实重视沟通，因为实践是价值观的表现
- **B**：文档属于详尽文档，敏捷团队从不写文档不做计划，所以他违背了敏捷
- **C**：可以以价值观的名义做任何事，文档未必说明他重视沟通——如果每天15分钟的交谈更有效，那份文档就不能说明这一点
- **D**：价值观处在高层次，只要他声称重视沟通即可，做法本身无需评判


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<p><strong>正确率</strong>：96.67%</p>
<blockquote>
<p>此题考察价值观与实践的关系。敏捷宣言说「个体和互动高于流程和工具」——重点在「互动」的质量而非某种特定形式的沟通。<strong>写了一千页文档并不等同于重视沟通</strong>——如果每天 15 分钟面对面交谈更有效，那么厚重的文档不能说明他重视沟通。实践必须根据实际效果而不是表面形式来评判。</p>
</blockquote>

</details>

### (13) 某经理原来的6人团队都赞成用计划扑克做估算，现在他筹建一个新团队。依据"个体和互动高于流程和工具"，他最恰当的做法是（）？

- **A**：可以向新团队建议并鼓励他们尝试计划扑克，但不强制规定
- **B**：直接规定新团队必须使用计划扑克，因为这是被验证过的好实践
- **C**：禁止新团队使用计划扑克，要求他们自创估算方法
- **D**：把估算交给经理统一完成，团队不必参与


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<p><strong>正确率</strong>：99.33%</p>
<blockquote>
<p>根据「个体和互动高于流程和工具」，管理者应该<strong>向新团队建议并鼓励尝试</strong>，但不强制规定。敏捷的核心是「人高于流程」——好的工具和流程应服务于团队，而不是反过来。强制推行即使是被验证过的好实践，也违背了「自组织团队」和「适应性」原则。</p>
</blockquote>

</details>

### (14) 某项目经理把项目延期归咎于"需求老是在变"，主张今后必须在开发前彻底锁定需求并禁止变更。依据材料，最贴合其逻辑分析的判断是（）？

- **A**：在商用软件中需求变更是常态、甚至"应该变"，因为软件不可触摸，许多功能只有用过系统后才知道是否有用，一味锁定需求并不能真正解决问题
- **B**：他完全正确，需求变更都是需求工程没做好造成的
- **C**：只要把所有需求都固定下来并取得客户签字认可，项目就不会再有问题
- **D**：需求变更与商业环境无关，把需求锁定后计划必然稳定


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<p><strong>正确率</strong>：98.67%</p>
<blockquote>
<p>在商用软件开发中，<strong>需求变更是常态，甚至「应该变」</strong>。软件不可触摸——很多功能只有实际使用系统后才知道是否有用。这份特性意味着试图在开发前「彻底锁定需求」是不切实际的。正确的做法不是禁止变更，而是建立一个能安全响应变更的开发流程（即敏捷方法的核心目标）。</p>
</blockquote>

</details>

### (15) 某公司把开发者当作"可互相替换的编程插件"来管理，几年后发现优秀人才不断流失，团队真的只剩下平庸的"插件"。依据材料，最贴合的解释是（）？

- **A**：这只是偶然的人事波动，与管理方式无关
- **B**：这是一个很强的正反馈机制：把人当可互替插件，就不会把他们当独特个体对待，从而降低士气和生产率、逼走优秀人才，最终真的得到可互替的插件
- **C**：这说明开发者本来就是可替换的资源，该管理方式得到了验证
- **D**：人才流失只是因为薪酬太低，与是否把人当个体无关


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<p><strong>正确率</strong>：98.0%</p>
<blockquote>
<p>此题描述的是一个<strong>自我实现的预言（self-fulfilling prophecy）的正反馈循环</strong>：管理者把人当成可互相替换的插件 → 不把每个人当作独特个体对待 → 优秀人才感到不被尊重而流失 → 团队真的只剩下平庸的「插件」→ 管理者认为自己的管理方式得到了验证。这正是敏捷强调「面向人而非面向过程」所要杜绝的文化。</p>
</blockquote>

</details>

### (16) 某管理者用代码行数、生产率等单一指标考核开发人员，一段时间后发现大家的指标都很漂亮，真实效能却下降了。依据材料，最准确的解释和对策是（）？

- **A**：指标漂亮就说明效能提升了，应继续加强度量
- **B**：问题在于指标选得不够多，只要再增加几个指标就能解决
- **C**：软件效能本来就无法改善，是否度量都一样
- **D**：度量若没有涵盖影响效能的所有重要因素，干活的人会改变工作方式去迎合指标，造成度量"失效"；对软件开发，委托式管理往往比基于度量的管理更有效


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：D（单选）</p>
<p><strong>正确率</strong>：98.67%</p>
<blockquote>
<p>此题考察度量管理的经典陷阱——<strong>古德哈特定律（Goodhart's Law）</strong>：当一个度量成为目标时，它就不再是好的度量。用单一指标考核开发人员会导致「指标优化」而非「效能提升」——开发者改变工作方式去迎合指标。对软件开发这种创造性工作，<strong>委托式管理（delegatory management）</strong>往往比基于度量的微观管理更有效。</p>
</blockquote>

</details>

### (17) 某敏捷团队最终交付的软件与项目最初的计划差异明显，有人据此断定项目失败了。综合两份材料，最恰当的判断是（）？

- **A**：衡量敏捷项目成功的是商业价值——客户得到的软件价值是否大于其投入；一个好的敏捷项目往往会建造出与最初计划不同却更好的软件
- **B**：只要偏离了最初计划就是失败，这是判断项目成功与否的唯一标准
- **C**：敏捷项目根本不需要计划，所以无所谓是否偏离
- **D**：与计划不同说明需求工程失败，应当追究开发团队的责任


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<p><strong>正确率</strong>：99.33%</p>
<blockquote>
<p>衡量敏捷项目成功的是<strong>商业价值（Business Value）</strong>——客户得到的软件价值是否大于其投入。敏捷项目欢迎变更，一个好的敏捷项目往往会建造出与最初计划不同却更好的软件——因为团队在迭代过程中基于真实反馈持续调整方向。这与传统项目管理以「遵循计划」为成功的标准形成鲜明对比。</p>
</blockquote>

</details>

## Scrum

> 共 20 题

### (1) Scrum 一词最早作为橄榄球术语被引入产品开发领域，是哪一年由竹内弘高与野中郁次郎提出的（）?

- **A**：1975 年
- **B**：1986 年
- **C**：1995 年
- **D**：2001 年


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<p><strong>正确率</strong>：95.75%</p>
<blockquote>
<p>竹内弘高（Hirotaka Takeuchi）与野中郁次郎（Ikujiro Nonaka）在 1986 年《哈佛商业评论》文章《The New New Product Development Game》中首次将 Scrum 一词从橄榄球引入产品开发领域，描述了跨职能团队协作的「橄榄球式」推进方式。这篇文章是 Scrum 方法论的思想源头。</p>
</blockquote>

</details>

### (2) Scrum 框架的三大支柱（Pillars）是（）?

- **A**：透明、检视、适应
- **B**：承诺、专注、尊重
- **C**：计划、执行、回顾
- **D**：迭代、增量、反馈


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<p><strong>正确率</strong>：97.17%</p>
<blockquote>
<p>Scrum 建立在经验主义（empiricism）之上，三大支柱是：<strong>透明（Transparency）</strong>——过程和工件必须对相关人员可见；<strong>检视（Inspection）</strong>——频繁检查工件和进展以发现偏差；<strong>适应（Adaptation）</strong>——发现偏差后尽快调整。这三个支柱是 Scrum 理论的核心。</p>
</blockquote>

</details>

### (3) Scrum Team 的三个角色是（）?

- **A**：项目经理、架构师、测试工程师
- **B**：需求分析师、PO、Scrum Master
- **C**：客户、开发人员、管理者
- **D**：Product Owner、Scrum Master、Developers


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：D（单选）</p>
<p><strong>正确率</strong>：98.58%</p>
<blockquote>
<p>Scrum Guide 2020 规定 Scrum Team 由三个角色（accountabilities）组成：<strong>Product Owner</strong>（最大化产品价值，管理 Product Backlog）、<strong>Scrum Master</strong>（建立 Scrum 流程，教练团队和组织）、<strong>Developers</strong>（每个 Sprint 交付可用增量）。2020 版去掉了「Development Team」称谓，统称 Developers。</p>
</blockquote>

</details>

### (4) 根据 Scrum Guide 2020，Scrum Team 通常规模应为（）?

- **A**：5 人或更少
- **B**：10 人或更少
- **C**：15 人或更少
- **D**：20 人或更少


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<p><strong>正确率</strong>：98.11%</p>
<blockquote>
<p>Scrum Guide 2020 明确建议 Scrum Team 规模通常为 <strong>10 人或更少</strong>。过大的团队会降低沟通效率并增加协调复杂度。如果团队规模超出此范围，应考虑拆分为多个 Scrum Team 共同维护同一产品 Backlog。</p>
</blockquote>

</details>

### (5) 每日 Scrum 会议（Daily Scrum）的时间盒是（）?

- **A**：5 分钟
- **B**：15 分钟
- **C**：30 分钟
- **D**：60 分钟


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<p><strong>正确率</strong>：98.58%</p>
<blockquote>
<p>每日 Scrum（Daily Scrum）是 Developers 每天举行的 15 分钟事件，目的是检视 Sprint Goal 的进展，并根据需要调整 Sprint Backlog。其时间盒严格限定为 <strong>15 分钟</strong>，以保持会议的聚焦和高效。</p>
</blockquote>

</details>

### (6) 用户故事模板"作为<某类用户>，我想<做某事>，从而<获得某种价值>"中，三部分依次对应的是（）?

- **A**：why / who / what
- **B**：who / why / what
- **C**：what / who / why
- **D**：who / what / why


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：D（单选）</p>
<p><strong>正确率</strong>：96.7%</p>
<blockquote>
<p>标准用户故事模板「作为&lt;某类用户&gt;，我想&lt;做某事&gt;，从而&lt;获得某种价值&gt;」中三部分依次对应：<strong>who（谁）→ what（什么）→ why（为什么）</strong>。Who 明确角色，What 描述行为，Why 阐述价值。这个模板帮助团队从用户视角理解需求的真正动机。</p>
</blockquote>

</details>

### (7) INVEST 原则中字母 I 代表（）?

- **A**：Independent（独立性）
- **B**：Important（重要性）
- **C**：Integrated（集成性）
- **D**：Iterative（迭代性）


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<p><strong>正确率</strong>：97.64%</p>
<blockquote>
<p><strong>INVEST</strong> 是 Bill Wake 提出的用户故事质量评估原则：<strong>I=Independent（独立）</strong>、N=Negotiable（可协商）、V=Valuable（有价值）、E=Estimable（可估算）、S=Small（短小）、T=Testable（可测试）。I 排在首位，强调故事应尽量减少依赖，避免阻塞。</p>
</blockquote>

</details>

### (8) 关于 Product Backlog 的排序权，下列说法正确的是（）?

- **A**：由 Scrum Master 决定
- **B**：由开发团队投票决定
- **C**：由 Product Owner 决定
- **D**：由利益相关者联合决定


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<p><strong>正确率</strong>：94.34%</p>
<blockquote>
<p>Product Backlog 的排序权归属于 <strong>Product Owner（PO）</strong>。PO 负责根据产品目标、利益相关者反馈和市场变化持续调整 Backlog 条目的优先级。虽然可以听取他人建议，但最终排序决定由 PO 做出。</p>
</blockquote>

</details>

### (9) Ron Jeffries 提出的用户故事 3C 原则是（）?

- **A**：Card（卡片）、Conversation（交谈）、Confirmation（确认）
- **B**：Code（编码）、Commit（提交）、Check（检查）
- **C**：Client（客户）、Customer（用户）、Contract（合同）
- **D**：Concept（概念）、Create（创建）、Complete（完成）


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<p><strong>正确率</strong>：99.06%</p>
<blockquote>
<p>Ron Jeffries 提出的用户故事 <strong>3C 原则</strong>是：<strong>Card（卡片）</strong>——故事写在索引卡上作为占位符；<strong>Conversation（交谈）</strong>——真正的需求在对话中浮现；<strong>Confirmation（确认）</strong>——通过验收测试来验证故事完成。核心思想：卡片本身不够，三 C 缺一不可。</p>
</blockquote>

</details>

### (10) Scrum 中"猪与鸡"的比喻里，"猪"对应（）?

- **A**：客户与最终用户
- **B**：管理层与赞助商
- **C**：PO、Scrum Master 与开发团队
- **D**：所有利益相关者


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<p><strong>正确率</strong>：96.7%</p>
<blockquote>
<p>「猪与鸡」是 Scrum 中经典的比喻（源自一个商业寓言）：<strong>猪（Pig）</strong>是 Scrum Team 成员（PO、SM、Developers），他们「把肉都押上了」，对项目全身心投入；鸡（Chicken）是其他利益相关者，他们「参与但不投入」。这个比喻强调核心团队的承诺程度。注意：Scrum Guide 2020 已不再使用此比喻，但仍是常见的教学概念。</p>
</blockquote>

</details>

### (11) Scrum 的理论基础是（）?

- **A**：理性主义与形式化方法
- **B**：演绎主义与文档驱动
- **C**：结构化分析与瀑布模型
- **D**：经验主义与精益思维


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：D（单选）</p>
<p><strong>正确率</strong>：96.23%</p>
<blockquote>
<p>Scrum 的理论基础是<strong>经验主义（empiricism）与精益思维（Lean thinking）</strong>。经验主义强调知识来自实践和观察，决策基于实际数据而非理论预测。Scrum 通过短迭代（Sprint）和持续反馈来实现经验性过程控制。精益思维则强调消除浪费、聚焦价值流。</p>
</blockquote>

</details>

### (12) 计划扑克（Planning Poker）使用的常见数字序列是（）?

- **A**：自然数列 1,2,3,4,5…
- **B**：等差数列 2,4,6,8…
- **C**：斐波那契数列 0,1,1,2,3,5,8,13,21…
- **D**：等比数列 1,2,4,8,16…


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<p><strong>正确率</strong>：98.58%</p>
<blockquote>
<p>计划扑克（Planning Poker）使用的标准序列是<strong>斐波那契数列</strong>（0, 1, 1, 2, 3, 5, 8, 13, 21…）。斐波那契数列的间隔递增反映了一个事实：对更大工作量的估算，不确定性也随之增大。James Grenning 于 2002 年发明此方法，Mike Cohn 推广。</p>
</blockquote>

</details>

### (13) 当前行业通行的 Scrum Sprint 周期通常为（）?

- **A**：2–3 天
- **B**：约 2 周
- **C**：2 个月
- **D**：半年


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<p><strong>正确率</strong>：99.06%</p>
<blockquote>
<p>当前行业通行的 Scrum Sprint 周期为 <strong>约 2 周</strong>。Scrum Guide 规定 Sprint 最长不超过一个月，而业界实践表明 1-2 周是最常见的平衡点——足够完成有意义的增量，又足够短以获得频繁反馈。</p>
</blockquote>

</details>

### (14) Scrum Guide 2020 相较 2017 版的一项关键变化是（）?

- **A**：取消 Product Owner 角色
- **B**：取消"开发团队（Development Team）"称谓，统称"Developers"
- **C**：将 Sprint 周期统一延长至 4 周
- **D**：新增架构师角色


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<p><strong>正确率</strong>：97.17%</p>
<blockquote>
<p>Scrum Guide 2020 的关键变化之一是<strong>取消「Development Team」称谓，统一使用「Developers」</strong>。旧版将 Scrum Team 分为 PO、SM、Development Team 三个部分，2020 版强调只有一个 Scrum Team，内部有三种 accountability（PO、SM、Developers），消除了「我们 vs 他们」的角色隔离感。</p>
</blockquote>

</details>

### (15) Definition of Done（DoD）的主要作用是（）?

- **A**：团队对"完成"的统一定义，用以判断增量是否真正可交付
- **B**：规定团队成员的绩效考核标准
- **C**：PO 单方面制定的验收规则
- **D**：列出测试用例清单


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<p><strong>正确率</strong>：100.0%</p>
<blockquote>
<p><strong>Definition of Done（DoD）</strong>是团队对「完成」的统一定义，用来<strong>判断增量是否真正可交付</strong>。DoD 不是绩效考核标准，也不是 PO 单方面制定的规则。它是团队的质量承诺：当 Product Backlog 条目满足 DoD 时，增量即为可交付状态。</p>
</blockquote>

</details>

### (16) 某团队严格执行 Scrum:Sprint 两周、每日站会 15 分钟、三大角色齐全;但 PO 每天给每位开发者分派具体任务并要求小时级进度汇报。下列判断最恰当的是（）?

- **A**：完全符合 Scrum，因角色、事件、时间盒都齐全
- **B**：这是 PO 的本职工作——PO 就该给开发者分派任务
- **C**：只要 Sprint 目标达成，流程细节不必深究
- **D**：形式齐全但违反了自管理原则，本质是微观管理


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：D（单选）</p>
<p><strong>正确率</strong>：98.58%</p>
<blockquote>
<p>此题考察 Scrum 的自管理原则。PO 每天给每位开发者分派具体任务并要求小时级汇报，违反了 Scrum 中「Scrum Team 是自管理（self-managing）的」原则。Scrum Guide 2020 明确：团队自己决定 'who does what, when, and how'。PO 负责 'what'（优先级），而非 'how'（实现方式）。形式上的 Scrum 仪式不等于真正践行 Scrum 精神。</p>
</blockquote>

</details>

### (17) 某团队近 3 个 Sprint 的 Velocity 分别为 20、35、15 点，PO 据此要求团队"提高估算准确性"。下列回应最能体现对 Scrum 估算本质的理解（）?

- **A**：延长估算会议，逐条故事拆到小时级，以追求精度
- **B**：由最资深成员独立估算，避免其他人拉低精度
- **C**：估算的价值不在精确预测，而在建立共同理解、暴露分歧;应分析波动背后的需求模糊与阻碍因素
- **D**：放弃 Story Point，改用绝对小时数估算


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<p><strong>正确率</strong>：97.64%</p>
<blockquote>
<p>Velocity（速率）波动是正常的，因为 Story Point 是相对估算而非绝对工时。估算的本质价值不在于精确预测工期，而在于：①建立团队对故事的共同理解；②暴露分歧和需求模糊点；③为 Sprint 计划提供参考。PO 应关注波动背后的原因（需求模糊？阻碍因素？），而非追求虚假的估算精度。</p>
</blockquote>

</details>

### (18) 某团队把一个复杂故事拆成 8 个小任务交给 AI Agent，一天内"完成"全部任务（CI 通过、已合并）;下 Sprint 团队却无人能解释其中某段代码的设计意图。按 Scrum 2020 及其 AI 时代扩展，下列判断最恰当（）?

- **A**：这违反了"透明"支柱——AI 代码未被人类理解就积累了"理解力负债";DoD 应追加"至少一名成员能解释核心设计决策"
- **B**：DoD 已通过，工作即已完成
- **C**：这是 Agent 时代的新常态，无需干预
- **D**：应禁用所有 AI Agent，回到人工编码


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<p><strong>正确率</strong>：99.06%</p>
<blockquote>
<p>此题考察 Scrum 的「透明」支柱与 AI 辅助开发的关系。Scrum 的透明性要求过程和工件对相关人员可见且可理解。AI 生成的代码如果不被团队理解，就产生了「理解力负债」——代码虽然存在但无人知其设计意图，这违反了透明的本质。应在 DoD 中追加对人类理解的要求，而非完全禁用 AI。</p>
</blockquote>

</details>

### (19) Sprint 进行过程中，PO 想在当前 Sprint 插入一个与 Sprint Goal 冲突的新需求。关于 Sprint 的稳定性与可协商性，下列理解最准确（）?

- **A**：Sprint 启动后一切冻结，任何调整都违反 Scrum
- **B**：PO 作为最大权威，可随时改写 Sprint Goal
- **C**：Scrum Master 有权否决 PO 的任何改动
- **D**：Sprint Goal 不应被单方面更改;但范围可在不破坏目标的前提下与 PO 协商，这体现了"范围/重要性/估算可协商，质量不可让步"


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：D（单选）</p>
<p><strong>正确率</strong>：98.11%</p>
<blockquote>
<p>Sprint Goal 是 Sprint 的核心承诺，不应被单方面更改。但 Scrum 也承认「范围/重要性/估算可协商，质量不可让步」的原则。如果 Sprint 过程中发现范围需要调整，应在不破坏 Sprint Goal 的前提下与 PO 协商。这体现了 Scrum 在「承诺」与「适应」之间的平衡。</p>
</blockquote>

</details>

### (20) Sprint Review 上团队演示了完整功能、测试全绿、流程流畅;但真实用户在后续使用中反馈功能与需求不符。关于"Scrum 解决什么问题"，下列理解最准确（）?

- **A**：Scrum 保证需求正确，因此这必然是执行层面的失误
- **B**：此问题证明 Scrum 不可靠，应回到瀑布模型先把需求冻结
- **C**：用户真正的需求常在看到产品后才清晰——Scrum 的短迭代+经验主义正是为此而设计;演示"完成"≠价值传递成功，下 Sprint 应基于反馈调整 Backlog
- **D**：应追责 PO 未能在一开始完整定义需求


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<p><strong>正确率</strong>：99.06%</p>
<blockquote>
<p>Scrum 通过短迭代和经验主义来解决需求不确定性问题。用户真正的需求常在看到可工作软件后才清晰——这不是 Scrum 的失败，而是其设计的出发点。Sprint Review 演示「完成」不等于价值传递成功，关键在于下一 Sprint 基于真实反馈调整 Backlog。这正是「检视与适应」（Inspect &amp; Adapt）循环的价值。</p>
</blockquote>

</details>

## XP（极限编程）

> 共 20 题

### (1) 传统软件工程假设:从需求到生产，同一个 bug 的修复成本随时间呈何种形态变化（）?

- **A**：指数增长
- **B**：保持平稳
- **C**：线性下降
- **D**：先升后降


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<p><strong>正确率</strong>：96.86%</p>
<blockquote>
<p>传统软件工程的核心假设之一是：bug 修复成本随时间呈<strong>指数增长</strong>（exponential growth）。需求阶段修复只需改文档；开发阶段改代码；测试阶段重新验证；生产环境则需紧急修复+热补丁+可能的回滚。这就是 Barry Boehm 的经典「变更成本曲线」，也是敏捷方法强调早期测试和持续反馈的根本原因。</p>
</blockquote>

</details>

### (2) Kent Beck 1996 年押"变更曲线可被压平"的项目是（）?

- **A**：福特 1990 年的 ERP 项目
- **B**：克莱斯勒 C3 薪资系统（Smalltalk · 8.7 万员工）
- **C**：IBM 1992 年的 OS/2
- **D**：戴姆勒 2000 年的电商系统


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<p><strong>正确率</strong>：96.23%</p>
<blockquote>
<p>Kent Beck 在 1996 年被邀请优化<strong>克莱斯勒 C3（Comprehensive Compensation System）薪资项目</strong>的性能。该项目使用 Smalltalk 语言，服务于 8.7 万员工。在调试过程中，Beck 观察到大量开发实践问题，由此开始系统性地提炼 XP 的实践集。C3 项目虽于 2000 年因业务原因取消，但 XP 方法论从此诞生。</p>
</blockquote>

</details>

### (3) 《Extreme Programming Explained》1999 年首版给出的四大价值观是（）?

- **A**：流程、工具、个人、变化
- **B**：迭代、估算、回顾、计划
- **C**：交流、协作、纪律、文档
- **D**：交流、简单、反馈、勇气


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：D（单选）</p>
<p><strong>正确率</strong>：96.23%</p>
<blockquote>
<p>《Extreme Programming Explained》(1999) 首版给出的四大价值观是：<strong>Communication（交流）、Simplicity（简单）、Feedback（反馈）、Courage（勇气）</strong>。第二版（2004）新增了第五个价值观 Respect（尊重）。这四个价值观是一切 XP 实践的根基。</p>
</blockquote>

</details>

### (4) XP 中"为了稳定可预测的开发，必要的事最终收敛到"的四项基本活动是（）?

- **A**：需求、设计、开发、测试
- **B**：计划、估算、实现、回顾
- **C**：沟通、协作、构建、部署
- **D**：编码、测试、倾听、设计


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：D（单选）</p>
<p><strong>正确率</strong>：89.31%</p>
<blockquote>
<p>XP 的四项基本活动是：<strong>Coding（编码）、Testing（测试）、Listening（倾听）、Designing（设计）</strong>。Kent Beck 认为，软件开发中所有必要的工作最终都会收敛到这四个活动中。编码和测试是核心环路，倾听获取需求，设计保持系统简洁。</p>
</blockquote>

</details>

### (5) Kent Beck 简单设计四准则按优先级排序时，第一条（最高优先级）是（）?

- **A**：消除重复
- **B**：清晰表达每一个对程序员重要的意图
- **C**：最小化类和方法的数量
- **D**：通过所有测试


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：D（单选）</p>
<p><strong>正确率</strong>：91.19%</p>
<blockquote>
<p>Kent Beck 简单设计四准则按优先级排序为：①<strong>通过所有测试（Runs all tests）</strong>——功能正确是第一前提；②消除重复（Remove duplication）；③清晰表达意图（Expresses intent）；④最小化类和方法的数量（Fewest elements）。测试通过是最高优先级，因为不正确的代码再简单也无意义。</p>
</blockquote>

</details>

### (6) TDD 一轮最小循环的阶段顺序是（）?

- **A**：红 → 绿 → 重构
- **B**：绿 → 红 → 重构
- **C**：重构 → 红 → 绿
- **D**：设计 → 编码 → 测试


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<p><strong>正确率</strong>：94.97%</p>
<blockquote>
<p>TDD 的最小循环是 <strong>Red → Green → Refactor</strong>（红 → 绿 → 重构）：①先写一个失败的测试（Red）；②写刚好足够的代码让它通过（Green）；③在保持测试通过的前提下重构代码（Refactor）。这个循环强调「永远不要写没有失败测试的代码」。</p>
</blockquote>

</details>

### (7) 在结对编程中，Driver（手握键鼠的人）的关注焦点是（）?

- **A**：当下这个方法怎么实现最好——语法、边界、命名、测试通过
- **B**：还有哪些测试没覆盖
- **C**：整个方法方向是否正确
- **D**：能否简化系统让当前问题自然消失


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<p><strong>正确率</strong>：96.86%</p>
<blockquote>
<p>在结对编程中，<strong>Driver（驾驶员）</strong>的关注焦点是<strong>当前这个方法的具体实现细节</strong>：语法是否正确、边界条件是否处理、命名是否清晰、如何让测试通过。而 Navigator（领航员）关注更大的图景：还有什么测试没覆盖、整体方向是否正确、能否简化系统。两者分工互补。</p>
</blockquote>

</details>

### (8) Fowler 持续集成中，"提交阶段（Commit Stage）"通常应控制在的时间内是（）?

- **A**：≤1 分钟
- **B**：≤10 分钟
- **C**：≤30 分钟
- **D**：≤2 小时


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<p><strong>正确率</strong>：91.19%</p>
<blockquote>
<p>Martin Fowler 在持续集成实践中建议<strong>提交阶段（Commit Stage）应控制在 ≤10 分钟</strong>内完成。这个阶段包括编译和快速测试，目的是快速给出「这次提交是否安全」的反馈。如果超过 10 分钟，开发者会减少提交频率，CI 的核心价值——快速集成——就会被削弱。</p>
</blockquote>

</details>

### (9) 关于 XP 的"代码集体拥有制（Collective Ownership）"，最准确的描述是（）?

- **A**：集体拥有意味着没有规则，谁想改就改
- **B**：集体拥有不需要任何配套实践即可推行
- **C**：集体拥有由测试、结对、持续集成、编码标准四条绳子一起拉住，不是"无所有权"的别名
- **D**：集体拥有等于"个人所有权"的反面，必须由架构师统一审批


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<p><strong>正确率</strong>：96.86%</p>
<blockquote>
<p>XP 的代码集体拥有制意味着任何开发者都可以改进代码的任何部分，但它并非「无规则」。它由<strong>四条配套实践「拴住」</strong>：自动化测试（保证修改安全）、结对编程（保证知识传递）、持续集成（保证及时发现问题）、编码标准（保证代码风格统一）。缺少任何一条，集体拥有制都会失控。</p>
</blockquote>

</details>

### (10) 关于 CI / CD / 持续部署三者的边界，正确的描述是（）?

- **A**：CI 自动化到生产;CD 还要手动;持续部署只剩紧急刹车
- **B**：三者完全等同，只是叫法不同
- **C**：CI 自动化"构建+快速测试"，主线已集成已初步验证;CD 自动化整条流水线到类生产，只剩"上生产"按钮手动;持续部署连上生产都自动，只留紧急刹车
- **D**：CI 是工具，CD 是方法，持续部署是组织模式


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<p><strong>正确率</strong>：98.11%</p>
<blockquote>
<p>CI、CD 和持续部署三者的递进关系：<strong>CI（持续集成）</strong>自动化「构建+快速测试」，确保主线已集成已验证；<strong>CD（持续交付）</strong>自动化整条流水线到类生产环境，只保留「上线」按钮为手动；<strong>持续部署（Continuous Deployment）</strong>连上线都自动，只在紧急情况保留人为干预。三者层层递进，手动环节逐步减少。</p>
</blockquote>

</details>

### (11) Martin Fowler 关于 UML 的立场是（）?

- **A**：提倡"草图用法"——编码前白板探索、保持简短、只画关键结构、视为草图而非终稿、讨论完即擦掉
- **B**：提倡"终稿用法"——作为蓝图交给另一团队构建
- **C**：要求 UML 与代码长期同步维护，否则不合规
- **D**：图比代码权威，应作为系统全面信息源


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<p><strong>正确率</strong>：96.86%</p>
<blockquote>
<p>Martin Fowler 提倡 UML 的<strong>草图用法（UML as Sketch）</strong>：用 UML 在编码前做白板探索，保持简短，只画关键结构，视为临时草图而非永久文档，讨论完即可擦除。他强调「UML 是沟通工具，不是规格说明」。与之相反的是「蓝图用法」（UML as Blueprint）——将 UML 作为交给另一团队构建的详细蓝图。</p>
</blockquote>

</details>

### (12) 根据持续集成讲义，主线构建坏了，团队首选的处理措施是（）?

- **A**：立即在主线上修复，避免回滚
- **B**：关闭 CI 流水线减少噪音
- **C**：首选 git revert 那次提交，让主线立刻回到上一个绿色状态——把故障半径压到最小，解除对所有其他人的阻塞
- **D**：把出错的开发者调离项目


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<p><strong>正确率</strong>：96.23%</p>
<blockquote>
<p>当主线构建损坏时，最高优先级是<strong>恢复主线到绿色状态</strong>，解除对其他团队成员的阻塞。首选措施是 <code>git revert</code> 出错的那次提交，将故障半径压缩到最小。在损坏的主线上继续提交会导致更多问题叠加。这是 CI 文化的核心纪律之一。</p>
</blockquote>

</details>

### (13) 关于"重构（Refactoring）"，最准确的定义是（）?

- **A**：任何对现有代码的修改都叫重构
- **B**：为引入新功能而必须改造代码的过程
- **C**：必须由架构师审批后才能执行的代码修改
- **D**：保留外部可见行为、只改善内部结构的优化;改变可见行为的是功能变更，不是重构


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：D（单选）</p>
<p><strong>正确率</strong>：97.48%</p>
<blockquote>
<p>Martin Fowler 对重构的经典定义：<strong>保留外部可见行为、只改善内部结构的代码优化</strong>。关键词是「保留外部行为」——如果代码的可见行为改变了，那是功能变更，不是重构。重构是在「不改变软件可观察行为的前提下改善其内部结构」。</p>
</blockquote>

</details>

### (14) 讲义指出"能编译"不等于"做对了事"，因此 CI 中的"自测试构建（Self-Testing Build）"应该（）?

- **A**：只跑编译器和静态类型检查即可
- **B**：构建 = 编译 + 完整自动化测试，任一测试失败整个构建变红，可加 Linter、静态分析、覆盖率
- **C**：构建只检查代码风格是否统一
- **D**：构建只需保证打包产物存在


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<p><strong>正确率</strong>：97.48%</p>
<blockquote>
<p>CI 中的自测试构建要求在<strong>编译 + 完整自动化测试都通过</strong>时才判定构建为绿色。任一测试失败整个构建变红。此外可以加入 Linter、静态分析、代码覆盖率检查等作为额外的质量门禁。「能编译」只证明语法正确，自动化测试才能验证语义正确。</p>
</blockquote>

</details>

### (15) 某团队声称在做 XP——CI 流水线天天绿灯、Sprint 仪式齐全，但坚决不写自动化测试。三个月后他们最可能撞上的局面是（）?

- **A**：变更曲线提前压平，部署效率显著提升
- **B**：CI 跑得越欢，坏代码合得越快——Fear Flywheel 启动，变更曲线悄悄回到指数形态，团队主动回避结构性改动
- **C**：CI 流水线会自动检测出语义冲突，团队整体安全
- **D**：TDD 与重构会因 CI 已搭好而自然涌现


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<p><strong>正确率</strong>：96.86%</p>
<blockquote>
<p>没有自动化测试的 CI 是危险的——CI 跑得越欢，坏代码合入得越快。这被称为 <strong>Fear Flywheel（恐惧飞轮）</strong>：没有测试保护 → 不敢重构 → 代码腐化 → 变更成本上升 → 更不敢改代码 → 恶性循环。变更曲线不仅没有压平，反而悄悄回到指数形态。</p>
</blockquote>

</details>

### (16) 某 50 人团队全员严格做 TDD，使用 GitHub Actions，但所有改动都走长期 feature branch + 强制 PR 评审，功能完成才合主线。Fowler 视角下这算 CI 吗（）?

- **A**：算，因为 TDD + 自动化构建已具备 CI 的核心要素
- **B**：算，工具用什么不重要，关键看自动化程度
- **C**：不算——CI 的"集成"字面意思是合到主线，判定标准是每天有没有真把代码合回主线，长期分支只是"分支上的自动化构建"
- **D**：不算，因为团队规模超过 10 人，CI 不适合大团队


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<p><strong>正确率</strong>：94.34%</p>
<blockquote>
<p>Martin Fowler 对 CI 的核心判定标准是<strong>有没有真把代码频繁合回主线</strong>。长期 feature branch + PR 评审的模式，即使有自动化构建，也只是「分支上的自动化构建」，不是 CI。CI 的「集成」二字是指每天（甚至更频繁）将代码合并到 trunk/mainline，通过频繁集成来降低集成风险。</p>
</blockquote>

</details>

### (17) 有人主张 XP 的"简单设计 + YAGNI"实质就是"粗糙、应付了事"。最准确的判断是（）?

- **A**：确实如此，简单等于不做设计
- **B**：简单设计以重构能力 + 自动化测试套件为底气;缺这两条会退化成粗糙——简单不等于粗糙
- **C**：YAGNI 反对一切抽象层和接口
- **D**：简单设计就是 Code-fix 的另一种叫法


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<p><strong>正确率</strong>：96.86%</p>
<blockquote>
<p><strong>简单设计不等于粗糙</strong>。XP 的简单设计以两大支柱为基础：①重构能力——随时可以在测试保护下改善设计；②自动化测试套件——确保改动不会破坏已有功能。YAGNI（You Aren't Gonna Need It）要求「不提前构建不需要的东西」，而不是「不做设计」。原则是只做满足当前需求的最简设计，并通过持续重构保持其优良性。</p>
</blockquote>

</details>

### (18) 某项目长期靠每周 50–60 小时加班维持进度，管理层认为这就是"敬业"。最贴合 XP 视角的判断是（）?

- **A**：加班是高效团队的常态，应受表彰
- **B**：只要每周不严格超过 40 小时就违规
- **C**：长期加班是计划/范围/设计/测试出严重问题的征兆，不是救命稻草;疲劳的程序员更易破坏测试、引入回归，整体速度反而下降;正确做法是用计划游戏砍范围，用测试和集成压低返工
- **D**：加班只与个人意志有关，与项目工程状态无关


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<p><strong>正确率</strong>：98.11%</p>
<blockquote>
<p>从 XP 视角看，<strong>长期加班是计划/范围/设计/测试出了严重问题的征兆</strong>。XP 提倡「可持续的步伐（Sustainable Pace）」——每周不超过 40 小时。疲劳的程序员更易写出 bug、跳过测试、引入回归。真正的解决方案是用计划游戏砍范围或调整优先级，而非简单堆砌加班时间。</p>
</blockquote>

</details>

### (19) 某新项目刚启动，架构师建议先建好数据库 schema、领域模型、缓存层、加密货币接口等"以后可能要用"的扩展点。最贴合演进式设计观的做法是（）?

- **A**：必须先把数据库和领域模型建齐，否则后期重构成本指数级飙升
- **B**：起步什么都不上，用内存结构跑最小闭环;海量数据到来时才引入数据库，业务复杂度（if-else 嵌套到第三层）到来时才引入领域模型;存疑时默认 YAGNI
- **C**：按行业最佳实践直接引入完整三层架构 + 微服务
- **D**：应该提前设计加密货币等"明天可能要"的扩展点，留出可逆开关


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<p><strong>正确率</strong>：98.11%</p>
<blockquote>
<p>演进式设计（Evolutionary Design）的核心思想：<strong>存疑时默认不上</strong>。起步时用最简单的方案跑通最小闭环（如内存结构而非数据库），当真正的需求（如海量数据、复杂业务逻辑）到来时才引入相应的技术组件。这与 YAGNI 和简单设计一脉相承：不在不确定需要的时候提前构建扩展点。</p>
</blockquote>

</details>

### (20) 关于 AI 时代 TDD 的真正价值，最贴合讲义观点的判断是（）?

- **A**：TDD 在 AI 时代过时了——AI 自带正确性，先写测试是浪费
- **B**：TDD 在 AI 时代只用于面试题，不影响实际开发
- **C**：David Luhr 2024 提出:先写测试 = 把对业务的理解编码为可执行规格，AI 必须在规格约束下生成实现，从"自由发挥"变成"目标规格";同时迫使工程师在让 AI 写代码前先把需求想清楚——这恰是 TDD 在传统开发中的核心价值
- **D**：TDD 让 AI 工具运行更快，是性能优化手段


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<p><strong>正确率</strong>：98.11%</p>
<blockquote>
<p>David Luhr（2024）提出的观点：在 AI 时代，TDD 的价值不是降低，而是<strong>升华</strong>。先写测试 = 把对业务的理解编码为可执行的规格。AI 不是自由发挥，而必须在人类定义的测试约束下生成实现。TDD 从「验证正确性」变为了「定义正确性的标准」。这使 TDD 在 AI 辅助开发中更加不可或缺。</p>
</blockquote>

</details>

## Kanban

> 共 17 题

### (1) Kanban 最早起源于哪个国家的哪个行业（）?

- **A**：美国汽车制造业
- **B**：德国机械工业
- **C**：日本电子工业
- **D**：日本汽车制造业


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：D（单选）</p>
<p><strong>正确率</strong>：99.34%</p>
<blockquote>
<p>Kanban（看板）最早起源于<strong>日本的汽车制造业</strong>，具体来说是由丰田汽车在 1940-50 年代开发的丰田生产系统（TPS）。大野耐一（Taiichi Ohno）从美国超市的「按需补货」模式获得灵感，发明了看板作为拉动式生产的信号工具——下游工序只在需要时通过看板向上游「拉动」零件。</p>
</blockquote>

</details>

### (2) 《Kanban 指南》将看板定义为"通过使用何种系统来优化流程中价值流动的策略"（）?

- **A**：可视化、推动式
- **B**：推动式、自动化
- **C**：自动化、迭代式
- **D**：可视化、拉动式


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：D（单选）</p>
<p><strong>正确率</strong>：96.03%</p>
<blockquote>
<p>Kanban 指南将看板定义为通过<strong>可视化（Visualize）和拉动式（Pull）系统</strong>来优化流程中价值流动的策略。关键点是「拉动式」而非「推动式」——工作不是被推给下一环节，而是由下一环节在有能力时主动拉取。这与传统制造业的「推动式」生产形成对比。</p>
</blockquote>

</details>

### (3) 2003 年出版《精益软件开发:敏捷工具箱》、把丰田精益原则系统性引入软件开发的作者是（）?

- **A**：David J. Anderson
- **B**：Poppendieck 夫妇
- **C**：Corey Ladas
- **D**：大野耐一


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<p><strong>正确率</strong>：94.04%</p>
<blockquote>
<p>2003 年，<strong>Mary 和 Tom Poppendieck</strong> 出版了《Lean Software Development: An Agile Toolkit》，首次系统地将丰田精益原则映射到软件开发领域。他们将七个精益原则和七种软件浪费做了同构翻译，为后来的看板方法和精益软件开发奠定了基础。</p>
</blockquote>

</details>

### (4) David J. Anderson 出版里程碑著作《Kanban: Successful Evolutionary Change for Your Technology Business》的年份是（）?

- **A**：2003 年
- **B**：2007 年
- **C**：2010 年
- **D**：2020 年


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<p><strong>正确率</strong>：94.04%</p>
<blockquote>
<p>David J. Anderson 的里程碑著作《Kanban: Successful Evolutionary Change for Your Technology Business》出版于 <strong>2010 年</strong>。这本书首次完整定义了看板方法（Kanban Method）的六大实践，并提出了「从你现在做的开始，追求增量式的、演进式的改变」这一核心原则。</p>
</blockquote>

</details>

### (5) Kanban Method 六大实践中，下列哪一项不属于（）?

- **A**：可视化
- **B**：限制在制品
- **C**：显式化策略
- **D**：固定迭代节奏


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：D（单选）</p>
<p><strong>正确率</strong>：97.35%</p>
<blockquote>
<p>Kanban Method 的六大实践是：①可视化（Visualize）；②限制在制品（Limit WIP）；③管理流动（Manage Flow）；④显式化策略（Make Policies Explicit）；⑤实施反馈循环（Implement Feedback Loops）；⑥协作改进、实验性演进（Improve Collaboratively, Evolve Experimentally）。<strong>固定迭代节奏不属于这六大实践</strong>——那是 Scrum 的特征（Sprint）。看板不强制时间盒。</p>
</blockquote>

</details>

### (6) Kanban 中"工作流的定义"（DoW）指的是（）?

- **A**：Definition of Workflow
- **B**：Definition of Done
- **C**：Definition of Want
- **D**：Day of Work


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<p><strong>正确率</strong>：98.01%</p>
<blockquote>
<p>看板中 <strong>DoW = Definition of Workflow</strong>（工作流定义）。这是团队对工作如何在看板系统中流动的显式定义，包括：从「开始」到「结束」的所有状态列、每个状态的进入/退出条件、WIP 限制等。DoW 不同于 Scrum 中的 DoD（Definition of Done）。</p>
</blockquote>

</details>

### (7) Kanban Guides 中"产能（Throughput）"的定义是（）?

- **A**：每单位时间内完成的工作项数量
- **B**：已开始但未完成的工作项数量
- **C**：工作项从开始到当前时刻所经过的时间
- **D**：85% 工作项的最长完成时间


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<p><strong>正确率</strong>：98.68%</p>
<blockquote>
<p>产能（Throughput）在 Kanban 语境中定义为<strong>每单位时间内完成的工作项数量</strong>（如每周完成 8 张卡片）。它度量的是系统的「出产速率」。与之相关的指标还有 Cycle Time（一个工作项从开始到完成的时间）和 Lead Time（从请求提出到最终交付的时间）。</p>
</blockquote>

</details>

### (8) 关于"周期时间（Cycle Time）"与"交付时间（Lead Time）"的差异，材料中正确的说法是（）?

- **A**：周期时间一定大于交付时间
- **B**：两者完全等同
- **C**：交付时间通常还包括需求提出到启动前的等待时间
- **D**：周期时间统计未完成的任务，交付时间统计已完成的任务


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<p><strong>正确率</strong>：96.03%</p>
<blockquote>
<p><strong>Lead Time（交付时间）</strong>从客户提出需求的时刻开始计时，通常还包括需求在「待办池」中等待启动的时间。<strong>Cycle Time（周期时间）</strong>仅从工作被「拉入」开发流程（如从 To Do 移到 Doing）的时刻开始计时。因此 <strong>Lead Time 通常 ≥ Cycle Time</strong>，多的那部分就是「前置等待时间」。</p>
</blockquote>

</details>

### (9) 精益思想的演化顺序（从早到晚）正确的是（）?

- **A**：丰田 TPS → 福特流水线 → Poppendieck
- **B**：福特流水线 → 丰田 TPS → Poppendieck
- **C**：Poppendieck → 丰田 TPS → 福特流水线
- **D**：福特流水线 → Poppendieck → 丰田 TPS


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<p><strong>正确率</strong>：92.72%</p>
<blockquote>
<p>精益思想的演化顺序为：<strong>福特流水线（1913）→ 丰田 TPS（1940s-50s）→ Poppendieck 精益软件开发（2003）</strong>。亨利·福特首先发明了大规模流水线生产；丰田在其基础上加入「拉动」和「消除浪费」思想，发展出 TPS；Poppendieck 夫妇将精益原则从制造业翻译到软件领域。三者是递进演化关系。</p>
</blockquote>

</details>

### (10) 关于"自働化"，下列说法正确的是（）?

- **A**：就是"自动化"的别字
- **B**：强调机器完全自主，不需要人参与
- **C**：英文翻译为 automation
- **D**：是和制汉字，比"自動化"多一个"亻"旁，对应 autonomation


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：D（单选）</p>
<p><strong>正确率</strong>：100.0%</p>
<blockquote>
<p>「自働化（Jidoka）」是丰田生产系统的核心概念之一，读者可能注意到它写作「自<strong>働</strong>」而非「自<strong>動</strong>」。<strong>働</strong>是一个和制汉字，比「動」多了一个「亻」（单人旁），体现了「赋予机器以人的智能」——机器不只是自动运转（automation），而是在出现异常时能「自主判断并停机」。对应的英文是 <strong>autonomation</strong>（autonomous + automation），而非简单的 automation。</p>
</blockquote>

</details>

### (11) Poppendieck 在精益软件开发上的核心贡献是（）?

- **A**：同构映射:把"库存"翻译成"在制品（WIP）"
- **B**：提出 Kanban 六大实践
- **C**：发明可视化看板
- **D**：提出 Scrumban


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<p><strong>正确率</strong>：94.7%</p>
<blockquote>
<p>Poppendieck 夫妇的核心贡献是做了<strong>精益概念的同构映射（isomorphic mapping）</strong>：把制造业的「库存（inventory）」翻译成软件的「在制品（WIP，如未合并的代码分支）」；把「过度生产」翻译成「额外功能（extra features）」；把「运输」翻译成「交接（hand-offs）」等。这种同构翻译使得丰田的精益原则能在软件领域落地。</p>
</blockquote>

</details>

### (12) 软件七种浪费中不包括下列哪一项（）?

- **A**：部分完成的工作
- **B**：任务切换
- **C**：过度沟通
- **D**：重新学习


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<p><strong>正确率</strong>：80.79%</p>
<blockquote>
<p>精益软件开发中的<strong>七种浪费（Seven Wastes）</strong>包括：①部分完成的工作；②额外功能（Extra Features）；③重新学习（Relearning）；④交接（Handoffs）；⑤延迟（Delays）；⑥任务切换（Task Switching）；⑦缺陷（Defects）。<strong>过度沟通不在七种浪费之列</strong>——相反，缺乏沟通或沟通不畅才是浪费的常见来源。</p>
</blockquote>

</details>

### (13) 精益"推迟决策"原则中提到的关键概念是（）?

- **A**：最早决定时刻（Earliest Commitment Moment）
- **B**：最后责任时刻（Last Responsible Moment）
- **C**：迭代决策时刻
- **D**：批量决策时刻


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<p><strong>正确率</strong>：98.68%</p>
<blockquote>
<p>精益的「推迟决策」原则中的关键概念是 <strong>Last Responsible Moment（最后责任时刻，LRM）</strong>。这个原则告诉团队：不要过早做出不可逆的决策，而是等到拥有了足够信息、再不做就来不及的那一刻才决定。LRM 不等于「拖延」，而是在不确定性和决策成本之间做最优平衡。</p>
</blockquote>

</details>

### (14) 某公司发布流水线 CI 红灯了，工程师为了赶发版用 `--no-verify` 跳过检查直接合并。按精益视角最贴切的判断是（）?

- **A**：这是合理的工程权衡，因为快速交付是第一原则
- **B**：这违反了内建质量中"自働化"对应的停线权——红灯即应阻塞合并
- **C**：这违反了"尊重人"——不该让 CI 阻塞工程师
- **D**：这违反了"创建知识"——应该先开个回顾会议


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<p><strong>正确率</strong>：100.0%</p>
<blockquote>
<p>CI 红灯代表流水线检测到了问题。用 <code>--no-verify</code> 跳过检查直接合并，<strong>违反了内建质量（Build Quality In）的「停线权」</strong>——在丰田 TPS 中称为 <strong>Jidoka（自働化）</strong>：任何人发现问题都有权「停止生产线」。红灯意味着「停下来修问题」，而不是「绕过问题继续」。</p>
</blockquote>

</details>

### (15) 某 Kanban 团队的瓶颈列堆积了 8 张卡，团队 6 人，每天加班赶工依然完不成。最贴合材料原则的应对是（）?

- **A**：把瓶颈列 WIP 上限调到约 4，停止往里推工作，先疏通瓶颈
- **B**：临时绕开 WIP 限制，把卡片放进快速通道
- **C**：把瓶颈列拆给前面流程的空闲工人
- **D**：让所有人加班直到追平


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<p><strong>正确率</strong>：99.34%</p>
<blockquote>
<p>Kanban 的核心原则之一是<strong>限制在制品（Limit WIP）</strong>。当瓶颈列出现堆积时，正确的做法是：<strong>收紧 WIP 限制</strong>（这里建议从默认调到约 4），停止往瓶颈前推工作，集中力量疏通瓶颈（如分析原因、补充资源、优化流程）。其他选项（绕开限制、拆给空闲工人、加班）都违反了「暴露瓶颈 → 解决瓶颈」的精益原则。</p>
</blockquote>

</details>

### (16) 团队反思会上有人提议:"开发已经很快了，但测试总是积压。我们应给开发团队加更多 KPI 提升速度。"按精益视角最贴切的判断是（）?

- **A**：对，开发越快，整体越快
- **B**：对，KPI 是局部优化的好工具
- **C**：错，局部最优 ≠ 全局最优;开发更快只会让测试队列更长，整体仍慢
- **D**：错，应取消测试这一环节


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<p><strong>正确率</strong>：100.0%</p>
<blockquote>
<p>此题考察精益的全局优化原则：<strong>局部最优 ≠ 全局最优（Sub-optimization）</strong>。开发更快只会让下游测试队列积压更多，整体交付速度并不会变快——瓶颈仍然在测试环节。正确的做法是分析整个价值流，找到真正的瓶颈（约束理论中的约束点）并进行系统性优化。</p>
</blockquote>

</details>

### (17) 某团队把 Kanban 当作"待办列表的电子化"——每张卡有人写有人做，但没有 WIP 限制、没有显式策略、也没有反馈会议。下列判断最准确的是（）?

- **A**：这就是 Kanban，因为 Kanban 没有强制角色和会议
- **B**：这只是看板的"形"，缺了"限制 WIP""显式化策略""反馈循环"等核心实践，称不上 Kanban 方法
- **C**：这是 Scrumban，因为只用了部分 Kanban 实践
- **D**：这违反了 Scrum，因为没有 Sprint 计划


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<p><strong>正确率</strong>：98.68%</p>
<blockquote>
<p>只把看板当作「待办列表的电子化」但缺少 <strong>WIP 限制、显式策略和反馈循环</strong>，这只是看板的「形」而非「神」。Kanban Method 的核心不仅仅是可视化板，而是通过 WIP 限制暴露瓶颈、通过显式策略定义规则、通过反馈循环持续改进。缺少这些核心实践的工具只是任务追踪系统，称不上 Kanban 方法。</p>
</blockquote>

</details>

## DevOps

> 共 60 题

### (1) "Measure twice, Cut once" 是哪个阶段的典型开发特征？

- **A**：软件作坊阶段
- **B**：软件成为独立产品阶段
- **C**：网络化阶段
- **D**：软硬件一体化阶段


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：D（单选）</p>
<blockquote>
<p>「Measure twice, Cut once」（量两次，锯一次）是制造业中的经典格言，强调在动手之前充分规划和验证。在软件发展史中，这对应最早期「软硬件一体化」阶段——软件作为硬件的附属，修改成本极高，因而必须在编码前做充分的设计和规格确认。IBM System/360 是这一阶段的典型代表。</p>
</blockquote>

</details>

### (2) 关于软件过程管理，以下哪一种说法是比较贴切的：

- **A**：进入互联网时代，软件过程管理是过于老套的话题。
- **B**：软件过程管理是软件企业发展到较高层次才需要关心的话题。
- **C**：软件过程管理关注的是企业软件过程能力的稳定输出和提升。
- **D**：软件过程管理主要关注软件成本和质量目标的达成。


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<blockquote>
<p>软件过程管理的核心关注点是「企业软件过程能力的稳定输出和提升」，这个表述准确捕捉了 CMM/CMMI 和过程改进运动的本质——不是关注单次项目的成败，而是组织级的长期能力建设。选项 D 偏窄（仅关注成本和质量），A 和 B 过度轻视了过程管理的价值。</p>
</blockquote>

</details>

### (3) 软件开发的本质难题中哪一个与软件发展阶段没有直接关系？

- **A**：复杂性
- **B**：可变性
- **C**：一致性
- **D**：不可见性


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：D（单选）</p>
<blockquote>
<p>软件开发的本质难题中，复杂性、可变性、一致性都是固有且随软件不同发展阶段表现各异的问题。而「不可见性（Invisibility）」是软件的根本特征——软件本身没有物理形态，本质上不可见——这与处于哪个发展阶段没有直接关系，而是软件与生俱来的特性。</p>
</blockquote>

</details>

### (4) "Code and Fix" 是软件发展哪个阶段的典型开发特征？

- **A**：网络化和服务化
- **B**：软件作为独立产品
- **C**：互联网时代
- **D**：软硬件一体化


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：D（单选）</p>
<blockquote>
<p>「Code and Fix」（边写边改）是最原始的开发方式——没有正式的开发流程和规范，编码和调试交替进行。这种模式在软件依附于硬件的「软硬件一体化」阶段最为典型，因为当时软件规模小、需求简单，且软件本身不单独销售。</p>
</blockquote>

</details>

### (5) 以下哪个因素促成了软件成为独立的产品？

- **A**：互联网的出现
- **B**：个人电脑的出现
- **C**：高级程序设计语言的出现
- **D**：操作系统的出现


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：D（单选）</p>
<blockquote>
<p>操作系统的出现是软件独立为产品的关键推动力。在操作系统出现之前，应用程序必须直接管理硬件资源，软件与特定硬件深度绑定。操作系统提供了标准化的硬件抽象层（通过系统调用），使得同一软件可以运行在不同硬件上，软件因此才可能作为独立产品销售。这一转折发生在 1960 年代 IBM System/360 及 OS/360 时期。</p>
</blockquote>

</details>

### (6) 软件危机和软件工程这两个概念提出时间是？

- **A**：上世纪八十年代
- **B**：上世纪五十年代
- **C**：上世纪七十年代
- **D**：上世纪六十年代


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：D（单选）</p>
<blockquote>
<p>「软件危机」(Software Crisis)和「软件工程」(Software Engineering)这两个术语均出现于 1968 年 NATO 软件工程会议。但概念的酝酿和问题的暴露始于 1960 年代中期——随着第三代计算机的普及，软件规模和复杂度急剧增长，导致大量项目超支、延期甚至失败。</p>
</blockquote>

</details>

### (7) 关于形式化方法的描述当中，不正确的有哪些？

- **A**：这种方法应用范围有限，例如：不适合跟客户讨论需求。
- **B**：这种方法是网络化和服务化阶段用来应对软件开发本质四大难题而提出来的
- **C**：这种方法对开发人员技能有较高的要求
- **D**：这种方法的主要目的是解决软件开发的效率问题


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：['B', 'D']（多选）</p>
<blockquote>
<p>题目要求选「不正确」的选项。选中项是两条不正确的说法：①「形式化方法是网络化和服务化阶段才提出的」——这是错误的，因为形式化方法早在 1970-80 年代就已存在（如 VDM、Z、B 方法等），远早于网络化时代。②「形式化方法的主要目的是解决软件开发的效率问题」——这也是错误的，它的主要目的是解决正确性和可靠性问题。未选中的两条是正确的：形式化方法确实应用范围有限，且对开发人员技能有较高要求。</p>
</blockquote>

</details>

### (8) 关于迭代式方法的说法哪些是比较恰当的？

- **A**：迭代式方法是上世纪九十年代中后期才出现的一种方法
- **B**：迭代式方法是指一类具有类似特征的方法
- **C**：迭代式方法主要特征在于将软件开发过程视作一个逐步学习和交流的过程
- **D**：迭代式方法主要是为了解决软件开发的质量问题


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：['B', 'C']（多选）</p>
<blockquote>
<p>题目要求选「比较恰当」的说法。选中项是两条恰当的描述：①「迭代式方法是指一类具有类似特征的方法」——这准确描述了迭代式方法的本质是一个方法论族，而非单一方法。②「迭代式方法主要特征在于将软件开发过程视作一个逐步学习和交流的过程」——这抓住了迭代的核心：通过增量交付获得反馈，在反馈中学习和调整。未选中的两条不恰当：迭代式方法远早于 1990 年代就已存在，且它的主要目标不仅是解决质量问题。</p>
</blockquote>

</details>

### (9) DevOps方法的出现具有一定的必然性，与以下哪些软件应用特征相匹配？

- **A**：软件系统部署环境越来越错综复杂
- **B**：用户需求多变所带来了软件系统的快速演化的要求
- **C**：软件在社会生活当中扮演了越来越关键的角色
- **D**：软件定义世界，软件随处可见


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：['A', 'B', 'C', 'D']（多选）</p>
<blockquote>
<p>DevOps 的出现与四个特征均高度相关：(A) 部署环境复杂化——现代系统涉及云、容器、多环境；(B) 需求快速演化——敏捷和精益要求快速交付和反馈；(C) 软件在社会中的关键角色——对可靠性和速度的要求提升；(D) 软件无处不在——软件定义世界的趋势。这四者共同构成了 DevOps 的「必然性」背景。</p>
</blockquote>

</details>

### (10) DevOps的哪些特点可以有效支撑当前社会对软件系统的期望？

- **A**：微服务架构设计
- **B**：工具链支持高效率的自动化
- **C**：虚拟机技术的大量应用
- **D**：敏捷开发、精益思想以及看板方法，支持快速开发、交付、迭代和演化


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：['A', 'B', 'C', 'D']（多选）</p>
<blockquote>
<p>DevOps 通过多种技术实践支撑现代软件系统的期望：微服务架构设计支持独立部署和扩展；工具链自动化（CI/CD）提高交付效率；虚拟机/容器技术提供环境一致性和资源弹性；敏捷和精益思想保证快速迭代和价值交付。这四个选项共同描述了 DevOps 的技术支撑体系。</p>
</blockquote>

</details>

### (11) DevOps中的XaaS特指 SaaS、PaaS以及IaaS这三种。

- **A**：正确
- **B**：错误


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<blockquote>
<p>XaaS（Everything as a Service / Anything as a Service）是一个统称，泛指一切以「即服务」模式提供的产品。它不仅包括 SaaS、PaaS、IaaS，还包括 DaaS（数据即服务）、FaaS（函数即服务）、BaaS（后端即服务）等数十种细分类型。因此说 XaaS「特指」这三种是不准确的。</p>
</blockquote>

</details>

### (12) 下述各个度量项中，哪一个不是PSP的基本度量项？

- **A**：时间
- **B**：缺陷
- **C**：风险
- **D**：规模


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<blockquote>
<p>PSP 的三个基本度量项是：时间（Time）、缺陷（Defect）、规模（Size）。Watts Humphrey 提出：「软件开发的三个主要过程度量是时间、规模和缺陷。如果能精确度量这三者，其他大多数重要度量都可以从中导出。」「风险」不是 PSP 的基本度量项——它属于更高级的管理层面。</p>
</blockquote>

</details>

### (13) 关于面向用户的质量观，我们应该关注如下哪些问题：

- **A**：用户期望是否有优先级？
- **B**：用户期望的优先级对软件开发的影响？
- **C**：界面和可操作性是首要的，因为这是用户能直接感受到的。
- **D**：真实用户是谁？


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：['A', 'B', 'D']（多选）</p>
<blockquote>
<p>面向用户的质量观关注的是用户的真实期望。选中项是三个正确关注点：①真实用户是谁——这是首要问题，不同用户有不同的质量期望；②用户期望是否有优先级——因为不是所有期望都同等重要；③用户期望的优先级对软件开发的影响——决定了开发资源的分配。未选中的一条不正确：界面和可操作性是用户直接感知的，但并非「首要」——用户更关心功能是否满足实际需求。</p>
</blockquote>

</details>

### (14) PSP当中为什么用缺陷管理替代质量管理？下述说法中正确的是：

- **A**：因为缺陷管理相关的活动（例如，测试等）本来就是软件开发中必须要开展的活动。
- **B**：因为缺陷往往对应了面向用户质量观中的首要用户期望。
- **C**：因为缺陷管理和质量管理其实是一回事。
- **D**：因为单纯质量管理很难操作。


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：['B', 'D']（多选）</p>
<blockquote>
<p>PSP 用缺陷管理替代质量管理是因为：①「缺陷往往对应了面向用户质量观中的首要用户期望」——用户首先关心软件是否正常工作，缺陷直接反映软件是否满足功能需求。②「单纯质量管理很难操作」——「质量」是一个模糊的、多维度的概念，难以直接度量；而缺陷是具体的、可计数的，可以作为质量的代理指标。未选中的两条不正确：缺陷管理相关活动是必须开展的但这不等于它就是质量管理；缺陷管理和质量管理并非一回事。</p>
</blockquote>

</details>

### (15) 关于PROBE估算法，下述各种说法中，不正确的有哪些？

- **A**：PROBE估算结果带着小数，肯定不准确，因而， 不应该在项目估算的时候使用。
- **B**：PROBE方法不能用来估算质量。
- **C**：PROBE不能给出精确估算，因而适合用来跟用户讨论需求和规模。
- **D**：PROBE方法不需要历史数据。


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：['A', 'C', 'D']（多选）</p>
<blockquote>
<p>题目要求选「不正确」的说法。选中项是三条不正确的说法：①「PROBE 估算结果带着小数，肯定不准确」——统计方法产生小数是正常特征，不代表不准确。②「PROBE 不能给出精确估算，因而适合用来跟用户讨论需求和规模」——PROBE 恰是基于历史数据的估算方法，用于项目内部计划，不是与用户讨论需求的工具。③「PROBE 方法不需要历史数据」——PROBE 的核心前提就是需要历史数据来建立估算基准。未选中的一条正确：PROBE 方法不能用来估算质量。</p>
</blockquote>

</details>

### (16) 关于质量路径（Quality Journey），下列说法中哪些不恰当。

- **A**：质量路径中所列举的方法都是提升开发质量的有效手段，可以随意选择使用。
- **B**：进入测试之前的高质量，是获得测试之后高质量软件系统的前提条件。
- **C**：高质量软件产品最终还是需要依赖测试来确保。v
- **D**：质量路径与个体软件工程师无关，是团队层面的集体努力。


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：['A', 'D']（多选）</p>
<blockquote>
<p>题目要求选「不恰当」的说法。选中项是两条不恰当的说法：①「质量路径中所列举的方法可以随意选择使用」——不恰当，因为这些方法有严格的依赖关系和适用条件，PSP 必须先于 TSP，个人度量先于团队度量。②「质量路径与个体软件工程师无关，是团队层面的集体努力」——不恰当，因为质量路径恰恰始于个体软件工程师的自我管理和度量（PSP），再逐步扩展到团队（TSP）。未选中的两条恰当：进入测试前的高质量是前提；最终仍需依赖测试来确保质量。</p>
</blockquote>

</details>

### (17) 关于评审检查表，下述说法中不恰当的是：

- **A**：项目团队所有人应该共用一份评审检查表，体现统一性
- **B**：评审检查表应该保持稳定，确保缺陷不会被遗漏
- **C**：评审检查表应该定期更新
- **D**：评审检查表应该是个性化的


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：['A', 'B']（多选）</p>
<blockquote>
<p>题目要求选「不恰当」的说法。选中项是两条不恰当的说法：①「项目团队所有人应该共用一份评审检查表，体现统一性」——不恰当，不同角色、不同模块、不同类型的缺陷需要不同的检查视角，个性化检查表更有针对性。②「评审检查表应该保持稳定，确保缺陷不会被遗漏」——不恰当，检查表应该定期更新以反映团队积累的经验和常见缺陷模式。未选中的两条恰当：检查表应定期更新、应是个性化的。</p>
</blockquote>

</details>

### (18) 关于PQI，下述说法中不恰当的是：

- **A**：PQI越高越好，最好达到1.0
- **B**：PQI可以用来辅助判断模块开发的质量
- **C**：PQI五个分指标都可以超过1.0，比如，设计时间多于编码时间的时候，该分指标就超过1.0了
- **D**：PQI可以为过程改进提供依据


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：['A', 'C']（多选）</p>
<blockquote>
<p>题目要求选「不恰当」的说法。选中项是两条不恰当的说法：①「PQI 越高越好，最好达到 1.0」——不恰当，PQI 达到 1.0 意味着各指标在理想范围，但超过 1.0 不代表「更好」，需要具体分析。②「PQI 五个分指标都可以超过 1.0」——不恰当，各分指标有各自的计量方式，并非都能超过 1.0。未选中的两条恰当：PQI 可辅助判断模块质量、可为过程改进提供依据。</p>
</blockquote>

</details>

### (19) 关于评审，下述说法中不恰当是：

- **A**：代码的个人评审也应该通过评审检查表来进行。
- **B**：代码的个人评审最好交叉进行，因为阅读自己代码容易产生思维定式，不利于缺陷发现。
- **C**：代码的个人评审应该安排在单元测试之后，确保评审对象有着较高的质量，提升评审价值。
- **D**：如果安排了代码的小组评审，那么代码个人评审就可以不用做。


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：['B', 'C']（多选）</p>
<blockquote>
<p>题目要求选「不恰当」的说法。选中项是两条不恰当的说法：①「代码的个人评审最好交叉进行」——不恰当，个人评审是阅读自己的代码，针对自身常犯错误进行自查，交叉评审是小组评审的做法。②「代码的个人评审应该安排在单元测试之后」——不恰当，个人评审应在单元测试之前进行，先评审再测试，及早发现缺陷，降低修复成本。未选中的两条恰当：个人评审应通过检查表来进行；如果已安排小组评审，个人评审依然需要做。</p>
</blockquote>

</details>

### (20) 根据敏捷宣言，以下哪项描述了更多的价值？

- **A**：个体和交互、可工作的软件、客户协作、响应变化
- **B**：响应变化、个体和交互、流程和工作、客户协作
- **C**：可工作的软件、个体交互、响应变化、相近的文档
- **D**：客户协作、遵循计划、可工作的软件、个体交互


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<blockquote>
<p>敏捷宣言的四条价值观（按优先级）为：个体和交互高于流程和工具、可工作的软件高于详尽的文档、客户协作高于合同谈判、响应变化高于遵循计划。选项 A 完整列出这四个左项，是正确描述。其他选项混淆了左右项或混入了非宣言内容。</p>
</blockquote>

</details>

### (21) 下列哪一项更好地描述了敏捷宣言？

- **A**：它包含了许多敏捷团队使用的实践
- **B**：它概述了构建软件的最有效方法
- **C**：它包含了建立敏捷思维方式的价值观
- **D**：它定义了构建软件的规则


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<blockquote>
<p>敏捷宣言本质上是一组价值观声明，目的是建立敏捷思维方式的哲学基础。它不是具体的实践指南（A 错），没有定义「最有效的方法」（B 错），也不是规则手册（D 错）。它体现了「是什么比怎么做更重要」——价值观引领实践，而非反过来。</p>
</blockquote>

</details>

### (22) 你是一个软件团队的开发人员。 一个用户向你的团队询问有关构建新功能的信息，并以规范的形式提供了需求。 她非常确定这个功能要如何工作，并承诺不会有任何变化。 哪种敏捷价值最适用于这种情况？

- **A**：工作的软件 高于 详尽的文档
- **B**：个体和互动 高于 流程和工具
- **C**：客户合作 高于 合同谈判
- **D**：响应变化 高于 遵循计划


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<blockquote>
<p>题中用户提供了详尽的需求规范且承诺不会有变化。这种情况下，关键问题不是应对变化（D）、不是合同谈判（C）、也不是团队互动流程（B），而是「如何将规范转化为可工作的软件」。这正是「可工作的软件高于详尽的文档」这条价值观的应用场景——即使有详尽的规范文档，最终衡量标准仍是交付可工作的软件。</p>
</blockquote>

</details>

### (23) Sean是一个正在构建财务软件的团队的开发人员。 他的团队被要求开发一个新的交易系统。 他和他的团队召开会议来提出他们正在使用的工作流的图景。 然后，他们将流程放在白板上，流程中的每个步骤都有一列。 经过对团队在白板上的工作项目进行了几周观察，他们注意到这个过程中有几个步骤似乎过载了。对于他们来说，下一步应该做什么？

- **A**：与团队合作，在工作进展缓慢的阶段更好地完成工作
- **B**：专注于完成看板上的工作
- **C**：对过载步骤中正在进行的工作项目的数量进行限制
- **D**：在较慢的步骤中使用更多的人力


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<blockquote>
<p>题目描述的场景是典型的看板实施：团队可视化了工作流（白板）、观察了几周后发现某些步骤过载。根据看板方法，下一步应该是限制在制品（WIP）——对过载步骤中正在进行的工作项数量设置上限。这是看板的核心实践之一：通过限制 WIP 来暴露瓶颈、平衡流动，而不是简单地加人（会引入更多沟通成本）或仅仅「更好地完成工作」（太模糊）。</p>
</blockquote>

</details>

### (24) 下列哪一个不是精益原则？

- **A**：实施反馈循环
- **B**：消除浪费
- **C**：尽可能晚的做决定
- **D**：识别所有的步骤


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<blockquote>
<p>精益原则包括：消除浪费、内建质量、创造知识、推迟决策（尽可能晚做决定）、快速交付、尊重人、优化全局。A「实施反馈循环」不在这七个精益原则之中——反馈循环是看板方法和敏捷实践的核心，而非波彭迪克夫妇提出的七个精益原则本身。</p>
</blockquote>

</details>

### (25) 下列哪一个更好地描述了如何使用看板？

- **A**：帮助团队自我组织，并了解工作流程中的瓶颈所在
- **B**：观察特征如何流经过程，以便团队可以确定如何限制WIP并通过工作流程中的步骤确定最均匀的工作流程
- **C**：跟踪WIP限制和当前任务状态，以便团队知道他们还有多少工作要做
- **D**：跟踪缺陷和问题，并创建解决产品问题的最快途径


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<blockquote>
<p>看板的核心使用方式是：观察工作项如何在流程中流动，通过数据来分析和优化 WIP 限制，使工作流程尽可能均匀和平滑。这不仅仅是跟踪状态或缺陷，而是「观察、度量、优化」的持续改进循环。选项 B 最完整地描述了这一核心思想。</p>
</blockquote>

</details>

### (26) 在制品规模越小越好，因为这样可以优化前置时间，并且团队的效率会变高。

- **A**：正确
- **B**：错误


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<blockquote>
<p>「在制品规模越小越好」是一个常见误解。看板和精益强调的是「适当」的 WIP 限制——太小会导致频繁的上下文切换和闲置时间（瓶颈前的人无事可做），太大则导致任务堆积和前置时间膨胀。存在一个最优的 WIP 范围，而非追求无限小。过小的 WIP 反而可能降低整体吞吐量。</p>
</blockquote>

</details>

### (27) 在组成派看来，软件架构是指？

- **A**：软件架构是一系列重要决策的集合，包括构成系统的结构要素及其接口的选择。
- **B**：软件架构包括系统组件、连接件和约束的集合。
- **C**：软件架构由软件元素、这些元素的外部可见属性，以及元素之间的关系组成。
- **D**：软件架构将系统定义为计算组件及组件间的交互。


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：['B', 'C', 'D']（多选）</p>
<blockquote>
<p>在软件架构领域，「组成派」将软件架构视为系统组件、连接件和约束的集合（B），或计算组件及其交互的集合（D），或软件元素及其外部可见属性和关系的集合（C）。而选项 A（软件架构是一系列重要决策的集合）是「决策派」的观点，不属于组成派。</p>
</blockquote>

</details>

### (28) 分层架构将软件系统的组件分成多个互不重叠的层，包括

- **A**：物理层
- **B**：表现层
- **C**：业务层
- **D**：应用层


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：['B', 'C']（多选）</p>
<blockquote>
<p>经典的分层架构通常包含：表现层（处理用户界面和外部请求）、业务层（核心业务逻辑）、持久层（数据访问）、数据库层。题目问分层架构「包括」哪些——选中项是表现层和业务层，这两层是分层架构最核心的「必选」分层。物理层不是软件分层的标准命名，应用层在不同语境下有不同含义（有时等同于业务层）。此题以课程材料中的分类为准。</p>
</blockquote>

</details>

### (29) 在应用分层架构的软件系统中，最先处理外部请求的是：

- **A**：业务层
- **B**：应用层
- **C**：表现层
- **D**：数据层


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<blockquote>
<p>在分层架构中，外部请求的典型路径是：表现层（Presentation Layer）→ 业务层（Business Layer）→ 持久层（Persistence Layer）→ 数据库。因此，最先处理外部请求的是表现层。它负责接收 HTTP 请求、解析参数、调用下层服务，并将结果渲染返回。</p>
</blockquote>

</details>

### (30) 分层架构模式的缺点包括：

- **A**：不易于持续发布和部署
- **B**：由于层间依赖关系，软件系统的可扩展性差
- **C**：软件升级需要暂停整个服务
- **D**：额外的性能开销


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：['A', 'B', 'C', 'D']（多选）</p>
<blockquote>
<p>分层架构的四个主要缺点：(A) 不易于持续发布和部署——因为代码耦合为整体，每次变更需要全量构建和部署；(B) 层间依赖关系导致可扩展性差——垂直扩展容易，水平扩展困难；(C) 升级需要暂停服务——单体架构通常不支持热更新；(D) 性能开销——请求需要穿越多个层，每层都有序列化/反序列化和网络或进程间调用成本。</p>
</blockquote>

</details>

### (31) 以下哪几个不是面向服务架构强调的实现原则？

- **A**：服务去中心化
- **B**：服务简单
- **C**：服务重用
- **D**：服务解耦


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：['A', 'B']（多选）</p>
<blockquote>
<p>题目要求选「不是」SOA 核心原则的选项。面向服务架构（SOA）强调的实现原则包括：服务重用、服务解耦、服务抽象、服务自治、服务可组合性等。A「服务去中心化」和 B「服务简单」不是 SOA 的核心实现原则——前者是微服务架构的特征，后者也不符合 SOA 企业级重量级的定位。C（服务重用）和 D（服务解耦）是 SOA 的核心原则，因此未被选中。</p>
</blockquote>

</details>

### (32) 本质上，微服务架构是SOA的一种扩展。

- **A**：错误
- **B**：正确


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<blockquote>
<p>微服务架构在本质上是 SOA 的一种演进和精化——两者共享「通过服务接口进行系统分解」的核心理念。但微服务更强调去中心化治理、去中心化数据管理、轻量级通信协议（REST 而非 SOAP），以及独立部署。业界普遍认为微服务是「SOA 做对了的样子」(SOA done right)。</p>
</blockquote>

</details>

### (33) 以下选项中，哪些属于微服务架构的特点？

- **A**：中心化
- **B**：基础设施自动化
- **C**：通过服务组件化
- **D**：内聚和解耦


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：['B', 'C', 'D']（多选）</p>
<blockquote>
<p>微服务架构的核心特点包括：(B) 基础设施自动化——容器化、CI/CD、自动化部署；(C) 通过服务组件化——每个微服务是一个独立的可部署组件；(D) 内聚和解耦——服务内部高内聚、服务之间松耦合。而 (A) 中心化是单体架构的特征，微服务强调去中心化。</p>
</blockquote>

</details>

### (34) 以下对于微服务优点的描述中，哪一个是错误的？

- **A**：微服务系统测试变得非常简单
- **B**：单个微服务很简单，只关注一个业务功能
- **C**：微服务可以使用RPC进行服务间通信
- **D**：不同的微服务可以使用不同的语言进行开发


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<blockquote>
<p>微服务架构的一个显著挑战是测试复杂性——分布式系统的集成测试和端到端测试远比单体系统复杂。其他三个选项都是微服务的真实优点：单个服务职责单一、可以使用不同技术栈、通过 RPC/REST 进行服务间通信。因此 A「测试变得非常简单」是错误的。</p>
</blockquote>

</details>

### (35) 与面向服务架构相关的Web服务标准包括：

- **A**：UML
- **B**：HTTPS
- **C**：SOAP
- **D**：WSDL


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：['B', 'C', 'D']（多选）</p>
<blockquote>
<p>SOA 相关的 Web 服务标准包括：SOAP（Simple Object Access Protocol）——基于 XML 的消息协议；WSDL（Web Services Description Language）——描述服务接口；UDDI（Universal Description, Discovery and Integration）——服务注册与发现。HTTPS 是传输层安全协议，也是 Web 服务通信的基础。UML 是建模语言，不属于 Web 服务标准。</p>
</blockquote>

</details>

### (36) 以下哪些是Docker的存储驱动：

- **A**：其他都是
- **B**：Device mapper
- **C**：OverlayFS
- **D**：AUFS


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<blockquote>
<p>Docker 支持多种存储驱动：AUFS（早期的默认驱动，需内核补丁）、Device Mapper（RHEL/CentOS 推荐的块级驱动）、OverlayFS（目前最推荐的默认驱动，overlay2）。因此选项 A「其他都是」是正确的——这三者都是 Docker 的合法存储驱动。</p>
</blockquote>

</details>

### (37) 以下哪个命令可以查看当前运行容器：

- **A**：docker top
- **B**：docker run
- **C**：docker ps
- **D**：docker logs


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<blockquote>
<p><code>docker ps</code> 是查看当前运行中的容器的命令（默认只显示运行中的；<code>-a</code> 显示包括已停止的所有容器）。<code>docker run</code> 创建并启动新容器；<code>docker top</code> 显示容器的进程信息（非列出容器）；<code>docker logs</code> 查看容器日志。</p>
</blockquote>

</details>

### (38) 以下哪些是Kubernetes的控制器：

- **A**：Rolling Updates
- **B**：ReplicaSet
- **C**：Deployment
- **D**：Both ReplicaSet and Deployment


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：D（单选）</p>
<blockquote>
<p>Kubernetes 的控制器（Controller）包括 ReplicaSet（确保指定数量的 Pod 副本运行）和 Deployment（建立在 ReplicaSet 之上，提供声明式更新和回滚）。Rolling Updates 是 Deployment 的一种更新策略，不是独立的控制器。因此「Both ReplicaSet and Deployment」是正确的。</p>
</blockquote>

</details>

### (39) 以下哪些是Kubernetes的核心概念

- **A**：Volumes
- **B**：Services
- **C**：其他都是
- **D**：Pods


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<blockquote>
<p>Kubernetes 的核心概念包括 Pods（最小的部署单元）、Services（稳定的网络接入点）、Volumes（持久化存储）等。选项中 Pods、Services、Volumes 都是核心概念，所以「其他都是」正确。</p>
</blockquote>

</details>

### (40) Kubernetes里面的Replication控制器的职责是：

- **A**：当已存在的Pod异常退出后，创建新的Pod
- **B**：删除或者更新多个Pod
- **C**：其他都是
- **D**：帮助达到预期的状态


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<blockquote>
<p>Replication 控制器（现在称为 ReplicaSet）的职责包括：当已存在的 Pod 异常退出时创建新的（A）、帮助达到并维持期望的 Pod 数量状态（D）、以及管理 Pod 的生命周期（创建/删除/更新）。因此「其他都是」正确。在 Kubernetes 中，ReplicaSet 确保在任何时刻都有指定数量的 Pod 副本在运行。</p>
</blockquote>

</details>

### (41) 如何通过命令行创建一个容器

- **A**：docker run
- **B**：docker start
- **C**：docker poll
- **D**：docker create


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<blockquote>
<p><code>docker run</code> 是创建并启动一个新容器的命令（等价于 <code>docker create</code> + <code>docker start</code>）。<code>docker start</code> 启动一个已存在但停止的容器；<code>docker create</code> 创建容器但不启动；没有 <code>docker poll</code> 命令。</p>
</blockquote>

</details>

### (42) 使用Kubernetes带来的好处有哪些

- **A**：自动回滚
- **B**：自动调度
- **C**：其他都是
- **D**：横向扩展


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<blockquote>
<p>Kubernetes 的好处包括：自动调度（将 Pod 分配到合适的节点上）、自动回滚（通过 Deployment 的实现）、横向扩展（自动或手动调整 Pod 副本数量）。这些都属于 Kubernetes 的核心功能，因此「其他都是」正确。</p>
</blockquote>

</details>

### (43) 以下哪项用于确保pod不会被调度到不适当的节点上？

- **A**：Taints 和 Tolerations
- **B**：Taints
- **C**：以上都不是
- **D**：Tolerations


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<blockquote>
<p>Taints（污点）和 Tolerations（容忍）是 Kubernetes 中用于 Pod 调度的机制。Taints 标记在 Node 上，表示「不要调度不匹配的 Pod 到这个节点」；Tolerations 标记在 Pod 上，表示「这个 Pod 可以容忍这个节点的污点」。两者配合使用才能确保 Pod 不会被调度到不适当的节点上。单独的 Taints 或 Tolerations 都不够——必须两者配合。</p>
</blockquote>

</details>

### (44) 关于Kubernetes的namespace的论述是否正确：命名空间是在多个用户之间划分群集资源的方法

- **A**：错误
- **B**：正确


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<blockquote>
<p>Kubernetes 中的 Namespace 是用于在多个用户或团队之间划分集群资源的虚拟隔离机制。它提供了一种方法将集群资源划分为互不重叠的组，适合多团队共享同一集群的场景。这个描述是正确的。</p>
</blockquote>

</details>

### (45) Docker容器的状态有

- **A**：Restarting
- **B**：Exited
- **C**：Paused
- **D**：Running


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：['B', 'D']（多选）</p>
<blockquote>
<p>Docker 容器的标准状态包括：Created（已创建）、Running（运行中）、Paused（暂停）、Restarting（重启中）、Exited（已退出）、Dead（已死亡）。题中选项 B（Exited）和 D（Running）是 Docker 容器的正式状态。Paused 和 Restarting 也是 Docker 状态，但此题答案标记为 B、D，可能源于特定课堂材料中的状态分类。</p>
</blockquote>

</details>

### (46) 下列哪项不属于协同开发工具？

- **A**：Rally
- **B**：JIRA
- **C**：Kanban
- **D**：Confluence


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：D（单选）</p>
<blockquote>
<p>协同开发工具指用于团队协作和项目管理的工具。Rally（敏捷项目管理）、JIRA（事务跟踪和项目管理）、Kanban（看板工具）都属于协同开发工具。Confluence 是 Atlassian 的 Wiki 和知识管理工具——虽然也用于协同，但在分类上更偏「文档协作」而非「开发协同」。此题中的分类以课程材料为准。</p>
</blockquote>

</details>

### (47) 下列哪种持续集成工具是目前DevOps领域使用最广泛的？

- **A**：TeamCity
- **B**：Jenkins
- **C**：Travis CI
- **D**：VSTS


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<blockquote>
<p>Jenkins 是目前 DevOps 领域使用最广泛的持续集成工具。根据多份行业调查报告（如 JetBrains Developer Survey、Stack Overflow Survey），Jenkins 的 CI/CD 市场份额长期领先于 TeamCity、Travis CI 和 Azure DevOps (VSTS)。</p>
</blockquote>

</details>

### (48) Jenkins支持工作流即代码（pipeline-as-code）。

- **A**：正确
- **B**：错误


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<blockquote>
<p>Jenkins 支持 Pipeline-as-Code，即用 Jenkinsfile（基于 Groovy DSL）来定义构建流水线。这使得 CI/CD 流程可以像代码一样进行版本控制、代码审查和重用。这一特性自 Jenkins 2.0（2016 年）引入后成为其标志性功能。</p>
</blockquote>

</details>

### (49) 以下哪项不是Git的文件目录？

- **A**：Documents
- **B**：加载区
- **C**：工作目录
- **D**：.git目录


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<blockquote>
<p>Git 的核心目录结构包括：工作目录（Working Directory）——存放实际文件的目录；暂存区（Staging Area / Index）——暂存要提交的更改；.git 目录——存放所有版本控制元数据的隐藏目录（包括对象库、引用、配置等）。「Documents」不是 Git 的固有概念——它与 Git 的工作机制无关。</p>
</blockquote>

</details>

### (50) 下列哪种编译工具无法编译JAVA语言？

- **A**：Gradle
- **B**：Ant
- **C**：MSBuild
- **D**：Maven


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：C（单选）</p>
<blockquote>
<p>Gradle（基于 Groovy/Kotlin DSL）、Ant（基于 XML）、Maven（基于 POM）都是 Java 生态中的主流构建工具。MSBuild 是 Microsoft Build Engine，用于 .NET 和 C++ 项目，不能直接编译 Java 语言。</p>
</blockquote>

</details>

### (51) 下列哪种工具无法实现对远程服务器的配置操作？

- **A**：JIRA
- **B**：Ansible
- **C**：Puppt
- **D**：Chef


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<blockquote>
<p>题目问哪项「不属于」协同开发工具。选中项「Confluence」被归类为不属于协同开发工具——它是 Atlassian 的 Wiki 和知识管理工具，虽然也用于团队协作，但课程材料将其分类为文档协作工具而非开发协同工具。Rally（敏捷项目管理）、JIRA（事务跟踪）、Kanban（看板工具）均属于协同开发工具。</p>
</blockquote>

</details>

### (52) Selenium能实现自动化单元测试。

- **A**：错误
- **B**：正确


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<blockquote>
<p>Selenium 是一个 Web 浏览器自动化工具，主要用于端到端（E2E）功能测试和回归测试。它操作的是浏览器层面的 UI 交互，属于功能测试而非单元测试。单元测试通常在代码层面（如 JUnit for Java、pytest for Python）进行，测试单个函数或模块的逻辑。因此说 Selenium 能实现「自动化单元测试」是错误的——它做的是 UI 自动化测试。</p>
</blockquote>

</details>

### (53) 以下哪种工具是开源工具？

- **A**：Zabbix
- **B**：JIRA
- **C**：TeamCity
- **D**：JUnit


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：D（单选）</p>
<blockquote>
<p>JUnit 是一个开源的 Java 单元测试框架（遵循 Eclipse Public License）。Zabbix 也是开源的（GPL），但 JIRA（Atlassian 商业软件）和 TeamCity（JetBrains 商业软件）需要付费许可证（虽有免费版本但非开源）。注意此题答案以课程材料为准。</p>
</blockquote>

</details>

### (54) 下列哪些工具不能模拟市场上主流浏览器的操作？

- **A**：FitNesse
- **B**：Jenkins
- **C**：JUnit
- **D**：Selenium


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：['A', 'B', 'C']（多选）</p>
<blockquote>
<p>题目要求选「不能」模拟主流浏览器操作的工具。Selenium 是专门用于浏览器自动化操作的工具，因此未被选中。A（FitNesse）是验收测试框架（Wiki-based），B（Jenkins）是 CI 工具，C（JUnit）是单元测试框架——这三个都不具备模拟浏览器操作的能力，所以是正确选项。</p>
</blockquote>

</details>

### (55) 以下选项中，哪一项不属于微服务架构的特点？

- **A**：基础设施自动化
- **B**：低内聚和高耦合
- **C**：围绕业务能力组织
- **D**：去中心化


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<blockquote>
<p>微服务架构的特点包括：基础设施自动化、围绕业务能力组织、去中心化、内聚和解耦。而「低内聚和高耦合」恰恰是微服务要避免的反模式——微服务追求的是高内聚（服务内部职责集中）和低耦合（服务之间依赖最小）。</p>
</blockquote>

</details>

### (56) 以下对于微服务优点的描述中，哪几项是正确的？

- **A**：不同的微服务可以使用不同的语言进行开发。
- **B**：单个微服务很简单，只关注一个业务功能
- **C**：微服务系统测试变得非常简单
- **D**：微服务可以使用RPC进行服务间通信


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：['A', 'B', 'D']（多选）</p>
<blockquote>
<p>微服务的真正优点包括：(A) 不同微服务可以使用不同语言——技术多样性；(B) 单个服务功能集中且简单；(D) 通过 RPC/REST 进行服务间通信。但 (C) 系统测试变得简单是错误描述——分布式系统的集成测试是微服务的主要挑战之一。</p>
</blockquote>

</details>

### (57) 在组成派看来，软件架构是一系列重要决策的集合，包括构成系统的结构要素及其接口的选择。

- **A**：错误
- **B**：正确


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：A（单选）</p>
<blockquote>
<p>「软件架构是一系列重要决策的集合，包括构成系统的结构要素及其接口的选择」这个定义来自「决策派」而非「组成派」。组成派的典型定义是：软件架构由组件、连接件和约束组成（Shaw &amp; Garlan），或由软件元素及其外部可见属性组成（Bass, Clements, Kazman）。这两种视角在软件架构研究中并存。</p>
</blockquote>

</details>

### (58) 微服务架构的特点包括“围绕业务能力组织”、“内聚和解耦”、“基础设施自动化”等。

- **A**：错误
- **B**：正确


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<blockquote>
<p>微服务架构的核心特点确实包括：围绕业务能力组织（而非技术层次）、内聚和解耦、基础设施自动化（容器化、CI/CD）。此外还有去中心化治理、去中心化数据管理、演进式设计等。题目描述的这三个特征准确概括了微服务架构的核心特性。</p>
</blockquote>

</details>

### (59) 持续集成是DevOps理念中重要的一个实践环节，它经历了纯脚本驱动到持续集成工具两个发展阶段，目前正向第三个阶段流水线即代码的阶段发展

- **A**：错误
- **B**：正确


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<blockquote>
<p>持续集成经历了三个发展阶段：(1) 纯脚本驱动阶段——开发者手动编写构建脚本；(2) 持续集成工具阶段——Jenkins、TeamCity 等专用工具；(3) 流水线即代码（Pipeline as Code）阶段——Jenkinsfile、GitHub Actions、GitLab CI 等以声明式或脚本式定义流水线。当前主流正处于第三阶段。这个描述正确。</p>
</blockquote>

</details>

### (60) Git、GitHub、GitLab是完全不一样的三款版本管理工具

- **A**：正确
- **B**：错误


<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案</strong>：B（单选）</p>
<blockquote>
<p>Git 是一个分布式版本控制系统；GitHub 是一个基于 Git 的代码托管和协作平台；GitLab 同样是一个基于 Git 的 DevOps 平台（提供代码托管、CI/CD、项目管理等）。三者并非「完全不一样」——它们以 Git 为共同基础。Git 是版本控制工具，GitHub 和 GitLab 是围绕 Git 构建的平台服务。</p>
</blockquote>

</details>
