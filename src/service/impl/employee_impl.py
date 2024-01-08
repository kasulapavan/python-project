from http import HTTPStatus

from src.database import SessionLocal
from src.dto.beans import  EmployeeDetails
from src.dto.utility import  apiResponse, set_employee_details_data
from src.service.employee_serivce import EmployeeService

db = SessionLocal()


class EmployeeServiceImpl(EmployeeService):
    def save_employee(self, employee_details:EmployeeDetails):
        new_user = set_employee_details_data(employee_details)
        db.add(new_user)
        db.commit()
        return apiResponse(HTTPStatus.OK, 'employee saved', None)
