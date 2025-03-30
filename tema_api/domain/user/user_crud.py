from models import User, SubUser
import uuid
from datetime import datetime


def get_user_by_account(db, user_account: str):
    return db.query(User).filter(User.user_account == user_account).first()

def get_user_by_email(db, email: str):
    return db.query(User).filter(User.email == email).first()

def delete_user_by_account(db, user_account: str):
    user = get_user_by_account(db=db, user_account=user_account)
    if user:
        db.delete(user) 
        db.commit() 
    return user 

def create_sub_user(db, user_form, user):
    sub_user = SubUser(user_id=user.id,
                    is_main_user=user_form.isMainUser,
                    uuid=uuid.uuid4(), 
                    name=user_form.name,
                    birth_day=user_form.birthDay,
                    gender=user_form.gender,
                    weight=str(user_form.weight),
                    height=str(user_form.height),
                    create_dt=datetime.now(),
                    update_dt=datetime.now()
                )
    db.add(sub_user)
    db.commit()
    return {
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
    }
