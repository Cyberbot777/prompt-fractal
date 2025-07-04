# iris_agent.py 

import os
from dotenv import load_dotenv
from openai import OpenAI

def run_agent():
    print("Iris Agent Starting...")

    # Load API key from .env
    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Send a simple test prompt to GPT-3.5 Turbo (new API)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Summarize the phrase 'Prompt Fractal' in one sentence."}
        ]
    )

    reply = response.choices[0].message.content.strip()
    print("LLM Response:", reply)

if __name__ == "__main__":
    run_agent()
