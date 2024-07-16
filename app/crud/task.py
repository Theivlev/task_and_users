from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models import Task
from app.schemas.task import TaskCreate, TaskUpdate


class CRUDTask:

    async def get_tasks(self, session: AsyncSession, user_id: int):
        """Получение записей"""
        query = select(Task).where(Task.user_id == user_id)
        result = await session.execute(query)
        return result.scalars().all()

    async def get_task(self, session: AsyncSession, task_id: int, user_id: int):
        """Получение записи"""
        query = select(Task).where(Task.id == task_id, Task.user_id == user_id)
        result = await session.execute(query)
        return result.scalars().first()

    async def create_task(self, session: AsyncSession, task: TaskCreate, user_id: int):
        """Создание записи"""
        db_task = Task(**task.dict(), user_id=user_id)
        session.add(db_task)
        await session.commit()
        await session.refresh(db_task)
        return db_task

    async def update_task(self, session: AsyncSession, task_id: int, task: TaskUpdate, user_id: int):
        """Обновление записи"""
        db_task = await session.get(Task, task_id)
        if db_task is None or db_task.user_id != user_id:
            return None
        for var, value in task.dict().items():
            setattr(db_task, var, value)
        await session.commit()
        return db_task

    async def delete_task(self, session: AsyncSession, task_id: int, user_id: int):
        """Удаление записи"""
        db_task = await session.get(Task, task_id)
        if db_task is not None and db_task.user_id == user_id:
            await session.delete(db_task)
            await session.commit()
            return db_task
        return None


task_crud = CRUDTask()