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
        "expected_tool": "get_current_time",
        "judge_rubric": "The answer should include a specific time.",
    },
    {
        "input": 'How many words are in: "LangChain makes tool calling easier"',
        "expected_keyword": "5",
        "expected_tool": "get_word_count",
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
        "expected_tool": "get_word_count",
        "judge_rubric": (
            "The assistant should call the get_word_count tool."
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

# -----------------------------
# Run the evals
# -----------------------------

def run_evals():
    agent = build_agent()
    passed_count = 0

    for i, case in enumerate(TEST_CASES, start=1):
        # Run the agent
        result = agent.invoke({
            "messages": [
                { "role": "user", "content": case["input"] }
            ]
        })

        answer = result["messages"][-1].content
        tool_calls = []
        for msg in result["messages"]:
            calls = getattr(msg, "tool_calls", None)
            if calls:
                for call in calls:
                    tool_calls.append(call["name"])

        print(f"[Answer] Test {i}: {answer} \n[Tools] {tool_calls}")


        # Check each criterion
        keyword_check = check_keyword(answer, case["expected_keyword"])
        tool_check = check_tool(tool_calls, case["expected_tool"])
        llm_check = llm_judge(case["input"], answer, case["judge_rubric"])

        passed = keyword_check and tool_check and llm_check
        if passed:
            passed_count += 1

        # Print the result
        status = "PASS" if passed else "FAIL"
        print(f"[{status}] Test {i}: {case['input']}")
        if not keyword_check:
            print(f"    - keyword check failed (expected '{case['expected_keyword']}')")
        if not tool_check:
            print(f"    - tool check failed (expected {case['expected_tool']}, got {tool_calls})")
        if not llm_check:
            print(f"    - judge said NO")

    print(f"\n{passed_count}/{len(TEST_CASES)} passed")

if __name__ == "__main__":
    run_evals()