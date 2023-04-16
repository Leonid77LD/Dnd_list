"""DButils module."""

from fastapi import Depends

from app.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession


async def execute_command_insert(stmt, session: AsyncSession = Depends(get_async_session)):
    """Выполнить команду SQL."""
    await session.execute(stmt)
    await session.commit()
    return True
