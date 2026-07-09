from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Notification(Base):
    __tablename__ = "notifications"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.id")
    )

    message: Mapped[str] = mapped_column(
        String(500)
    )

    is_read: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    customer = relationship("User")
    order = relationship("Order")