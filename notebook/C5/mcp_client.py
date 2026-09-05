"""
MCP Client 示例:发现并调用工具
================================
演示 MCP 客户端如何连接 Server、列出工具、调用工具。

流程:
1. 以子进程方式启动 mcp_weather_server.py(stdio 传输)
2. 建立 MCP 会话
3. 列出 server 暴露的所有工具(名称 + 描述)
4. 调用 get_weather(city="北京") 并打印结果

运行方式:
    python mcp_client.py

依赖: pip install "mcp>=2.0"
"""

import asyncio
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# 指定要启动的 MCP Server 子进程(stdio 传输)
SERVER_CMD = "mcp_weather_server.py"

server_params = StdioServerParameters(
    # 用当前解释器启动 server 子进程, 保证两边在同一个虚拟环境、都能 import mcp
    command=sys.executable,
    args=[SERVER_CMD],
)


async def main() -> None:
    # stdio_client 负责启动子进程并建立双向管道
    async with stdio_client(server_params) as (read, write):
        # ClientSession 封装 MCP 协议层:初始化握手、方法调用
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 1. 列出所有工具
            print("=" * 50)
            print("MCP Server 暴露的工具:")
            tools = await session.list_tools()
            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description}")

            # 2. 调用工具
            print("=" * 50)
            print("调用 get_weather(city='北京') ...")
            result = await session.call_tool("get_weather", {"city": "北京"})
            # CallToolResult: content 是列表, 每个元素是 TextContent/ImageContent 等
            for content in result.content:
                print("结果:", content.text)


if __name__ == "__main__":
    asyncio.run(main())
