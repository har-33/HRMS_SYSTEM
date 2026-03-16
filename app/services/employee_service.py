from sqlalchemy.orm import Session
from app.models.employee import Employee


def create_employee(db: Session, employee_data):

    employee = Employee(**employee_data.dict())

    db.add(employee)
    db.commit()
    db.refresh(employee)

    return employee


def get_employees(db: Session):

    return db.query(Employee).all()


def get_employee(db: Session, employee_id: int):

    return db.query(Employee).filter(
        Employee.id == employee_id
    ).first()


def delete_employee(db: Session, employee_id: int):

    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if employee:
        db.delete(employee)
        db.commit()

    return employee
