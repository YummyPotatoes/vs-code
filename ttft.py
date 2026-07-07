import requests
import time

url = "http://localhost:11434/api/generate"

llm = input("Choose one of these models: llama 3.2:3b, " \
"mistral:7b, " \
"qwen 2.5:3b, " \
"qwen 3:4b, " \
"phi-3 mini, " \
"gemma 3:2b")

data = {
    "model": llm,
    "prompt": "Explain how neural networks work",
    "stream": True
}

print("You have selected: ", llm)

start = time.time()

response = requests.post(url, json=data, stream=True)

first_token = None

for line in response.iter_lines():
    if line:
        if first_token is None:
            first_token = time.time()
            print("Time to first token:",
                  first_token - start,
                  "seconds")
            break