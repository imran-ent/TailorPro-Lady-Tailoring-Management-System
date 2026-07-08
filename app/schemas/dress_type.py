from pydantic import BaseModel, Field


class DressCreate(BaseModel):
    name: str = Field(..., min_length=2)

    image: str | None = None

    base_price: float