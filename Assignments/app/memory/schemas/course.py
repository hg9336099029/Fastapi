from pydantic import BaseModel

class CourseCreate(BaseModel):
    name: str
    description: str
    duration: str

class Course(CourseCreate):
    id: str
