from fastapi import FastAPI
from app.routers import auth, student, admin

app = FastAPI(title="FastAPI Auth + RBAC Example")

app.include_router(auth.router)
app.include_router(student.router)
app.include_router(admin.router)

@app.get("/")
def read_root():
    return {"msg": "Auth + RBAC demo. Use /auth/register and /auth/login."}
