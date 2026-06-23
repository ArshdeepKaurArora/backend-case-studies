from fastapi import FastAPI

from api.v1.routes import router as user_router

app =  FastAPI()

app.include_router(
    user_router,
    prefix="/users"
)