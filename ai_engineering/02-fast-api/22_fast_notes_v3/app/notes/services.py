from app.db.config import async_session
from app.notes.models import Note
from sqlalchemy import select
from fastapi import HTTPException
from app.notes.schemas import NoteCreate, NoteDeleteResponse, NoteUpdate, NotePartialUpdate, NoteResponse
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession


# Create Note
async def create_note(session: AsyncSession, new_note: NoteCreate) -> NoteResponse:
    note = Note(title=new_note.title, content=new_note.content)
    session.add(note)
    await session.commit()
    await session.refresh(note)
    return note


# Get Note by ID
async def get_note_by_id(session: AsyncSession, note_id: int) -> NoteResponse:
    note = await session.get(Note, note_id)

    if note is None:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    return note


# Get All Notes
async def get_all_notes(session: AsyncSession) -> List[NoteResponse]:
    stmt = select(Note)
    notes = await session.scalars(stmt)
    return [note for note in notes.all()]



# Update Note
async def update_note(session: AsyncSession, note_id: int, updated_note: NoteUpdate) -> NoteResponse:
    note = await session.get(Note, note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    note.title = updated_note.title
    note.content = updated_note.content
    await session.commit()
    await session.refresh(note)
    return note


# Partial Update Note
async def partial_update_note(session: AsyncSession, note_id: int, updated_fields: NotePartialUpdate) -> NoteResponse:
    note = await session.get(Note, note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    if updated_fields.title is not None:
            note.title = updated_fields.title
    if updated_fields.content is not None:
            note.content = updated_fields.content
    await session.commit()
    await session.refresh(note)
    return note


# Delete Note
async def delete_note(session: AsyncSession, note_id: int):
    note = await session.get(Note, note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    await session.delete(note)
    await session.commit()
    return {"message": "Note deleted successfully"}
