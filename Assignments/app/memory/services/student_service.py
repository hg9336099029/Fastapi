import uuid

# In-memory storage for students
students_db = {}

def create_student(student_data: dict) -> dict:
    student_id = str(uuid.uuid4())
    student = {"id": student_id, **student_data}
    students_db[student_id] = student
    return student

def get_students() -> list:
    return list(students_db.values())

def get_student(student_id: str) -> dict:
    return students_db.get(student_id)
