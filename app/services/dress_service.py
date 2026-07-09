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
def get_dress_by_id(
    db: Session,
    dress_id: int,
):

    return (
        db.query(DressType)
        .filter(DressType.id == dress_id)
        .first()
    )
def update_dress(
    db: Session,
    dress: DressType,
    data: DressCreate,
):

    dress.name = data.name
    dress.image = data.image
    dress.base_price = data.base_price

    db.commit()
    db.refresh(dress)

    return dress
def delete_dress(
    db: Session,
    dress: DressType,
):

    db.delete(dress)

    db.commit()