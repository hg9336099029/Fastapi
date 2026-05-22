from datetime import timedelta
from typing import Optional

from app.services.user_service import get_user_by_username
from app.core.security import verify_password, create_access_token
from app.schemas.auth_schema import LoginForm, Token
from app.models.user import UserInDB

ACCESS_TOKEN_EXPIRE_MINUTES = 60

def authenticate_user(username: str, password: str) -> Optional[UserInDB]:
    user = get_user_by_username(username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def create_login_token(form_data: LoginForm) -> Optional[Token]:
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        return None
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "role": user.role}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
