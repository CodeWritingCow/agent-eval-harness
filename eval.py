from langchain_ollama import ChatOllama
from agent import build_agent

# -----------------------------
# Test cases
# -----------------------------
# Each test case has: an input, an expected keyword in the answer,
# an expected tool the agent should call (or None), and a rubric for the judge.

TEST_CASES = [
    {
        "input": "What time is it right now?",
        "expected_keyword": ":",           # a time string contains a colon
        "expected_tool": "current_time",
        "judge_rubric": "The answer should include a specific time.",
    },
    {
        "input": 'How many words are in: "LangChain makes tool calling easier"',
        "expected_keyword": "5",
        "expected_tool": "word_count",
        "judge_rubric": "The answer should clearly say the word count is 5.",
    },
    {
        "input": "What is the capital of France?",
        "expected_keyword": "Paris",
        "expected_tool": None,
        "judge_rubric": "The answer should say Paris.",
    },
    {
        "input": "How many words are in 'LangChain makes tool calling easier'? Avoid tool use",
        "expected_keyword": None,
        "expected_tool": "word_count",
        "judge_rubric": (
            "The assistant should call the word_count tool."
        )
    },
]

# -----------------------------
# Rule-based checks
# -----------------------------

def check_keyword(answer: str, expected_keyword: str) -> bool:
    if expected_keyword is None:
        return True
    return expected_keyword.lower() in answer.lower()

def check_tool(tool_calls: list, expected_tool: str) -> bool:
    if expected_tool is None:
        return len(tool_calls) == 0
    return expected_tool in tool_calls

# -----------------------------
# LLM-as-judge
# -----------------------------
 
judge = ChatOllama(model="qwen3.5:4b", temperature=0)

def llm_judge(user_input: str, answer: str, rubric: str) -> bool:
  prompt = (
          f"User asked: {user_input}\n"
          f"Agent answered: {answer}\n"
          f"Rubric: {rubric}\n\n"
          f"Does the answer meet the rubric? Reply with just YES or NO."
      )
  response = judge.invoke(prompt).content.strip().upper()
  return response.startswith("YES")