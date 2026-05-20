import uuid

# In-memory storage for courses
courses_db = {}

def create_course(course_data: dict) -> dict:
    course_id = str(uuid.uuid4())
    course = {"id": course_id, **course_data}
    courses_db[course_id] = course
    return course

def get_courses() -> list:
    return list(courses_db.values())

def get_course(course_id: str) -> dict:
    return courses_db.get(course_id)
