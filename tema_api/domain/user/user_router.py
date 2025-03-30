from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from database import get_db
from .user_crud import *
from .user_schema import *
from configs import PROJECT_NAME, logger


router = APIRouter(
    prefix='/user',
)

@router.get('/isExists')
async def user_is_exists(userAccount: str, db: Session = Depends(get_db)) -> dict:
    user = get_user_by_account(db, user_account=userAccount)
    if user:
        return {'exists': True}
    else:
        return {'exists': False}

@router.get('/isEmailExists')
async def email_is_exists(email: str, db: Session = Depends(get_db)) -> dict:
    user = get_user_by_email(db, email=email)
    if user:
        return {'exists': True}
    else:
        return {'exists': False}

@router.get('/account/{user_account}')
async def acount(user_account: str, db: Session = Depends(get_db)) -> dict:
    user = get_user_by_account(db, user_account=user_account)
    if user:
        return {'exists': True}
    else:
        return {'exists': False}

@router.post('/initPassword')
async def init_password(user_form: UserEmail, db: Session = Depends(get_db)) -> dict:
    user = get_user_by_account(db, user_account=user_account)
    if user:
        return {'exists': True}
    else:
        return {'exists': False}

@router.post('/delete/{user_account}')
async def delete_user(user_account: str, db: Session = Depends(get_db)) -> dict:
    user = delete_user_by_account(db, user_account=user_account)
    if user:
        return {'message': 'ok'}
    else:
        return {'message': 'there is not the user!'}

@router.post('/subuser/add', response_model=SubUserResponse)
async def add_sub_user(request: Request, user_form: SubUser, db: Session = Depends(get_db)) -> dict:
    user = request.state.user
    return create_sub_user(db, user_form, user)
