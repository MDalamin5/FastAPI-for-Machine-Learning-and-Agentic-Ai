import os
from sqlmodel import Session, create_engine
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
# A synchronous engine:
engine = create_engine(DATABASE_URL, echo=True, pool_size=10, max_overflow=20)

def get_session():
    with Session(engine) as session:
        yield session
