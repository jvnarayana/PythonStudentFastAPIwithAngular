from jose import JWTError, jwt
from datetime import datetime, timedelta
from ..dbConfig.config import settings
from ..models.User import User

SECRET_KEY = settings.JWT_SECRET_KEY
ALGORITHM = settings.JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE = timedelta(minutes=settings.JWT_EXPIRATION_TIME)


def create_jwt_token(user: User) -> str:
    to_encode = user.copy()
    expire = datetime.utcnow() + ACCESS_TOKEN_EXPIRE
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt


def verify_jwt_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

