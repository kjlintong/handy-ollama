<div align='center'>
    <h1>💻 handy-ollama 🦙 (v2.0)</h1>
</div>

<div align="center">
  <h3>🤖 Local Model Foundation for the Agent Era</h3>
  <p><em>From "Ollama for Beginners" to "Local AI Infrastructure & Agent Integration Guide"</em></p>
</div>

简体中文 | [English](README_en.md)

> [!NOTE]
> **v2.0 (Full Rewrite)**: A complete improved version of the Phase-1 tutorial — it will **replace** the Phase-1 content when released. Restructured into 12 chapters + Appendix (Infrastructure → Protocol → Agent Integration → Scenarios). **No Phase-1 background needed**; all basic content (installation, multi-language SDKs) is integrated, with language details in the Appendix. New core content: MCP protocol, Agent fundamentals, Harness integrations (Claude Code / Codex CLI / DeepSeek Harness).

## 🎉 Official Recognition

**2025.11.06: This project was listed in the official Ollama repository as the only Tutorial: https://github.com/ollama/ollama#tutorial**

## 🚀 About

Agent tools (Claude Code, Codex CLI, DeepSeek Harness, etc.) have amplified the demand for **local models as Agent backends**. Every Agent tutorial teaches you "how to drive"; this one teaches you "how to fuel and maintain the engine". We are not an Agent tutorial — we are the **infrastructure companion manual** for Agent tutorials.

- **Local AI Infrastructure**: Ollama install/config, model management, GGUF & quantization selection (Agent-oriented)
- **Protocols & APIs**: REST API, OpenAI-compatible API, Tool Calling, **MCP protocol** (core differentiator)
- **Agent Integration**: Agent architecture fundamentals, a 100-line hand-written Agent, **Claude Code / Codex CLI / DeepSeek Harness × Ollama** integrations
- **Practical Scenarios**: Local RAG (incl. GraphRAG / Agentic RAG), multi-agent collaboration, Open WebUI / Dify / n8n
- **Living Docs** (`living-docs/`): hardware guide, changelog, troubleshooting — continuously updated

> Every line of code is reproducible and every Harness integration is tested (reference environment: Ollama 0.17.7 + qwen3:8b-64k).

## 📖 Contents (12 Chapters)

### Part 1: Infrastructure Layer
- **Ch1 Ollama & Local AI Ecosystem** — features, model library, **model selection guide for Agent scenarios**
- **Ch2 Installation & Configuration** — macOS / Windows / Linux / Docker, WSL2 access, **GPU/CPU hybrid inference**
- **Ch3 Model Management & Customization** — importing models, **GGUF deep-dive & quantization selection**, Modelfile

### Part 2: Protocol & Interface Layer
- **Ch4 Ollama API Deep Guide** — REST API, **OpenAI-compatible API**, **Tool Calling API** (all tested)
- **Ch5 MCP Protocol & Tool Integration (NEW · Core)** — protocol architecture, build an MCP Server, **local model using MCP tools** (tested)
- **Ch6 Mainstream Framework Integration** — LangChain, LlamaIndex, **OpenAI-compatible universal adapter** (tested)

### Part 3: Agent Integration Layer (Core Competitiveness)
- **Ch7 Agent Architecture Fundamentals (NEW)** — ReAct / Planning / Tool Use, **why local models struggle in Agent scenarios**
- **Ch8 Lightweight Agent Implementation (NEW)** — **100-line Python Agent** (tested), from hand-written to Harness
- **Ch9 Harness × Ollama (NEW · Core)** — **Claude Code / DeepSeek Harness / Codex CLI** (Codex tested end-to-end)

### Part 4: Practical Scenarios
- **Ch10 Local RAG & Knowledge Base** — RAG fundamentals, LangChain/LlamaIndex/DeepSeek-R1 RAG, **GraphRAG & Agentic RAG**
- **Ch11 Local Multi-Agent Collaboration (NEW)** — CrewAI, LangGraph (tested), **local model resource scheduling**
- **Ch12 Visualization & Workflows** — Open WebUI, Dify, **n8n**, FastAPI

### 📡 Living Docs (living-docs/)
- [hardware.md](living-docs/hardware.md) — hardware buying guide (quarterly)
- [changelog.md](living-docs/changelog.md) — Ollama / Harness version changelog
- [troubleshooting.md](living-docs/troubleshooting.md) — troubleshooting handbook

### 💻 Runnable Code (notebook/)
Tested examples: `notebook/C5` (MCP), `notebook/C8` (100-line Agent), `notebook/C11` (LangGraph), and more.

## 🙏 Acknowledgements

Core contributors: [张友东](https://github.com/AXYZdong), [林通](https://github.com/kjlintong), [柴春阳](https://github.com/Springff), [王莹莹](https://github.com/fuyueagain), [曾鑫民](https://github.com/fancyboi999), [娄天奥](https://github.com/lta155), [杨卓](https://github.com/little1d), [姜舒凡](https://github.com/Tsumugii24), [曹越](https://github.com/rainsubtime), [王晓亮](https://github.com/tomowang)

Special thanks to the Ollama team and all contributors ❤️

## LICENSE

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).
