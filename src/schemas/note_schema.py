from pydantic import BaseModel


class NoteSchema(BaseModel):
    text: str


class SingleNoteResponse(BaseModel):
    id: int
    text: str
    done: bool
