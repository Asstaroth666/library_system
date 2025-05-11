from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from server.database import get_db

router = APIRouter()

@router.get("/books")
def list_books(db: Session = Depends(get_db)):
    return [{"id": 1, "title": "1984", "available_copies": 0}]
 