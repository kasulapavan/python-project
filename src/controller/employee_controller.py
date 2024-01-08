from fastapi import APIRouter

from src.dto.beans import EmployeeDetails
from src.service.impl.employee_impl import EmployeeServiceImpl

router = APIRouter(tags=["employee"])
# Create an instance of EmployeeServiceImpl
employee_service_instance = EmployeeServiceImpl()


@router.post('/save-employee')
async def saveEmployee(employee_details: EmployeeDetails):
    return employee_service_instance.save_employee(employee_details)
