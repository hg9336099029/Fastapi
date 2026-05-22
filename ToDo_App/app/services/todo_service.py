from app.crud.todo import create_todo, list_todos_for_user
from app.schemas.todo import ToDoOut


def todo_to_schema(todo, current_user):
    shared = False
    if todo.owner_id == current_user.id:
        shared = len(todo.shared_with) > 0
    else:
        shared = any(u.id == current_user.id for u in todo.shared_with)
    return ToDoOut(id=todo.id, title=todo.title, description=todo.description, owner_id=todo.owner_id, shared=shared)
