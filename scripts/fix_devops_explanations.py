"""修复 devops.json 中所有多选题解析（修正 INCORRECT 类题目的解析方向）"""
import json

FILE = 'src/data/devops.json'

FIXED = {
    7: {
        "explanation": "题目要求选「不正确」的选项。B 不正确：形式化方法（Formal Methods）并非网络化和服务化阶段才提出的——早在 1970-80 年代就已存在（如 VDM、Z、B 方法等），远早于网络化时代。D 不正确：形式化方法的主要目的是解决软件的「正确性」和「可靠性」问题，而非「效率」问题。A 和 C 是正确描述：形式化方法确实应用范围有限且对开发者技能要求高，因此未被选中。",
        "source": "参考：Formal Methods 概述 (Wikipedia)",
        "source_url": "https://en.wikipedia.org/wiki/Formal_methods"
    },
    15: {
        "explanation": "题目要求选「不正确」的说法。A 不正确：PROBE 估算结果带小数是统计方法的正常特征，不代表不准确，仍可用于项目估算。C 不正确：PROBE 是基于历史数据的统计方法，不能给出精确估算，但这恰是其优势，它提供的是概率性的范围估算而非精确值——但题目将该说法归为不正确可能着眼于「PROBE 能给出较准确的参考范围」这一观点。D 不正确：PROBE 恰恰需要历史数据——没有历史数据就无法建立估算基准。B 正确（未被选中）：PROBE 主要估算规模和工时，不能直接用来估算质量。",
        "source": "参考：Watts Humphrey, PSP 教材 PROBE 方法",
        "source_url": "https://www.sei.cmu.edu/publications/books/a-discipline-for-software-engineering/"
    },
    16: {
        "explanation": "题目要求选「不恰当」的说法。A 不恰当：质量路径中的方法有严格的依赖关系和适用条件，不能随意选择使用——PSP 必须先于 TSP，个人度量先于团队度量。D 不恰当：质量路径恰恰始于个体软件工程师的自我管理和度量（PSP），再扩展到团队（TSP），并非与个人无关的集体努力。B 正确（进入测试前的高质量是测试后高质量的前提）、C 正确（最终仍需依赖测试来确保），因此未被选中。",
        "source": "参考：SEI TSP/PSP 材料",
        "source_url": "https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=5283"
    },
    17: {
        "explanation": "题目要求选「不恰当」的说法。A 不恰当：评审检查表不应该是统一的——不同角色、不同模块、不同类型的缺陷需要不同的检查视角，个性化检查表更有针对性。B 不恰当：检查表不应该一成不变——应该定期更新以反映团队积累的经验和常见缺陷模式。C 和 D 正确（检查表应定期更新、应个性化），因此未被选中。",
        "source": "参考：PSP 评审检查表实践",
        "source_url": "https://www.sei.cmu.edu/publications/books/a-discipline-for-software-engineering/"
    },
    18: {
        "explanation": "题目要求选「不恰当」的说法。A 不恰当：PQI（Process Quality Index）不是越高越好——达到 1.0 意味着各指标在理想范围，超过 1.0 不代表「更好」，需要具体分析。C 不恰当：PQI 的五个分指标有各自的计量方式，并非都能超过 1.0（如设计/编码时间比的设计上限）。B 和 D 正确（PQI 可辅助判断模块质量、可为过程改进提供依据），因此未被选中。",
        "source": "参考：PSP 教材中 PQI 指标说明",
        "source_url": "https://www.sei.cmu.edu/publications/books/a-discipline-for-software-engineering/"
    },
    19: {
        "explanation": "题目要求选「不恰当」的说法。B 不恰当：个人评审不应交叉进行——那是小组评审的做法。个人评审是阅读自己的代码，针对自身常犯错误进行自查。C 不恰当：个人评审应在单元测试之前进行，而非之后——先评审再测试，及早发现缺陷，降低修复成本。A 和 D 正确，因此未被选中。",
        "source": "参考：PSP 个人评审实践",
        "source_url": "https://www.sei.cmu.edu/publications/books/a-discipline-for-software-engineering/"
    },
    31: {
        "explanation": "题目要求选「不是」SOA 核心原则的选项。面向服务架构（SOA）强调的实现原则包括：服务重用、服务解耦、服务抽象、服务自治、服务可组合性等。A「服务去中心化」和 B「服务简单」不是 SOA 的核心实现原则——前者是微服务架构的特征，后者也不符合 SOA 企业级重量级的定位。C（服务重用）和 D（服务解耦）是 SOA 的核心原则，因此未被选中。",
        "source": "参考：Thomas Erl, \"SOA Principles of Service Design\"",
        "source_url": "https://www.soaschool.com/"
    },
    54: {
        "explanation": "题目要求选「不能」模拟主流浏览器操作的工具。Selenium 是专门用于浏览器自动化操作的工具，因此未被选中。A（FitNesse）是验收测试框架（Wiki-based），B（Jenkins）是 CI 工具，C（JUnit）是单元测试框架——这三个都不具备模拟浏览器操作的能力，所以是正确选项。",
        "source": "参考：各工具官方文档对比",
        "source_url": "https://www.selenium.dev/"
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
