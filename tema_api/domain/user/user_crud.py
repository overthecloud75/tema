from models import User


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