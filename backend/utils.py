# utils.py

def extract_final_prompt(text: str) -> str:
    """Extract only the rewritten prompt from review output."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip().lower().startswith("rewritten prompt:"):
            # Collect lines after "Rewritten Prompt:" until empty line or next section
            prompt_lines = []
            for j in range(i + 1, len(lines)):
                line = lines[j].strip()
                if not line or line.lower().startswith(("clarity rating:", "specific issues:")):
                    break
                prompt_lines.append(line)
            prompt = " ".join(prompt_lines).strip().strip('"')
            if prompt:
                return prompt
    # Fallback: Look for quoted prompt
    for line in lines:
        if line.strip().startswith('"') and line.strip().endswith('"'):
            return line.strip().strip('"')
    raise ValueError("Could not extract rewritten prompt from text")