# iris_agent.py — Iris
import os
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime
from sqlalchemy import text

# Database imports for vector memory
from db import SessionLocal
from models import Memory

# pgvector wrapper and adapter
from pgvector import Vector
from pgvector.psycopg import register_vector

# Load environment variables and initialize OpenAI client
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
- Provide a clarity rating from 1 to 10 in whole number only.
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

    # Single Prompt Pass
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

def multi_pass_refine_prompt(initial_prompt: str, passes: int = 5, auto_stop_score: int = 9) -> dict:
    """Runs Iris agent recursively to refine a prompt with stability-based auto-stop."""
    prompt = initial_prompt
    history = []
    previous_score = None

    for i in range(passes):
        result = review_and_rewrite_prompt(prompt)
        history.append({
            "pass": i + 1,
            "review_output": result["review_output"],
            "prompt_after_pass": result["review_output"]
        })
        prompt = result["review_output"]

        score = None
        try:
            lines = result["review_output"].splitlines()
            for line in lines:
                if "clarity" in line.lower() and ("rating" in line.lower() or "score" in line.lower()):
                    clean_line = line.replace("**", "").replace(":", "").strip()
                    digits = [int(s) for s in clean_line.split() if s.isdigit()]
                    if digits:
                        score = digits[0]
                        break
        except Exception as e:
            print(f"Auto-stop check failed: {e}")

        print(f"[Debug] Current score: {score}, Previous score: {previous_score}")
        if score is not None:
            if previous_score is not None and score >= auto_stop_score and previous_score >= (auto_stop_score - 1):
                print(f"\nAuto-stop triggered at Pass {i + 1} — Stable Clarity {score}")
                return {
                    "final_prompt": prompt,
                    "history": history
                }
            previous_score = score

    return {
        "final_prompt": prompt,
        "history": history
    }

def save_prompt_to_memory(prompt_text: str):
    """Save a prompt and its embedding to the vector memory DB."""
    response = client.embeddings.create(
        input=[prompt_text],
        model="text-embedding-3-small"
    )
    embedding = response.data[0].embedding

    db = SessionLocal()
    try:
        memory = Memory(description=prompt_text, embedding=embedding)
        db.add(memory)
        db.commit()
        print("Memory saved successfully.")
    finally:
        db.close()

def find_similar_prompt(prompt_text: str, similarity_threshold: float = 0.2):
    """Find the most similar prompt from memory using vector similarity."""
    response = client.embeddings.create(
        input=[prompt_text],
        model="text-embedding-3-small"
    )
    embedding = Vector(response.data[0].embedding)

    db = SessionLocal()
    try:
        # ✅ Register the pgvector adapter on this live connection
        register_vector(db.connection().connection)

        result = db.execute(
            text("""
                SELECT id, description, embedding <=> :embedding AS distance
                FROM memories
                ORDER BY distance
                LIMIT 1;
            """),
            {"embedding": embedding}
        ).fetchone()

        if result and result.distance <= similarity_threshold:
            print(f"Found similar prompt (Distance: {result.distance}):\n{result.description}")
            return result.description
        else:
            print("No similar prompt found (or not similar enough).")
            return None

    finally:
        db.close()

if __name__ == "__main__":
    # run_agent()

    messy_prompt = "How can teams work better together?"
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

    save_prompt_to_memory(result["final_prompt"])

    test_prompt = "How can team members in a technology development project enhance their communication and coordination strategies?"
    find_similar_prompt(test_prompt, similarity_threshold=0.2)
