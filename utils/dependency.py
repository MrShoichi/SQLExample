from contextlib import asynccontextmanager

from sqlalchemy.exc import SQLAlchemyError

from models.db import AsyncSession
import typing as tp


@asynccontextmanager
async def get_db():
    session = AsyncSession()

    try:
        yield session
    except SQLAlchemyError as err:
        await session.rollback()
        raise err
    finally:
        await session.close()


async def get_session() -> tp.AsyncGenerator[AsyncSession, None]:
    async with get_db() as session:
        yield session
