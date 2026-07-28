from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

# ------------------ User Model ------------------

class User(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    email: EmailStr
    password: str = Field(min_length=8, max_length=20)

# ------------------ Note Model ------------------

class Note(BaseModel):
    id: int
    title: str = Field(min_length=3, max_length=50)
    content: str = Field(min_length=10, max_length=200)

# In-memory databases
users = []
notes = []

# ------------------ User API ------------------

@app.post("/register")
def register(user: User):
    users.append(user)
    return {
        "message": "User registered successfully",
        "username": user.username,
        "email": user.email
    }

# ------------------ Notes API ------------------

@app.post("/notes/")
def create_note(note: Note):
    notes.append(note)
    return {
        "message": "Note added successfully",
        "note": note
    }

@app.get("/notes/")
def get_notes():
    return notes