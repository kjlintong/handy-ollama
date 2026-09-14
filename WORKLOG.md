# WORKLOG — handy-ollama 二期改写工作日志

> 本文件记录本项目(二期重构/改写)的工作进度、已完成的修改、编辑约定与验证方法,便于跨会话继续。
> 仓库:`kjlintong/handy-ollama`(上游 datawhalechina/handy-ollama),工作分支 **phase2**。

## 当前文档结构(11 章,已完成章节前移)

| 章 | 目录 | 内容 |
|---|---|---|
| 第1章 | docs/C1 | Ollama 与本地 AI 生态(1 节) |
| 第2章 | docs/C2 | 安装与配置(macOS / Windows / Linux / Docker,4 节) |
| 第3章 | docs/C3 | 模型管理与自定义(1 存储位置 / 2 导入模型 / 3 GGUF 深度解析与量化 / 4 Modelfile 高级编写 / 5 GPU-CPU 混合推理配置) |
| 第4章 | docs/C4 | Ollama API 深度指南(1 REST API / 2 OpenAI 兼容 / 3 Tool Calling / 4 多语言调用附录入口) |
| 第5章 | docs/C5 | MCP 协议与工具集成(1 协议架构 / 2 构建 Server / 3 Client 调用链 / 4 常用 Server 配合) |
| 第6章 | docs/C6 | 主流框架集成(LangChain Py / LangChain JS / LlamaIndex / OpenAI 兼容对接任意框架) |
| 第7章 | docs/C7 | **Agent 原理与轻量级实现(原第7+8章合并)**(1 Agent 架构原理 / 2 轻量级实现 100 行 / 3 从手写到 Harness) |
| 第8章 | docs/C8 | **主流 Harness × Ollama(原第9章,小节 8.1-8.3)**(Claude Code / DeepSeek Harness / Codex CLI) |
| 第9章 | docs/C9 | **本地 RAG 与知识库(原第10章,9.1-9.5)**(原理 / LangChain / LlamaIndex / DeepSeek R1 / GraphRAG-Agentic) |
| 第10章 | docs/C10 | **本地多 Agent 协作(原第11章,10.1-10.3)**(CrewAI / LangGraph / 本地模型资源调度) |
| 第11章 | docs/C11 | **可视化界面与工作流(原第12章,11.1-11.4)**(Open WebUI / Dify / n8n / FastAPI) |

- 第一期旧版全量归档在 `v1/`(README 与 _sidebar 有归档入口)。
- `living-docs/`(hardware / changelog / troubleshooting)与 `appendix/` 随章节前移已同步。

## 已完成工作(按提交,新→旧)

