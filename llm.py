from langchain_ollama import ChatOllama

llm = ChatOllama(
    model=input("Choose one of these models: llama 3.2:3b, " \
"mistral:7b, " \
"qwen 2.5:3b, " \
"qwen 3:4b, " \
"ministral-3:3b, " \
"gemma 3:2b: ")
    )