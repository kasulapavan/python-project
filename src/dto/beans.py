from pydantic import BaseModel, Field


class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True


class UserDetails(OurBaseModel):
    name: str = Field(min_length=1)
    email: str = Field(min_length=1)
    password: str = Field(min_length=1)

class EmployeeDetails(OurBaseModel):
    name: str = Field(min_length=1)
    email: str = Field(min_length=1)
    connect_number: str = Field(min_length=1)
    department_id:int =Field(ge=1)

class DepartmentDetails(OurBaseModel):
    name: str = Field(min_length=1)
class LoginDetails(OurBaseModel):
    email: str = Field(min_length=1)
    password: str = Field(min_length=1)
