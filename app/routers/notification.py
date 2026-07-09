from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database import get_db
from app.models.user import User
from app.services.notification_service import get_notifications

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"],
)


@router.get("/")
def notifications(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_notifications(
        db,
        current_user.id,
    )