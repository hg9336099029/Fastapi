from sqlalchemy import Table, Column, Integer, ForeignKey
from app.core.database import Base


todo_shares = Table(
    "todo_shares",
    Base.metadata,
    Column("todo_id", Integer, ForeignKey("todos.id"), primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
)
