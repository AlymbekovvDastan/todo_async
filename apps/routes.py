from fastapi import APIRouter
from apps.todo import todo
from apps.user import user

routes = APIRouter()

routes.include_router(todo.router, prefix='/todo', tags=['Todo'])
routes.include_router(user.router, prefix='/users', tags=['Users'])