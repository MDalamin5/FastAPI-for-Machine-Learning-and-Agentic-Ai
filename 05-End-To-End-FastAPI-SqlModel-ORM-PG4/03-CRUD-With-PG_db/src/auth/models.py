from sqlmodel import SQLModel, Field
import uuid
from datetime import datetime
from sqlmodel import Column
import sqlalchemy.dialects.postgresql as pg



"""
class User:
    uid: uuid.UUID
    username: str
    email: str
    first_name: 
    last_name: str
    is_verified: bool = false
    created_at: datetime
    updated_at: datetime
"""

from sqlmodel import SQLModel, Field
import uuid
from datetime import datetime

class User(SQLModel, table=True):
    __tablename__ = "users"

    uid: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False
    )

    username: str
    email: str
    first_name: str
    last_name: str
    is_verified: bool = Field(default=False)

    password_hash: str  # don’t exclude here → exclude in schema, not in model

    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    update_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"
