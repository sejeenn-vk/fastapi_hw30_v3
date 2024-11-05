from pydantic import BaseModel


class MainPage(BaseModel):
    message: str = "Вы находитесь на главной странице"


class Recipe(BaseModel):
    ...