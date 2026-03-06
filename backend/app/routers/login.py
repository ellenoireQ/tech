from starlette.responses import JSONResponse
from datetime import timedelta

from app.utils.jwt import create_access_token
from app.utils.validate_user import validate_user
from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserLogin

router = APIRouter()


#
@router.post("")
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
    response = JSONResponse({"message": "Login success"})
    response.set_cookie(
        key="token", value=access_token, httponly=True, max_age=1800, samesite="strict"
    )
    return response
