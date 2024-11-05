from pydantic import BaseModel


class MainPage(BaseModel):
    message: str = "Вы находитесь на главной странице"


class Recipe(BaseModel):
    id: int | None
    recipe_name: str
    cooking_time: int
    views: int | None
    recipe_description: str | None
