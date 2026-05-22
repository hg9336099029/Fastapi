from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import Tuple, List
from app.models.todo import ToDo
from app.models.association import todo_shares
from app.models.user import User


def create_todo(db: Session, owner_id: int, title: str, description: str = None) -> ToDo:
    todo = ToDo(title=title, description=description, owner_id=owner_id)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def get_todo_by_id(db: Session, todo_id: int) -> ToDo:
    return db.query(ToDo).filter(ToDo.id == todo_id).first()


def delete_todo(db: Session, todo_id: int):
    todo = get_todo_by_id(db, todo_id)
    if todo:
        db.delete(todo)
        db.commit()


def share_todo_with_users(db: Session, todo: ToDo, user_ids: List[int]) -> List[User]:
    users = []
    for uid in user_ids:
        user = db.query(User).filter(User.id == uid).first()
        if user and user not in todo.shared_with:
            todo.shared_with.append(user)
            users.append(user)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return users


def list_todos_for_user(db: Session, user_id: int, q: str = None, page: int = 1, size: int = 10) -> Tuple[List[ToDo], int]:
    query = db.query(ToDo).outerjoin(todo_shares, ToDo.id == todo_shares.c.todo_id).filter(
        or_(ToDo.owner_id == user_id, todo_shares.c.user_id == user_id)
    ).distinct()
    if q:
        q_like = f"%{q}%"
        query = query.filter(or_(ToDo.title.ilike(q_like), ToDo.description.ilike(q_like)))
    total = query.count()
    offset = max(page - 1, 0) * size
    todos = query.order_by(ToDo.created_at.desc()).offset(offset).limit(size).all()
    return todos, total