1. **5514447** 第九章第 2~4 节重构为新风格:段落标题统一为中文序号(「一、环境设置」…);C9/2 删除英文残留(「You can also see this page…」完整嵌入模型列表句 + 三行 Note 噪音)并拟人化机翻句;三节结尾「总结/参考文献」→「本节小结+延伸阅读」;版本基线补「本节定位」;「>注:」格式统一;C9/4 旧 GitHub docs/C7 链接与 Step 序号改本地引用/中文步骤;同章引用 ../C9/ → ./;v0.2 嵌入链接升级新版(概念类 v0.2 链接保留,与教程 API 配套)。
2. **e3851d8** 第七章第二节:措辞拟人化(「每一步都是上一步的超集」→「后面的版本只加功能、不删功能」),删第五节标题「（诚实清单）」。
3. **2f205c7** 章节大重组:第七章(Agent 架构原理)并入原第八章 → 新**第7章 Agent 原理与轻量级实现**;原 9→8、10→9、11→10、12→11;物理目录 C8-C12 → C7-C11;删除各节冗余「本节范围」块;migration-map 的 C3 过时映射一并修正。
4. **1ae00ff** 第五章+全库:C5 病句修复(「薄胶水模式」首次出现即解释,5.3 展开为两步);「章节定位/本章定位」统一「本节定位」;清理版本基线/定位/边界自检中的作者口吻(写作时/改版刷新/边界铁律/核心新增等);「边界自检」节更名「本节范围」。
5. **05a0aaa** 第四章:「本章小结」全库统一「本节小结」(25 处);修 4.1 目录锚点(#四删除模型→#四复制模型)、给 4.1 补本节小结+延伸阅读;4.2 引用编号笔误(C2.5→C2.2);4.4 与附录 A-0 的 JS notebook 错误路径(notebook/C5→—)。
6. **bfa228b** 第三章重组:C2/5 GPU-CPU 混合推理配置移入 C3/5;删除过时的「自定义在 GPU 中运行」(错误默认 CPU + 废弃 OLLAMA_GPU_LAYER);「自定义导入模型」重写去重(删 GGUF 原理重复、删自定义 Prompt 整节、use_auth_token→token、修 HF_ACCESS_TOKE 笔误);「存储位置」整理编号错乱;全库 10 处引用同步,顺带修 C1 链接多空格的 %20 与 README ../docs 越界链接。
7. **296cd54**(云端提交,已同步本地)删除 docs/C1/1. Ollama 介绍.md。

## 编辑约定(已统一,新内容必须遵守)

- 开头块:`> **版本基线**:...` + `> **本节定位**:...`(读者视角,禁作者口吻如"写作时/改版/边界铁律");无定位价值时省略。版本基线传达"基于什么版本/环境实测"。
- 每节文件末尾统一 `## 本节小结`(不叫"本章小结")+ `## 延伸阅读`。
- 不加「本节范围/边界自检」块(已全删,内容与定位重复)。
- 术语:「薄胶水模式」= 只做格式转换、不改动两端的薄层连接代码(首次出现需解释)。
- 小节编号与「第N章」随章节一致;跨章引用优先指向具体小节(如"8.2 轻量级 Agent 实现")而非整章。
- 链接用 URL 编码(%20),注意"与 本地"/"与本地"这类空格差异;改动后必须跑链接校验。

## 验证流程(每轮改动后必做)

```bash
cd /home/ryan/project/handy-ollama-kjlintong
# 链接校验(主库 0 坏链接才是合格;v1/ 归档的 27 个坏链接是既存问题,不在本阶段范围)
python3 - <<'EOF'
import os, re, urllib.parse
allp, mds = set(), {}
for r, ds, fs in os.walk("."):
    ds[:] = [d for d in ds if d not in (".git", ".venv", "node_modules")]
    for f in fs:
        p = os.path.normpath(os.path.join(r, f)); allp.add(p)
        if f.endswith(".md"): mds[p] = None
ln = re.compile(r'\[[^\]]*\]\(([^)]+)\)|!\[[^\]]*\]\(([^)]+)\)')
bad = []
for f in sorted(mds):
    t = open(f, encoding="utf-8").read()
    for m in ln.finditer(t):
        tg = (m.group(1) or m.group(2)).strip()
        if not tg or tg.startswith(("http", "#", "mailto:")) or tg.startswith("**"): continue
        rs = os.path.normpath(os.path.join(os.path.dirname(f), urllib.parse.unquote(tg.split("#")[0])))
        if not os.path.isdir(rs) and rs not in allp: bad.append((f, tg))
print("主库坏链接:", [b for b in bad if not b[0].startswith("v1/")])
EOF
```

- 章节编号/目录名改动时,替换要"基于原文一次匹配、防级联"(见 2f205c7 教训:若分条顺序替换,../C11→C10 后再跑 C10→C9 会把新 C10 再次降位)。
- 注意目录级引用 `../C11`(无斜杠)与文件级 `../C11/3.xxx`、living-docs 的双层路径 `../docs/C11/...` 三种形态都要处理;替换前先 grep 全形态。

## 已知问题 / 下一步待办

- [ ] 第 10、11 章(新编号)内容尚未逐节细审(用户按章推进,已检 C3-C9)。
- [ ] C6/1、C6/2(LangChain Py/JS)是第一期末期风格、未重写(仅修 model 定义顺序小问题);C1、C2 同属旧版,可考虑后续重写。
- [ ] README_en.md 无章节表格,未随中文章节结构同步(若需英文版需补)。
- [ ] v1/ 归档的 27 个坏链接(README_en 的 docs/ 前缀、C3 脚本内误匹配等)——归档快照,是否修复待用户决定。
- [ ] notebook 目录编号与章节编号已脱节(notebook/C8 存第7章代码;notebook/C7 被第一期占用)——当前刻意保留,引用指向真实路径即可。
- [ ] C1 的「GA4 ID」等相关事项属个人主页仓库,与本仓库无关(勿混)。