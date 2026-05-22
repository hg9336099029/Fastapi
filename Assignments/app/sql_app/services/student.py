from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from Assignments.app.sql_app.models.student import Student
from Assignments.app.sql_app.schemas.student import StudentCreate, StudentUpdate

def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Student).offset(skip).limit(limit).all()

def create_student(db: Session, student: StudentCreate):
    db_student = Student(**student.model_dump())
    try:
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already registered")

def update_student(db: Session, student_id: int, student: StudentUpdate):
    db_student = get_student(db, student_id)
    if db_student:
        update_data = student.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_student, key, value)
        try:
            db.commit()
            db.refresh(db_student)
            return db_student
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="Email already registered")
    return None

def delete_student(db: Session, student_id: int):
    db_student = get_student(db, student_id)
    if db_student:
        db.delete(db_student)
        db.commit()
        return True
    return False
