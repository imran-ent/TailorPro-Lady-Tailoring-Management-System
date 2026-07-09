from sqlalchemy.orm import Session

from app.models.notification import Notification


def create_notification(
    db: Session,
    customer_id: int,
    order_id: int,
    message: str,
):

    notification = Notification(
        customer_id=customer_id,
        order_id=order_id,
        message=message,
    )

    db.add(notification)
    db.commit()


def get_notifications(
    db: Session,
    customer_id: int,
):

    return (
        db.query(Notification)
        .filter(
            Notification.customer_id == customer_id
        )
        .order_by(Notification.created_at.desc())
        .all()
    )