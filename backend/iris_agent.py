# iris_agent.py — Iris  Test (Phase 1)
import os
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def review_and_rewrite_prompt(messy_prompt: str) -> dict:
    """Run Iris agent to review and rewrite a prompt."""
    review_template = f"""
Analyze the following prompt for clarity, length, and level of detail.

Check specifically:
1. Is this prompt too long or overly complex?
2. Is this prompt too short or lacking necessary context or details?
3. Are there any ambiguous or unclear phrases?

Prompt:
\"\"\"{messy_prompt}\"\"\"

Provide:
- A clarity rating from 1 to 10.
- Specific issues found.
- Suggestions for improving the prompt.
- A fully rewritten version of the prompt that resolves the identified issues, phrased clearly and professionally.
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert prompt engineer."},
            {"role": "user", "content": review_template}
        ]
    )

    return {
        "original_prompt": messy_prompt,
        "review_output": response.choices[0].message.content.strip()
    }

def run_agent():
    print("Iris Agent Starting...")

    messy_prompt = (
        "Explain how to get are carrer as a lwayer but like go deep but also make it simple "
        "but not too simple and also give examples and maybe something else too idk."
    )

    result = review_and_rewrite_prompt(messy_prompt)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    phase = "Phase 1 — Review Test"

    print("\n=== Iris Prompt Review ===")
    print(f"=== {phase} — {timestamp} ===\n")
    print(f"Original Prompt:\n{messy_prompt}\n")
    print("Review Output:")
    print(result["review_output"])

# Mutli Pass Refinment w/Auto Stop
def multi_pass_refine_prompt(initial_prompt: str, passes: int = 5, auto_stop_score: int = 9) -> dict:
    """Runs Iris agent recursively to refine a prompt with stability-based auto-stop."""
    prompt = initial_prompt
    history = []
    previous_score = None  # Track previous pass score for stability check

    for i in range(passes):
        result = review_and_rewrite_prompt(prompt)
        history.append({
            "pass": i + 1,
            "review_output": result["review_output"],
            "prompt_after_pass": result["review_output"]
        })
        prompt = result["review_output"]

        # Extract clarity rating from review output
        score = None
        if "clarity rating" in result["review_output"].lower():

            try:
                lines = result["review_output"].splitlines()
                for line in lines:
                    if "Clarity rating" in line:
                        score = int(''.join(filter(str.isdigit, line)))
                        break
            except Exception as e:
                print(f"Auto-stop check failed: {e}")

        # Stability-based auto-stop: two consecutive passes ≥ auto_stop_score
        print(f"[Debug] Current score: {score}, Previous score: {previous_score}")
        if score is not None:
            if previous_score is not None and score >= auto_stop_score and previous_score >= (auto_stop_score - 1):
                print(f"\nAuto-stop triggered at Pass {i + 1} — Stable Clarity {score}")
                return {
                    "final_prompt": prompt,
                    "history": history
                }
            previous_score = score  # Update previous score for next pass

    return {
        "final_prompt": prompt,
        "history": history
    }



if __name__ == "__main__":
    # run_agent()

    # PHASE 2 Multi-pass refinement test:
    messy_prompt = "Describe how to apply for a driver’s license."

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    phase = "Phase 2 — Multi-Pass Refinement Test"

    print("\n=== Iris Prompt Review ===")
    print(f"=== {phase} — {timestamp} ===\n")
    print("=== Original Messy Prompt (Starting Point) ===")
    print(messy_prompt + "\n")

    result = multi_pass_refine_prompt(messy_prompt, passes=5)

    for pass_data in result["history"]:
        print(f"\n=== Pass {pass_data['pass']} ===")
        print(pass_data["review_output"])

    print("\n=== Final Refined Prompt ===")
    print(result["final_prompt"])

    
