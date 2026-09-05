<div align='center'>
    <img src="./images/header.svg" alt="alt text" width="100%">
    <h1>💻 handy-ollama 🦙 (v2.0)</h1>
</div>

<div align="center">
  <img src="https://img.shields.io/github/stars/datawhalechina/handy-ollama?style=flat&logo=github" alt="GitHub stars"/>
  <img src="https://img.shields.io/github/forks/datawhalechina/handy-ollama?style=flat&logo=github" alt="GitHub forks"/>
  <img src="https://img.shields.io/github/issues/datawhalechina/handy-ollama?style=flat&logo=github" alt="GitHub issues"/>
  <img src="https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-brighgreen?style=flat&logo=github" alt="GitHub license"/>
<a href="https://datawhalechina.github.io/handy-ollama/"><img src="https://img.shields.io/badge/在线阅读-Online%20Reading-green?style=flat&logo=gitbook" alt="Online Reading"></a>
</div>

<div align="center">
  <h3>🤖 Agent 时代的本地模型底座</h3>
  <p><em>从"Ollama 新手教程"升级为"本地 AI 基础设施与 Agent 集成实战指南"</em></p>
</div>

简体中文 | [English](README_en.md)

> [!NOTE]
> **v2.0（全新改版）**：本版为第一期的**完整改进版**，上线后将直接替换第一期内容。教程按「基础设施层 → 协议层 → Agent 集成层 → 场景实战层」重构为 12 章 + 附录，**从零开始、无需第一期基础**；第一期的安装配置、多语言调用等基础内容已全部整合进来（多语言细节移至附录）。持续完善中，欢迎提 Issue 反馈。

## 🎉 官方收录

**2025.11.06，本项目被 Ollama 官方仓库收录，且是目前唯一的 Tutorial：https://github.com/ollama/ollama#tutorial**

## 🚀 项目简介

Agent 工具（Claude Code、Codex CLI、DeepSeek Harness 等）的爆发没有削弱 Ollama 的价值，反而放大了**"本地模型作为 Agent 后端"**的需求。市面上的 Agent 教程都在教"怎么开车"，而本教程教你"怎么给车加油、保养发动机、选什么油"——**我们不是 Agent 教程，而是 Agent 教程的"基础设施配套手册"**。

本教程**零基础可读**（前 3 章从安装讲起，第一期的全部基础内容均已整合），涵盖：

- **本地 AI 基础设施**：Ollama 安装配置、模型管理、GGUF 与量化选型（Agent 场景视角）；
- **协议与接口**：REST API、OpenAI 兼容接口、Tool Calling、**MCP 协议**（本书核心差异化内容）；
- **Agent 集成**：Agent 架构原理、100 行手写 Agent、**Claude Code / Codex CLI / DeepSeek Harness × Ollama 集成实战**；
- **场景实战**：本地 RAG（含 GraphRAG / Agentic RAG）、多 Agent 协作、Open WebUI / Dify / n8n 部署；
- **在线补充文档**（living-docs/）：硬件选购、版本变更、故障排查，持续更新。

> 每一行代码均可复现，每一个 Harness 集成均经实测（本书实测环境：Ollama 0.17.7 + qwen3:8b-64k + WSL2）。

## 📖 内容导航

### 第一部分：基础设施层

| 章节 | 关键内容 | 状态 |
|---|---|---|
| **第1章 Ollama 与本地 AI 生态** | | |
| [1. Ollama 与本地 AI 生态](docs/C1/1.%20Ollama%20与%20本地%20AI%20生态.md) | 核心特性、模型库、**Agent 场景模型选型指南** | ✅ |
| **第2章 安装与配置** | | |
| [1. macOS 安装与配置](docs/C2/1.%20Ollama%20在%20macOS%20下的安装与配置.md) | macOS 安装 | ✅ |
| [2. Windows 安装与配置](docs/C2/2.%20Ollama%20在%20Windows%20下的安装与配置.md) | Windows 安装、环境变量、**WSL2 访问** | ✅ |
| [3. Linux 安装与配置](docs/C2/3.%20Ollama%20在%20Linux%20下的安装与配置.md) | Linux 安装、systemd | ✅ |
| [4. Docker 安装与配置](docs/C2/4.%20Ollama%20在%20Docker%20下的安装与配置.md) | Docker 部署 | ✅ |
| [5. GPU/CPU 混合推理配置](docs/C2/5.%20GPU-CPU%20混合推理配置.md) | 混合推理、显存优化 | ✅ |
| **第3章 模型管理与自定义** | | |
| [1. 自定义导入模型](docs/C3/1.%20自定义导入模型.md) | GGUF / Safetensors 导入 | ✅ |
| [2. 自定义模型存储位置](docs/C3/2.%20自定义模型存储位置.md) | 存储路径迁移 | ✅ |
| [3. 自定义在 GPU 中运行](docs/C3/3.%20自定义在%20GPU%20中运行.md) | GPU 配置 | ✅ |
| [4. GGUF 深度解析与量化选型](docs/C3/4.%20GGUF%20深度解析与量化选型.md) | 量化原理、**Agent 场景量化权衡** | ✅ |
| [5. Modelfile 高级编写](docs/C3/5.%20Modelfile%20高级编写.md) | 系统提示词/参数固化 | ✅ |

