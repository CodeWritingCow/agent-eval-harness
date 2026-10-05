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