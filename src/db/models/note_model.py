from .base_model import Base, bool_false, intpk, text

from sqlalchemy.orm import Mapped


class Note(Base):
    __tablename__ = "note"

    id: Mapped[intpk]
    text: Mapped[text]
    done: Mapped[bool_false]