### 第二部分：协议与接口层

| 章节 | 关键内容 | 状态 |
|---|---|---|
| **第4章 Ollama API 深度指南** | | |
| [1. REST API 核心交互](docs/C4/1.%20REST%20API%20核心交互.md) | 请求/响应结构、流式、JSON 模式 | ✅ |
| [2. OpenAI 兼容接口](docs/C4/2.%20OpenAI%20兼容接口.md) | **对接 Harness 的事实标准** | ✅ |
| [3. Tool Calling API](docs/C4/3.%20Tool%20Calling%20API.md) | **工具调用请求/响应详解（实测）** | ✅ |
| [4. 多语言调用（附录入口）](docs/C4/4.%20多语言调用（附录）.md) | Python / JavaScript / Java / C++ / Go（详见[附录A](../docs/appendix/A-多语言调用/0.%20多语言调用概览.md)） | ✅ |
| **第5章 MCP 协议与工具集成（新增·核心）** | | |
| [1. MCP 协议架构](docs/C5/1.%20MCP%20协议架构.md) | 协议原理、架构、调用链 | ✅ |
| [2. 用 Ollama 构建 MCP Server](docs/C5/2.%20用%20Ollama%20构建%20MCP%20Server.md) | 天气服务 Server（实测） | ✅ |
| [3. MCP Client 调用链](docs/C5/3.%20MCP%20Client%20调用链.md) | **本地模型使用 MCP 工具（实测）** | ✅ |
| [4. 常用 MCP Server 与 Ollama 配合](docs/C5/4.%20常用%20MCP%20Server%20与%20Ollama%20配合.md) | 官方/社区 Server 接入 | ✅ |
| **第6章 主流框架集成** | | |
| [1. LangChain 集成 - Python](docs/C6/1.%20LangChain%20集成%20-%20Python.md) | LangChain + Ollama | ✅ |
| [2. LangChain 集成 - JavaScript](docs/C6/2.%20LangChain%20集成%20-%20JavaScript.md) | LangChain.js | ✅ |
| [3. LlamaIndex 集成](docs/C6/3.%20LlamaIndex%20集成.md) | LLM + Embedding 双后端（实测） | ✅ |
| [4. OpenAI 兼容接口对接任意框架](docs/C6/4.%20OpenAI%20兼容接口对接任意框架.md) | **万能对接法（实测）** | ✅ |

### 第三部分：Agent 集成层（本期核心竞争力）

| 章节 | 关键内容 | 状态 |
|---|---|---|
| **第7章 Agent 架构原理（新增）** | | |
| [1. Agent 架构原理](docs/C7/1.%20Agent%20架构原理.md) | ReAct / Planning / Tool Use、**本地模型三大短板** | ✅ |
| **第8章 轻量级 Agent 实现（新增）** | | |
| [1. 轻量级 Agent 实现](docs/C8/1.%20轻量级%20Agent%20实现.md) | **100 行 Python Agent（实测）** | ✅ |
| [2. 从手写 Agent 到 Harness](docs/C8/2.%20从手写%20Agent%20到%20Harness.md) | 原理 → 成熟工具的迁移路径 | ✅ |
| **第9章 主流 Harness × Ollama（新增·核心）** | | |
| [1. Claude Code](docs/C9/1.%20Claude%20Code.md) | 后端配置、模型选型、混合策略 | ✅ |
| [2. DeepSeek Harness](docs/C9/2.%20DeepSeek%20Harness.md) | `ollama launch dsh` 集成 | ✅ |
| [3. Codex CLI](docs/C9/3.%20Codex%20CLI.md) | `--oss` 模式、profile 配置（**实测跑通**） | ✅ |

### 第四部分：场景实战层

