"""
让本地 Ollama 模型使用 MCP 工具(核心示例)
=============================================
演示完整的 Agent 循环: 本地模型 + MCP 工具 = 能查天气的 Agent。

流程:
1. 连接 MCP Server(天气服务), 获取工具清单
2. 把 MCP 工具的 JSON Schema 转换成 Ollama /api/chat 的 tools 参数
3. 循环(最多 5 轮):
   - 调用 Ollama chat 接口
   - 模型返回 tool_calls → 通过 MCP 执行工具 → 结果回传给模型
   - 模型不再调用工具 → 输出最终回答

环境变量:
    OLLAMA_HOST   Ollama 服务地址, 默认 http://localhost:11434
    OLLAMA_MODEL  模型名, 默认 qwen3:8b

运行方式:
    python ollama_mcp_agent.py

依赖: pip install "mcp>=2.0" ollama
"""

import asyncio
import json
import os
import sys

import ollama
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "qwen3:8b")
MAX_ROUNDS = 5  # 防止无限循环

client = ollama.Client(host=OLLAMA_HOST)


def to_ollama_tools(mcp_tools: list) -> list:
    """把 MCP 工具 schema 转换成 Ollama 的 tools 参数格式。

    MCP 工具形如:
        Tool(name='get_weather', description='...', inputSchema={...})
    Ollama 需要 OpenAI function calling 格式:
        {"type": "function", "function": {"name", "description", "parameters"}}
    """
    tools = []
    for tool in mcp_tools:
        tools.append({
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description or "",
                "parameters": tool.input_schema,  # 本身就是 JSON Schema
            },
        })
    return tools


async def run_agent(session: ClientSession, user_query: str) -> None:
    # 1. 从 MCP Server 拉取工具
    tools_result = await session.list_tools()
    tools = to_ollama_tools(tools_result.tools)
    print(f"[MCP] 发现 {len(tools)} 个工具: {[t['function']['name'] for t in tools]}\n")

    # 对话历史: 始终把工具的 JSON Schema 放进 tools 参数, 而不是塞进提示词
    messages = [{"role": "user", "content": user_query}]

    for round_no in range(1, MAX_ROUNDS + 1):
        print(f"===== 第 {round_no} 轮 =====")

        # 2. 调用本地模型
        response = client.chat(model=OLLAMA_MODEL, messages=messages, tools=tools)
        msg = response.message

        # 3. 模型决定调用工具
        if msg.tool_calls:
            messages.append({"role": "assistant", "content": msg.content or "", "tool_calls": msg.tool_calls})
            for call in msg.tool_calls:
                fn = call.function
                print(f"[模型] 调用工具: {fn.name}({json.dumps(fn.arguments, ensure_ascii=False)})")
                # 4. 通过 MCP 执行工具
                result = await session.call_tool(fn.name, fn.arguments or {})
                text = "".join(c.text for c in result.content if hasattr(c, "text"))
                print(f"[工具] 返回: {text}")
                # 5. 结果回传: ollama 包使用 role="tool"
                messages.append({"role": "tool", "content": text})
        else:
            # 模型给出最终回答
            print(f"[模型] 最终回答: {msg.content}")
            return

    print(f"[警告] 达到最大轮数 {MAX_ROUNDS}, 停止。")


async def main() -> None:
    server_params = StdioServerParameters(
        command=sys.executable,
        args=["mcp_weather_server.py"],
    )
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            # 演示任务: 读者可改成任意问题
            await run_agent(session, "北京今天天气怎么样? 顺便看看未来三天的预报。")


if __name__ == "__main__":
    asyncio.run(main())
