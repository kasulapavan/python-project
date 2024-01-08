from fastapi import APIRouter

from src.dto.beans import EmployeeDetails, DepartmentDetails
from src.service.impl.department_impl import DepartmentServiceImpl

router = APIRouter(tags=["department"])
# Create an instance of EmployeeServiceImpl
department_service_instance = DepartmentServiceImpl()


@router.post('/save-department')
async def saveDepartment(department_details: DepartmentDetails):
    return department_service_instance.save_department(department_details)
