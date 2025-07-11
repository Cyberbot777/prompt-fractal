from db import engine, Base
import models

# Create tables in DB (runs CREATE TABLE if missing)
Base.metadata.create_all(bind=engine)

print("Database tables created.")
