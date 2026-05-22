from pydantic import BaseModel

class CourseBase(BaseModel):
    name: str
    course_code: str
    credits: int

class CourseCreate(CourseBase):
    pass

class CourseUpdate(BaseModel):
    name: str | None = None
    course_code: str | None = None
    credits: int | None = None

class Course(CourseBase):
    id: int

    class Config:
        from_attributes = True
