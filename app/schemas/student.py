from pydantic import BaseModel, EmailStr

class StudentBase(BaseModel):
    name: str
    email: EmailStr
    age: int

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    age: int | None = None

class Student(StudentBase):
    id: int

    class Config:
        from_attributes = True
