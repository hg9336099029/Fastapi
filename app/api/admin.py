from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.sql_app.models.student import Student as DBStudent
from app.sql_app.models.course import Course as DBCourse
from app.core.security import require_roles

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/students")
def list_students(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1),
    db: Session = Depends(get_db),
    _=Depends(require_roles(["admin"])),
):
    page_size = max(1, min(page_size, 100))
    total_items = db.query(DBStudent).count()
    total_pages = (total_items + page_size - 1) // page_size if total_items else 1
    offset = (page - 1) * page_size
    students = db.query(DBStudent).offset(offset).limit(page_size).all()
    items = [{"id": s.id, "name": s.name, "email": s.email, "age": s.age} for s in students]
    return {"items": items, "total_items": total_items, "total_pages": total_pages, "page": page, "page_size": page_size}


@router.get("/courses")
def list_courses(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1),
    db: Session = Depends(get_db),
    _=Depends(require_roles(["admin"])),
):
    page_size = max(1, min(page_size, 100))
    total_items = db.query(DBCourse).count()
    total_pages = (total_items + page_size - 1) // page_size if total_items else 1
    offset = (page - 1) * page_size
    courses = db.query(DBCourse).offset(offset).limit(page_size).all()
    items = [{"id": c.id, "name": c.name, "course_code": c.course_code, "credits": c.credits} for c in courses]
    return {"items": items, "total_items": total_items, "total_pages": total_pages, "page": page, "page_size": page_size}
