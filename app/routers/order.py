from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database import get_db
from app.models.user import User
from app.schemas.order import OrderCreate
from app.services.order_service import (
    create_order,
    get_my_orders,
)

router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)


@router.post("/")
def place_order(
    data: OrderCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    order, error = create_order(
        db,
        current_user.id,
        data,
    )

    if error:
        raise HTTPException(
            status_code=400,
            detail=error,
        )

    return {
        "message": "Order placed successfully",
        "order_id": order.id,
        "status": order.status,
    }


@router.get("/")
def my_orders(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_my_orders(
        db,
        current_user.id,
    )