from fastapi import APIRouter, status
from typing import List
from apps.todo.schemas import Status, StatusBase
from apps.todo import utils
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

