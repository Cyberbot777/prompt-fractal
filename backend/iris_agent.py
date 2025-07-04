# iris_agent.py — Iris Prompt Review Test (Phase 1)
import os
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime

def run_agent():
    print("Iris Agent Starting...")

    # Load API key
    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Hardcoded messy prompt to analyze
    messy_prompt = (
    "Explain how to get are carrer as a lwayer but like go deep but also make it simple but not too simple and also give examples and maybe something else too idk."
    )

    # Review meta-prompt template
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

    # Send review task to LLM
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert prompt engineer."},
            {"role": "user", "content": review_template}
        ]
    )

    review_output = response.choices[0].message.content.strip()

    # Prepare timestamp and phase label
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    phase = "Phase 1 — Review Test"

    # Print results in clean order
    print("\n=== Iris Prompt Review ===")
    print(f"=== {phase} — {timestamp} ===\n")
    print(f"Original Prompt:\n{messy_prompt}\n")
    print("Review Output:")
    print(review_output)


if __name__ == "__main__":
    run_agent()
