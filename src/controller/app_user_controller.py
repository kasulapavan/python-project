from fastapi import APIRouter

from src.dto.beans import UserDetails, LoginDetails
from src.service.impl.app_user_impl import save_user, login

router = APIRouter(tags=["app_user"])


@router.post('/sign-up')
async def signup(user_details: UserDetails):
    return save_user(user_details)


@router.post('/login-in')
async def loginIn(login_details: LoginDetails):
    return login(login_details)
