# prompt_decomposer.py — PromptDecomposer (Chain-of-Thought Preprocessor)
from openai import OpenAI
import os
from dotenv import load_dotenv
import re

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



# Subtask Refinement
def refine_subtask(subtask: str) -> str:
    """
    Use OpenAI to refine a subtask into a clear, actionable instruction.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a world-class prompt engineer. Your job is to rewrite a single subtask prompt "
                    "to be clear, concise, and directly actionable. Use precise language. Avoid ambiguity or fluff."
                )
            },
            {"role": "user", "content": f"Rewrite this subtask:\n{subtask}"}
        ]
    )
    return response.choices[0].message.content.strip()

# Decompose Complex Prompt into Subtasks
def decompose_prompt_into_subtasks(prompt: str) -> list[str]:
    """
    Use OpenAI to split a complex prompt into a flat list of subtasks.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert prompt engineer. Your task is to break down any complex, multi-part prompt "
                    "into 3 to 6 clear, standalone subtasks. Each subtask must be a complete instruction or question "
                    "that can be understood independently. Avoid vague wording, outlines, or nested bullets. "
                    "Subtasks should be actionable, specific, and phrased for direct execution. "
                    "Return the subtasks as a clean, numbered list only.\n\n"
                    "Example:\n"
                    "1. Identify the core challenges described in the prompt.\n"
                    "2. List relevant data or background information required to address them.\n"
                    "3. Break down the problem-solving steps in logical order.\n"
                    "4. Recommend an approach based on clarity, feasibility, and impact."
                )
            },
            {"role": "user", "content": prompt}
        ]
    )

    output = response.choices[0].message.content.strip()
    lines = [line.strip() for line in output.splitlines() if line.strip()]
    subtasks = [re.sub(r"^\s*\d+[\.\)]\s*", "", line) for line in lines]
    return subtasks

# Recompose Subtasks into Chain-of-Thought Prompt
def recompose_subtasks(subtasks: list[str]) -> str:
    return " ".join(subtasks)

# Main Runner
if __name__ == "__main__":
    test_prompt = """
    You're designing a decentralized voting system for a global organization.
    Explain the core components needed for secure and transparent voting.
    Evaluate the trade-offs between using Ethereum vs. a custom Layer 2 solution.
    List at least three key privacy concerns and how you would address them.
    Recommend a final architecture and justify your reasoning.
    """

    print("\n=== PromptDecomposer Test ===\n")
    print("Prompt:")
    print(test_prompt.strip())

    subtasks = decompose_prompt_into_subtasks(test_prompt)
    print("\n=== Subtasks Detected ===")
    for i, sub in enumerate(subtasks, 1):
        print(f"{i}. {sub}")

    refined_subtasks = [refine_subtask(s) for s in subtasks]
    print("\n=== Refined Subtasks ===")
    for i, sub in enumerate(refined_subtasks, 1):
        print(f"{i}. {sub}")

    final_prompt = recompose_subtasks(refined_subtasks)
    print("\n=== Recomposed Chain-of-Thought Prompt ===")
    print(final_prompt.strip())
