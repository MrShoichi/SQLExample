from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

url = 'sqlite+aiosqlite:///test.db'

engine = create_async_engine(url)
AsyncSession = async_sessionmaker(engine, autocommit=False, autoflush=False)

