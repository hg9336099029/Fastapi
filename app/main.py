from fastapi import FastAPI
from app.database import engine, Base
from app.api import students, courses

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="College Management API with SQLAlchemy")

# Include routers
app.include_router(students.router)
app.include_router(courses.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the College Management API!"}
