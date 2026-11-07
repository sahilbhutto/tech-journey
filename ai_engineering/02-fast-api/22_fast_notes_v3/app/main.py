from fastapi import FastAPI, Depends
from app.notes import services as notes_services
from app.notes.schemas import NoteCreate, NoteUpdate, NotePartialUpdate, NoteResponse, NoteDeleteResponse
from typing import List
from app.db.config import SessionDependency, get_db

app = FastAPI(title ="Fast Notes API", version="1.0.0")


# Create Note
@app.post("/notes", response_model=NoteResponse, status_code=201)
async def note_create(session: SessionDependency, new_note: NoteCreate):
    note = await notes_services.create_note(session, new_note)
    return note


# Read Note by ID
@app.get("/notes/{note_id}", response_model=NoteResponse, status_code=200)
async def note_get(session: SessionDependency, note_id: int):
    note = await notes_services.get_note_by_id(session, note_id)
    return note


# Read All Notes
@app.get("/notes", response_model= List[NoteResponse], status_code=200)
async def note_get_all(session: SessionDependency):
    notes = await notes_services.get_all_notes(session)
    return notes


# Update Note
@app.put("/notes/{note_id}", response_model=NoteResponse, status_code=200)
async def note_update(session: SessionDependency, note_id: int, updated_note: NoteUpdate):
    note = await notes_services.update_note(session, note_id, updated_note)
    return note


# Partial Update Note
@app.patch("/notes/{note_id}", response_model=NoteResponse, status_code=200)
async def note_patch(session: SessionDependency, note_id: int, updated_fields: NotePartialUpdate):
    note = await notes_services.partial_update_note(session, note_id, updated_fields)
    return note


# Delete Note
@app.delete("/notes/{note_id}", response_model=NoteDeleteResponse, status_code=200)
async def note_delete(session: SessionDependency, note_id: int):
    response = await notes_services.delete_note(session, note_id)
    return response
