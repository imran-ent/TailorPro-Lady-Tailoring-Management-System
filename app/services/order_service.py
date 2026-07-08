from sqlalchemy.orm import Session

from app.models.dress_type import DressType
from app.models.measurement import Measurement
from app.models.order import Order
from app.schemas.order import OrderCreate


def create_order(
    db: Session,
    customer_id: int,
    data: OrderCreate,
):

    dress = (
        db.query(DressType)
        .filter(DressType.id == data.dress_type_id)
        .first()
    )

    if not dress:
        return None, "Dress type not found"

    measurement = (
        db.query(Measurement)
        .filter(
            Measurement.id == data.measurement_id,
            Measurement.customer_id == customer_id,
        )
        .first()
    )

    if not measurement:
        return None, "Measurement not found"

    order = Order(
        customer_id=customer_id,
        dress_type_id=data.dress_type_id,
        measurement_id=data.measurement_id,
        special_instruction=data.special_instruction,
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    return order, None


def get_my_orders(
    db: Session,
    customer_id: int,
):

    return (
        db.query(Order)
        .filter(Order.customer_id == customer_id)
        .all()
    )
def get_all_orders(db: Session):
    return db.query(Order).all()
def get_order_by_id(db: Session, order_id: int):
    return (
        db.query(Order)
        .filter(Order.id == order_id)
        .first()
    )


def accept_order(db: Session, order: Order, data):

    order.status = "ACCEPTED"
    order.appointment_date = data.appointment_date
    order.expected_delivery_date = data.expected_delivery_date

    db.commit()
    db.refresh(order)

    return order


def reject_order(db: Session, order: Order, data):

    order.status = "REJECTED"
    order.rejection_reason = data.rejection_reason

    db.commit()
    db.refresh(order)

    return order


def update_order_status(db: Session, order: Order, status: str):

    order.status = status

    db.commit()
    db.refresh(order)

    return order