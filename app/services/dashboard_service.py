from sqlalchemy.orm import Session

from app.models.order import Order
from app.models.user import User
from app.constants.order_status import OrderStatus
from app.models.order import Order
from app.constants.order_status import OrderStatus


def get_customer_dashboard(
    db: Session,
    user: User
):

    orders = (
        db.query(Order)
        .filter(Order.customer_id == user.id)
        .all()
    )

    total_orders = len(orders)

    pending_orders = len(
        [
            order for order in orders
            if order.status == OrderStatus.PENDING.value
        ]
    )

    active_orders = len(
        [
            order for order in orders
            if order.status != OrderStatus.DELIVERED.value
        ]
    )

    latest_orders = sorted(
        orders,
        key=lambda order: order.created_at,
        reverse=True,
    )[:5]

    return {
        "customer": {
            "id": user.id,
            "name": user.full_name,
            "email": user.email,
        },
        "statistics": {
            "total_orders": total_orders,
            "pending_orders": pending_orders,
            "active_orders": active_orders,
        },
        "latest_orders": latest_orders,
    }
def get_admin_dashboard(db: Session):

    orders = db.query(Order).all()

    return {

        "total_orders": len(orders),

        "pending_orders": len([
            o for o in orders
            if o.status == OrderStatus.PENDING.value
        ]),

        "accepted_orders": len([
            o for o in orders
            if o.status == OrderStatus.ACCEPTED.value
        ]),

        "stitching_orders": len([
            o for o in orders
            if o.status == OrderStatus.STITCHING.value
        ]),

        "ready_orders": len([
            o for o in orders
            if o.status == OrderStatus.READY.value
        ]),

        "delivered_orders": len([
            o for o in orders
            if o.status == OrderStatus.DELIVERED.value
        ]),

        "rejected_orders": len([
            o for o in orders
            if o.status == OrderStatus.REJECTED.value
        ])
    }