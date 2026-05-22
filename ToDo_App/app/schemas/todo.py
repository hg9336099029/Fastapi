from pydantic import BaseModel
from typing import Optional, List


class ToDoCreate(BaseModel):
    title: str
    description: Optional[str] = None


class ToDoOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    owner_id: int
    shared: bool

    class Config:
        orm_mode = True


class ShareRequest(BaseModel):
    user_ids: List[int]
