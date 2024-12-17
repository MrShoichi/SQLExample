import typing as tp

from pydantic import Field

from . import baseDto

__all__ = [
    'Order',
    "OrderWithId",
]


class Order(baseDto.Base):
    name: tp.Annotated[str, Field()]
    description: tp.Annotated[str, Field()]
    cost: tp.Annotated[int, Field()]
    employee_id: tp.Annotated[int, Field()]


class OrderWithId(Order):
    id: tp.Annotated[int, Field()]

