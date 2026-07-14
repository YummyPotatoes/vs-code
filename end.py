import requests
import time
import json

# -----------------------------
# Settings
# -----------------------------

MODEL = input("Select your model: ")

PROMPT = """
Write a 500-word summary of machine learning.
"""

URL = "http://localhost:11434/api/generate"


# -----------------------------
# Run benchmark
# -----------------------------

data = {
    "model": MODEL,
    "prompt": PROMPT,
    "stream": True
}

print(f"Running {MODEL}...")
print("Generating response...\n")

start_time = time.perf_counter()

first_token_time = None
full_response = ""

eval_count = 0
eval_duration = 0


response = requests.post(
    URL,
    json=data,
    stream=True
)

for line in response.iter_lines():

    if line:
        chunk = json.loads(line)

        # Time when first token arrives
        if first_token_time is None:
            first_token_time = time.perf_counter()

        # Collect text
        if "response" in chunk:
            full_response += chunk["response"]

        # Final statistics
        if chunk.get("done"):
            eval_count = chunk["eval_count"]
            eval_duration = chunk["eval_duration"]


end_time = time.perf_counter()


# -----------------------------
# Calculate metrics
# -----------------------------

ttft = first_token_time - start_time

generation_time = eval_duration / 1_000_000_000

tokens_per_second = eval_count / generation_time

total_time = end_time - start_time


# -----------------------------
# Results
# -----------------------------

print("========== Benchmark Results ==========")
print(f"Model: {MODEL}")
print(f"Prompt tokens: {len(PROMPT.split())}")
print(f"Generated tokens: {eval_count}")

print(f"\nTime to First Token: {ttft:.3f} seconds")
print(f"Generation Time: {generation_time:.3f} seconds")
print(f"Tokens per Second: {tokens_per_second:.2f} tok/s")
print(f"Total Time: {total_time:.3f} seconds")