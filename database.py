from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./blog.db"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},# sqlite specific 
)
 
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# this class is used to tell sqlalchemy that the classes that will inherit from it will be database tables
class Base(DeclarativeBase):
    pass

# Create a database session, call it db, and automatically clean it up when we're finished
# It is a dependency function which is simply a normal Python function that provides something an endpoint needs.
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session   