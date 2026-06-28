# 考前速背清单 · 快速问答

> 提取自 [课程总结必背](final-recite.md) 中所有 <u>（背）</u> 标记内容。答案默认隐藏，点击展开。


## 一、基础概念与过程管理

### 软件过程定义

<details>
<summary>点击查看答案</summary>

<table>
<thead><tr><th></th><th>生命周期模型</th><th>软件过程</th></tr></thead>
<tbody>
<tr><td><strong>定义</strong></td><td>对软件过程的一种人为划分</td><td>为了实现一个或多个事先定义目标而建立的一组实践的集合，这组实践之间往往有一定的先后顺序，最为整体来实现一个或多个事先定义的目标（背）</td></tr>
<tr><td><strong>粒度</strong></td><td>粗粒度框架</td><td>包含具体活动、角色、工件、技术实践和管理实践</td></tr>
<tr><td><strong>内容</strong></td><td>通常不含技术实践</td><td>包含技术实践和管理实践</td></tr>
</tbody></table>
<p><strong>典型生命周期模型</strong>：瀑布模型、迭代式模型、增量模型、螺旋模型、原型法。</p>
<p><u><strong>区别</strong>（背）</u></p>


</details>

### 瀑布模型

<details>
<summary>点击查看答案</summary>

<ul>
<li>瀑布模型<strong>不是单一模型</strong>，而是一系列模型，覆盖最简单的场景（过程元素少）到最复杂的场景（过程元素多）。</li>
<li>软件项目应该结合实际情况选择合适过程元素的瀑布模型，基本原则是项目面临的困难和挑战越多，选择的模型应该越复杂</li>
<li>软件项目团队往往低估了项目挑战，选择了过于简单的不实用的瀑布模型。</li>
<li>瀑布模型在软件成为独立产品阶段被广泛使用，成为重文档、慢节奏的过程。</li>
</ul>
<blockquote>
<p><strong>知识点出处</strong>：<code>软件质量与管理.第二讲.pdf</code> Slide 11-13</p>
</blockquote>


</details>

### 软件过程管理目的

<details>
<summary>点击查看答案</summary>

<p><u><strong>软件过程管理</strong>的目的（背）</u>：让软件过程在开发效率、质量等方面有着更好性能绩效。</p>


</details>

### CMMI五级

<details>
<summary>点击查看答案</summary>

<p><u><strong>CMMI 五级成熟度</strong>（背）</u>：</p>
<table>
<thead>
<tr>
<th>等级</th>
<th>名称</th>
<th>核心特征</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Initial 原始级</td>
<td>混乱，依赖个人英雄主义，救火文化</td>
</tr>
<tr>
<td>2</td>
<td>Managed 已管理级</td>
<td>项目层面有计划、跟踪、需求管理、配置管理</td>
</tr>
<tr>
<td>3</td>
<td>Defined 已定义级</td>
<td>组织层面有标准过程，项目可裁剪</td>
</tr>
<tr>
<td>4</td>
<td>Quantitatively Managed 定量管理级</td>
<td>统计过程控制（SPC）和预测模型</td>
</tr>
<tr>
<td>5</td>
<td>Optimizing 优化级</td>
<td>持续识别偏差、根因并改进</td>
</tr>
</tbody>
</table>
<p><strong>为什么 4/5 级是高等级</strong>：</p>
<ul>
<li>2/3 级关注<strong>当前状态</strong>——过程是否按计划执行。</li>
<li>4 级用统计过程控制和预测模型，能根据量化数据<strong>预判未来</strong>。</li>
<li>5 级主动识别偏差、找到根因并消除，实现<strong>持续优化</strong>。</li>
</ul>
<p><strong>关键理解</strong>：</p>


</details>


## 二、敏捷方法与 DevOps

### 敏捷宣言

<details>
<summary>点击查看答案</summary>

