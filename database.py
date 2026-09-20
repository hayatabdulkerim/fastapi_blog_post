from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"


engine = create_engine(
  SQLALCHEMY_DATABASE_URL,
  connect_args={"check_same_thread": False}, # sqlite specific 
)

# Factory that creates a session for each and every database interaction
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# this class is used to tell sqlalchemy that the classes that will inherit from it will be database tables
class Base(DeclarativeBase):
  pass

# Create a database session, call it db, and automatically clean it up when we're finished
# It is a dependency function which is simply a normal Python function that provides something an endpoint needs.
def get_db():
  with SessionLocal() as db:
    yield db

    