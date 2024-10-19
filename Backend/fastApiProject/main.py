from fastapi import FastAPI
from .middlewares.logging_middleware import logging_middleware
from .middlewares.jwt_auth import jwt_auth_middleware
from .api import student_api
app = FastAPI()

app.middleware("http")(logging_middleware)
app.middleware("http")(jwt_auth_middleware)
app.include_router(student_api.router)


if __name__ == "__main__":
    import  uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)