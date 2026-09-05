# 第二期重构:章节映射与编辑规范

> 本文件是第二期（v2.0）重构的操作蓝图，供维护者使用，不进入教程正文导航。
> 对应总体规划：`handy-ollama-第二期总体规划-v1.1-线上版.md`

---

## 一、目录结构（第二期）

```
handy-ollama/
├── README.md               # 第二期版（含 12 章导航）
├── README_en.md            # 英文简介
├── LICENSE                 # CC BY-NC-SA 4.0（沿用）
├── docs/
│   ├── C1/   第1章  Ollama 与本地 AI 生态
│   ├── C2/   第2章  安装与配置
│   ├── C3/   第3章  模型管理与自定义
│   ├── C4/   第4章  Ollama API 深度指南
│   ├── C5/   第5章  MCP 协议与工具集成（新增）
│   ├── C6/   第6章  主流框架集成
│   ├── C7/   第7章  Agent 架构原理（新增）
│   ├── C8/   第8章  轻量级 Agent 实现（新增）
│   ├── C9/   第9章  主流 Harness × Ollama 集成实战（新增）
│   ├── C10/  第10章 本地 RAG 与知识库
│   ├── C11/  第11章 本地多 Agent 协作（新增）
│   ├── C12/  第12章 可视化界面与工作流
│   └── _meta/              # 内部文档（本文件），不进入导航
├── notebook/
│   ├── C3/ … C12/          # 与章节对应的可运行代码
├── images/                 # 教程插图（每章 ≤5 张截图）
└── living-docs/            # 在线补充文档（书中原理 ↔ 线上配置）
    ├── hardware.md         # 硬件选购指南（每季度更新）
    ├── changelog.md        # Ollama / Harness 版本变更日志
    └── troubleshooting.md  # 常见问题排查
```

## 二、章节映射（第一期 → 第二期）

| 第一期（main 分支，7 章） | 第二期去向 | 处理方式 |
|---|---|---|
| C1 Ollama 介绍 | → C1 Ollama 与本地 AI 生态 | 重写：刷新特性，新增 Agent 场景模型选型 |
| C2.1-2.4 安装（macOS/Win/Linux/Docker） | → C2.1-2.4 | 保留刷新：版本号、命令、截图 |
| （无） | → C2.5 GPU/CPU 混合推理配置 | 新增 |
| C3.1 自定义导入模型 | → C3.1 | 保留刷新，补 GGUF 深度解析 |
| C3.2 模型存储位置 | → C3.2 | 保留 |
| C3.3 GPU 运行 | → C3.3 | 保留 |
| （无） | → C3.4 Modelfile 高级编写 | 新增（Agent 场景 system prompt/参数固化） |
| （无） | → C3.5 量化选型（Q4_K_M/Q8_0 权衡） | 新增 |
| C4.1 API 使用指南 | → C4.1 REST API 核心交互 | 重写：聚焦请求/响应结构 |
| （无） | → C4.2 OpenAI 兼容接口 | 新增（Harness 对接的事实标准） |
| （无） | → C4.3 Tool Calling API | 新增（请求/响应结构详解） |
| C4.2-4.6 多语言调用（Py/Java/JS/C++/Go） | → C4.4 多语言调用（精简合并） | 保留精简：保留 Python/JS/Java，C++/Go 移入附录或 notebook |
| （无） | → C5 MCP 协议与工具集成 | 全新（核心差异化章节） |
| C5.1-5.2 LangChain 集成 | → C6.1 LangChain 集成 | 重写刷新 |
| （无） | → C6.2 LlamaIndex 集成 | 新增（含 Embedding 后端 RAG） |
| （无） | → C6.3 OpenAI 兼容接口对接任意框架 | 新增 |
| （无） | → C7 Agent 架构原理 | 全新（控制篇幅，原理层） |
| （无） | → C8 轻量级 Agent 实现 | 全新（100 行 Python，承上启下） |
| （无） | → C9 Claude Code / DeepSeek Harness / Codex CLI | 全新（核心章节，每个集成必须实测） |
| C7.3 LangChain RAG / C7.4 LlamaIndex RAG / C7.7 DeepSeek R1 RAG | → C10.2 本地 RAG 实战 | 合并重写，去重 |
| （无） | → C10.3 GraphRAG / Agentic RAG | 新增 |
| （无） | → C11 CrewAI / LangGraph 多 Agent + 资源调度 | 全新 |
| C6.1 FastAPI 界面 / C6.2 WebUI | → C12.1-12.4 Open WebUI / Dify / n8n / FastAPI | 重写：聚焦集成原理，UI 截图 ≤5 张 |
| C7.2 Dify 接入 | → C12.2 | 保留刷新 |
| C7.1 AI Copilot / C7.5 LangChain Agent / C7.6 LlamaIndex Agent | 部分并入 C7/C8 原理与实现，其余废弃 | 拆分吸收 |

## 三、编辑规范（硬性约束）

### 3.1 边界铁律（源自总体规划 1.3，每章完成后自检）

- ❌ 不教 Harness 本身怎么用（Plan Mode、插件系统架构、交互技巧）
- ✅ 只教「Ollama 怎么和这个 Harness 配合」：后端配置、模型选型、调参、混合策略
- ❌ 不追逐短期 UI 变化；✅ 聚焦 MCP、OpenAI-compatible API 等通用协议
- ❌ 不造 Agent 框架；✅ 用轻量代码理解原理后快速接入现有 Harness

### 3.2 可复现性标准

- 每段代码注明：Ollama 版本基线、模型名称与 tag、操作系统/环境
- **版本基线：Ollama 0.17.x**（2026-09 实测 0.17.7）
- 每个 Harness 集成必须经本地实测跑通，代码写入 `notebook/` 对应目录
- 实测环境：Windows 11 (WSL2) + Ollama 0.17.7（Windows 侧服务，WSL 内经网关 IP 访问）

### 3.3 原理:实操比例

- Part 1-2（C1-C6）：原理:实操 ≈ 3:7
- Part 3-4（C7-C12）：原理:实操 ≈ 5:5

### 3.4 时效性控制

- 每章 UI 截图 ≤5 张；易变内容（版本号、API 参数、截图）用「文字描述 + 链接」指向 living-docs/
- living-docs/ 维护节奏：hardware 每季度、changelog 随版本、troubleshooting 持续

### 3.5 语言与风格

- 正文中文；代码注释中英皆可（中文为主）
- 章节结构：`# 章节名` → 引言段 → `## 一、二、三…` 编号小节 → 小结/自检清单
- 命令、代码一律用围栏代码块，标注语言与 shell 类型
- 每章结尾附「本章小结」与「边界自检」记录

## 四、工作流

1. 在 `kjlintong/handy-ollama` fork 的 `phase2` 分支上开发
2. 每完成一章（或一个完整小节）提交一次，commit message 标注章节号
3. 全部完成后：本地校验（代码实测 + 链接检查）→ 合并回 main → 向上游 datawhalechina/handy-ollama 提 PR
4. 代码示例统一放 `notebook/C{n}/`，docs 内嵌代码与 notebook 文件保持一致（notebook 为源）
