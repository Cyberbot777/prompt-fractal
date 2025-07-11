from sqlalchemy import Column, Integer, String
from pgvector.sqlalchemy import Vector
from db import Base

class Memory(Base):
    __tablename__ = "memories"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    embedding = Column(Vector(1536))  # Adjust dimension if needed

