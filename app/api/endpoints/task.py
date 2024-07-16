from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, insert   # noqa
from sqlalchemy.exc import NoResultFound  # noqa
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_cache.decorator import cache

from app.core.db import get_async_session
from app.core.user import auth_backend, fastapi_users, current_user  # noqa
from app.models import User, Task  # noqa
from app.schemas.task import TaskCreate, TaskUpdate
from app.crud.task import task_crud

router = APIRouter()


@router.get('/')
@cache(expire=30)
async def get_tasks(session: AsyncSession = Depends(get_async_session),
                    current_user: User = Depends(current_user)):
    """Пользователь получает список задач"""
    return await task_crud.get_tasks(session, current_user.id)


@router.get('/{task_id}')
@cache(expire=30)
async def read_task(task_id: int,
                    session: AsyncSession = Depends(get_async_session),
                    current_user: User = Depends(current_user)):
    """Пользователь получает задачу"""
    task = await task_crud.get_task(session, task_id, current_user.id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Запись не найдена")
    return task


@router.post('/')
async def create_task(new_task: TaskCreate,
                      session: AsyncSession = Depends(get_async_session),
                      current_user: User = Depends(current_user)):
    """Пользователь создает задачу"""
    existing_task = await session.execute(
        select(Task).filter_by(title=new_task.title, user_id=current_user.id))
    if existing_task.scalar() is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ты уже создавал запись с таким заголовком"
        )
    return await task_crud.create_task(session, new_task, current_user.id)


@router.put('/{task_id}')
async def update_task(task_id: int, modified_task: TaskUpdate,
                      session: AsyncSession = Depends(get_async_session),
                      current_user: User = Depends(current_user)):
    """Пользователь обновляет задачу"""
    task = await task_crud.update_task(session, task_id, modified_task, current_user.id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Запись не найдена или вы пытаетесь редактировать чужую запись!")
    return task


@router.delete("/{task_id}")
async def delete_task(task_id: int,
                      session: AsyncSession = Depends(get_async_session),
                      current_user: User = Depends(current_user)):
    """Пользователь удаляет задачу"""
    task = await task_crud.delete_task(session, task_id, current_user.id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Запись не найдена или вы пытаетесь удалить чужую запись!")
    return task