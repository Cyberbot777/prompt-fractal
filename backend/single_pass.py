# === Phase 1 — Single Pass ===
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