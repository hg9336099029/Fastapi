from app.crud.user import get_user_by_username
from app.core.security import verify_password, create_access_token, get_password_hash


def authenticate_user(db, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def hash_password(password: str) -> str:
    return get_password_hash(password)


def create_token_for_user(user):
    return create_access_token(str(user.id))
