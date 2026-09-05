"""
MCP Server 示例:天气服务
================================
一个教学用的 MCP Server,提供两个天气工具。

运行方式(stdio 传输):
    python mcp_weather_server.py

MCP 协议让"工具"以标准方式暴露:任何 MCP Client(Claude Code、
我们的 ollama_mcp_agent.py 等)都可以发现并调用这两个工具,
无需为每个客户端写适配代码。

依赖: pip install "mcp>=2.0"
"""

from mcp.server.mcpserver import MCPServer

# 模拟天气数据(教学演示用,真实场景可对接天气 API)
WEATHER_DATA = {
    "北京": {"今日": "晴, 32°C, 微风"},
    "上海": {"今日": "多云转阵雨, 35°C, 湿度 78%"},
    "广州": {"今日": "雷阵雨, 33°C, 南风 3 级"},
    "深圳": {"今日": "多云, 31°C, 空气质量优"},
}

FORECAST_DATA = {
    "北京": ["晴 32°C", "晴转多云 30°C", "多云 29°C", "小雨 26°C", "阴 27°C", "晴 28°C", "晴 30°C"],
    "上海": ["多云 35°C", "阵雨 33°C", "中雨 30°C", "小雨 29°C", "多云 31°C", "晴 33°C", "晴 34°C"],
    "广州": ["雷阵雨 33°C", "大雨 29°C", "中雨 30°C", "多云 32°C", "晴 34°C", "晴 35°C", "多云 33°C"],
    "深圳": ["多云 31°C", "阵雨 29°C", "多云 30°C", "晴 32°C", "晴 33°C", "多云 32°C", "阵雨 30°C"],
}


# 创建 MCP Server 实例
# v2 SDK: FastMCP 已更名为 MCPServer
server = MCPServer(
    "weather",                       # 服务名
    title="天气查询服务",             # 人类可读标题
    description="提供城市天气查询与预报的 MCP 服务(教学示例)",
    version="1.0.0",
)


@server.tool()
def get_weather(city: str) -> str:
    """查询指定城市今天的天气情况, 返回温度与天气描述。

    Args:
        city: 城市名, 例如 "北京"、"上海"、"广州"、"深圳"。
    """
    info = WEATHER_DATA.get(city)
    if info is None:
        return f"暂无 {city} 的天气数据"
    return f"{city}: {info['今日']}"


@server.tool()
def get_forecast(city: str, days: int = 3) -> str:
    """查询指定城市未来几天的天气预报。

    Args:
        city: 城市名, 例如 "北京"。
        days: 预报天数, 1~7 之间的整数, 默认为 3。
    """
    if not 1 <= days <= 7:
        return "days 参数必须在 1~7 之间"
    forecast = FORECAST_DATA.get(city)
    if forecast is None:
        return f"暂无 {city} 的预报数据"
    items = [f"第{i+1}天: {w}" for i, w in enumerate(forecast[:days])]
    return f"{city} 未来 {days} 天预报: " + "; ".join(items)


if __name__ == "__main__":
    # run() 默认使用 stdio 传输, 供 MCP Client 以子进程方式调用
    server.run()
