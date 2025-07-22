import os
import re
from dotenv import load_dotenv
from openai import OpenAI
# from langsmith import traceable


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



# Decompose Complex Prompt into Subtasks
# @traceable(name="Decompose Prompt into Subtasks")
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

# Subtask Refinement
# @traceable(name="Refine Subtask")
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


# Recompose Subtasks into CoT Prompt
def recompose_subtasks(subtasks: list[str]) -> str:
    return " ".join(subtasks)


# Entry Point
# @traceable(name="PromptDecomposer CoT Flow")
def run_prompt_decomposer(prompt: str) -> str:
    print("\n=== PromptDecomposer Test ===\n")
    print("Prompt:")
    print(prompt.strip())

    subtasks = decompose_prompt_into_subtasks(prompt)
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

    return final_prompt.strip()


if __name__ == "__main__":
    
    test_prompt = "I want to be come a movie star. How do I get there if no degree?"
    
    run_prompt_decomposer(test_prompt)
