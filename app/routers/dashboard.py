from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_user
from app.models.user import User
from app.database import get_db
from sqlalchemy.orm import Session

from app.services.dashboard_service import get_customer_dashboard

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get("/")
def dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_customer_dashboard(
        db,
        current_user,
    )