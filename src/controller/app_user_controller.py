from fastapi import APIRouter

from src.dto.beans import UserDetails
from src.service.impl.app_user_impl import save_user

router = APIRouter(tags=["app_user"])


@router.post('/sign-up')
async def signup(user_details: UserDetails):
    return save_user(user_details)
