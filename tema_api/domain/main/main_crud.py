from passlib.context import CryptContext
from sqlalchemy import or_
from datetime import datetime 

from models import User, SubUser
from database import get_sessin_db
from configs import logger 

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto', bcrypt__rounds=10) # ToBe : bcrypt__rounds=12로 원복 

def create_user(db, user_form):
    user = User(user_account=user_form.userAccount,
                   password=pwd_context.hash(user_form.password),
                   email=user_form.email, 
                   create_dt=datetime.now(),
                   use_marketing=user_form.useMarketing
                )
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

def get_sub_users(db, user):
    sub_users = db.query(SubUser).filter(SubUser.user_id == user.id).all()
    sub_user_list = []
    for sub_user in sub_users:
        sub_user_list.append({
            'userId': sub_user.user_id,
            'uuid': str(sub_user.uuid),
            'isMainUser': sub_user.is_main_user,
            'name': sub_user.name,
            'birthDay': sub_user.birth_day,
            'gender': sub_user.gender,
            'weight': sub_user.weight,
            'height': sub_user.height,
            'createDt': sub_user.create_dt,
            'updateDt': sub_user.update_dt
        })
    return sub_user_list


