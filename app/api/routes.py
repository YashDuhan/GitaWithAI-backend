from fastapi import APIRouter
from .endpoints import root, health_check, fetch_chapters

app_router = APIRouter()

# Default route
app_router.get("/")(root)

# Health check route
app_router.get("/health")(health_check)

# Fetch chapters
app_router.get("/chapters")(fetch_chapters)

