from fastapi import FastAPI, HTTPException, status, UploadFile, File, Form

app = FastAPI()

fake_notes_db = []

@app.post("/notes/", status_code=status.HTTP_201_CREATED)
async def add_note(
    id: int = Form(...),
    title: str = Form(...),
    content: str = Form(...),
    attachment: UploadFile = File(...)
):

    for note in fake_notes_db:
        if note["id"] == id:
            raise HTTPException(
                status_code=400,
                detail="A note with this ID already exists."
            )

    file_data = await attachment.read()

    new_note = {
        "id": id,
        "title": title,
        "content": content,
        "filename": attachment.filename,
        "file_type": attachment.content_type,
        "file_size": len(file_data)
    }

    fake_notes_db.append(new_note)

    return {
        "message": "Note added successfully.",
        "note": new_note
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
        if note["id"] == note_id:
            return note

    raise HTTPException(
        status_code=404,
        detail="Note not found."
    )


@app.put("/notes/{note_id}")
def update_note(
    note_id: int,
    title: str = Form(...),
    content: str = Form(...)
):

    for note in fake_notes_db:
        if note["id"] == note_id:
            note["title"] = title
            note["content"] = content

            return {
                "message": "Note updated successfully.",
                "note": note
            }

    raise HTTPException(
        status_code=404,
        detail="Cannot update. Note not found."
    )


@app.delete("/notes/{note_id}")
def delete_note(note_id: int):

    for note in fake_notes_db:
        if note["id"] == note_id:
            fake_notes_db.remove(note)
            return {
                "message": "Note deleted successfully."
            }

    raise HTTPException(
        status_code=404,
        detail="Cannot delete. Note not found."
    )