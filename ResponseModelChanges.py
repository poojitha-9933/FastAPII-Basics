from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

# Input Model
class NoteIn(BaseModel):
    id: int
    title: str
    content: str

# Response Model
class NoteOut(BaseModel):
    id: int
    title: str

# In-memory database
fake_notes_db = []

# Create a Note
@app.post("/notes/", response_model=NoteOut, status_code=status.HTTP_201_CREATED)
def create_note(note: NoteIn):
    fake_notes_db.append(note)
    return note

# Get All Notes
@app.get("/notes/", response_model=list[NoteOut])
def get_notes():
    return fake_notes_db    