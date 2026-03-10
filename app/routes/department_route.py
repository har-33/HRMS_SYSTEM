from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.department_schema import DepartmentCreate
from app.services.department_service import (
    create_department,
    get_departments,
    get_department
)
from app.database.session import get_db

router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)


@router.post("/")
def create(department: DepartmentCreate, db: Session = Depends(get_db)):
    
    return create_department(db, department.name, department.description)
    
@router.get("/")
def list_departments(db: Session = Depends(get_db)):
    
    return get_departments(db)

@router.get("/{department_id}")
def get(department_id: int, db: Session = Depends(get_db)):
    
    return get_department(db, department_id)