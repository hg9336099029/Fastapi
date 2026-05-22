from typing import Dict, Optional

from app.models.user import UserInDB
from app.schemas.auth_schema import UserCreate
from app.core.security import get_password_hash

fake_users_db: Dict[str, UserInDB] = {}

def create_user(user_in: UserCreate) -> UserInDB:
    if user_in.username in fake_users_db:
        raise ValueError("User already exists")
    hashed = get_password_hash(user_in.password)
    user_db = UserInDB(username=user_in.username, role=user_in.role, hashed_password=hashed)
    fake_users_db[user_in.username] = user_db
    return user_db

def get_user_by_username(username: str) -> Optional[UserInDB]:
    return fake_users_db.get(username)
