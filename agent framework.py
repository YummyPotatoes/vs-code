from langgraph.graph import StateGraph
from langchain_community.llms import Ollama

llm = Ollama(model="llama3.2:3b")

def chat_node(state):
    user_input = state["input"]
    response = llm.invoke(user_input)
    return {"output": response}

graph = StateGraph(dict)

graph.add_node("chat", chat_node)
graph.set_entry_point("chat")
graph.set_finish_point("chat")

app = graph.compile()

while True:
    q = input("You: ")
    result = app.invoke({"input": q})
    print("Bot:", result["output"])

## install package pip3 install langgraph langchain langchain-community