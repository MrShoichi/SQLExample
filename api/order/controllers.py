from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession

import schemas
from api.order import services
from utils.dependency import get_session

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.get("/", response_model=list[schemas.Order])
async def get_orders(session: Annotated[AsyncSession, Depends(get_session)]):
    return await services.get_orders(session)


@router.post("/add", response_model=schemas.OrderWithId)
async def add_order(order: schemas.Order,
                        session: Annotated[AsyncSession, Depends(get_session)]):
    try:
        return await services.create_order(order, session=session)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.patch("/update", response_model=schemas.OrderWithId)
async def update_order(order: schemas.OrderWithId,
                        session: Annotated[AsyncSession, Depends(get_session)]):
    try:
        return await services.update_order(order, session=session)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{order_id}", response_model=schemas.InfoMessage)
async def delete_order(order_id: Annotated[int, Path(ge=1)],
                        session: Annotated[AsyncSession, Depends(get_session)]):
    try:
        return await services.delete_order(order_id, session=session)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))