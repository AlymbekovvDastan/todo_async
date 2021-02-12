from datetime import datetime

from pydantic import BaseModel


class TodoBase(BaseModel):
    text: str


class TodoCreate(TodoBase):
    status_id: int
    date_to: datetime

    class Config:
        orm_mode = True


class Todo(BaseModel):
    id: int
    text: str
    date_to: datetime
    created_at: datetime
    status: str


class StatusBase(BaseModel):
    name: str


class Status(StatusBase):
    id: int
