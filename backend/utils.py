# utils.py
def extract_final_prompt(text: str) -> str:
    if "Rewritten prompt:" in text:
        return text.split("Rewritten prompt:")[-1].strip().strip('"')
    elif "Fully rewritten prompt:" in text:
        return text.split("Fully rewritten prompt:")[-1].strip().strip('"')
    else:
        return text.strip().strip('"')
