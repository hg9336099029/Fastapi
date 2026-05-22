from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError
from app.core.database import get_db
from app.core.security import decode_token
from app.crud.user import get_user_by_id


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


# re-export get_db so routers can `Depends(deps.get_db)`
get_db = get_db


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_token(token)
        sub = payload.get("sub")
        if sub is None:
            raise credentials_exception
        user_id = int(sub)
    except (JWTError, ValueError):
        raise credentials_exception
    user = get_user_by_id(db, user_id)
    if user is None:
        raise credentials_exception
    return user


def get_current_active_user(current_user = Depends(get_current_user)):
    return current_user


def get_current_active_admin(current_user = Depends(get_current_user)):
    if not getattr(current_user, "is_admin", False):
        raise HTTPException(status_code=403, detail="Admin privileges required")
    return current_user
