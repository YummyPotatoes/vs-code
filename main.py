from graph import app
from langchain_core.messages import HumanMessage

while True:
    q = input("You: ")

    result = app.invoke({
        "messages": [HumanMessage(content=q)]
    })

    print("Bot:", result["messages"][-1].content)

## install package pip3 install langgraph langchain langchain-community
## pip install langgraph langchain langchain-community langchain-core duckduckgo-search sympy