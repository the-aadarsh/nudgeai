from fastapi import APIRouter

router = APIRouter()

@router.get("/sync")
async def sync_flashcards_endpoint():
    pass
