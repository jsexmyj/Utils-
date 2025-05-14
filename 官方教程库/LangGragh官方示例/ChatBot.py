import io
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from PIL import Image
from langchain.chat_models import init_chat_model
from toolBot import BasicToolNode, echo_tool

# 定义状态
class State(TypedDict):
    messages:Annotated[list,add_messages]

# 初始化图流程
graph_builder = StateGraph(State)

# 配置大模型
llm = init_chat_model(
    "deepseek-ai/DeepSeek-V3",     # <model_provider>:<model_name>
    api_key="",  # 或者依赖环境变量 DEEPSEEK_API_KEY
    api_base="https://api.siliconflow.cn/v1"
)
tools = [echo_tool]
llm_tool = llm.bind_tools(tools)
# 节点函数
def chatbot(state: State):
    return {"messages": [llm_tool.invoke(state["messages"])]}

tool_node = BasicToolNode(tools)


def route_tools(
    state: State,
):
    """
    Use in the conditional_edge to route to the ToolNode if the last message
    has tool calls. Otherwise, route to the end.
    """
    if isinstance(state, list):
        ai_message = state[-1]
    elif messages := state.get("messages", []):
        ai_message = messages[-1]
    else:
        raise ValueError(f"No messages found in input state to tool_edge: {state}")
    if hasattr(ai_message, "tool_calls") and len(ai_message.tool_calls) > 0:
        return "tools"
    return END

# 添加条件边的常规案例
# def route_check_node(state: State):
#     messages = state.get("messages", [])
#     ai_message = messages[-1]
#     if ai_message.content != "yes":  # 这里只能是yes或者no
#         return END
#     return "next"

graph_builder.add_node("tools", tool_node)
graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge("chatbot", END)

graph_builder.add_conditional_edges(
    "chatbot",          # 源节点
    route_tools,        # 候选目标节点列表
    {"tools": "tools",  # 条件映射：state["tools"] 的值
     END: END},         # 默认出口：当 state["tools"] 没有匹配时跳到 END
)
graph = graph_builder.compile()


# 图可视化
try:
    image = Image.open(io.BytesIO(graph.get_graph().draw_mermaid_png()))
    image.save('gragh.png')
except Exception:
    # This requires some extra dependencies and is optional
    pass

# 运行聊天机器人
def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)

# 正式运行
while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        stream_graph_updates(user_input)
    except:
        # fallback if input() is not available
        user_input = "What do you know about LangGraph?"
        print("User: " + user_input)
        stream_graph_updates(user_input)
        break