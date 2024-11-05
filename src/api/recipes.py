from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api import crud as recipe_crud
from core.models import db_helper
from core.schemas.routes import Recipe

router = APIRouter(tags=["Рецепты"])


@router.get("/recipes", response_model=list[Recipe])
async def get_all_recipes(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),

    ],
):
    recipes = await recipe_crud.get_all_recipes(session=session)
    return recipes
