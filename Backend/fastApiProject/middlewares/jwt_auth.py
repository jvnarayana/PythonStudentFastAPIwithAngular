from fastapi import Depends, HTTPException, Request, Response
from fastapi.security import OAuth2PasswordBearer, HTTPBearer
from ..services.auth_service import verify_jwt_token

security = HTTPBearer()


async def jwt_auth_middleware(request: Request, call_next):
    token = request.headers.get('Authorization')
    if not token:
        raise HTTPException(status_code=403, detail="Token is missing")
    payload = verify_jwt_token(token.split('Bearer ')[1])
    if not payload:
        raise HTTPException(status_code=403, detail="Token payload is invalid")

    request.state.user = payload['sub']
    return await call_next(request)



