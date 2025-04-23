from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models import Note
from src.schemas import NoteSchema


async def get_all_notes(session: AsyncSession):
    stmt = select(Note)

    result = await session.scalars(stmt)

    return list(result)


async def get_note(session: AsyncSession, id: int):
    stmt = select(Note).where(Note.id == id)

    result = await session.scalar(stmt)

    return result


async def add_note(session: AsyncSession, schema: NoteSchema):
    note = Note(
        text=schema.text
    )

    session.add(note)

    await session.commit()

    return note


async def edit_note(session: AsyncSession, note: Note, schema: NoteSchema):
    note.text = schema.text

    await session.commit()

    return note


async def mark_as_done(session: AsyncSession, note: Note):
    note.done = True

    await session.commit()

    return note


async def delete_note(session: AsyncSession, note: Note):
    await session.delete(note)
    await session.commit()

    return note
