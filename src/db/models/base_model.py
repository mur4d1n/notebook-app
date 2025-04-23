from typing import Annotated

from sqlalchemy import Boolean, Integer, Text
from sqlalchemy.orm import DeclarativeBase, mapped_column

bool_false = Annotated[bool, mapped_column(default=False)]
intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
text = Annotated[str, mapped_column(Text)]


class Base(DeclarativeBase):
    """Базовый класс моделей."""

    type_annotation_map = {
        bool_false: Boolean,
        intpk: Integer,
        text: Text,
    }
