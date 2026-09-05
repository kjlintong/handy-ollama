"""LangGraph + Ollama 最小实测: 用预构建 ReAct Agent 调本地模型"""
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

# 本地模型(OpenAI 兼容接口)
model = ChatOpenAI(
    base_url="http://172.28.176.1:11434/v1",
    api_key="ollama",
    model="qwen3:8b-64k",
    temperature=0.2,
)

# 一个简单的工具
def get_weather(city: str) -> str:
    """查询指定城市今天的天气。city: 城市名"""
    data = {"北京": "晴, 32°C", "上海": "多云转阵雨, 35°C", "广州": "雷阵雨, 33°C"}
    return f"{city}: {data.get(city, '暂无数据')}"

agent = create_agent(model, tools=[get_weather])

result = agent.invoke({"messages": [("user", "北京今天天气怎么样?")]})
for msg in result["messages"]:
    print(f"[{msg.type}] {msg.content[:80]}")
