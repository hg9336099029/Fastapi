from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    email: str
    age: int

class Student(StudentCreate):
    id: str
