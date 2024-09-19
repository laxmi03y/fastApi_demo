from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class ToDo(Base):
    """This table is for storing todo app"""
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(String(255))
    completed = Column(Boolean)
    is_active = Column(Boolean)
