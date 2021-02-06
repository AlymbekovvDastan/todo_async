from datetime import datetime, timedelta
from passlib.context import CryptContext
from sqlalchemy import and_

from apps.user.schemas import UserCreate
from db.database import database
from apps.user.models import users_table, tokens_table

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def get_user_by_email(email: str):
    """Возвращает информацию о пользователе"""
    query = users_table.select().where(users_table.c.email == email)
    return await database.fetch_one(query)


async def get_user_by_token(token: str):
    """Возвращает информацию о владельце указанного токена"""
    query = tokens_table.join(users_table).select().where(
        and_(
            tokens_table.c.token == token,
            tokens_table.c.expires > datetime.now()
        )
    )
    return await database.fetch_one(query)


async def create_token(user_id: int):
    """ Создать токен для роользувателя с  указанным user_id"""
    query = (
        tokens_table.insert().values(
            expires=datetime.now() + timedelta(weeks=2), user_id=user_id
        ).returning(tokens_table.c.token, tokens_table.c.expires)
    )

    return await database.fetch_one(query)


async def create_user(user: UserCreate):
    """ Создает нового пользувателя в БД"""
    hashed_password = get_password_hash(user.password)
    query = users_table.insert().values(
        email=user.email, name=user.name, password=hashed_password
    )
    user_id = await database.execute(query)
    token = await create_token(user_id)
    token_dict = {'token': token['token'], 'expires': token['expires']}
    return {**user.dict(), 'id': user_id, 'is_active': True, 'token': token_dict}