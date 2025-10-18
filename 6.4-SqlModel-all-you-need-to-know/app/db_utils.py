# app/db_utils.py
import os
from sqlmodel import create_engine, Session
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("BLOG_POSTGRES_SQL")

if not DATABASE_URL:
    raise ValueError("❌ BLOG_POSTGRES_SQL not found in environment variables.")

engine = create_engine(DATABASE_URL, echo=False)

def get_session():
    return Session(engine)
