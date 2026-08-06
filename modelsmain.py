from fastapi import FastAPI
from Databaseconfigurationfiles import engine, Base
import models

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Primary keys and required fields added successfully!"}