from fastapi import FastAPI
from Databaseconfigurationfiles import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "message": "Database connected successfully!"
    }
