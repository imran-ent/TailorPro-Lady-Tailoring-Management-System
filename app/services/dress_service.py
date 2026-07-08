from sqlalchemy.orm import Session

from app.models.dress_type import DressType
from app.schemas.dress_type import DressCreate


def create_dress(
    db: Session,
    dress: DressCreate
):

    new_dress = DressType(
        name=dress.name,
        image=dress.image,
        base_price=dress.base_price
    )

    db.add(new_dress)
    db.commit()
    db.refresh(new_dress)

    return new_dress


def get_all_dresses(db: Session):

    return db.query(DressType).all()