from fastapi import APIRouter, status, Depends
from typing import List
from apps.todo.schemas import Status, StatusBase, Todo, TodoCreate
from apps.todo import utils
from apps.user.dependecies import get_current_user
from apps.user.schemas import User

router = APIRouter()


@router.get('/status', response_model=List[Status])
async def get_status_list():
    return await utils.get_status()


@router.post('/status/create', response_model=Status, status_code=status.HTTP_201_CREATED)
async def create_status(status_data: StatusBase):
    return await utils.create_status(status_data)


@router.put('status/update/{status_id}', response_model=Status)
async def update_status(status_id: int, status_data: StatusBase):
    return await utils.update_status(status_id, status_data)


@router.delete('status/delete/{status_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_status(status_id: int):
    return await utils.delete_status(status_id)


@router.get('/', response_model=List[Todo])
async def get_todo_list(current_user: User = Depends(get_current_user)):
    return await utils.get_todos(current_user)


@router.post('/create', response_model=TodoCreate)
async def create_todo(todo_data: TodoCreate, current_user: User = Depends(get_current_user)):
    return await utils.create_todo(todo_data, current_user)


@router.put('/update/{todo_id}', response_model=TodoCreate)
async def update_todo(todo_id: int, todo_data: TodoCreate, current_user: User = Depends(get_current_user)):
    return await utils.update_todo(todo_id, todo_data)


@router.delete('/delete/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int, current_user: User = Depends(get_current_user)):
    return await utils.delete_todo(todo_id)