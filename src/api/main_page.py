from fastapi import APIRouter
from core.schemas.routes import MainPage, Recipe

router = APIRouter(tags=["Главная страница сайта"])


@router.get("/", response_model=MainPage)
def main_page():
    return {"message": "Вы находитесь на главной странице"}
