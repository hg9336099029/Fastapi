from fastapi import APIRouter, Depends

from app.core.security import require_roles

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/dashboard")
def admin_dashboard(current_user = Depends(require_roles(["admin"]))):
    return {"message": f"Welcome to the admin area, {current_user.username}"}
