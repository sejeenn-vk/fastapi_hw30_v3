from fastapi import APIRouter
from core.config import settings
from .all_routes import router as main_page

router = APIRouter()
router.include_router(main_page)
