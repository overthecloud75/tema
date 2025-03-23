from passlib.context import CryptContext
from sqlalchemy import or_
from datetime import datetime 

from models import User
from database import get_sessin_db
from configs import logger 

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def create_user(db, user_form):
    user = User(user_account=user_form.userAccount,
                   password=pwd_context.hash(user_form.password),
                   email=user_form.email, 
                   create_dt=datetime.now())
    db.add(user)
    db.commit()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_existing_user(db, user_form):
    return db.query(User).filter(
        or_(User.user_account == user_form.userAccount, User.email == user_form.email)
    ).first()

def get_user_by_account(db=None, user_account: str = ''):
    try:
        if db:
            user = db.query(User).filter(User.user_account == user_account).first()
        else:
            db = get_sessin_db()
            user = db.query(User).filter(User.user_account == user_account).first()
            db.close()
    except Exception as e:
            logger.error(e)
            user = None
    return user

