"""
Plan-and-Execute 最小实现: 规划 → 逐步执行 → 汇总
====================================================
与第 7 章 3.1 节配套的完整可运行版本。

运行:
    python plan_execute.py

环境变量:
    OLLAMA_HOST  默认 http://localhost:11434
    OLLAMA_MODEL 默认 qwen3:8b

依赖: pip install ollama
"""

import os

import ollama

OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "qwen3:8b")

client = ollama.Client(host=OLLAMA_HOST)


def make_plan(task: str) -> list[str]:
    """第一步: 让模型把任务拆成步骤清单"""
    resp = client.chat(model=OLLAMA_MODEL, messages=[
        {"role": "system", "content": "把任务拆成 3~5 个可执行的步骤, 每行一个, 不要多余解释。"},
        {"role": "user", "content": task},
    ])
    steps = [line.strip() for line in resp.message.content.splitlines() if line.strip()]
    return steps


def execute_step(step: str) -> str:
    """第二步: 逐步执行(这里简化为直接问答, 实际可接工具调用)"""
    resp = client.chat(model=OLLAMA_MODEL, messages=[{"role": "user", "content": step}])
    return resp.message.content


def run(task: str) -> None:
    plan = make_plan(task)                    # 1. 规划
    print("计划:", plan)
    results = []
    for step in plan:                         # 2. 逐步执行
        print(f"执行: {step}")
        results.append(execute_step(step))
    # 3. 汇总
    summary = client.chat(model=OLLAMA_MODEL, messages=[
        {"role": "user", "content": f"基于以下分步结果, 输出最终答案:\n{chr(10).join(results)}"}])
    print("最终答案:", summary.message.content)


if __name__ == "__main__":
    run("调研并介绍 3 个本地大模型工具")
