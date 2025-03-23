from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from utils import get_access_token
from configs import logger
from database import get_db
from .main_crud import *
from .main_schema import UserLogin, UserRegister

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

@router.post('/login')
async def login(user_form: UserLogin, db: Session = Depends(get_db)) -> dict:
    user = get_user_by_account(db, user_account=user_form.userAccount)
    if not user or not verify_password(user_form.password, user.password):
        response = JSONResponse(
            status_code=401,
            content={'message': 'invalid user account or password'}
        )
        response.headers['authorization'] = 'Bearer'
        return response

    access_token = get_access_token(user)
    response = JSONResponse(
            status_code=200,
            content={'message': 'ok'}
        )
    response.headers['authorization'] = f'Bearer {access_token}'
    return response

