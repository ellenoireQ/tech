import jwt
from pydantic import BaseModel
from typing import Annotated
from datetime import datetime, timedelta, timezone
from app.schemas.user import UserLogin
from app.core.config import settings


# Token Base Model
class Token(BaseModel):
    access_token: str
    token_type: str


# create_access_token
# Description:
# Creating encoded JWT Token
#
# example:
# create_access_token(data={"sub": email}, expires_delta=timedelta(minutes=x))
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt
