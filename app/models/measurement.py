from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Measurement(Base):
    __tablename__ = "measurements"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    profile_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    height: Mapped[float] = mapped_column(Float)

    chest: Mapped[float] = mapped_column(Float)

    waist: Mapped[float] = mapped_column(Float)

    hip: Mapped[float] = mapped_column(Float)

    shoulder: Mapped[float] = mapped_column(Float)

    sleeve_length: Mapped[float] = mapped_column(Float)

    neck: Mapped[float] = mapped_column(Float)

    notes: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    customer = relationship(
        "User",
        back_populates="measurements"
    )