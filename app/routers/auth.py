from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User

from app.auth.dependencies import get_current_user
from app.auth.jwt import create_access_token

from app.schemas.user import UserRegister
from app.schemas.profile import UpdateProfile

from app.services.user_service import (
    create_user,
    get_user_by_email,
    get_user_by_phone,
    authenticate_user,
    update_profile,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db),
):

    existing_user = get_user_by_email(
        db,
        user.email,
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )

    existing_phone = get_user_by_phone(
        db,
        user.phone,
    )

    if existing_phone:
        raise HTTPException(
            status_code=400,
            detail="Phone number already registered",
        )

    new_user = create_user(
        db,
        user,
    )

    return {
        "message": "Registration Successful",
        "user_id": new_user.id,
    }


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):

    db_user = authenticate_user(
        db,
        form_data.username,
        form_data.password,
    )

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    access_token = create_access_token(
        {
            "sub": db_user.email,
            "role": db_user.role,
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


@router.get("/me")
def read_me(
    current_user: User = Depends(get_current_user),
):

    return {
        "id": current_user.id,
        "full_name": current_user.full_name,
        "email": current_user.email,
        "phone": current_user.phone,
        "role": current_user.role,
    }


@router.put("/profile")
def profile_update(
    data: UpdateProfile,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):

    user = update_profile(
        db,
        current_user,
        data,
    )

    return {
        "message": "Profile Updated",
        "user": {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "phone": user.phone,
            "role": user.role,
        },
    }