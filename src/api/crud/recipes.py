from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.recipe import Recipe


async def get_all_recipes(
        session: AsyncSession,
) -> Sequence[Recipe]:
    stmt = select(Recipe).order_by(Recipe.id)
    result = await session.scalars(stmt)
    return result.all()
