
# In this file we will create our database/sqlalchemy models

from .database import Base
from sqlalchemy import Boolean, Column, Integer, String, DateTime, TIMESTAMP
from datetime import datetime
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

class User(Base):
        __tablename__ = "users"
        id = Column(Integer, primary_key=True, nullable=False)
        email = Column(String, nullable=False, unique=True)
        password = Column(String, nullable=False)
        access_count = Column(Integer, default=10, nullable=False)
        created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('(CURRENT_TIMESTAMP)'))
