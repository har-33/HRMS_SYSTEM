from sqlalchemy.orm import Session
from app.models.user import User
from app.utils.security import hash_password, verify_password, create_access_token


def create_user(db: Session, email: str, password: str):

    hashed_password = hash_password(password)

    user = User(
        email=email,
        password_hash=hashed_password,
        role="employee"
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def login_user(db: Session, email: str, password: str):
   
    user = db.query(User).filter(User.email == email).first()
   
    if not user:
        return None
   
    if not verify_password(password, user.password_hash):
        return None
   
    token = create_access_token({"sub": user.email, "role": user.role})
   
    return {"access_token": token, "token_type": "bearer"}
