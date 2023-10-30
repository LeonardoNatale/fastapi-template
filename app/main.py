import uvicorn
from fastapi import FastAPI

from app.api.base import api_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(api_router)


def start():
    """Launched with `poetry run dev` at root level"""
    uvicorn.run("app.main:app", reload=True)
