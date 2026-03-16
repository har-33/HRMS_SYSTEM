from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.database.connection import Base


class Employee(Base):

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    position = Column(String)
    salary = Column(Integer)
    department_id = Column(Integer, ForeignKey("departments.id"))
    hire_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
