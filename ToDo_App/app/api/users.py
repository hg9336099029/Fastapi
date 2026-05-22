from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.api import deps
from app.schemas.user import UserCreate, UserOut
from app.crud.user import get_user_by_username, get_user_by_email, create_user, search_users, get_user_by_id, delete_user

router = APIRouter()


@router.post("/register", response_model=UserOut)
def register(user_in: UserCreate, db: Session = Depends(deps.get_db)):
    if get_user_by_username(db, user_in.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    if get_user_by_email(db, user_in.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    from app.core.security import get_password_hash
    hashed = get_password_hash(user_in.password)
    user = create_user(db, user_in.username, user_in.email, hashed)
    return user


@router.get("/users/search", response_model=List[UserOut])
def users_search(q: Optional[str] = None, db: Session = Depends(deps.get_db), current_user=Depends(deps.get_current_user)):
    users = search_users(db, q, exclude_user_id=current_user.id)
    return users


@router.delete("/users/{user_id}", status_code=204)
def delete_user_endpoint(user_id: int, db: Session = Depends(deps.get_db), admin_user=Depends(deps.get_current_active_admin)):
    if not get_user_by_id(db, user_id):
        raise HTTPException(status_code=404, detail="User not found")
    delete_user(db, user_id)
    return
