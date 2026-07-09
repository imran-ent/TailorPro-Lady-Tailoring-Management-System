from sqlalchemy.orm import Session

from app.models.measurement import Measurement
from app.schemas.measurement import MeasurementCreate


def create_measurement(
    db: Session,
    user_id: int,
    data: MeasurementCreate
):

    measurement = Measurement(
        customer_id=user_id,
        profile_name=data.profile_name,
        height=data.height,
        chest=data.chest,
        waist=data.waist,
        hip=data.hip,
        shoulder=data.shoulder,
        sleeve_length=data.sleeve_length,
        neck=data.neck,
        notes=data.notes,
    )

    db.add(measurement)
    db.commit()
    db.refresh(measurement)

    return measurement


def get_measurements(
    db: Session,
    user_id: int
):

    return (
        db.query(Measurement)
        .filter(
            Measurement.customer_id == user_id
        )
        .all()
    )
def get_measurement_by_id(
    db: Session,
    measurement_id: int,
    user_id: int
):

    return (
        db.query(Measurement)
        .filter(
            Measurement.id == measurement_id,
            Measurement.customer_id == user_id
        )
        .first()
    )
def update_measurement(
    db: Session,
    measurement: Measurement,
    data: MeasurementCreate
):

    measurement.profile_name = data.profile_name
    measurement.height = data.height
    measurement.chest = data.chest
    measurement.waist = data.waist
    measurement.hip = data.hip
    measurement.shoulder = data.shoulder
    measurement.sleeve_length = data.sleeve_length
    measurement.neck = data.neck
    measurement.notes = data.notes

    db.commit()
    db.refresh(measurement)

    return measurement
def delete_measurement(
    db: Session,
    measurement: Measurement
):

    db.delete(measurement)

    db.commit()
def get_measurement_by_id(db, measurement_id):

    return (
        db.query(Measurement)
        .filter(Measurement.id == measurement_id)
        .first()
    )


def update_measurement(db, measurement, data):

    measurement.profile_name = data.profile_name
    measurement.height = data.height
    measurement.chest = data.chest
    measurement.waist = data.waist
    measurement.hip = data.hip
    measurement.shoulder = data.shoulder
    measurement.sleeve_length = data.sleeve_length
    measurement.neck = data.neck
    measurement.notes = data.notes

    db.commit()
    db.refresh(measurement)

    return measurement


def delete_measurement(db, measurement):

    db.delete(measurement)

    db.commit()