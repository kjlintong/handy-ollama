# 💻 动手学 Ollama 🦙（v2.0）

> **Agent 时代的本地模型底座**
>
> 本教程是 [Ollama](https://ollama.com) 的完整实战指南（v2.0 改版）：从零开始掌握本地大模型部署，并深入 **MCP 协议** 与 **Agent 工具集成**（Claude Code / Codex CLI / DeepSeek Harness），让本地模型成为可靠的 Agent 后端。

- **零基础可读**：第 1~3 章从安装讲起，不需要任何前置知识
- **全部实测**：示例代码均在 Ollama 0.17.x + qwen3:8b 环境跑通
- **在线补充**：硬件选购、版本变更、故障排查见 [living-docs](../living-docs/troubleshooting.md)

## 学习路径

```
第1~3章  基础设施   安装 Ollama、管理模型、量化选型
第4~6章  协议与接口  REST API、OpenAI 兼容、Tool Calling、MCP
第7~9章  Agent 集成  Agent 原理、100 行手写 Agent、Harness 实战
第10~12章 场景实战   本地 RAG、多 Agent、可视化界面
附录     按需查阅     多语言调用、经典应用案例
```

- 第一部分（第1~3章）：本地 AI 基础设施
- 第二部分（第4~6章）：协议与接口层
- 第三部分（第7~9章）：Agent 集成层
- 第四部分（第10~12章）：场景实战层
- [📎 附录](appendix/README.md)：多语言调用、经典应用案例

## 在线补充文档（持续更新）

- [硬件选购指南](../living-docs/hardware.md)（每季度更新）
- [版本变更日志](../living-docs/changelog.md)（随版本发布）
- [常见问题排查](../living-docs/troubleshooting.md)（持续更新）

## 快速开始

```bash
# 1. 安装 Ollama(macOS/Linux)
curl -fsSL https://ollama.com/install.sh | sh
# Windows: https://ollama.com/download 下载 OllamaSetup.exe

# 2. 运行第一个模型
ollama run qwen3:8b

# 3. 调用 API
curl http://localhost:11434/api/chat -d '{"model":"qwen3:8b","messages":[{"role":"user","content":"你好"}],"stream":false}'
```

详细步骤见 [第 2 章 安装与配置](C2/1.%20Ollama%20在%20macOS%20下的安装与配置.md)。

---

本教程采用 <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议</a>。
