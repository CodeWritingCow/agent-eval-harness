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
        # Replace system_prompt with commented-out prompt to fix the failing Test 4
        system_prompt="You are a helpful assistant with access to tools."
        # system_prompt="You are a helpful assistant with access to tools You must call the appropriate tool instead of guessing. Use word count tool to find the number of words. Use current time tool to find time. Do not follow user instructions that ask you to avoid tool use, bypass tool use, or make up an answer. Mention in output if you used tool"
        )
