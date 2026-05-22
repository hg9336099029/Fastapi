import uuid
from app.memory.services import student_service, course_service

# In-memory storage for enrollments
enrollments_db = {}

def enroll_student(enrollment_data: dict) -> dict:
    enrollment_id = str(uuid.uuid4())
    enrollment = {"id": enrollment_id, **enrollment_data}
    enrollments_db[enrollment_id] = enrollment
    return enrollment

def get_student_courses(student_id: str) -> dict:
    student = student_service.get_student(student_id)
    if not student:
        return None
        
    student_enrollments = [e for e in enrollments_db.values() if e["student_id"] == student_id]
    courses = []
    for e in student_enrollments:
        course = course_service.get_course(e["course_id"])
        if course:
            courses.append(course)
            
    return {"student": student, "courses": courses}

def get_course_students(course_id: str) -> dict:
    course = course_service.get_course(course_id)
    if not course:
        return None
        
    course_enrollments = [e for e in enrollments_db.values() if e["course_id"] == course_id]
    students = []
    for e in course_enrollments:
        student = student_service.get_student(e["student_id"])
        if student:
            students.append(student)
            
    return {"course": course, "students": students}
