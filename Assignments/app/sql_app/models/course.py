from sqlalchemy import Column, Integer, String
from Assignments.app.database import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    course_code = Column(String, unique=True, index=True)
    credits = Column(Integer)
