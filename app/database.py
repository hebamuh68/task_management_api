from sqlmodel import SQLModel, create_engine, Session
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Use environment variable for database URL
sqlite_url = os.getenv("DATABASE_URL", "sqlite:///./task.db")
engine = create_engine(sqlite_url, echo=True)


def create_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
