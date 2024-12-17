from typing import Annotated
from pydantic import Field
from . import baseDto, order

__all__ = [
    "Employee",
    "EmployeeWithId",
    "EmployeeWithOrders"
]


class Employee(baseDto.Base):
    fio: Annotated[str, Field()]
    experience: Annotated[int, Field()]
    salary: Annotated[int, Field()]


class EmployeeWithId(Employee):
    id: Annotated[int, Field()]


class EmployeeWithOrders(EmployeeWithId):
    orders: list[order.Order]
