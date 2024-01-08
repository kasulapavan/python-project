from http import HTTPStatus

from src.dto.beans import UserDetails, EmployeeDetails
from src.database import SessionLocal
from src.dto.utility import set_user_details_data, apiResponse, set_employee_details_data

db = SessionLocal()


def save_user(self: UserDetails):
    new_user = set_user_details_data(self)
    db.add(new_user)
    db.commit()
    return apiResponse(HTTPStatus.OK, 'signup_message')
