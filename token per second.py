import time

start = time.time()
token_count = 0

for chunk in llm.stream("Tell me a story"):
    token_count += 1      # Approximate: one streamed chunk is not always exactly one token

elapsed = time.time() - start

print(f"Approx. tokens/sec: {token_count / elapsed:.2f}")