from pydantic import BaseModel
from typing import List
from app.memory.schemas.student import Student
from app.memory.schemas.course import Course

class EnrollmentCreate(BaseModel):
    student_id: str
    course_id: str

class Enrollment(EnrollmentCreate):
    id: str

class StudentCoursesResponse(BaseModel):
    student: Student
    courses: List[Course]

class CourseStudentsResponse(BaseModel):
    course: Course
    students: List[Student]
