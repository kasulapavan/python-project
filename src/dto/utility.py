from passlib.context import CryptContext

from src.model import models
from src.dto.beans import UserDetails, EmployeeDetails, DepartmentDetails
from fastapi.responses import JSONResponse

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def apiResponse(responseCode=None, message=None, payload=None):
    return JSONResponse({'statusCode': responseCode, "message": message, 'payload': payload}, status_code=responseCode)


def set_user_details_data(user_details: UserDetails):
    return models.AppUser(
        name=user_details.name,
        email=user_details.email,
        password=pwd_context.hash(user_details.password),  # bcrypt  the password store in db

    )


def set_employee_details_data(employeeDetails: EmployeeDetails):
    return models.Employee(
        name=employeeDetails.name,
        email=employeeDetails.email,
        connect_number=employeeDetails.connect_number,
        department_id=employeeDetails.department_id

    )


def set_department_details_data(departmentDetails: DepartmentDetails):
    return models.Department(
        name=departmentDetails.name
    )
