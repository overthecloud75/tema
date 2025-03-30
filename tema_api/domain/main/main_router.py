from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from utils import get_access_token
from configs import logger
from database import get_db
from .main_crud import *
from .main_schema import UserLogin, UserRegister, UserResponse


router = APIRouter(
    prefix='',
)

@router.get('/')
async def root():
    return {'message': 'Hello World'}

@router.get('/favicon.ico')
async def favicon():
    return JSONResponse(
            status_code=204,
            content={'message': ''}
        )

@router.post('/register')
async def register(user_form: UserRegister, db: Session = Depends(get_db)) -> dict:
    user = get_existing_user(db, user_form=user_form)
    if user:
        return JSONResponse(
            status_code=409,
            content={'message': '이미 존재하는 사용자입니다.'}
        )
    create_user(db=db, user_form=user_form)
    return {'message': 'ok'}

@router.post('/login', response_model=UserResponse)
async def login(user_form: UserLogin, db: Session = Depends(get_db)) -> dict:
    user = get_user_by_account(db, user_account=user_form.userAccount)
    sub_users = get_sub_users(db, user)
    if not user or not verify_password(user_form.password, user.password):
        response = JSONResponse(
            status_code=401,
            content={'message': 'invalid user account or password'}
        )
        return response
    return {
            'createDt': user.create_dt,
            'useMarketing': user.use_marketing,
            'subUserIds': sub_users,
            'tokenInfo': {
                'access_token': get_access_token(user),
                'token_type': 'Bearer'
            },
        }

