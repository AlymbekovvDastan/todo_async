from datetime import datetime

from pydantic import BaseModel


class TodoBase(BaseModel):
    text: str


class TodoCreate(TodoBase):
    status_id: int
    date_to: datetime


class Todo(TodoCreate):
    id: int
    created_at: datetime
