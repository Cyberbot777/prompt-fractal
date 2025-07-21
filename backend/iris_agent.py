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

# LangChain / LangSmith
from langsmith import traceable



# Debug Flag - False for clean output, True for full dev logs
DEBUG_MODE = True 

# Load environment variables and initialize OpenAI client
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))





# # Complexity Detection
# def is_complex_prompt(prompt: str) -> bool:
#     """
#     Detect whether a prompt is complex or multi-step.
#     This checks for common patterns that suggest subtasks, sequencing, or comparisons.
#     """
#     indicators = [
#         "compare and contrast",
#         "step by step",
#         "multiple steps",
#         "multiple parts",
#         "in order",
#         "1.", "2.", "3.",
#         "then", "after that", "next",
#         "list and explain",
#         "analyze and summarize"
#     ]

#     prompt_lower = prompt.lower()
#     return any(indicator in prompt_lower for indicator in indicators)



# Prompt Review
def review_and_rewrite_prompt(messy_prompt: str, memory_context: str = "") -> dict:
    """Run Iris agent to review and rewrite a prompt, optionally using memory context."""

    prompt_intro = f"\nPrompt:\n\"\"\"{messy_prompt}\"\"\"\n"

    full_prompt = ""
    if memory_context:
        full_prompt += memory_context.strip() + "\n\n"

    full_prompt += "Analyze the following prompt for clarity, length, and level of detail.\n\n"
    full_prompt += "Check specifically:\n"
    full_prompt += "1. Is this prompt too long or overly complex?\n"
    full_prompt += "2. Is this prompt too short or lacking necessary context or details?\n"
    full_prompt += "3. Are there any ambiguous or unclear phrases?\n"
    full_prompt += prompt_intro
    full_prompt += "\nProvide:\n"
    full_prompt += "- Provide a clarity rating from 1 to 10 in whole number only.\n"
    full_prompt += "- Specific issues found (exactly 3).\n"
    full_prompt += "- Suggestions for improving the prompt (exactly 3).\n"
    full_prompt += "- A fully rewritten version of the prompt that resolves the identified issues, phrased clearly and professionally.\n"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert prompt engineer."},
            {"role": "user", "content": full_prompt}
        ]
    )

    return {
        "original_prompt": messy_prompt,
        "review_output": response.choices[0].message.content.strip()
    }


# Multi Pass Refinement
@traceable(name="Multi Pass Prompt Refinement")
def multi_pass_refine_prompt(initial_prompt: str, passes: int = 5, auto_stop_score: int = 9, memory_context: str = "") -> dict:
    prompt = initial_prompt
    history = []
    previous_score = None
    best_score = None 

    for i in range(passes):
        combined_prompt = f"{memory_context.strip()}\n{prompt.strip()}" if memory_context else prompt
        result = review_and_rewrite_prompt(combined_prompt)

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

        # Update best score if applicable
        if score is not None:
            if best_score is None or score > best_score:
                best_score = score

            if previous_score is not None and score >= auto_stop_score and previous_score >= (auto_stop_score - 1):
                print(f"\nAuto-stop triggered at Pass {i + 1} — Stable Clarity {score}")
                return {
                    "final_prompt": prompt,
                    "clarity_rating": best_score,
                    "history": history
                }
            previous_score = score

    return {
        "final_prompt": prompt,
        "clarity_rating": best_score,
        "history": history
    }



# Final Prompt Saver
def save_prompt_to_memory(final_prompt: str, clarity_score: int = None) -> None:
    """Embed and store the final refined prompt in the vector DB with optional clarity score."""

    with SessionLocal() as db:
        embedding = client.embeddings.create(
            model="text-embedding-3-small",
            input=final_prompt
        ).data[0].embedding

        memory = Memory(description=final_prompt, embedding=embedding, clarity=clarity_score)
        db.add(memory)
        db.commit()

    print("Memory saved successfully:")
    print(final_prompt)
    

# Memory Context Builder
def build_memory_context(matches: list) -> str:
    """
    Build a contextual string from top-N memory matches for use in the prompt review process.
    Highlights the top (most similar) match as a high-priority prior success.
    """
    if not matches:
        return ""

    context = ["You’ve previously rewritten prompts like these:\n"]
    for i, (desc, dist, clarity) in enumerate(matches, 1):
        context.append(f'{i}. "{desc.strip()}"  (similarity: {dist:.4f}, clarity: {clarity})')

    top_match = matches[0][0].strip()
    top_score = matches[0][1]
    top_clarity = matches[0][2]
    context.append("\nMost relevant prior success (highest similarity):")
    context.append(f'"{top_match}"  (similarity: {top_score:.4f}, clarity: {top_clarity})')

    context.append("\nBased on these examples, review and rewrite the new prompt below:\n")
    return "\n".join(context)


# Top-N Memory Retrieval
def find_top_n_matches(prompt_text: str, top_n: int = 3) -> list:
    """Return the top-N most similar prompts from memory with their distances and clarity scores."""
    response = client.embeddings.create(
        input=[prompt_text],
        model="text-embedding-3-small"
    )
    embedding = Vector(response.data[0].embedding)

    db = SessionLocal()
    try:
        raw_conn = db.connection().connection
        register_vector(raw_conn.driver_connection)

        results = db.execute(
            text("""
                SELECT description, embedding <=> :embedding AS distance, clarity
                FROM memories
                ORDER BY distance
                LIMIT :top_n;
            """),
            {"embedding": embedding, "top_n": top_n}
        ).fetchall()

        return [(row.description, row.distance, row.clarity) for row in results]

    finally:
        db.close()

# if __name__ == "__main__":
#     test_prompts = [
#         "What is the difference between classification and regression?",
#         "Compare and contrast Bitcoin and Ethereum in terms of consensus mechanism, smart contract capability, and real-world usage. Then recommend use cases for each.",
#         "Explain how to fine-tune a model using LoRA. List steps in order and give one example at each stage.",
#         "Write a fun sci-fi story prompt for a solo RPG game."
#     ]

#     print("\n=== Complexity Detection Test ===")
#     for p in test_prompts:
#         is_complex = is_complex_prompt(p)
#         print(f"\nPrompt:\n{p}\n→ Complex: {is_complex}")




# Entry Point — Memory-Aware Agent with Top-N Recall
if __name__ == "__main__":
    test_prompt = "I want to be come a movie star. How do I get there if no degree?"

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    print("\n=== Iris Prompt Review (Memory-Aware Mode) ===")
    print(f"=== {timestamp} ===\n")
    print("Test Prompt:")
    print(test_prompt)

    print("\n=== Retrieving Top-N Memory Matches ===")
    matches = find_top_n_matches(test_prompt, top_n=3)

    memory_context = ""
    if matches and matches[0][1] < 0.2 and matches[0][2] == 10:
        memory_context = build_memory_context(matches)
        if DEBUG_MODE:
            print("\n=== Memory Context ===")
            print(memory_context)
    else:
        print("Memory matches not close enough — skipping memory context.")

    print("\n=== Running Refinement ===")
    result = multi_pass_refine_prompt(test_prompt, passes=5, memory_context=memory_context)

    print("\n=== Final Refined Prompt ===")
    print(result["final_prompt"])

    final_clean_prompt = extract_final_prompt(result["final_prompt"])
    save_prompt_to_memory(final_clean_prompt, clarity_score=result["clarity_rating"])