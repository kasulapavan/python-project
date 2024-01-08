from abc import ABC, abstractmethod

from src.dto.beans import DepartmentDetails


class DepartmentService(ABC):
    @abstractmethod
    def save_department(self, department_details: DepartmentDetails):
        pass
