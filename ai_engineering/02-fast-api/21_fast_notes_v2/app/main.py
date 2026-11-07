from fastapi import FastAPI
from app.notes import services as notes_services
from app.notes.schemas import NoteCreate, NoteUpdate, NotePartialUpdate, NoteResponse, NoteDeleteResponse
from typing import List

app = FastAPI(title ="Fast Notes API", version="1.0.0")


# Create Note
@app.post("/notes", response_model=NoteResponse, status_code=201)
async def note_create(new_note: NoteCreate):
    note = await notes_services.create_note(new_note)
    return note


# Read Note by ID
@app.get("/notes/{note_id}", response_model=NoteResponse, status_code=200)
async def note_get(note_id: int):
    note = await notes_services.get_note_by_id(note_id)
    return note


# Read All Notes
@app.get("/notes", response_model= List[NoteResponse], status_code=200)
async def note_get_all():
    notes = await notes_services.get_all_notes()
    return notes


# Update Note
@app.put("/notes/{note_id}", response_model=NoteResponse, status_code=200)
async def note_update(note_id: int, updated_note: NoteUpdate):
    note = await notes_services.update_note(note_id, updated_note)
    return note


# Partial Update Note
@app.patch("/notes/{note_id}", response_model=NoteResponse, status_code=200)
async def note_patch(note_id: int, updated_fields: NotePartialUpdate):
    note = await notes_services.partial_update_note(note_id, updated_fields)
    return note


# Delete Note
@app.delete("/notes/{note_id}", response_model=NoteDeleteResponse, status_code=200)
async def note_delete(note_id: int):
    response = await notes_services.delete_note(note_id)
    return response
