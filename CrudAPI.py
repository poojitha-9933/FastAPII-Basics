from fastapi import FastAPI, HTTPException

app = FastAPI()

notes = [
    {"id": 1, "title": "Python", "content": "Learn FastAPI"},
    {"id": 2, "title": "SQL", "content": "Learn SQLAlchemy"}
]

@app.put("/notes/{note_id}")
def update_note(note_id: int, updated_note: dict):
    for note in notes:
        if note["id"] == note_id:
            note["title"] = updated_note["title"]
            note["content"] = updated_note["content"]
            return {
                "message": "Note updated successfully",
                "note": note
            }

    raise HTTPException(status_code=404, detail="Note not found")


@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            return {"message": "Note deleted successfully"}

    raise HTTPException(status_code=404, detail="Note not found")

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found")