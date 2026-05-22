from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.association import todo_shares


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    todos = relationship("ToDo", back_populates="owner", cascade="all, delete-orphan")
    shared_todos = relationship("ToDo", secondary=todo_shares, back_populates="shared_with")
