# 开发流程

如果设计文档添加/变更，务必同步更新mkdocs配置，必要时更新首页`index.html`或`index.md`

## Markdown 标题层级规范

对于 mkdocs 文档，必须遵循如下标题层级，以确保右侧目录（TOC）正确生成：

- **`#`（H1）**：仅用于页面标题，**整个文件只能有一个 H1**
- **`##`（H2）**：用于页面内的一级章节（如：过程线、项目管理线、质量管理线、附录、考前速背清单）
- **`###`（H3）**：用于 H2 章节下的二级小节
- **`####`（H4）**：用于三级细分内容，最深到此为止

**禁止**在页面标题之外使用 `#`（H1），否则 mkdocs-material 的右侧 TOC 将无法渲染。
**禁止**使用 `#####`（H5），渲染效果不佳。最深层内容使用 `####`（H4）配合 **粗体** 段落标题即可。

## Markdown 列表渲染规范

mkdocs 使用的 Python-Markdown 解析器要求**列表前必须有空行**，否则列表将被视为上一段落的延续文本而无法正确渲染。

正确格式：

```markdown
**知识点：**

- 列表项一
- 列表项二
```

错误格式（缺少空行将导致列表不渲染）：

```markdown
**知识点：**
- 列表项一
- 列表项二
```

**规则**：在 `- ` 无序列表或 `1. ` 有序列表开始之前，如果前一行是非列表、非标题、非表格的段落文本，必须插入一个空行。

## 考试题目答案折叠规范

为了在 mkdocs 中默认隐藏考题答案（防止学生无意中看到），所有考试文件（`docs/exams/*.md`）中的**答案与解析部分**必须使用 `<details><summary>` HTML 标签包裹。

**核心规则**：

- 题目文本和选项保留为普通的 Markdown，始终可见
- 自 `**答案**` 或 `**解答**` 行开始，直到下一个题目/章节标题之前的所有内容，包裹在 `<details><summary>` 中，默认隐藏
- `<details>` 内部的 Markdown 内容（粗体、列表、表格、代码、块引用等）必须转换为**原生 HTML**，以确保在 mkdocs-material 中正确渲染

**正确格式**（内部使用原生 HTML）：

```html
### （1）题目文字

A. 选项一　　B. 选项二　　C. 选项三　　D. 选项四

<details>
<summary>点击查看答案与解析</summary>

<p><strong>答案：B</strong></p>
<blockquote>
<p><strong>题目解析</strong>：解析文字……</p>
<p><strong>知识点出处</strong>：<code>软件质量与管理.第二讲.pdf</code></p>
</blockquote>

</details>
```

**常见 Markdown → HTML 转换对照**：

| Markdown | HTML |
|---|---|
| `**粗体**` | `<strong>粗体</strong>` |
| `- 列表项` | `<li>列表项</li>`（需包在 `<ul>` 或 `<ol>` 中） |
| `` `code` `` | `<code>code</code>` |
| `> 引用` | `<blockquote><p>引用</p></blockquote>` |
| `| 表格 |` | `<table><thead><tr><th>...</th></tr></thead><tbody>...</tbody></table>` |

**处理方式**：

使用 Python `markdown` 库（`pip install markdown`）配合 `extra`、`codehilite`、`tables` 扩展，批量将 Markdown 答案内容转换为 HTML：

```python
import markdown
html = markdown.markdown(md_text, extensions=['extra', 'codehilite', 'tables'])
```

**禁止事项**：

- 禁止将题目文本和选项也放入 `<details>` 中（题目和选项必须始终可见）
- 禁止在 `<details>` 内部直接使用 Markdown 语法（必须转换为原生 HTML）
- 禁止在 `<details>` 内部使用 `###` 或 `##` 等标题（这会破坏 TOC 结构）

# 参考资料

`assets`目录下是参考资料，无论回答什么问题，都要关注参考资料，回答问题时尽可能找到参考资料依据并给出出处

`assets/exams`目录下是往年考题或习题，回答问题时需要重点关注出现过的的习题，特别是考试试题

`assets/other`目录下是一些学长整理的参考资料，可以参考，但没那么重要

`assets/reference`目录下是同学整理的一些背书资料，需要重点关注

`assets/slides`目录下是课堂课件，其中的`课程总结.pptx`/`课堂总结.pdf`是绝对的重点。每个pptx都有对应的pdf格式导出版本，路径在同级目录，根据你的喜好选择pptx或pdf。

`docs/assets`目录下是敏捷部分课堂小测和devops慕课的题目原始html，题目的json数据在`docs/quiz/data`

# 工作契约

所有的学长资料都不是绝对可靠的，确保能从课件中找出相应的出处，如果还存在问题，请想我提问，不要揣测我的意图，将问答记录在`.claude/qa.md`