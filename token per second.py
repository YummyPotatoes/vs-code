import time
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)

start = time.time()
chunk_count = 0

for chunk in llm.stream("Tell me a story"):
    chunk_count += 1

elapsed = time.time() - start

print(f"Elapsed: {elapsed:.2f} s")
print(f"Chunks/sec: {chunk_count / elapsed:.2f}")