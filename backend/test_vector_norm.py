import openai
import numpy as np
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Grab API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.embeddings.create(
    input=["Test string for embedding"],
    model="text-embedding-3-small"
)

vec = response.data[0].embedding
norm = np.linalg.norm(vec)

print("Vector norm:", norm)
