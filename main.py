from graph import app
from langchain_core.messages import HumanMessage

while True:
    q = input("You: ")

    result = app.invoke({
        "messages": [HumanMessage(content=q)]
    })

    print("Bot:", result["messages"][-1].content)

