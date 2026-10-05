# Agent Eval Harness

Repeatable evaluation harness for AI agents using rule-based checks and LLM-as-a-judge

This example uses **LangChain**, **Ollama**, and **Qwen**. The project evaluates agent behavior against predefined test cases using automated checks and an LLM-as-a-judge approach.

Based on the freeCodeCamp tutorial [How to Evaluate AI Agents with an LLM-as-a-Judge Harness in Python](https://www.freecodecamp.org/news/how-to-evaluate-ai-agents-with-an-llm-as-a-judge-harness-in-python/).

## Features

* Run AI agent evaluations against repeatable test cases
* Use an LLM as a judge to evaluate agent responses
* Combine deterministic checks with LLM-based evaluation
* Generate pass/fail evaluation results
* Run evaluations locally using Ollama and Qwen
* Built with LangChain

## Tech Stack

* **Python**
* **LangChain**
* **LangChain Core**
* **LangChain Ollama**
* **Ollama**
* **Qwen**

## Prerequisites

Before installing the project, make sure you have:

* Python 3.10+
* [Ollama](https://ollama.com/) installed and running
* A Qwen model downloaded through Ollama
* [uv](https://docs.astral.sh/uv/) (optional)

For example:

```bash
ollama pull qwen3.5:4b
```

Verify that Ollama is working:

```bash
ollama list
```

## Installation

### Using Python `venv`

#### 1. Clone the repository

Using HTTPS:

```bash
git clone https://github.com/CodeWritingCow/agent-eval-harness.git
cd agent-eval-harness
```

Or using SSH:

```bash
git clone git@github.com:CodeWritingCow/agent-eval-harness.git
cd agent-eval-harness
```

#### 2. Create a virtual environment

##### Windows

```powershell
python -m venv venv
```

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell prevents activation, you can use Command Prompt:

```cmd
venv\Scripts\activate
```

##### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### Using Conda

Create a Conda environment:

```bash
conda create -n agent-eval-harness python=3.12
```

Activate the environment:

```bash
conda activate agent-eval-harness
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### Using uv

[uv](https://docs.astral.sh/uv/) can be used to create and manage the project's Python environment.

#### 1. Clone the repository

Using HTTPS:

```bash
git clone https://github.com/CodeWritingCow/agent-eval-harness.git
cd agent-eval-harness
```

Or using SSH:

```bash
git clone git@github.com:CodeWritingCow/agent-eval-harness.git
cd agent-eval-harness
```

#### 2. Create a virtual environment

```bash
uv venv
```

By default, uv creates a `.venv` directory in the project.

Activate the environment if desired:

##### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

##### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

##### macOS / Linux

```bash
source .venv/bin/activate
```

#### 3. Install dependencies

```bash
uv pip install -r requirements.txt
```

You can also install the requirements without manually activating the environment:

```bash
uv pip install --python .venv -r requirements.txt
```

## Usage

Make sure Ollama is running and the required Qwen model is available:

```bash
ollama list
```

Then run the evaluation harness:

```bash
python eval.py
```

If using uv without activating the virtual environment:

```bash
uv run --python .venv python eval.py
```

> The entry-point filename may change depending on the final project structure.

The harness runs the predefined evaluation cases and reports whether the agent passes the configured checks and LLM-as-a-judge evaluation.

## Project Structure

```text
agent-eval-harness/
├── agent.py
├── eval.py
├── requirements.txt
├── README.md
└── ...
```

## Evaluation Approach

The evaluation harness is designed to make agent testing **repeatable**.

Each test case provides a known input to the agent and evaluates the resulting behavior. Evaluations can include:

1. **Deterministic checks** — Verify specific properties of the agent's output.
2. **LLM-as-a-judge** — Use another LLM to assess whether the response satisfies the expected criteria.
3. **Pass/fail results** — Summarize the results so changes to the agent can be evaluated consistently.

This makes it possible to rerun the same evaluations after modifying prompts, tools, models, or agent logic and identify regressions.

## License

This project is licensed under the MIT License.

## Tutorial

This project is based on the freeCodeCamp tutorial:

[How to Evaluate AI Agents with an LLM-as-a-Judge Harness in Python](https://www.freecodecamp.org/news/how-to-evaluate-ai-agents-with-an-llm-as-a-judge-harness-in-python/)

The implementation has been adapted for local execution with Ollama and Qwen.
