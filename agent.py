from datetime import datetime

from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

@tool
def get_current_time() -> str:
    """Return the current local date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@tool
def get_word_count(text: str) -> int:
    """Return the number of words in the given text."""
    return len(text.split())

def build_agent():
    model = ChatOllama(model="qwen3.5:4b", temperature=0)
    
    return create_agent(
        model=model,
        tools = [get_current_time, get_word_count],
        system_prompt="You are a helpful assistant with access to tools."
        )
