from typing import Annotated

import uvicorn

from fastapi import Depends, FastAPI

from src.dependencies import note_service
from src.schemas import NotFoundExceptionSchema, NoteSchema, SingleNoteResponse
from src.services import NoteService


app = FastAPI()


@app.get(
    "/",
    summary="Получить список всех заметок",
    description="Возвращает все заметки из БД",
    tags=["Notes"],
    response_description="Список всех заметок в БД",
    response_model=list[SingleNoteResponse],
)
async def get_all_notes(service: Annotated[NoteService, Depends(note_service)]):
    return await service.get_all_notes()


@app.get(
    "/{id}",
    summary="Получить заметку",
    description="Возвращает заметку с переданным в query-параметре id",
    tags=["Notes"],
    response_description="Заметка с указанным id",
    response_model=SingleNoteResponse,
    responses={
        404: {"model": NotFoundExceptionSchema, "description": "Заметка не найдена"}
    }
)
async def get_note(id: int, service: Annotated[NoteService, Depends(note_service)]):
    return await service.get_note(id=id)


@app.post(
    "/",
    summary="Добавить новую заметку в БД",
    description="Добавляет новую заметку с указанным в теле запроса текстом. Созданные заметки по умолчанию считаются 'невыполненными'",
    tags=["Notes"],
    response_description="Созданная заметка",
    response_model=SingleNoteResponse,
)
async def add_note(schema: NoteSchema, service: Annotated[NoteService, Depends(note_service)]):
    return await service.add_note(schema=schema)


@app.patch(
    "/{id}",
    summary="Изменить текст заметки",
    description="Изменяет текст существующей заметки. При отсутствии заметки с указанным id возвращает 404",
    tags=["Notes"],
    response_description="Изменённая заметка",
    response_model=SingleNoteResponse,
    responses={
        404: {"model": NotFoundExceptionSchema, "description": "Заметка не найдена"}
    }
)
async def edit_note(schema: NoteSchema, id: int, service: Annotated[NoteService, Depends(note_service)]):
    return await service.edit_note(id=id, schema=schema)


@app.post(
    "/{id}",
    summary="Пометить заметку как выполненную",
    description="Помечает заметку с указанным id как выполненную. При отсутствии заметки возвращает 404",
    tags=["Notes"],
    response_description="Изменённая заметка",
    response_model=SingleNoteResponse,
    responses={
        404: {"model": NotFoundExceptionSchema, "description": "Заметка не найдена"}
    }
)
async def mark_note_as_done(id: int, service: Annotated[NoteService, Depends(note_service)]):
    return await service.mark_as_done(id=id)


@app.delete(
    "/{id}",
    summary="Удалить заметку",
    description="Удаляет из БД заметку с указанным id. При отсутствии таковой возвращает 404",
    tags=["Notes"],
    response_description="Удалённая заметка",
    response_model=SingleNoteResponse,
    responses={
        404: {"model": NotFoundExceptionSchema, "description": "Заметка не найдена"}
    }
)
async def delete_note(id: int, service: Annotated[NoteService, Depends(note_service)]):
    return await service.delete_note(id=id)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
