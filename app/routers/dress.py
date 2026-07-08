from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.dress_type import DressCreate
from app.services.dress_service import (
    create_dress,
    get_all_dresses,
)

router = APIRouter(
    prefix="/dress",
    tags=["Dress Types"]
)


@router.post("/")
def add_dress(
    dress: DressCreate,
    db: Session = Depends(get_db)
):
    return create_dress(db, dress)


@router.get("/")
def all_dresses(
    db: Session = Depends(get_db)
):
    return get_all_dresses(db)