import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2:3b",
        "prompt": "Explain how a neural network works.",
        "stream": False
    }
)

data = response.json()

eval_count = data["eval_count"]
eval_duration = data["eval_duration"]  # nanoseconds

tokens_per_second = eval_count / (eval_duration / 1e9)

print(f"Generated tokens: {eval_count}")
print(f"Generation time: {eval_duration/1e9:.2f} s")
print(f"Tokens/sec: {tokens_per_second:.2f}")