from fastapi import FastAPI, HTTPException
from typing import List
from schemas.student import StudentCreate, Student
from schemas.course import CourseCreate, Course
from schemas.enrollment import EnrollmentCreate, Enrollment, StudentCoursesResponse, CourseStudentsResponse
from services import student_service, course_service, enrollment_service

app = FastAPI(title="College API")

# -- Routes --

@app.post("/students/", response_model=Student)
def register_student(student: StudentCreate):
    return student_service.create_student(student.model_dump())

@app.get("/students/", response_model=List[Student])
def read_students():
    return student_service.get_students()

@app.get("/students/{student_id}", response_model=Student)
def read_student(student_id: str):
    student = student_service.get_student(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.post("/courses/", response_model=Course)
def register_course(course: CourseCreate):
    return course_service.create_course(course.model_dump())

@app.get("/courses/", response_model=List[Course])
def read_courses():
    return course_service.get_courses()

@app.get("/courses/{course_id}", response_model=Course)
def read_course(course_id: str):
    course = course_service.get_course(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@app.post("/enrollments/", response_model=Enrollment)
def create_enrollment(enrollment: EnrollmentCreate):
    return enrollment_service.enroll_student(enrollment.model_dump())

@app.get("/enrollments/student/{student_id}", response_model=StudentCoursesResponse)
def read_student_courses(student_id: str):
    result = enrollment_service.get_student_courses(student_id)
    if not result:
        raise HTTPException(status_code=404, detail="Student not found")
    return result

@app.get("/enrollments/course/{course_id}", response_model=CourseStudentsResponse)
def read_course_students(course_id: str):
    result = enrollment_service.get_course_students(course_id)
    if not result:
        raise HTTPException(status_code=404, detail="Course not found")
    return result

@app.get("/")
def read_root():
    return {"message": "Welcome to the College API"}
