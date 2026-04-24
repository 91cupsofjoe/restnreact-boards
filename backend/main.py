from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pathlib import Path
import os

# Routing is split among 3 different modules
from backend.routers.posts import posts_router
from backend.routers.users import users_router
from backend.routers.threads import threads_router

# Load settings.env (in root directory) for CORS and database parameters
settings_filepath = Path(__file__).parent / "settings.env"
load_dotenv(settings_filepath)

# Create FastAPI object
app = FastAPI()

# Get frontend credentials
origins = [(
    f"{os.getenv('FRONTEND_PROTOCOL')}://"
    f"{os.getenv('FRONTEND_HOST')}:"
    f"{os.getenv('FRONTEND_PORT')}"
)]

# Set frontend credentials
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Don't forget to include the routers from users, threads, and posts modules
app.include_router(users_router)
app.include_router(threads_router)
app.include_router(posts_router)