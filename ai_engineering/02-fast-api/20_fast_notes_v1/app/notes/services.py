from app.db.config import async_session
from app.notes.models import Note
from sqlalchemy import select
from fastapi import HTTPException


async def create_note(title: str, content: str) :
    async with async_session() as session:
        note = Note(title=title, content=content)
        session.add(note)
        await session.commit()
        await session.refresh(note)
        return note


async def get_note_by_id(note_id: int):
    async with async_session() as session:
        note = await session.get(Note, note_id)

        if note is None:
            raise HTTPException(
                status_code=404,
                detail="Note not found"
            )

        return note


async def get_all_notes():
    async with async_session() as session:
        stmt = select(Note)
        notes = await session.scalars(stmt)
        return notes.all()


async def update_note(note_id: int, title: str, content: str):
    async with async_session() as session:
        note = await session.get(Note, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        note.title = title
        note.content = content
        await session.commit()
        await session.refresh(note)
        return note


async def partial_update_note(note_id: int, title: str = None, content: str = None):
    async with async_session() as session:
        note = await session.get(Note, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        if title is not None:
            note.title = title
        if content is not None:
            note.content = content
        await session.commit()
        await session.refresh(note)
        return note


async def delete_note(note_id: int):
    async with async_session() as session:
        note = await session.get(Note, note_id)
        if note is None:
            raise HTTPException(status_code=404, detail="Note not found")
        await session.delete(note)
        await session.commit()
        return {"message": "Note deleted successfully"}
