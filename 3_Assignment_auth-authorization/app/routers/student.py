from fastapi import APIRouter, Depends

from app.schemas.auth_schema import UserOut
from app.core.security import get_current_active_user, require_roles

router = APIRouter(prefix="/students", tags=["students"])


@router.get("/me", response_model=UserOut)
def read_own_profile(current_user = Depends(get_current_active_user)):
    return UserOut(username=current_user.username, role=current_user.role)


@router.get("/only-students")
def only_students(current_user = Depends(require_roles(["student"]))):
    return {"message": f"Hello student {current_user.username}"}
