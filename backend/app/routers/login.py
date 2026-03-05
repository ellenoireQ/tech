from app.utils.jwt import Token
from datetime import timedelta

from app.utils.jwt import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from app.utils.validate_user import validate_user
from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserLogin

router = APIRouter()

# 
@router.post("", response_model=Token)
def login(user: UserLogin):
    user = validate_user(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

