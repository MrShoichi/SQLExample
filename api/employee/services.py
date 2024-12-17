from fastapi import HTTPException
from sqlalchemy import sql
from sqlalchemy.orm import selectinload

import schemas
from models.db import AsyncSession
from models.employee import Employee


async def get_employees(session: AsyncSession):
    result = await session.execute(
        sql.select(Employee).options(selectinload(Employee.orders))
    )
    return list(result.scalars().all())


async def create_employee(
        employee: schemas.Employee,
        *,
        session: AsyncSession):
    db_employee = Employee(**employee.dict())
    session.add(db_employee)
    await session.commit()
    await session.refresh(db_employee)
    return db_employee


async def update_employee(
        employee: schemas.Employee,
        *,
        session: AsyncSession):
    db_employee = await session.execute(sql.select(Employee).filter(Employee.id == employee.id))
    db_employee = db_employee.scalar_one_or_none()

    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    for field, value in employee.dict(exclude_unset=True).items():
        setattr(db_employee, field, value)

    await session.commit()
    await session.refresh(db_employee)

    return db_employee


async def delete_employee(
        employee_id: int,
        *,
        session: AsyncSession):
    db_employee = await session.execute(sql.select(Employee).filter(Employee.id == employee_id))
    db_employee = db_employee.scalar_one_or_none()

    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    await session.delete(db_employee)
    await session.commit()

    return schemas.InfoMessage()
