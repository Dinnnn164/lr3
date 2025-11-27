from pydantic import BaseModel
from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class BaseSchema(BaseModel):
    class Config:
        from_attributes = True

class ResponseSchema(BaseModel, Generic[T]):
    status: str
    message: str
    data: Optional[T] = None