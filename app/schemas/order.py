from pydantic import BaseModel


class OrderCreate(BaseModel):

    dress_type_id: int

    measurement_id: int

    special_instruction: str | None = None