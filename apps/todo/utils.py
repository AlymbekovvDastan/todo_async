from datetime import datetime

from sqlalchemy import select, desc

from apps.todo.models import todos_table, status_table
from apps.todo.schemas import TodoCreate, StatusBase
from db.database import database


async def create_todo(todo: TodoCreate, user):
    query = (
        todos_table.insert().values(
            **todo.dict(), created_at=datetime.now(),
            user_id=user['id']
        ).returning(
            todos_table.c.id,
            todos_table.c.text,
            todos_table.c.created_at,
        )
    )

    todo = await database.fetch_one(query)
    todo = dict(zip(todo, todo.values()))
    todo['user_name'] = user['name']
    return todo


async def update_todo(todo_id: int, todo: TodoCreate):
    query = (
        todos_table.update()
        .where(todos_table.c.id == todo_id)
        .values(**todo.dict())
    )
    return await database.execute(query)


async def get_todos(user):
    query = (
        select([
            todos_table.c.id,
            todos_table.c.text,
            todos_table.c.created_at,
            todos_table.c.date_to,
            todos_table.c.status_id,
            status_table.c.name.label('status'),
        ]
        )
        .where(todos_table.c.user_id == user['id'])
        .select_from(todos_table.join(status_table))
        .oredr_by(desc(todos_table.c.created_at))
    )
    return await database.fetch_all(query)


async def create_status(status: StatusBase):
    query = status_table.insert().values(**status.dict()).returning(status_table.c.id, status_table.c.name)
    return await database.fetch_one(query)


async def update_status(status_id, status: StatusBase):
    query = status_table.update().where(
        status_table.c.id == status_id
    ).values(**status.dict()).returning(status_table.c.id, status_table.c.name)
    return await database.fetch_one(query)


async def get_status():
    query = (
        select([status_table.c.id, status_table.c.name])
        .select_from(status_table)
    )
    return await database.fetch_all(query)


async def delete_status(status_id: int):
    query = status_table.delete().where(status_table.c.id == status_id)
    return await database.execute(query)