| 章节 | 关键内容 | 状态 |
|---|---|---|
| **第10章 本地 RAG 与知识库** | | |
| [1. RAG 原理与本地组件](docs/C10/1.%20RAG%20原理与本地组件.md) | 流程、组件选型、调优 | ✅ |
| [2. LangChain 本地 RAG](docs/C10/2.%20使用%20LangChain%20搭建本地%20RAG%20应用.md) | LangChain + Chroma | ✅ |
| [3. LlamaIndex 本地 RAG](docs/C10/3.%20使用%20LlamaIndex%20搭建本地%20RAG%20应用.md) | LlamaIndex RAG | ✅ |
| [4. DeepSeek R1 本地 RAG](docs/C10/4.%20使用%20DeepSeek%20R1%20和%20Ollama%20实现本地%20RAG%20应用.md) | 推理模型 + RAG | ✅ |
| [5. GraphRAG 与 Agentic RAG](docs/C10/5.%20GraphRAG%20与%20Agentic%20RAG.md) | 进阶方向（LightRAG / 检索工具化） | ✅ |
| **第11章 本地多 Agent 协作（新增）** | | |
| [1. CrewAI 多 Agent 协作](docs/C11/1.%20CrewAI%20多%20Agent%20协作.md) | CrewAI + Ollama | ✅ |
| [2. LangGraph 多 Agent 协作](docs/C11/2.%20LangGraph%20多%20Agent%20协作.md) | 图编排（**实测**） | ✅ |
| [3. 本地模型资源调度](docs/C11/3.%20本地模型资源调度.md) | 显存规划、并发策略 | ✅ |
| **第12章 可视化界面与工作流** | | |
| [1. Open WebUI 部署](docs/C12/1.%20Open%20WebUI%20部署.md) | WebUI 部署 | ✅ |
| [2. Dify 接入 Ollama](docs/C12/2.%20Dify%20接入%20Ollama.md) | Dify 集成本地模型 | ✅ |
| [3. n8n 工作流自动化](docs/C12/3.%20n8n%20工作流自动化.md) | 自动化流程接入 | ✅ |
| [4. FastAPI 自定义对话界面](docs/C12/4.%20使用%20FastAPI%20部署自定义对话界面.md) | 自定义界面 | ✅ |

### 📎 附录（基础操作细节与经典案例）

| 文档 | 内容 | 状态 |
|---|---|---|
| [附录说明](docs/appendix/README.md) | 附录结构总览 | ✅ |
| [A. 多语言调用概览](docs/appendix/A-多语言调用/0.%20多语言调用概览.md) | 各语言路线选择 | ✅ |
| [A-1. Python 完整指南](docs/appendix/A-多语言调用/1.%20在%20Python%20中使用%20Ollama%20API.md) | 官方 Python SDK | ✅ |
| [A-2. JavaScript 完整指南](docs/appendix/A-多语言调用/2.%20在%20JavaScript%20中使用%20Ollama%20API.md) | 官方 JS SDK | ✅ |
| [A-3. Java 完整指南](docs/appendix/A-多语言调用/3.%20在%20Java%20中使用%20Ollama%20API.md) | 官方 Java SDK + Spring AI | ✅ |
| [B-1. AI Copilot 编程助手](docs/appendix/B-应用案例/1.%20搭建本地的%20AI%20Copilot%20编程助手.md) | Continue 插件接入本地模型 | ✅ |
| [B-2/3. 框架原生 Agent 参考](docs/appendix/B-应用案例/2.%20LangChain%20本地%20Agent%20参考.md) | LangChain / LlamaIndex Agent | ✅ |

### 📡 在线补充文档（living-docs/，持续更新）

| 文档 | 内容 | 更新频率 |
|---|---|---|
| [hardware.md](living-docs/hardware.md) | 本地 AI 硬件选购指南（2026 版） | 每季度 |
| [changelog.md](living-docs/changelog.md) | Ollama / Harness 版本变更记录 | 随版本 |
| [troubleshooting.md](living-docs/troubleshooting.md) | 常见问题排查手册 | 持续 |

### 💻 可运行代码（notebook/）

与章节配套的可运行代码：`notebook/C5`（MCP 示例，实测通过）、`notebook/C8`（100 行 Agent，实测通过）、`notebook/C11`（LangGraph，实测通过）等。所有代码标注运行环境与依赖。

**_注：欢迎感兴趣的开发者们提出 Issue 或提交 PR，让我们一起完善这个项目！_**

**想要深度参与的同学可以联系我们，我们会将你加入到项目的维护者中。**

## 📦 目录结构

```
handy-ollama/
├── docs/            # 教程正文（12 章 + 附录）
├── notebook/        # 可运行代码示例
├── living-docs/     # 在线补充文档（硬件/变更/排障）
├── images/          # 教程插图
└── README.md        # 本文件
```

## 🙏 致谢

### 核心贡献者

- [张友东](https://github.com/AXYZdong)（Datawhale成员）
- [林通](https://github.com/kjlintong)（Datawhale成员）
- [柴春阳](https://github.com/Springff)（内容创作者）
- [王莹莹](https://github.com/fuyueagain)（Datawhale成员）
- [曾鑫民](https://github.com/fancyboi999)（内容创作者）
- [娄天奥](https://github.com/lta155)（Datawhale成员）
- [杨卓](https://github.com/little1d)（内容创作者）
- [姜舒凡](https://github.com/Tsumugii24)（Datawhale成员）
- [曹越](https://github.com/rainsubtime)（内容创作者）
- [王晓亮](https://github.com/tomowang)（Datawhale成员）

### 特别感谢
- Ollama 官方仓库：https://github.com/ollama/ollama
- 感谢  [@Sm1les](https://github.com/Sm1les) 对本项目的帮助与支持
- 感谢所有为本项目做出贡献的开发者们 ❤️

<a href="https://github.com/AXYZdong/handy-ollama/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=AXYZdong/handy-ollama" />
</a>

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=datawhalechina/handy-ollama&type=Date)](https://star-history.com/#datawhalechina/handy-ollama&Date)

## LICENSE

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey" /></a><br />本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议</a>进行许可。
