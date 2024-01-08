from http import HTTPStatus

from src.database import SessionLocal
from src.dto.beans import EmployeeDetails, DepartmentDetails
from src.dto.utility import apiResponse,  set_department_details_data
from src.service.department_service import DepartmentService

db = SessionLocal()


class DepartmentServiceImpl(DepartmentService):
    def save_department(self, department_details:DepartmentDetails):
        new_user = set_department_details_data(department_details)
        db.add(new_user)
        db.commit()
        return apiResponse(HTTPStatus.OK, 'Department saved', None)
