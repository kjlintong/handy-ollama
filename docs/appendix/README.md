# 附录

> 本附录收录两类内容：
> 1. **基础操作细节**——各语言 SDK 的完整调用指南（正文第 4 章聚焦协议与接口原理，语言细节在此展开）；
> 2. **经典应用案例**——第一期沉淀的实用案例，改版后保留参考价值。

## A. 多语言调用

| 文档 | 内容 |
|---|---|
| [0. 多语言调用概览](A-多语言调用/0.%20多语言调用概览.md) | 各语言路线选择与统一方案 |
| [1. 在 Python 中使用 Ollama API](A-多语言调用/1.%20在%20Python%20中使用%20Ollama%20API.md) | 官方 Python SDK 完整指南 |
| [2. 在 JavaScript 中使用 Ollama API](A-多语言调用/2.%20在%20JavaScript%20中使用%20Ollama%20API.md) | 官方 JS SDK 完整指南 |
| [3. 在 Java 中使用 Ollama API](A-多语言调用/3.%20在%20Java%20中使用%20Ollama%20API.md) | 官方 Java SDK + Spring AI |
| C++ / Go | 文档与代码见 `notebook/C4/` |

## B. 经典应用案例

| 文档 | 内容 |
|---|---|
| [1. 搭建本地的 AI Copilot 编程助手](B-应用案例/1.%20搭建本地的%20AI%20Copilot%20编程助手.md) | Continue 插件接入本地模型 |
| [2. LangChain 本地 Agent 参考](B-应用案例/2.%20LangChain%20本地%20Agent%20参考.md) | 框架原生 Agent 用法（正文第 8 章为更通用的手写方案） |
| [3. LlamaIndex 本地 Agent 参考](B-应用案例/3.%20LlamaIndex%20本地%20Agent%20参考.md) | 同上 |

## 附录与正文的关系

- 正文 12 章构成完整学习路径（从安装到 Agent 实战），不依赖附录；
- 附录是"按需查阅"的参考手册：写 Python 程序时翻附录 A-1，想给 IDE 配本地模型时翻附录 B-1；
- 附录内容与正文同一版本基线（Ollama 0.17.x），随 living-docs 一起维护。
