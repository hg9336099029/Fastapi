from pydantic import BaseModel
from typing import List
from schemas.student import Student
from schemas.course import Course

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