<p><u><strong>敏捷宣言四条</strong>（背）</u>：</p>
<ol>
<li><strong>个体和互动</strong> 胜过 流程和工具</li>
<li><strong>可以工作的软件</strong> 胜过 详尽的文档</li>
<li><strong>客户合作</strong> 胜过 合同谈判</li>
<li><strong>响应变化</strong> 胜过 遵循计划</li>
</ol>
<blockquote>
<p>尽管右项有其价值，但更重视左项的价值。</p>
</blockquote>
<p><u><strong>如何正确理解敏捷宣言</strong>（背）</u>（已考 2020-mid、2022、2023 简答）：</p>
<ol>
<li><strong>不是否定右项</strong>：敏捷宣言并不是说流程和工具、文档、合同谈判、计划不重要，而是强调左项（个体互动、可工作软件、客户合作、响应变化）具有更高的优先级。</li>
<li><strong>"胜过"而非"替代"</strong>：关键词是"胜过"（over），而非"替代"。敏捷团队仍然需要流程、文档、合同和计划，只是这些不应该是核心关注点。</li>
<li><strong>价值观导向</strong>：敏捷宣言是价值观层面的宣言，不是具体的操作方法。它指导团队在各种决策中做出符合敏捷精神的选择。</li>
<li><strong>实践服务于价值观</strong>：具体的敏捷实践（如 Scrum、XP 等）都是为了实现这些价值观而设计的，不应本末倒置地将实践本身当作目标。</li>
<li><strong>与规范方法的关系</strong>：计划驱动的开发人员必须敏捷，敏捷开发人员必须规范。敏捷和规范不是对立的两极，而是软件开发中需要平衡的两个维度。</li>
</ol>


</details>

### DevOps典型方法

<details>
<summary>点击查看答案</summary>

<p><u><strong>DevOps 典型方法</strong>（背）</u>：</p>
<ul>
<li>方法论基础：敏捷软件开发、精益思想以及看板 Kanban 方法</li>
<li>以领域驱动设计为指导的微服务架构</li>
<li>大量虚拟化技术的使用</li>
<li>一切皆服务（XaaS）的理念指导</li>
<li>构建了强大的工具链，支持高水平自动化</li>
</ul>


</details>

### DevOps Three Ways

<details>
<summary>点击查看答案</summary>

<h3><u>DevOps Three Ways（背）</u></h3>
<p><strong>First Way：从左到右的流动</strong> —— 打通开发→测试→部署→运维→生产的价值流。小批量、限制 WIP、持续构建/集成/交付。</p>
<p><strong>Second Way：从右到左的反馈</strong> —— 生产中的问题快速回流到开发。自动化测试、监控、日志、告警、停止生产线。</p>
<p><strong>Third Way：持续学习与实验文化</strong> —— 允许安全失败，从失败中学习。鼓励小实验、持续改进、高信任文化。</p>
<h3>DevOps 的优势（已考 2018 简答）</h3>


</details>


## 三、项目管理

### 三大目标+定义

<details>
<summary>点击查看答案</summary>

<p>软件项目管理的<strong>三大典型目标</strong>：<u><strong>成本、质量、工期</strong>（背）</u>。</p>
<p><u>软件项目管理定义（背）</u>：应用<strong>方法</strong>、<strong>工具</strong>、<strong>技术</strong>以及<strong>人员能力</strong>来完成软件项目，实现项目目标的过程。</p>
<p>软件项目管理包含：估算、计划、跟踪、风险管理、范围管理、人员管理、沟通管理。</p>


</details>

### 规模估算要点

<details>
<summary>点击查看答案</summary>

<p><u><strong>规模估算的基本要点</strong>（背）</u></p>
<ul>
<li>尽可能划分详细一些</li>
<li>建立对结果的信心</li>
<li>依赖数据</li>
<li>估算要的是过程，而非结果；估算的过程是相关干系人达成一致共识的过程</li>
</ul>


</details>

### PROBE基本思想

<details>
<summary>点击查看答案</summary>

<p><u><strong>PROBE估算的基本思想</strong>（背）</u>：</p>


</details>

### PROBE流程

<details>
<summary>点击查看答案</summary>

