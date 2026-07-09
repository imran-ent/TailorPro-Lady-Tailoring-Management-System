from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserRegister
from app.auth.hash import hash_password, verify_password


def get_user_by_email(db: Session, email: str):
    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )


def create_user(db: Session, user_data: UserRegister):

    user = User(
        full_name=user_data.full_name,
        email=user_data.email,
        phone=user_data.phone,
        password=hash_password(user_data.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def authenticate_user(
    db: Session,
    email: str,
    password: str
):

    user = get_user_by_email(
        db,
        email
    )

    if not user:
        return None

    if not verify_password(
        password,
        user.password
    ):
        return None

    return user
def get_user_by_phone(db: Session, phone: str):
    return (
        db.query(User)
        .filter(User.phone == phone)
        .first()
    )
def update_profile(db, user, data):

    user.full_name = data.full_name
    user.phone = data.phone

    db.commit()
    db.refresh(user)

    return user