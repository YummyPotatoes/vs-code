import requests
import time

url = "http://localhost:11434/api/generate"

data = {
    "model": "llama3.2:3b",
    "prompt": "Explain how neural networks work",
    "stream": True
}

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