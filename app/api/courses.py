from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.course import Course, CourseCreate, CourseUpdate
from app.services import course as course_service
from app.database import get_db

router = APIRouter(
    prefix="/courses",
    tags=["courses"]
)

@router.post("/", response_model=Course, status_code=201)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    return course_service.create_course(db=db, course=course)

@router.get("/", response_model=List[Course])
def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return course_service.get_courses(db, skip=skip, limit=limit)

@router.get("/{course_id}", response_model=Course)
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = course_service.get_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course

@router.put("/{course_id}", response_model=Course)
def update_course(course_id: int, course: CourseUpdate, db: Session = Depends(get_db)):
    db_course = course_service.update_course(db, course_id=course_id, course=course)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course

@router.delete("/{course_id}", status_code=204)
def delete_course(course_id: int, db: Session = Depends(get_db)):
    success = course_service.delete_course(db, course_id=course_id)
    if not success:
        raise HTTPException(status_code=404, detail="Course not found")
    return None
