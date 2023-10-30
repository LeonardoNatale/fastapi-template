from fastapi import APIRouter

from app.api.endpoints.item import router as item_router

api_router = APIRouter()

api_router.include_router(item_router, prefix="/items", tags=["items"])
