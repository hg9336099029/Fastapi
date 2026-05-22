from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List, Optional
from app.models.user import User


def get_user_by_username(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter(User.username == username).first()


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, username: str, email: str, hashed_password: str, is_admin: bool = False) -> User:
    user = User(username=username, email=email, hashed_password=hashed_password, is_admin=is_admin)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if user:
        db.delete(user)
        db.commit()


def search_users(db: Session, q: str = None, exclude_user_id: int = None, limit: int = 20) -> List[User]:
    query = db.query(User)
    if q:
        q_like = f"%{q}%"
        query = query.filter(or_(User.username.ilike(q_like), User.email.ilike(q_like)))
    if exclude_user_id:
        query = query.filter(User.id != exclude_user_id)
    return query.limit(limit).all()
