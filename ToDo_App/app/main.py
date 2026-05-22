from fastapi import FastAPI
from app.core import database
from app.api import auth, users, todos

app = FastAPI(title="ToDo App")


@app.on_event("startup")
def on_startup():
    database.Base.metadata.create_all(bind=database.engine)


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(todos.router)
