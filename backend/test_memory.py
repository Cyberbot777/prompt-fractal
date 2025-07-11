from db import SessionLocal
from models import Memory

# Dummy embedding — replace later with real embeddings
dummy_embedding = [0.1] * 1536  # Just a simple vector of 1536 dimensions

# Create DB session
db = SessionLocal()

try:
    # Insert new memory
    new_memory = Memory(
        description="Test memory with dummy embedding",
        embedding=dummy_embedding
    )
    db.add(new_memory)
    db.commit()
    db.refresh(new_memory)

    print("Memory saved with ID:", new_memory.id)

    # Query back from DB
    memory = db.query(Memory).first()
    print("Queried Memory:")
    print("ID:", memory.id)
    print("Description:", memory.description)
    print("Embedding (first 5 dims):", memory.embedding[:5])  
    
finally:
    db.close()
