from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, UUID4, Field, validator


class UserCreate(BaseModel):
    """ Проверяет sign-up запросы """
    email: EmailStr
    name: str
    password: str


class UserBase(BaseModel):
    """ Формирует тело ответа деталями пользувателя """
    id: int
    email: EmailStr
    name: str


class TokenBase(BaseModel):
    token: UUID4 = Field(..., alias="access_token")
    expires: datetime
    token_type: Optional[str] = "bearer"

    class Config:
        allow_population_by_field_name = True

    @validator("token")
    def hexlify_token(cls, value):
        """Конвертирует UUID в hex строку"""
        return value.hex


class User(UserBase):
    """Формирует тело ответа с деталями пользувателя и токеном"""
    token: TokenBase = {}
