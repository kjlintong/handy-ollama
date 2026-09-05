"""
100 行极简 Agent: 解析指令 + 调用工具 (ReAct 最小实现)
========================================================
三个内置工具:
  - get_weather(city):   查询城市天气(模拟数据)
  - calculator(expr):    计算数学表达式
  - read_file(path):     读取本地文本文件

流程(ReAct 循环):
  用户任务 → 模型思考 → 调用工具 → 观察结果 → 继续 → 最终回答

环境变量:
  OLLAMA_HOST  默认 http://localhost:11434
  OLLAMA_MODEL 默认 qwen3:8b

运行:
  python mini_agent.py "北京今天天气怎么样?"
  或进入交互模式: python mini_agent.py

依赖: pip install ollama
"""

import json
import os
import re
import sys

import ollama

OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "qwen3:8b")
MAX_ROUNDS = 6

client = ollama.Client(host=OLLAMA_HOST)

# ---------- 工具实现 ----------

WEATHER = {"北京": "晴, 32°C", "上海": "多云转阵雨, 35°C", "广州": "雷阵雨, 33°C"}

def get_weather(city: str) -> str:
    """查询指定城市今天的天气。city: 城市名"""
    return f"{city}: {WEATHER.get(city, '暂无数据')}"

def calculator(expr: str) -> str:
    """计算数学表达式, 如 '2*3+4'。expr: 数学表达式字符串"""
    expr = re.sub(r"[^0-9+\-*/().\s]", "", expr)  # 只允许数学字符(安全)
    try:
        return str(eval(expr))  # 教学示例; 生产环境请用安全求值库
    except Exception as e:
        return f"计算错误: {e}"

def read_file(path: str) -> str:
    """读取本地文本文件内容。path: 文件路径"""
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()[:2000]  # 截断, 防止上下文爆炸
    except Exception as e:
        return f"读取失败: {e}"

# 工具注册表: 名字 -> (函数, 描述, 参数schema)
TOOLS = [
    {"type": "function", "function": {
        "name": "get_weather", "description": get_weather.__doc__,
        "parameters": {"type": "object", "properties": {"city": {"type": "string"}}, "required": ["city"]}}},
    {"type": "function", "function": {
        "name": "calculator", "description": calculator.__doc__,
        "parameters": {"type": "object", "properties": {"expr": {"type": "string"}}, "required": ["expr"]}}},
    {"type": "function", "function": {
        "name": "read_file", "description": read_file.__doc__,
        "parameters": {"type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]}}},
]

FUNCS = {"get_weather": get_weather, "calculator": calculator, "read_file": read_file}

SYSTEM = "你是一个本地运行的 Agent 助手。需要外部信息时调用工具; 工具返回后基于结果回答; 全部使用中文。"

# ---------- ReAct 循环 ----------

def run_agent(task: str) -> None:
    messages = [{"role": "system", "content": SYSTEM},
                {"role": "user", "content": task}]
    for round_no in range(1, MAX_ROUNDS + 1):
        print(f"\n===== 第 {round_no} 轮 =====")
        resp = client.chat(model=OLLAMA_MODEL, messages=messages, tools=TOOLS)
        msg = resp.message
        if not msg.tool_calls:
            print(f"[模型] {msg.content}")
            return
        messages.append({"role": "assistant", "content": msg.content or "",
                         "tool_calls": msg.tool_calls})
        for call in msg.tool_calls:
            fn = call.function
            try:
                result = FUNCS[fn.name](**fn.arguments or {})
            except Exception as e:
                result = f"工具执行异常: {e}"
            print(f"[工具] {fn.name}{json.dumps(fn.arguments, ensure_ascii=False)} -> {result}")
            messages.append({"role": "tool", "content": str(result)})
    print(f"\n[警告] 达到最大轮数 {MAX_ROUNDS}, 停止。")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_agent(sys.argv[1])
    else:
        print("交互模式: 输入任务, Ctrl+D 退出")
        while True:
            try:
                task = input("\n> ")
            except EOFError:
                break
            run_agent(task)
