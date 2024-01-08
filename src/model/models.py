from sqlalchemy import String, Integer, Column, Boolean, DateTime, func, ForeignKey

from src.database import Base, engine


def create_tables():
    Base.metadata.create_all(engine)


class BaseEntity(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_on = Column(DateTime, default=func.now())
    updated_on = Column(DateTime, server_default=func.now(), onupdate=func.now())
    is_active = Column(Boolean)


class AppUser(BaseEntity):
    __tablename__ = "app_user"
    name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    # status = Column(String, nullable=False, server_default= UserStatus.ACTIVE)
    # role = Column(String, nullable=False, server_default= UserRoleEnum.USER)


class Employee(BaseEntity):
    __tablename__ = "employee"
    name = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)
    connect_number = Column(String(255))
    department_id = Column(Integer, ForeignKey("department.id"), nullable=False, index=True)


class Department(BaseEntity):
    __tablename__ = "department"
    name = Column(String(255), index=True)


# sdfsdfsdfsfsfsfsfsfsfs?
# sd?
# ?asdasda