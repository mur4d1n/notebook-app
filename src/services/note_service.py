from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.repository.note_crud import (
    get_all_notes,
    get_note,
    add_note,
    edit_note,
    mark_as_done,
    delete_note,
)
from src.schemas import NoteSchema


class NoteService:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_all_notes(self):
        return await get_all_notes(session=self._session)

    async def get_note(self, id: int):
        note = await get_note(session=self._session, id=id)

        if note is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Entity not found",
            )

        return note

    async def add_note(self, schema: NoteSchema):
        return await add_note(session=self._session, schema=schema)

    async def edit_note(self, schema: NoteSchema, id: int):
        note = await self.get_note(id=id)

        return await edit_note(session=self._session, note=note, schema=schema)

    async def mark_as_done(self, id: int):
        note = await self.get_note(id=id)

        return await mark_as_done(session=self._session, note=note)

    async def delete_note(self, id: int):
        note = await self.get_note(id=id)

        return await delete_note(session=self._session, note=note)
