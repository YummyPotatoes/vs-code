from langchain_core.tools import tool
from ddgs import DDGS
import sympy as sp

@tool
def web_search(query: str) -> str:
    """Search the web for up-to-date information."""
    results = DDGS().text(query, max_results=5)
    return "\n".join(r["title"] + ": " + r["body"] for r in results)

@tool
def calculator(expression: str) -> str:
    """Evaluate a math expression."""
    return str(sp.sympify(expression).evalf())