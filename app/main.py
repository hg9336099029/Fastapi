import logging
from fastapi import FastAPI

from app.database import engine, Base
from app.sql_app.api import students as sql_students, courses as sql_courses
from app.memory.routers import router as mem_router
from app.api import auth as auth_router
from app.api import admin as admin_router
from app.middleware import register_app_middleware, register_exception_handlers

# logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("merged_app")

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Merged College API")

# Register middleware and exception handlers from central modules
register_app_middleware(app)
register_exception_handlers(app)

# Include routers
app.include_router(sql_students.router, prefix="/sql")
app.include_router(sql_courses.router, prefix="/sql")
app.include_router(mem_router, prefix="/mem")
app.include_router(auth_router.router)
app.include_router(admin_router.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Merged College API!"}
