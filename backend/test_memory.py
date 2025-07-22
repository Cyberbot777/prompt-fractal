import os
from db import SessionLocal
from models import Memory
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv(dotenv_path="./backend/.env")


client = OpenAI()

# Text to embedding
text = f"How can AI agents improve prompt optimization? Run ID {os.urandom(2).hex()}"

response = client.embeddings.create(
    input=[text],
    model="text-embedding-3-small"
)
embedding = response.data[0].embedding

# Save to DB
db = SessionLocal()
try:
    memory = Memory(
        description=text,
        embedding=embedding
    )
    db.add(memory)
    db.commit()
    db.refresh(memory)
    print("Memory saved with ID:", memory.id)

    # Query back from DB
    result = db.query(Memory).order_by(Memory.id.desc()).first()
    print("Queried Memory:")
    print("ID:", result.id)
    print("Description:", result.description)
    print("Embedding (first 5 dims):", result.embedding[:5])  
    
finally:
    db.close()
