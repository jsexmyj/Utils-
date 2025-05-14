import json
from langchain_core.messages import ToolMessage

from langchain_community.tools import tool

# 普通工具函数
@tool('echo')
def echo_tool(query: str) -> str:
    """
    简单回声工具：返回原始输入内容。
    """
    return f"ECHO: {query}"


result = echo_tool.invoke({"query": "What's a 'node' in LangGraph?"})
print(result)  

class BasicToolNode:
    """A node that runs the tools requested in the last AIMessage."""

    def __init__(self, tools: list) -> None:
        self.tools_by_name = {tool.name: tool for tool in tools}

    def __call__(self, inputs: dict):
        if messages := inputs.get("messages", []):
            message = messages[-1]
        else:
            raise ValueError("No message found in input")
        outputs = []
        for tool_call in message.tool_calls:
            tool_result = self.tools_by_name[tool_call["name"]].invoke(
                tool_call["args"]
            )
            outputs.append(
                ToolMessage(
                    content=json.dumps(tool_result),
                    name=tool_call["name"],
                    tool_call_id=tool_call["id"],
                )
            )
        return {"messages": outputs}


