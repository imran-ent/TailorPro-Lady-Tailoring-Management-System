from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database import get_db
from app.models.user import User
from app.schemas.measurement import MeasurementCreate
from fastapi import APIRouter, Depends, HTTPException
from app.services.measurement_service import (
    create_measurement,
    get_measurements,
    get_measurement_by_id,
    update_measurement,
    delete_measurement,
)

router = APIRouter(
    prefix="/measurements",
    tags=["Measurements"],
)


@router.post("/")
def add_measurement(
    data: MeasurementCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_measurement(
        db,
        current_user.id,
        data,
    )


@router.get("/")
def all_measurements(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_measurements(
        db,
        current_user.id,
    )
@router.get("/{measurement_id}")
def get_one_measurement(
    measurement_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    measurement = get_measurement_by_id(
        db,
        measurement_id,
        current_user.id,
    )

    if not measurement:
        raise HTTPException(
            status_code=404,
            detail="Measurement not found"
        )

    return measurement
@router.put("/{measurement_id}")
def edit_measurement(
    measurement_id: int,
    data: MeasurementCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    measurement = get_measurement_by_id(
        db,
        measurement_id,
        current_user.id,
    )

    if not measurement:
        raise HTTPException(
            status_code=404,
            detail="Measurement not found"
        )

    return update_measurement(
        db,
        measurement,
        data,
    )
@router.delete("/{measurement_id}")
def remove_measurement(
    measurement_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    measurement = get_measurement_by_id(
        db,
        measurement_id,
        current_user.id,
    )

    if not measurement:
        raise HTTPException(
            status_code=404,
            detail="Measurement not found"
        )

    delete_measurement(
        db,
        measurement,
    )

    return {
        "message": "Measurement deleted successfully"
    }
@router.put("/{measurement_id}")
def edit_measurement(
    measurement_id: int,
    data: MeasurementCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    measurement = get_measurement_by_id(
        db,
        measurement_id,
    )

    if not measurement:
        raise HTTPException(404, "Measurement not found")

    return update_measurement(
        db,
        measurement,
        data,
    )


@router.delete("/{measurement_id}")
def remove_measurement(
    measurement_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    measurement = get_measurement_by_id(
        db,
        measurement_id,
    )

    if not measurement:
        raise HTTPException(404, "Measurement not found")

    delete_measurement(
        db,
        measurement,
    )

    return {
        "message": "Measurement Deleted"
    }