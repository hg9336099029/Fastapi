from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    username: str
    role: str
    disabled: Optional[bool] = False


class UserInDB(User):
    hashed_password: str
