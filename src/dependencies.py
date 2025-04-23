from typing import Type, TypeVar

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_session
from src.services import (
    NoteService,
)

# Для определения типа по мере выполнения.
T = TypeVar("T")


class ServiceDBFactory:
    """Сервис-фабрика с прокидыванием сессии БД."""

    def __init__(self, service_class: Type[T]):
        """Инициируем фабрику с сервисом на вход."""
        self.service_class = service_class

    async def __call__(
        self,
        session: AsyncSession = Depends(get_session),
    ) -> T:
        """Объявление зависимостей - БД."""
        return self.service_class(session)


note_service = ServiceDBFactory(NoteService)
