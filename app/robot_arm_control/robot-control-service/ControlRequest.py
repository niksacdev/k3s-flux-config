from pydantic import BaseModel
from datetime import datetime

class ControlRequestData(BaseModel):
    """Request to send in the post for control operations

    Args:
        BaseModel (_type_): _description_
    """
    servo: int | None = None
    angle: int | None = None
    time: int | None = None
    