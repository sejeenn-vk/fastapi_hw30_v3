from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.schemas.routes import MainPage, Recipe
router = APIRouter(tags=["Главная страница сайта"])


@router.get("/", response_model=MainPage)
def main_page():
    return {"message": "Вы находитесь на главной странице"}


@router.get("/recipes", response_model=list[Recipe])
async def get_all_recipes(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),

    ],
):
    recipes = await  
    return recipes
