from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    dress_type_id: Mapped[int] = mapped_column(
        ForeignKey("dress_types.id"),
        nullable=False
    )

    measurement_id: Mapped[int] = mapped_column(
        ForeignKey("measurements.id"),
        nullable=False
    )

    reference_image: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    special_instruction: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="PENDING"
    )
    appointment_date: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    expected_delivery_date: Mapped[datetime | None] = mapped_column(
       DateTime,
       nullable=True
    )

    rejection_reason: Mapped[str | None] = mapped_column(
       Text,
       nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    customer = relationship(
        "User",
        back_populates="orders"
    )

    dress_type = relationship(
        "DressType"
    )

    measurement = relationship(
        "Measurement"
    )