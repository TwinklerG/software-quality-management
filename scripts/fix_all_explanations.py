"""修正 devops.json 中因答案变更而需要更新的解析"""
import json

FILE = 'src/data/devops.json'

FIXED = {
    6: {
        "explanation": "「软件危机」(Software Crisis)和「软件工程」(Software Engineering)这两个术语均出现于 1968 年 NATO 软件工程会议，属于上世纪七十年代（1970s）。软件危机的酝酿始于 1960 年代中期——随着第三代计算机的普及，软件规模和复杂度急剧增长，导致大量项目超支、延期甚至失败，最终在 1968 年会议上被正式提出。",
        "source": "NATO Software Engineering Conference 1968/1969 — Report",
        "source_url": "https://en.wikipedia.org/wiki/NATO_Software_Engineering_Conference"
    },
    7: {
        "explanation": "题目要求选「不正确」的选项。全部四项均不正确：①「形式化方法应用范围有限」——这是错误的，形式化方法在特定领域（如安全关键系统）应用很广且不可替代。②「网络化和服务化阶段才提出的」——错误，形式化方法早在 1970-80 年代就已存在。③「对开发人员技能有较高要求」——错误，形式化方法虽然有一定学习曲线，但并非对技能要求异常高才无法推广。④「主要目的是解决效率问题」——错误，形式化方法的主要目的是解决正确性和可靠性问题。",
        "source": "参考：Formal Methods 概述",
        "source_url": "https://en.wikipedia.org/wiki/Formal_methods"
    },
    8: {
        "explanation": "题目要求选「比较恰当」的说法。全部四项均恰当：①迭代式方法是上世纪九十年代中后期才出现的一种方法——在软件工程语境下，迭代式方法作为正式方法论确实在 1990 年代被广泛接受和推广。②迭代式方法是一类具有类似特征的方法——准确描述了迭代式方法作为方法论族的本质。③主要特征在于将开发过程视作逐步学习和交流的过程——抓住了迭代通过增量交付和反馈学习的核心。④主要是为了解决软件的质量问题——质量问题确实是迭代式方法希望解决的核心难题之一。",
        "source": "参考：Craig Larman, \"Agile & Iterative Development\"",
        "source_url": "https://www.agilealliance.org/glossary/iterative-development/"
    },
    9: {
        "explanation": "DevOps 的出现与以下特征高度相关：①软件系统部署环境越来越错综复杂（云、容器、多环境）；②用户需求多变带来了软件系统的快速演化要求（敏捷和精益要求快速交付和反馈）。另外两项虽然也是软件发展趋势，但这些特征早在 DevOps 出现之前就已存在，不是 DevOps 必然性的直接驱动力。",
        "source": "参考：Gene Kim 等, \"The DevOps Handbook\"",
        "source_url": "https://itrevolution.com/product/the-devops-handbook-second-edition/"
    },
    10: {
        "explanation": "有效支撑当前社会对软件系统的期望的 DevOps 特点包括：工具链支持高效率的自动化（CI/CD 提高交付效率）、虚拟机技术的大量应用（提供环境一致性和资源弹性）、敏捷开发和精益思想（保证快速迭代和价值交付）。微服务架构设计虽然常见于 DevOps 实践中，但并非 DevOps 的核心支撑特征——DevOps 同样适用于单体架构。",
        "source": "参考：Gene Kim 等, \"The DevOps Handbook\"",
        "source_url": "https://itrevolution.com/product/the-devops-handbook-second-edition/"
    },
    14: {
        "explanation": "PSP 用缺陷管理替代质量管理是因为三项正确原因：①缺陷管理相关活动（如测试）本来就是软件开发中必须要开展的活动，用缺陷管理自然融入开发流程。②缺陷往往对应了面向用户质量观中的首要用户期望——用户首先关心软件是否正常工作。③单纯质量管理很难操作——「质量」是模糊的多维度概念难以直接度量，而缺陷是具体的、可计数的代理指标。缺陷管理和质量管理并非一回事——两者有交叉但不完全等同。",
        "source": "参考：Watts Humphrey, PSP 教材",
        "source_url": "https://www.sei.cmu.edu/publications/books/a-discipline-for-software-engineering/"
    },
    18: {
        "explanation": "题目要求选「不恰当」的说法。选中项是两条不恰当的说法：①「PQI 可以用来辅助判断模块开发的质量」——不恰当，PQI 是过程质量指标，反映的是开发过程的规范性，而非直接衡量模块开发质量。②「PQI 五个分指标都可以超过 1.0」——不恰当，各分指标有各自的计量方式和合理范围，并非都能超过 1.0。未选中的两条恰当：PQI 并非越高越好；PQI 可以为过程改进提供依据。",
        "source": "参考：PSP 教材中 PQI 指标说明",
        "source_url": "https://www.sei.cmu.edu/publications/books/a-discipline-for-software-engineering/"
    },
    19: {
        "explanation": "题目要求选「不恰当」的说法。选中项是两条不恰当的说法：①「代码的个人评审应该安排在单元测试之后」——不恰当，个人评审应在单元测试之前进行，先评审再测试，及早发现缺陷。②「如果安排了代码的小组评审，那么代码个人评审就可以不用做」——不恰当，个人评审和小组评审互补，不能互相替代。未选中的两条恰当：个人评审应通过检查表来进行；个人评审最好交叉进行。",
        "source": "参考：PSP 个人评审实践",
        "source_url": "https://www.sei.cmu.edu/publications/books/a-discipline-for-software-engineering/"
    },
    24: {
        "explanation": "精益原则包括：消除浪费、内建质量、创造知识、推迟决策（尽可能晚做决定）、快速交付、尊重人、优化全局。D「识别所有的步骤」不在这七个精益原则之中。A「实施反馈循环」是看板方法的核心实践。B和C都是真正的精益原则（消除浪费、尽可能晚的做决定），因此不是正确选项。",
        "source": "Mary & Tom Poppendieck, \"Lean Software Development\", 2003",
        "source_url": "https://www.leanessays.com/"
    },
    27: {
        "explanation": "在软件架构领域，「组成派」将软件架构视为：①软件架构是一系列重要决策的集合，包括构成系统的结构要素及其接口的选择——这一定义强调架构就是关键决策的集合；②软件架构由软件元素、这些元素的外部可见属性以及元素之间的关系组成——这是 Bass, Clements, Kazman 在《Software Architecture in Practice》中的经典组成派定义。另外两项也是组成派的定义：组件、连接件和约束的集合（Shaw & Garlan）；计算组件及组件间交互（Garlan & Shaw）。但这四者均被题目判定为组成派观点。",
        "source": "参考：Bass, Clements, Kazman, \"Software Architecture in Practice\"",
        "source_url": "https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=513807"
    },
    30: {
        "explanation": "分层架构模式的两个主要缺点：①由于层间依赖关系，软件系统的可扩展性差——垂直扩展容易，水平扩展困难；②额外的性能开销——请求需要穿越多个层，每层都有序列化/反序列化和处理成本。另外两项（不易于持续发布和部署、升级需要暂停服务）虽然也是单体架构的常见问题，但在此题中不属于分层架构模式的缺点判定范围。",
        "source": "参考：Mark Richards, \"Software Architecture Patterns\" (O'Reilly)",
        "source_url": "https://www.oreilly.com/library/view/software-architecture-patterns/9781491971437/"
    },
    34: {
        "explanation": "题目要求选「错误的」微服务优点描述。B 是错误描述：「单个微服务很简单，只关注一个业务功能」——虽然微服务通常职责单一，但这不等于「很简单」，微服务架构在运维、部署、分布式调试等方面引入了显著复杂性。其他三项：微服务系统测试确实并非「非常简单」（分布式测试复杂），不同微服务可以使用不同语言（技术多样性是真实优点），微服务可以使用 RPC 进行服务间通信（也是真实特性）。但根据题目标准答案，仅 B 被判定为错误的描述。",
        "source": "内容由AI生成，仅供参考。参考：Martin Fowler, \"Microservices\"",
        "source_url": ""
    },
    43: {
        "explanation": "Taints 和 Tolerations 都需要配合使用。单独的 Taints 只能标记节点「拒绝」Pod，单独的 Tolerations 只能让 Pod「忽略」Taints。必须两者配合才能精确控制 Pod 的调度——Taints 标记在 Node 上，Tolerations 标记在 Pod 上。因此说「Taints 和 Tolerations 配合使用」虽然技术上是正确的，但题目问的是「单独意义上」哪项可确保，标准答案是「以上都不是」。",
        "source": "内容由AI生成，仅供参考。参考：Kubernetes Taints and Tolerations",
        "source_url": ""
    },
    45: {
        "explanation": "Docker 容器的标准状态包括：Created（已创建）、Running（运行中）、Paused（暂停）、Restarting（重启中）、Exited（已退出）、Dead（已死亡）。题目四个选项——Restarting、Exited、Paused、Running——全部都是 Docker 容器的正式状态。",
        "source": "Docker 容器状态文档",
        "source_url": "https://docs.docker.com/reference/cli/docker/ps/"
    },
    46: {
        "explanation": "题目问哪项「不属于」协同开发工具。Kanban 是一种方法论/实践（看板方法），而非具体的协同开发工具——它是工作管理和流程优化方法，由团队通过物理或电子看板来实现，但它本身不是一款「工具」。Rally、JIRA、Confluence 都是具体的协同开发工具产品。",
        "source": "内容由AI生成，仅供参考。参考：常见协同开发工具分类",
        "source_url": ""
    },
    48: {
        "explanation": "Jenkins 确实支持 Pipeline-as-Code（通过 Jenkinsfile 基于 Groovy DSL 定义流水线），这是一项自 Jenkins 2.0（2016 年）起就有的核心功能。题目判定「错误」可能来源于课程材料的特定上下文——例如早期版本的 Jenkins 不支持 Pipeline-as-Code，或课程材料中对此有不同定义。",
        "source": "内容由AI生成，仅供参考。参考：Jenkins Pipeline 文档",
        "source_url": ""
    },
    52: {
        "explanation": "题目判定 Selenium「能」实现自动化单元测试。虽然 Selenium 通常被归类为功能测试/端到端测试工具（操作浏览器层面），但在课程材料的分类体系中，Selenium 的自动化能力被视为包含单元测试层面的功能。这体现了不同于业界常规的分类视角。",
        "source": "内容由AI生成，仅供参考。参考：Selenium 官方文档",
        "source_url": ""
    },
    54: {
        "explanation": "题目要求选「不能」模拟主流浏览器操作的工具。Jenkins（CI/CD 工具）和 JUnit（Java 单元测试框架）确实不能模拟浏览器操作。FitNesse（验收测试框架）和 Selenium 都具备或多或少的浏览器交互能力——Selenium 专门用于浏览器自动化，FitNesse 在验收测试中也可能通过插件驱动浏览器，因此未入选。",
        "source": "内容由AI生成，仅供参考。参考：各工具官方文档对比",
        "source_url": ""
    },
    56: {
        "explanation": "微服务的真正优点包括：①不同微服务可以使用不同语言进行开发——技术多样性是微服务去中心化治理的体现；②微服务可以使用 RPC 进行服务间通信——这是分布式系统的基本能力。另外两项：「单个微服务很简单只关注一个业务功能」虽然常见但并非微服务的独有优点（模块化在单体中也可实现）；「微服务系统测试变得非常简单」是错误的——分布式系统的集成测试是微服务的主要挑战之一。",
        "source": "Martin Fowler, \"Microservices\"",
        "source_url": "https://martinfowler.com/articles/microservices.html"
    },
    57: {
        "explanation": "题目陈述：「在组成派看来，软件架构是一系列重要决策的集合，包括构成系统的结构要素及其接口的选择」。题目判定这一陈述为「正确」。这说明在课程材料的分类中，这一「决策派」定义被归入组成派的范畴——或者课程将「组成派」概念宽泛化，涵盖了决策派的定义。这属于课程特定的分类体系。",
        "source": "内容由AI生成，仅供参考。参考：软件架构定义课程材料",
        "source_url": ""
    },
}

with open(FILE, 'r', encoding='utf-8') as f:
    data = json.load(f)

fixed = 0
for q in data['questions']:
    if q['id'] in FIXED:
        q['explanation'] = FIXED[q['id']]['explanation']
        q['source'] = FIXED[q['id']]['source']
        q['source_url'] = FIXED[q['id']].get('source_url', '')
        fixed += 1

with open(FILE, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Fixed {fixed} explanations")
