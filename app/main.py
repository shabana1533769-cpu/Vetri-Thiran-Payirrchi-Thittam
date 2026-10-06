from Fastapi import FastAPI
from Fastapi.staticfiles import StaticFiles

from app.database import init_db
from app.routes import router

app = FastAPI(
    title="FitBuddy - AI Fitness Plan Generator",
    description="AI-powered personalized fitness plan generator using Gemini.",
    version="1.0.0",
)

# Serve CSS/static files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# Register application routes
app.include_router(router)