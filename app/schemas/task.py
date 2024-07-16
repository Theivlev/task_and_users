from pydantic import BaseModel
from typing import Optional


class TaskBase(BaseModel):
    """Модель записи"""
    title: str
    description: Optional[str] = None


class TaskCreate(TaskBase):
    """Модель создания записи"""
    pass


class TaskUpdate(TaskBase):
    """Модель обновления записи"""
    pass
