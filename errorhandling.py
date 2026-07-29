from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class Note(BaseModel):
    id: int
    title: str
    content: str

fake_notes_db = []

@app.post("/notes/", status_code=status.HTTP_201_CREATED)
def add_note(note: Note):
    for n in fake_notes_db:
        if n.id == note.id:
            raise HTTPException(
                status_code=400,
                detail="A note with this ID already exists."
            )

    fake_notes_db.append(note)
    return {
        "message": "Note added successfully",
        "note": note
    }

@app.get("/notes/")
def get_notes():
    if not fake_notes_db:
        raise HTTPException(
            status_code=404,
            detail="No notes available."
        )

    return fake_notes_db

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    for note in fake_notes_db:
        if note.id == note_id:
            return note

    raise HTTPException(
        status_code=404,
        detail=f"Note with ID {note_id} not found."
    )

@app.put("/notes/{note_id}")
def update_note(note_id: int, updated_note: Note):
    for index, note in enumerate(fake_notes_db):
        if note.id == note_id:
            fake_notes_db[index] = updated_note
            return {
                "message": "Note updated successfully",
                "note": updated_note
            }

    raise HTTPException(
        status_code=404,
        detail=f"Cannot update. Note with ID {note_id} not found."
    )

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    for note in fake_notes_db:
        if note.id == note_id:
            fake_notes_db.remove(note)
            return {
                "message": "Note deleted successfully."
            }

    raise HTTPException(
        status_code=404,
        detail=f"Cannot delete. Note with ID {note_id} not found."
    )