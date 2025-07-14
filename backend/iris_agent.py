# iris_agent.py — Iris (with DEBUG_MODE)
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
import psycopg

# Final Prompt Util
from utils import extract_final_prompt

# === Debug Flag ===
DEBUG_MODE = False  # Set to False for clean output, True for full dev logs

# Load environment variables and initialize OpenAI client
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# === Prompt Review ===
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

# === Multi Pass Refinement ===
def multi_pass_refine_prompt(initial_prompt: str, passes: int = 5, auto_stop_score: int = 9) -> dict:
    prompt = initial_prompt
    history = []
    previous_score = None

    for i in range(passes):
        result = review_and_rewrite_prompt(prompt)
        output = result["review_output"]
        prompt = output

        score = None
        try:
            lines = output.splitlines()
            for line in lines:
                if "clarity" in line.lower() and ("rating" in line.lower() or "score" in line.lower()):
                    clean_line = line.replace("**", "").replace(":", "").strip()
                    digits = [int(s) for s in clean_line.split() if s.isdigit()]
                    if digits:
                        score = digits[0]
                        break
        except Exception as e:
            if DEBUG_MODE:
                print(f"[Debug] Auto-stop check failed: {e}")

        if DEBUG_MODE:
            print(f"\n=== Pass {i + 1} ===")
            print(output)
            print(f"[Debug] Current score: {score}, Previous score: {previous_score}")

        history.append({
            "pass": i + 1,
            "review_output": output,
            "score": score
        })

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

# === Memory Save ===
def save_prompt_to_memory(prompt_text: str):
    """Save only the final rewritten prompt to the vector memory DB."""
    final_prompt = extract_final_prompt(prompt_text)

    if DEBUG_MODE:
        print(f"[Debug] Extracted prompt:\n{final_prompt}")

    response = client.embeddings.create(
        input=[final_prompt],
        model="text-embedding-3-small"
    )
    embedding = response.data[0].embedding

    db = SessionLocal()
    try:
        memory = Memory(description=final_prompt, embedding=embedding)
        db.add(memory)
        db.commit()
        print(f"Memory saved successfully:\n{final_prompt}")
    finally:
        db.close()

# === Memory Similarity Recall ===
def find_similar_prompt(prompt_text: str, similarity_threshold: float = 0.2):
    response = client.embeddings.create(
        input=[prompt_text],
        model="text-embedding-3-small"
    )
    embedding = Vector(response.data[0].embedding)

    db = SessionLocal()
    try:
        raw_conn = db.connection().connection
        register_vector(raw_conn.driver_connection)

        result = db.execute(
            text("""
                SELECT id, description, embedding <=> :embedding AS distance
                FROM memories
                ORDER BY distance
                LIMIT 1;
            """),
            {"embedding": embedding}
        ).fetchone()

        if result:
            print(f"[Debug] Result row: {dict(result._mapping)}")
            print(f"[Similarity Score] Distance: {result.distance}")
            if result.distance <= similarity_threshold:
                print(f"Found similar prompt:\n{result.description}")
                return result.description
            else:
                print("Prompt exists, but similarity score is too low.")
                return None
        else:
            print("No similar prompt found.")
            return None

    finally:
        db.close()

# === Entry Point — Memory-First Agent ===
if __name__ == "__main__":
    test_prompt = "Why is the sky blue?"

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    print("\n=== Iris Prompt Review (Memory-Aware Mode) ===")
    print(f"=== {timestamp} ===\n")
    print("Test Prompt:")
    print(test_prompt)

    print("\n=== Checking Memory First ===")
    memory_match = find_similar_prompt(test_prompt, similarity_threshold=0.2)

    if memory_match:
        print("\nIris recalled a similar prompt — skipping refinement.")
        print(f"Recalled Prompt:\n{memory_match}")
    else:
        print("\nNo good memory match found — running refinement.")
        result = multi_pass_refine_prompt(test_prompt, passes=5)
        print("\n=== Final Refined Prompt ===")
        print(result["final_prompt"])
        save_prompt_to_memory(result["final_prompt"])
