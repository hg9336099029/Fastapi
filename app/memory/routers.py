from fastapi import APIRouter, HTTPException
from typing import List

from app.memory.schemas.student import Student, StudentCreate
from app.memory.schemas.course import Course, CourseCreate
from app.memory.schemas.enrollment import Enrollment, EnrollmentCreate, StudentCoursesResponse, CourseStudentsResponse
from app.memory.services import student_service, course_service, enrollment_service

router = APIRouter(
    prefix="",
    tags=["in-memory"]
)

# Students endpoints
@router.post("/students/", response_model=Student, status_code=201)
def create_student(student: StudentCreate):
    return student_service.create_student(student.model_dump())

@router.get("/students/", response_model=List[Student])
def read_students():
    return student_service.get_students()

@router.get("/students/{student_id}", response_model=Student)
def read_student(student_id: str):
    student = student_service.get_student(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Courses endpoints
@router.post("/courses/", response_model=Course, status_code=201)
def create_course(course: CourseCreate):
    return course_service.create_course(course.model_dump())

@router.get("/courses/", response_model=List[Course])
def read_courses():
    return course_service.get_courses()

@router.get("/courses/{course_id}", response_model=Course)
def read_course(course_id: str):
    course = course_service.get_course(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

# Enrollments endpoints
@router.post("/enrollments/", response_model=Enrollment, status_code=201)
def create_enrollment(enrollment: EnrollmentCreate):
    return enrollment_service.enroll_student(enrollment.model_dump())

@router.get("/enrollments/student/{student_id}", response_model=StudentCoursesResponse)
def read_student_courses(student_id: str):
    result = enrollment_service.get_student_courses(student_id)
    if not result:
        raise HTTPException(status_code=404, detail="Student not found")
    return result

@router.get("/enrollments/course/{course_id}", response_model=CourseStudentsResponse)
def read_course_students(course_id: str):
    result = enrollment_service.get_course_students(course_id)
    if not result:
        raise HTTPException(status_code=404, detail="Course not found")
    return result
