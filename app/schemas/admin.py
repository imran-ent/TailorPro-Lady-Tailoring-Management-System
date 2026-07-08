from datetime import datetime

from pydantic import BaseModel


class AcceptOrder(BaseModel):
    appointment_date: datetime
    expected_delivery_date: datetime


class RejectOrder(BaseModel):
    rejection_reason: str


class UpdateStatus(BaseModel):
    status: str