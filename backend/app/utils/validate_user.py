from app.schemas.user import UserLogin
from app.core.config import settings

# validate user
# Validate the user based by email and password.
# 
# Param:
# @email: str
# @password: str
#
# Return: UserLogin
def validate_user(user: UserLogin) -> UserLogin | None:
    if user.email == settings.DUMMY_ADMIN and user.password == settings.DUMMY_PASSWORD:
        return user
    return None