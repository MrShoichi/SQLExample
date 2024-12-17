from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession

import schemas
from api.employee import services
from utils.dependency import get_session

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.get("/", response_model=list[schemas.EmployeeWithOrders])
async def get_employees(session: Annotated[AsyncSession, Depends(get_session)]):
    return await services.get_employees(session)


@router.post("/add", response_model=schemas.EmployeeWithId)
async def get_employees(employee: schemas.Employee,
                        session: Annotated[AsyncSession, Depends(get_session)]):
    try:
        return await services.create_employee(employee, session=session)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.patch("/update", response_model=schemas.EmployeeWithId)
async def update_employee(employee: schemas.EmployeeWithId,
                        session: Annotated[AsyncSession, Depends(get_session)]):
    try:
        return await services.update_employee(employee, session=session)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{employee_id}", response_model=schemas.InfoMessage)
async def delete_employee(employee_id: Annotated[int, Path(ge=1)],
                        session: Annotated[AsyncSession, Depends(get_session)]):
    try:
        return await services.delete_employee(employee_id, session=session)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))