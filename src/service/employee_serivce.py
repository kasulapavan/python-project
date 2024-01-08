from abc import ABC, abstractmethod

from src.dto.beans import EmployeeDetails


class EmployeeService(ABC):
    @abstractmethod
    def save_employee(self, employee_details: EmployeeDetails):
        pass
