from fastapi import FastAPI
from app.notes import services as notes_services

app = FastAPI(title ="Fast Notes API", version="1.0.0")


@app.post("/notes")
async def note_create(new_note: dict):
    note = await notes_services.create_note(new_note["title"], new_note["content"])
    return note

@app.get("/notes/{note_id}")
async def note_get(note_id: int):
    note = await notes_services.get_note_by_id(note_id)
    return note

@app.get("/notes")
async def note_get_all():
    notes = await notes_services.get_all_notes()
    return notes

@app.put("/notes/{note_id}")
async def note_update(note_id: int, updated_note: dict):
    new_title = updated_note.get("title")
    new_content = updated_note.get("content")
    note = await notes_services.update_note(note_id, new_title, new_content)
    return note

@app.patch("/notes/{note_id}")
async def note_patch(note_id: int, updated_fields: dict):
    new_title = updated_fields.get("title")
    new_content = updated_fields.get("content")
    note = await notes_services.partial_update_note(note_id, new_title, new_content)
    return note

@app.delete("/notes/{note_id}")
async def note_delete(note_id: int):
    response = await notes_services.delete_note(note_id)
    return response
