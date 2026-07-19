import re
import csv
from datasets import load_dataset
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

# Configuration

MODEL_NAME = input("Enter the model name: ")      
SUBJECT = "all"              # "all" or a specific subject
MAX_QUESTIONS = 300         # Set to an integer for testing

# Load MMLU Dataset

dataset = load_dataset("cais/mmlu", SUBJECT)

test_set = dataset["test"]

if MAX_QUESTIONS:
    test_set = test_set.select(range(MAX_QUESTIONS))

# Initialize Ollama

llm = ChatOllama(
    model=MODEL_NAME,
    temperature=0,
    num_predict=5
)

# Helper Functions

def build_prompt(sample):

    choices = sample["choices"]

    prompt = f"""
Answer the following multiple choice question.

Question:
{sample["question"]}

A. {choices[0]}
B. {choices[1]}
C. {choices[2]}
D. {choices[3]}

Respond with ONLY ONE LETTER:
A
B
C
or D.
"""

    return prompt.strip()


def extract_answer(text):
    """
    Extract first occurrence of A/B/C/D.
    """

    match = re.search(r"\b([ABCD])\b", text.upper())

    if match:
        return match.group(1)

    return None


# Benchmark

correct = 0
wrong = 0
results = []

letters = ["A", "B", "C", "D"]

for i, sample in enumerate(test_set):

    prompt = build_prompt(sample)

    response = llm.invoke(
        [HumanMessage(content=prompt)]
    )

    prediction = extract_answer(response.content)

    answer = letters[sample["answer"]]

    is_correct = prediction == answer

    if is_correct:
        correct += 1
    else:
        print("FAILED RESPONSE:", repr(response.content))
        wrong += 1

    results.append([
        sample["question"],
        prediction,
        answer,
        is_correct
    ])

    print(
        f"[{i+1}/{len(test_set)}] "
        f"Pred={prediction} "
        f"GT={answer} "
        f"{'✓' if is_correct else '✗'}"
    )

# Final Statistics

total = correct + wrong
accuracy = (correct / total) * 100

print("\n==============================")
print(f"Model: {MODEL_NAME}")
print(f"Total Questions : {total}")
print(f"Correct         : {correct}")
print(f"Wrong           : {wrong}")
print(f"Accuracy        : {accuracy:.2f}%")
print("==============================")

# Save CSV

filename = f"{MODEL_NAME}_mmlu_results.csv"

with open(filename, "w", newline="", encoding="utf-8") as f:

    writer = csv.writer(f)

    writer.writerow([
        "Question",
        "Prediction",
        "GroundTruth",
        "Correct"
    ])

    writer.writerows(results)

print(f"\nSaved results to {filename}")