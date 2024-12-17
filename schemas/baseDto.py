from pydantic import BaseModel

__all__ = ['Base']


class Base(BaseModel):
    class Config:
        from_attributes = True
