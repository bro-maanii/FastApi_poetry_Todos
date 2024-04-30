from sqlalchemy import Boolean, Column, Integer, String

from .database import Base

# These classes are the SQLAlchemy models.
class Todos(Base):
    __tablename__ = "todos" #tells SQLAlchemy the name of the table to use in the database for each of these models.

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    # is_active = Column(Boolean, default=True)