from fastapi import APIRouter
from src.database.models import Notes
router = APIRouter()


@router.get("/")
async def list_notes():
    return await Notes.all()
