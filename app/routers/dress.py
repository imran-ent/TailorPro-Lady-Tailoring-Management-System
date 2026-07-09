from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.dress_type import DressCreate
from app.services.dress_service import (
    create_dress,
    get_all_dresses,
)
from app.services.dress_service import (
    create_dress,
    get_all_dresses,
    get_dress_by_id,
    update_dress,
    delete_dress,
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
@router.get("/{dress_id}")
def single_dress(
    dress_id: int,
    db: Session = Depends(get_db),
):

    dress = get_dress_by_id(
        db,
        dress_id,
    )

    if not dress:
        raise HTTPException(
            status_code=404,
            detail="Dress not found",
        )

    return dress
@router.put("/{dress_id}")
def edit_dress(
    dress_id: int,
    data: DressCreate,
    db: Session = Depends(get_db),
):

    dress = get_dress_by_id(
        db,
        dress_id,
    )

    if not dress:
        raise HTTPException(
            status_code=404,
            detail="Dress not found",
        )

    return update_dress(
        db,
        dress,
        data,
    )
@router.delete("/{dress_id}")
def remove_dress(
    dress_id: int,
    db: Session = Depends(get_db),
):

    dress = get_dress_by_id(
        db,
        dress_id,
    )

    if not dress:
        raise HTTPException(
            status_code=404,
            detail="Dress not found",
        )

    delete_dress(
        db,
        dress,
    )

    return {
        "message": "Dress deleted successfully"
    }