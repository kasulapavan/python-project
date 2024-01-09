from datetime import timedelta, datetime
from http import HTTPStatus
from jose import jwt

from src.dto.beans import UserDetails, EmployeeDetails, LoginDetails
from src.database import SessionLocal
from src.dto.enums import SECRET_KEY, ALGORITHM
from src.dto.utility import set_user_details_data, apiResponse
from src.model import models
from passlib.context import CryptContext

db = SessionLocal()

import redis

# Connect to the local Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def save_user(user: UserDetails):
    new_user = set_user_details_data(user)

    db.add(new_user)
    db.commit()
    return apiResponse(HTTPStatus.OK, 'signup_message')


def login(login_details: LoginDetails):
    find_by_user = db.query(models.AppUser).where(models.AppUser.email == login_details.email).first()
    if find_by_user is not None:
        password = pwd_context.verify(login_details.password, find_by_user.password)
        if password is not None:
            access_token = create_access_token(data={"sub": login_details.email}, expires_delta=timedelta(hours=1))
            r.set(access_token, access_token, ex=2000)
            return apiResponse(HTTPStatus.OK, "successfully saved", access_token)
        else:
            return apiResponse(HTTPStatus.BAD_REQUEST, "please enter valid password")
    else:
        return apiResponse(HTTPStatus.OK, 'please enter valid email')


