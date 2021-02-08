from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from apps.user.dependecies import get_current_user
from apps.user.schemas import User, UserCreate, TokenBase, UserBase
from apps.user.utils import get_user_by_email, create_user, verify_password, create_token

router = APIRouter()


@router.post('/sign-up', response_model=User)
async def sign_up(user: UserCreate):
    db_user = await get_user_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail='Email already registered')
    return await create_user(user=user)


@router.post('/auth', response_model=TokenBase)
async def auth(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await get_user_by_email(email=form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail='Неправильный адрес электронной почты или пароль')
    if not verify_password(form_data.password, user['password']):
        raise HTTPException(status_code=400, detail='Непрвавильный адрес или электронной пчты или пароль')
    return await create_token(user['id'])


@router.get('/me', response_model=UserBase)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
