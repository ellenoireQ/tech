from pydantic import BaseModel


# User Login Model
#
# example:
#
# UserLogin(
# email = "x@x.com"
# password = "x"
# )
class UserLogin(BaseModel):
    email: str
    password: str
