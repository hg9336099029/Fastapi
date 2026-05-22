from fastapi import APIRouter, HTTPException

from app.schemas.auth_schema import UserCreate, Token, LoginForm, UserOut
from app.services.user_service import create_user
from app.services.auth_service import create_login_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserOut)
def register(user_in: UserCreate):
    try:
        user = create_user(user_in)
        return UserOut(username=user.username, role=user.role)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=Token)
def login(form_data: LoginForm):
    token = create_login_token(form_data)
    if token is None:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return token
