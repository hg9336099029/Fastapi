from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.api import deps
from app.schemas.todo import ToDoCreate, ToDoOut, ShareRequest
from app.crud.todo import create_todo, get_todo_by_id, delete_todo, share_todo_with_users, list_todos_for_user
from app.services.todo_service import todo_to_schema
from app.schemas.user import UserOut

router = APIRouter()


@router.post("/todos/", response_model=ToDoOut)
def create_todo_endpoint(todo_in: ToDoCreate, db: Session = Depends(deps.get_db), current_user = Depends(deps.get_current_user)):
    if getattr(current_user, "is_admin", False):
        raise HTTPException(status_code=403, detail="Admins cannot create todos")
    todo = create_todo(db, current_user.id, todo_in.title, todo_in.description)
    return todo_to_schema(todo, current_user)


@router.delete("/todos/{todo_id}", status_code=204)
def delete_todo_endpoint(todo_id: int, db: Session = Depends(deps.get_db), current_user = Depends(deps.get_current_user)):
    todo = get_todo_by_id(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="ToDo not found")
    if getattr(current_user, "is_admin", False) or todo.owner_id == current_user.id:
        delete_todo(db, todo_id)
        return
    raise HTTPException(status_code=403, detail="Not authorized to delete this ToDo")


@router.post("/todos/{todo_id}/share", response_model=List[UserOut])
def share_todo_endpoint(todo_id: int, share: ShareRequest, db: Session = Depends(deps.get_db), current_user = Depends(deps.get_current_user)):
    todo = get_todo_by_id(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="ToDo not found")
    if todo.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Only owner can share this ToDo")
    users = share_todo_with_users(db, todo, share.user_ids)
    return users


@router.get("/todos/", response_model=List[ToDoOut])
def list_todos_endpoint(q: Optional[str] = None, page: int = 1, size: int = 10, db: Session = Depends(deps.get_db), current_user = Depends(deps.get_current_user)):
    todos, total = list_todos_for_user(db, user_id=current_user.id, q=q, page=page, size=size)
    return [todo_to_schema(t, current_user) for t in todos]


@router.get("/todos/{todo_id}", response_model=ToDoOut)
def get_todo_endpoint(todo_id: int, db: Session = Depends(deps.get_db), current_user = Depends(deps.get_current_user)):
    todo = get_todo_by_id(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="ToDo not found")
    if todo.owner_id != current_user.id and all(u.id != current_user.id for u in todo.shared_with):
        raise HTTPException(status_code=403, detail="Not authorized to view this ToDo")
    return todo_to_schema(todo, current_user)
