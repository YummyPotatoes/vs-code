from langchain_core.tools import tool
from duckduckgo_search import DDGS
import sympy as sp

@tool
def web_search(query: str) -> str:
    results = DDGS().text(query, max_results=5)
    return "\n".join(r["title"] + ": " + r["body"] for r in results)

@tool
def calculator(expression: str) -> str:
    return str(sp.sympify(expression).evalf())