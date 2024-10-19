from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .middlewares.logging_middleware import logging_middleware
from .middlewares.jwt_auth import jwt_auth_middleware
from .api import student_api, user_api

app = FastAPI(debug=True)
app.add_middleware(CORSMiddleware, allow_origins=['http://localhost:4200'], allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"], )
app.include_router(student_api.router, prefix="/student")
app.include_router(user_api.router, prefix="/user")
app.middleware("http")(logging_middleware)
#app.middleware("http")(jwt_auth_middleware)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
