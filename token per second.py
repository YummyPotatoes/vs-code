import requests

llm = input("Choose one of these models: llama 3.2:3b, " \
"mistral:7b, " \
"qwen 2.5:3b, " \
"qwen 3:4b, " \
"qwen2.5-coder:3b, " \
"gemma 3:2b")

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": llm,
        "prompt": "Explain how a neural network works.",
        "stream": False
    }
)

print("You have selected: ", llm)

data = response.json()

eval_count = data["eval_count"]
eval_duration = data["eval_duration"]  # nanoseconds

tokens_per_second = eval_count / (eval_duration / 1e9)

print(f"Generated tokens: {eval_count}")
print(f"Generation time: {eval_duration/1e9:.2f} s")
print(f"Tokens/sec: {tokens_per_second:.2f}")