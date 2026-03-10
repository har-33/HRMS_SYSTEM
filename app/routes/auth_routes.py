from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserRegister, UserLogin
from app.services.auth_service import create_user, login_user
from app.database.session import get_db
from app.utils.security import get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/register")
def register_user(user: UserRegister, db: Session = Depends(get_db)):

    new_user = create_user(db, user.email, user.password)

    return {
        "message": "User created",
        "user_id": new_user.id
    }

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    
    auth_result = login_user(db, user.email, user.password)
    
    if not auth_result:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return auth_result

@router.get("/protected")
def protected_route(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello {current_user}, you are authorized!"}