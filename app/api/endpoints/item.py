from fastapi import APIRouter

from app.models.item import Item

router = APIRouter()


@router.get("/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@router.post("/")
async def create_item(item: dict):
    return {"item": item}


@router.put("/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
