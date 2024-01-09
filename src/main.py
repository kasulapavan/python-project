
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.model import models
from src.controller.app_user_controller import  router as app_user
from src.controller.employee_controller import  router as employee
from src.controller.department_controller import  router as department


app = FastAPI()
models.create_tables()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(app_user, prefix="/app_user")
app.include_router(employee, prefix="/employee")
app.include_router(department, prefix="/department")



