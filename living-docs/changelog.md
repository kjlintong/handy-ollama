# living-docs：版本变更日志

> **维护频率**：随 Ollama / Harness 版本发布更新
> **说明**：记录影响本书内容的版本变化。正文引用本文以保持时效性。

## 一、Ollama 版本变更记录

### 0.17.x（本书基线，实测 0.17.7）

- `/api/create` 改用结构化字段（`from` / `system` / `parameters`），不再依赖 modelfile 文本（见[第3章](../docs/C3/5.%20Modelfile%20高级编写.md)）；
- OpenAI 兼容接口新增 `/v1/responses`（实测 200，Codex 集成依赖此端点，见[第9章](../docs/C9/3.%20Codex%20CLI.md)）；
- `ollama launch` 官方集成机制成熟：支持 Claude Code / Codex / DeepSeek Harness / OpenCode / n8n 等（见[第9章](../docs/C9)与[第12章](../docs/C12/3.%20n8n%20工作流自动化.md)）；
- 模型库新增 `gemma4`、`qwen3.5` 等新家族（见[第1章](../docs/C1)）。

### 历史要点（供升级参考）

| 版本 | 关键变化 | 影响 |
|---|---|---|
| 0.4.x | 引入 Tool Calling | Agent 场景基础 |
| 0.5.x | 结构化输出 format=json | 数据交互 |
| 0.9.x | 模型并行加载（MAX_LOADED_MODELS） | 多模型调度 |
| 0.14.x | `/api/embed` 统一嵌入端点 | RAG 简化 |
| 0.17.x | `ollama launch` + Responses API | Harness 集成 |

## 二、Harness 对接方式变更记录

| 日期 | 工具 | 变更 | 影响 |
|---|---|---|---|
| 2026-09 | Claude Code | `ollama launch claude` 支持 `--yes` 非交互模式 | CI 场景可用 |
| 2026-09 | Codex CLI | `ollama launch codex --restore` 可移除 Ollama profile | 配置回滚 |
| 2026-09 | DeepSeek Harness | 仍为 developer preview，配置可能变动 | 关注 dsh 升级 |
| 2026-09 | LangGraph | `create_react_agent` 迁移至 `langchain.agents.create_agent` | 新代码用新导入 |

## 三、模型生态变化

| 日期 | 模型 | 说明 |
|---|---|---|
| 2026-09 | qwen3.5 | 新一代通义模型，工具调用能力提升 |
| 2026-09 | gemma4 | Google 多模态模型，支持视觉 |
| 2026-09 | gpt-oss:120b | OpenAI 开源模型，Codex 集成常用 |

## 更新规范

- 每次 Ollama 发布新版本、Harness 对接方式变化、重要模型发布，在此追加记录；
- 记录格式：日期 + 对象 + 变更内容 + 对本书的影响（正文章节链接）；
- 每季度结合 [hardware.md](./hardware.md) 巡检一次。
