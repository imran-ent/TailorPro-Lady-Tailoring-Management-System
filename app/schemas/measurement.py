from pydantic import BaseModel, Field


class MeasurementCreate(BaseModel):

    profile_name: str = Field(..., min_length=2)

    height: float

    chest: float

    waist: float

    hip: float

    shoulder: float

    sleeve_length: float

    neck: float

    notes: str | None = None