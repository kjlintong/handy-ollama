# 💻 handy-ollama 🦙 (v2.0)

> **Local Model Foundation for the Agent Era**

A complete, hands-on tutorial for [Ollama](https://ollama.com) (v2.0 rewrite): from zero to deploying local models, plus deep dives into **MCP protocol** and **Agent integrations** (Claude Code / Codex CLI / DeepSeek Harness).

- **Beginner-friendly**: Chapters 1–3 start from installation, no prerequisites
- **All examples tested**: verified on Ollama 0.17.x + qwen3:8b
- **Living docs**: hardware guide, changelog, troubleshooting in [living-docs](../living-docs/hardware.md)

## Learning Path

```
Ch1–3   Infrastructure   Install Ollama, model management, quantization
Ch4–6   Protocols        REST API, OpenAI-compatible, Tool Calling, MCP
Ch7–9   Agent Integration  Agent fundamentals, 100-line Agent, Harnesses
Ch10–12 Scenarios        Local RAG, multi-agent, visualization UIs
Appendix                  Multi-language SDKs, classic use cases
```

- Part 1 (Ch1–3): Local AI Infrastructure
- Part 2 (Ch4–6): Protocols & Interfaces
- Part 3 (Ch7–9): Agent Integration
- Part 4 (Ch10–12): Practical Scenarios
- [Appendix](appendix/README.md): Multi-language SDKs & classic cases

## Quick Start

```bash
# 1. Install Ollama (macOS/Linux)
curl -fsSL https://ollama.com/install.sh | sh
# Windows: download OllamaSetup.exe from https://ollama.com/download

# 2. Run your first model
ollama run qwen3:8b

# 3. Call the API
curl http://localhost:11434/api/chat -d '{"model":"qwen3:8b","messages":[{"role":"user","content":"Hello"}],"stream":false}'
```

Licensed under [CC BY-NC-SA 4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/).