<p><u><strong>PROBE估算流程</strong>（背）</u>：</p>
<p>```mermaid</p>


</details>

### 计划框架链路

<details>
<summary>点击查看答案</summary>

<p><u><strong>通用计划框架计划链路</strong>（背）</u>：</p>
<ol>
<li>定义需求</li>
</ol>


</details>

### 风险应对策略

<details>
<summary>点击查看答案</summary>

<p><u><strong>四大风险应对策略</strong>（背）</u>：</p>
<table>
<thead>
<tr>
<th>策略</th>
<th>含义</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>规避</strong></td>
<td>改变计划以消除风险</td>
</tr>
<tr>
<td><strong>转移</strong></td>
<td>将风险影响和责任转移给第三方</td>
</tr>
<tr>
<td><strong>缓解</strong></td>
<td>降低风险发生概率或减少影响</td>
</tr>
</tbody>
</table>


</details>

### EVM三层

<details>
<summary>点击查看答案</summary>

<p><u><strong>三种实现层次</strong>（背）</u>：</p>
<table>
<thead>
<tr>
<th>层次</th>
<th>信息</th>
<th>能回答的问题</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>简单</strong></td>
<td>EV + PV</td>
<td>完成了多少有价值的工作？</td>
</tr>
<tr>
<td><strong>中级</strong></td>
<td>+ SV + SPI</td>
<td>进度超前还是落后？⚠️ <strong>不引入成本信息</strong></td>
</tr>
<tr>
<td><strong>高级</strong></td>
<td>+ AC + BAC + EAC</td>
<td>成本节约还是超支？预计完工成本？</td>
</tr>
</tbody>
</table>
<p>⚠️ <strong>中级实现不引入成本信息，成本信息属于高级实现。</strong> EV 强调<strong>完成任务才获得价值</strong>，比只看工时更能反映真实进展。</p>


</details>

### 燃尽图

<details>
<summary>点击查看答案</summary>

<ul>
<li><u>燃尽图（Burndown Chart）是 EVM 在敏捷项目中的简化变形（背）</u></li>
</ul>


</details>

### EVM适应软件项目

<details>
<summary>点击查看答案</summary>

<ul>
<li>软件工作的价值难以直接度量，EVM 通过<strong>完成百分比</strong>间接度量</li>
<li>EVM 将进度和成本用统一的"价值"单位衡量</li>
<li>适合<strong>分解清晰（WBS）</strong>的项目管理场景</li>
<li>EV 概念强调交付价值而非消耗时间，符合软件项目管理本质</li>
</ul>
<blockquote>
<p><strong>知识点出处</strong>：<code>软件质量与管理.第四讲.pdf</code>——挣值管理</p>
</blockquote>


</details>


## 四、团队与领导力

### 领导四品质

<details>
<summary>点击查看答案</summary>

<p><u><strong>知识工作领导者的四个品质</strong>（背）</u>（已考 2024Spring）：</p>
<table>
<thead>
<tr>
<th>品质</th>
<th>English</th>
<th>含义</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>诚实</strong></td>
<td>Honest</td>
<td>信守承诺，言行一致 —— "did what they said they would do"。让团队成员感到信任和尊重。</td>
</tr>
<tr>
<td><strong>能力</strong></td>
<td>Competent</td>
<td>展现出卓越的<strong>技能和知识</strong> —— "skills and knowledge"。知识工作团队的领导者需要让成员信服其专业判断。</td>
</tr>
<tr>
<td><strong>远见</strong></td>
<td>Visionary</td>
<td>能够超越眼前的挑战和任务，具备明确和可信的未来愿景 —— "can they see past the horizon, do they have a believable view of a desirable future?"</td>
</tr>
<tr>
<td><strong>激励</strong></td>
<td>Inspirational</td>
<td>传播积极、充满热情和能量的未来愿景 —— "do they have a positive, enthusiastic, and energetic view of the future?"</td>
</tr>
</tbody>
</table>


</details>

### Maslow五层

<details>
<summary>点击查看答案</summary>

<ol>
<li><strong>生理需求</strong> → 2. <strong>安全需求</strong> → 3. <strong>社交/归属需求</strong> → 4. <strong>尊重需求（Esteem）</strong> → 5. <strong>自我实现（Self-actualization）</strong></li>
</ol>
<p>关键记忆点：</p>
<ul>
<li>自我实现是最高层次。⚠️ 自我实现 ≠ 自尊（第 5 层 ≠ 第 4 层）。</li>
<li>激励来自为没有满足的需求而努力奋斗。</li>
<li>低层次的需求必须在高层次需求满足之前得到充分满足。</li>
<li>满足高层次需求的途径比满足低层次的途径更为广泛。</li>
<li>晚年修正：高层次需求不一定要等低层次完全满足后才出现。</li>
</ul>
<blockquote>
<p><strong>知识点出处</strong>：<code>软件质量与管理.第三讲.pdf</code> Slide 7-8</p>
</blockquote>


</details>

### 自主团队

<details>
<summary>点击查看答案</summary>

<p><u><strong>自主团队六大特征</strong>（背）</u>：</p>
<ol>
<li>自行定义项目的目标</li>
<li>自行决定团队组成形式以及成员的角色</li>
<li>自行决定项目的开发策略</li>
<li>自行定义项目的开发过程</li>
<li>自行制定项目的开发计划</li>
</ol>


</details>

### TSP六大角色

<details>
<summary>点击查看答案</summary>

<p><u><strong>TSP 六大角色</strong>（背）</u>（典型 7 个角色，含开发人员）：</p>
<table>
<thead>
<tr>
<th>角色</th>
<th>核心职责</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>项目组长</strong>（Team Leader）</td>
<td>建设和维持高效团队；激励成员；主持会议；汇报状态；合理处理团队成员问题</td>
</tr>
<tr>
<td><strong>计划经理</strong>（Planning Manager）</td>
<td>开发团队和个人计划；平衡计划；跟踪进度</td>
</tr>
<tr>
<td><strong>开发经理</strong>（Development Manager）</td>
<td>制定开发策略；规模和资源估算；需求规格说明；高层设计；实现与测试</td>
</tr>
<tr>
<td><strong>质量经理</strong>（Quality Manager）</td>
<td>制定和跟踪质量计划；警示质量问题；组织评审；在提交配置管理前评审消除质量问题</td>
</tr>
<tr>
<td><strong>过程经理</strong>（Process Manager）</td>
<td>维护过程数据、<u>开发标准</u>、会议记录；支持过程改进</td>
</tr>
<tr>
<td><strong>支持经理</strong>（Support Manager）</td>
<td>保证工具环境；配置管理；维护风险/问题跟踪系统；支持复用策略</td>
</tr>
<tr>
<td><strong>开发人员</strong>（Developer）</td>
<td>按计划完成开发任务</td>
</tr>
</tbody>
</table>


</details>

### TSP Launch

<details>
<summary>点击查看答案</summary>

<p><u><strong>TSP Launch 9 次会议</strong>（背）</u>：</p>
<table>
<thead>
<tr>
<th>会议</th>
<th>内容</th>
<th>关键问题</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>建立产品目标和业务目标</td>
<td>要做什么？要做得怎么样？</td>
</tr>
<tr>
<td>2</td>
<td>角色分配和小组目标定义</td>
<td>怎么安排？有没有与组织目标冲突？</td>
</tr>
<tr>
<td>3</td>
<td><strong>开发流程定义与策略选择</strong></td>
<td>使用什么样的过程？分为几个迭代？每个迭代做什么？组件如何获取？</td>
</tr>
<tr>
<td>4</td>
<td>整体计划</td>
<td>估算+计划，明确做哪些事情？产出物？规模？需要多少资源？</td>
</tr>
<tr>
<td>5</td>
<td>质量计划</td>
<td>有哪些质量实践？做到什么程度？需要投入多少资源？</td>
</tr>
<tr>
<td>6</td>
<td>个人计划以及计划平衡</td>
<td>个人要做哪些事情？如何寻求最早完成项目的时间？</td>
</tr>
<tr>
<td>7</td>
<td>风险评估</td>
<td>What if？</td>
</tr>
<tr>
<td>8</td>
<td>准备向管理层汇报计划</td>
<td>呼应第一次会议要求，体现团队述求，体现计划不是粗制滥造</td>
</tr>
<tr>
<td>9</td>
<td>向管理层汇报计划和讨论</td>
<td>汇报并讨论</td>
</tr>
</tbody>
</table>


</details>

### Scrum 33355

<details>
<summary>点击查看答案</summary>

<ul>
<li><strong>3 角色</strong>：Product Owner、Scrum Master、Developers</li>
<li><strong>3 工件</strong>：Product Backlog、Sprint Backlog、Increment</li>
<li><strong>3 支柱</strong>：透明（Transparency）、检视（Inspection）、适应（Adaptation）</li>
<li><strong>5 事件</strong>：Sprint、Sprint Planning、Daily Scrum、Sprint Review、Sprint Retrospective</li>
<li><strong>5 价值观</strong>：承诺（Commitment）、专注（Focus）、开放（Openness）、尊重（Respect）、勇气（Courage）</li>
</ul>


</details>


## 五、质量管理

### 用户质量观定义

<details>
<summary>点击查看答案</summary>

<p><u><strong>用户质量观 = 满足用户需求的程度</strong>（背）</u>，最终从用户价值和满意度判断。</p>


</details>

### 评审速度

<details>
<summary>点击查看答案</summary>

<ul>
<li><u><strong>评审速度（Review Rate）</strong>（背）</u>：</li>
<li>代码评审：不超过 <strong>200 LOC/小时</strong></li>
<li>文档评审：不超过 <strong>4 页/小时</strong></li>
<li><strong>检查表</strong>：应<strong>个性化</strong>、<strong>定期更新</strong></li>
<li>个人评审不能被小组评审替代</li>
</ul>


</details>

### A/FR

<details>
<summary>点击查看答案</summary>

<pre><code>A/FR = PSP 质检成本 / PSP 失效成本
     = (设计评审时间 + 代码评审时间) / (编译时间 + 单元测试时间)
</code></pre>
<ul>
<li>PSP 期望值约为 <strong>2.0</strong></li>
<li><strong>A/FR 过低</strong>（&lt; 1.0）：评审投入不足，缺陷大量漏到测试阶段</li>
<li><strong>A/FR 过高</strong>（&gt; 3.0）：可能评审过度，效率下降</li>
</ul>


</details>

### PQI五因子

<details>
<summary>点击查看答案</summary>

<p><u><strong>PQI五个因子</strong>（背）</u>（每个 0~1，越接近 1 越好）：</p>
<ol>
<li><strong>设计质量</strong>：设计时间应 &gt; 编码时间</li>
<li><strong>设计评审质量</strong>：设计评审时间应 &gt; 设计时间的 50%</li>
<li><strong>代码评审质量</strong>：代码评审时间应 &gt; 编码时间的 50%</li>
<li><strong>代码质量</strong>：编译缺陷密度应当小于10个/千行</li>
<li>
<p><strong>程序质量</strong>：单元测试缺陷密度应当小于5个/千行</p>
</li>
<li>
<p>设计质量 $\min{1, \frac{设计时间}{编码时间}}$</p>
</li>
<li>设计评审质量 $\min{1, \frac{2\times 设计评审时间}{设计时间}}$</li>
<li>代码评审质量 $\min{1, \frac{2\times 代码评审时间}{编码时间}}$</li>
<li>程序质量 $\min{1, \frac{20}{10+编译缺陷/千行}}$</li>
<li>程序质量 $\min{1, \frac{10}{5+单元测试缺陷/千行}}$</li>
</ol>
<pre><code>PQI = 设计质量 × 设计评审质量 × 代码评审质量 × 代码质量 × 程序质量
</code></pre>


</details>

### PQI本质差异

<details>
<summary>点击查看答案</summary>

<p><u><strong>PQI 五因子的本质差异</strong>（背）</u>：</p>
<ul>
<li><strong>前三者（设计质量、设计评审质量、代码评审质量）</strong>：属于<strong>过程度量/指标</strong>——在过程进行中可主动干预和调整（如增加设计时间、增加评审投入）。</li>
<li><strong>后两者（代码质量、程序质量）</strong>：属于<strong>结果度量/指标</strong>——反映过程执行后的最终产出，不可直接干预，仅起 <strong>confirm（验证/确认）</strong> 作用。</li>
</ul>


</details>

### PQI作用

<details>
<summary>点击查看答案</summary>

<p><u><strong>PQI 的作用</strong>（背）</u>：</p>
<ul>
<li>判断模块开发质量</li>
<li>指导质量计划</li>
<li>为过程改进提供线索</li>
</ul>


</details>

### Quality Journey

<details>
<summary>点击查看答案</summary>

<p><u><strong>Quality Journey（质量路径）顺序</strong>（背）</u>：</p>
<ol>
<li>各种测试</li>
<li>进入测试之前的产物质量提升</li>
<li>评审过程度量和稳定</li>
<li>质量意识和主人翁态度</li>
<li>个体review的度量和稳定</li>
<li>诉诸设计</li>
<li>缺陷预防</li>
<li>用户质量观——其他质量属性</li>
</ol>
<p><strong>体现的质量管理哲学</strong>：</p>


</details>


## 六、设计与验证

### PSP设计模板

<details>
<summary>点击查看答案</summary>

<p><u><strong>PSP 四大设计模板</strong>（背）</u>：</p>
<table>
<thead>
<tr>
<th>模板</th>
<th>全称</th>
<th>描述对象</th>
<th>覆盖维度</th>
<th>记忆点</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>OST</strong></td>
<td>Operational Specification Template 操作规格模板</td>
<td>操作场景、外部交互、正常/异常使用</td>
<td>外部 + 动态</td>
<td><strong>外部行为</strong></td>
</tr>
<tr>
<td><strong>FST</strong></td>
<td>Functional Specification Template 功能规格模板</td>
<td>对外接口、类/继承关系、外部可见属性和方法</td>
<td>外部 + 静态</td>
<td><strong>接口静态信息</strong></td>
</tr>
<tr>
<td><strong>SST</strong></td>
<td>State Specification Template 状态规格模板</td>
<td>程序所有状态、状态转移条件、转移动作</td>
<td>内部 + 动态</td>
<td><strong>内部动态信息</strong></td>
</tr>
<tr>
<td><strong>LST</strong></td>
<td>Logical Specification Template 逻辑规格模板</td>
<td>内部静态逻辑、伪代码、形式化逻辑</td>
<td>内部 + 静态</td>
<td><strong>内部静态/逻辑信息</strong></td>
</tr>
</tbody>
</table>


</details>


## 七、团队工程与支持

### 客户vs产品需求

<details>
<summary>点击查看答案</summary>

<p><u><strong>客户需求和产品需求的本质差异</strong>（背）</u>：用户（客户）需求是对问题的描述；产品需求描述的是解决方案。</p>


</details>

### V&V区别

<details>
<summary>点击查看答案</summary>

<p><u>验证是验证<strong>答案</strong>是否正确做出来；确认是确认<strong>问题</strong>是否被解决（背）</u></p>


</details>

### 配置项

<details>
<summary>点击查看答案</summary>

<ul>
<li><u><strong>配置项</strong>（背）</u>：受配置管理控制的工作产品（接口设计文档、源代码、用户手册、培训材料等）</li>
</ul>


</details>

### 基线

<details>
<summary>点击查看答案</summary>

<ul>
<li><u><strong>基线</strong>（背）</u>：经过正式评审和批准的配置项集合，作为后续工作的基础</li>
</ul>


</details>
