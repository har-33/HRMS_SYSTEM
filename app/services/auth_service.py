from sqlalchemy.orm import Session
from app.models.user import User
from app.utils.security import hash_password


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
