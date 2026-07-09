from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.order_service import get_all_orders
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.dashboard_service import get_admin_dashboard

from app.database import get_db
from app.schemas.admin import (
    AcceptOrder,
    RejectOrder,
    UpdateStatus,
)
from app.services.order_service import (
    get_all_orders,
    get_order_by_id,
    accept_order,
    reject_order,
    update_order_status,
)

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
)


@router.get("/orders")
def all_orders(
    db: Session = Depends(get_db),
):
    return get_all_orders(db)
@router.put("/orders/{order_id}/accept")
def accept(
    order_id: int,
    data: AcceptOrder,
    db: Session = Depends(get_db),
):

    order = get_order_by_id(db, order_id)

    if not order:
        raise HTTPException(404, "Order not found")

    return accept_order(
        db,
        order,
        data,
    )
@router.put("/orders/{order_id}/reject")
def reject(
    order_id: int,
    data: RejectOrder,
    db: Session = Depends(get_db),
):

    order = get_order_by_id(db, order_id)

    if not order:
        raise HTTPException(404, "Order not found")

    return reject_order(
        db,
        order,
        data,
    )
@router.put("/orders/{order_id}/status")
def status(
    order_id: int,
    data: UpdateStatus,
    db: Session = Depends(get_db),
):

    order = get_order_by_id(db, order_id)

    if not order:
        raise HTTPException(404, "Order not found")

    return update_order_status(
        db,
        order,
        data.status,
    )
@router.get("/dashboard")
def dashboard(
    db: Session = Depends(get_db),
):

    return get_admin_dashboard(db)