# living-docs：常见问题排查

> **维护频率**：持续更新
> **说明**：Harness 对接失败、模型加载错误、性能瓶颈的诊断手册。正文引用本文。

## 一、安装与启动类

### Q1: 端口 11434 被占用 / bind 报错
**现象**：`ollama serve` 报 `listen tcp 127.0.0.1:11434: bind: Only one usage of each socket address`。
**原因**：Ollama 已在运行（Windows 默认开机自启）。
**处理**：无需重复启动；或任务管理器禁用自启后重启（见[第2章](../docs/C2/2.%20Ollama%20在%20Windows%20下的安装与配置.md)）。

### Q2: WSL 里访问不到 Windows 侧 Ollama
**原因**：WSL2 是独立虚拟网络，`localhost` 不通。
**处理**：
```bash
ip route show default | awk '{print $3}'   # 得到网关 IP, 如 172.28.176.1
curl http://<网关IP>:11434/api/tags
```
Windows 侧需设置 `OLLAMA_HOST=0.0.0.0:11434`（见[第2章 WSL 小节](../docs/C2/2.%20Ollama%20在%20Windows%20下的安装与配置.md)）。

### Q3: 模型下载慢 / 下载失败
**处理**：换镜像源（`OLLAMA_HOST` 指向国内镜像）、检查磁盘空间（模型库默认在用户目录 `.ollama/models`）、`ollama pull` 断点续传重试。

## 二、模型加载与性能类

### Q4: 模型一直 100% CPU（没用上 GPU）
**原因**：显存不足自动回退 / 驱动问题 / CPU-only 环境。
**排查**：
```bash
ollama ps          # PROCESSOR 列看分配
nvidia-smi         # 确认显卡可见
ollama run qwen3:8b --verbose   # 看加载日志
```
**处理**：换小量化模型、缩短 `num_ctx`、更新驱动（NVIDIA 需 550+，见 [hardware.md](./hardware.md)）。

### Q5: 推理速度慢（token/s 低）
**原因**：CPU 推理 / 量化过高 / 上下文过长 / 后台任务抢占。
**处理**：确认 GPU 分配（Q4）；降量化到 Q4_K_M；缩短 `num_ctx`；`OLLAMA_NUM_PARALLEL` 调低避免抢占。

### Q6: 换模型时等待很久（反复加载）
**原因**：`OLLAMA_KEEP_ALIVE` 默认 5 分钟，模型被卸载。
**处理**：`export OLLAMA_KEEP_ALIVE=24h`（或 `-1` 常驻），见[第11章](../docs/C11/3.%20本地模型资源调度.md)。

### Q7: 显存 OOM / 崩溃
**处理**：三板斧——`keep_alive: 0` 及时卸载、`num_ctx` 缩短、换小模型；开启 `OLLAMA_FLASH_ATTENTION=1` + `OLLAMA_KV_CACHE_TYPE=q8_0`（见[第11章](../docs/C11/3.%20本地模型资源调度.md)）。

## 三、Agent / Harness 对接类

### Q8: Claude Code / Codex / dsh 连不上本地模型
**排查清单**：
1. `curl http://localhost:11434/api/tags` 通不通；
2. 环境变量是否生效（Claude Code 需 `ANTHROPIC_BASE_URL`，Codex 需 `base_url` 指向 `/v1/`，见[第9章](../docs/C9)）；
3. 模型名是否本地存在（`ollama list`）；
4. Harness 是否要求 64K+ 上下文（Codex 官方要求，见[第9章 3](../docs/C9/3.%20Codex%20CLI.md)）。

### Q9: 本地模型不调用工具 / 参数乱填
**原因**：模型工具调用能力不足 / 量化太低 / 工具描述不清。
**处理**：换工具调用友好模型（Qwen3 系）；量化 ≥ Q4_K_M；精简并写清工具描述（见[第5章](../docs/C5/4.%20常用%20MCP%20Server%20与%20Ollama%20配合.md)）；代码层加重试容错。

### Q10: Agent 跑着跑着"忘了任务"
**原因**：上下文超限被截断 / 目标不在可见范围。
**处理**：长上下文模型 + 合理 `num_ctx`；把目标固定进系统提示词；工具输出截断（见[第7章](../docs/C7/1.%20Agent%20架构原理.md)）。

### Q11: MCP 连接报 "No module named 'mcp'"
**原因**：Client 用系统 python 启动 Server，两边环境不一致。
**处理**：`command=sys.executable` 用同一解释器（见[第5章](../docs/C5/2.%20用%20Ollama%20构建%20MCP%20Server.md)）。

## 四、请求与 API 类

### Q12: 请求返回 503
**原因**：队列满（默认 512）。
**处理**：调大 `OLLAMA_MAX_QUEUE`，或减少并发、调大 `OLLAMA_NUM_PARALLEL`。

### Q13: OpenAI 兼容接口报模型不存在
**原因**：`model` 字段用了云端模型名。
**处理**：用 `ollama list` 里的本地模型名（见[第4章](../docs/C4/2.%20OpenAI%20兼容接口.md)）。

### Q14: 浏览器跨域被拦
**处理**：`OLLAMA_ORIGINS=*` 允许任意来源（开发环境）。

## 五、信息收集模板

提 Issue 时附上以下信息，可大幅加速排查：

```
Ollama 版本: (ollama --version)
系统: Windows/macOS/Linux + 显卡型号 + 显存
模型与量化: (ollama list)
复现命令: (可完整粘贴)
ollama ps 输出: (运行中模型与资源)
日志: ~/.ollama/logs/server.log 尾部 50 行
```
