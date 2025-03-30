from jose import jwt, JWTError
from datetime import datetime, timedelta

from domain.main.main_crud import get_user_by_account
from configs import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES, logger


def get_access_token(user):
    # make access token
    data = {
        'sub': user.user_account,
        'exp': datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    return jwt.encode(data, SECRET_KEY, algorithm='HS256')

def get_current_user(request):
    token = _get_authorization_bearer_token(request)
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_account: str = payload.get('sub')
        if user_account is None:
            raise Exception
    except JWTError:
        logger.error(JWTError)
        raise Exception
    else:
        user = get_user_by_account(user_account=user_account)
        if user is None:
            raise Exception
        return user

def _get_authorization_bearer_token(request) -> str:
    if 'authorization' in request.headers:
        if request.headers['authorization'].startswith('Bearer '):
            token = request.headers['authorization'][7:]
        else:
            token = ''
    else:
        token = ''
    return token

