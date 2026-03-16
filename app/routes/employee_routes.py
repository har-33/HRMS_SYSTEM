from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.employee_schema import EmployeeCreate
from app.services.employee_service import (
    create_employee,
    get_employees,
    get_employee,
    delete_employee
)

from app.database.session import get_db

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.post("/")
def create(employee: EmployeeCreate, db: Session = Depends(get_db)):

    return create_employee(db, employee)


@router.get("/")
def list_employees(db: Session = Depends(get_db)):

    return get_employees(db)


@router.get("/{employee_id}")
def get(employee_id: int, db: Session = Depends(get_db)):

    return get_employee(db, employee_id)


@router.delete("/{employee_id}")
def delete(employee_id: int, db: Session = Depends(get_db)):

    return delete_employee(db, employee_id)
