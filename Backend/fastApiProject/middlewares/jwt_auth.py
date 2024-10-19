from fastapi import Depends, HTTPException, Request, Response
from fastapi.security import OAuth2PasswordBearer, HTTPBearer
from ..services.auth_service import verify_jwt_token

security = HTTPBearer()


async def jwt_auth_middleware(request: Request, call_next):
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        raise HTTPException(status_code=403, detail="Token is missing")
    token = auth_header.split('Bearer ')[1]
    payload = verify_jwt_token(token)
    if not payload:
        raise HTTPException(status_code=403, detail="Token payload is invalid")

    request.state.user = payload['sub']

    response = await call_next(request)
    return response



