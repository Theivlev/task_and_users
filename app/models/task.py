from sqlalchemy import Column, Integer, String, ForeignKey

from app.core.db import Base


class Task(Base):
    """Модель записи"""
    user_id = Column(Integer, ForeignKey("user.id"))
    title = Column(String)
    description = Column(String)
