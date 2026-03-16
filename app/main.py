from fastapi import FastAPI
from app.routes.auth_routes import router as auth_router
from app.routes.department_route import router as department_router
from app.routes.employee_routes import router as employee_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(department_router)
app.include_router(employee_router)