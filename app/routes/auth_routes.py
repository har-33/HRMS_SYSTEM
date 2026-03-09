from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user_schema import UserRegister
from app.services.auth_service import create_user
from app.database.session import get_db

router = APIRouter(prefix="/auth")


@router.post("/register")
def register_user(user: UserRegister, db: Session = Depends(get_db)):

    new_user = create_user(db, user.email, user.password)

    return {
        "message": "User created",
        "user_id": new_user.id
    }
