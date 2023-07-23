from fastapi import FastAPI

from src.views import router

app = FastAPI(title="My app")

app.include_router(router)
