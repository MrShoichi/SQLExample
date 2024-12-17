from fastapi import HTTPException
from sqlalchemy import sql
from sqlalchemy.orm import selectinload

import schemas
from models.db import AsyncSession
from models.employee import Employee
from models.order import Order


async def get_orders(session: AsyncSession):
    statement = sql.select(Order).options(selectinload(Order.employee))
    result = await session.execute(
        statement
    )
    return list(result.scalars().all())


async def create_order(
        order: schemas.Order,
        *,
        session: AsyncSession):
    employee = await session.execute(sql.select(Employee).filter(Employee.id == order.employee_id))
    employee = employee.scalar_one_or_none()

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    order = Order(**order.dict())
    order.employee = employee
    session.add(order)
    await session.commit()
    await session.refresh(order)
    return order


async def update_order(
        order: schemas.Order,
        *,
        session: AsyncSession):
    order = await session.execute(sql.select(Order).filter(Order.id == Order.id))
    order = order.scalar_one_or_none()

    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    for field, value in order.dict(exclude_unset=True).items():
        setattr(order, field, value)

    await session.commit()
    await session.refresh(order)

    return order


async def delete_order(
        order_id: int,
        *,
        session: AsyncSession):
    order = await session.execute(sql.select(Order).filter(Order.id == order_id))
    order = order.scalar_one_or_none()

    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    await session.delete(order)
    await session.commit()

    return schemas.InfoMessage()
