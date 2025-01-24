# main module
import os
import sys
from fastapi import FastAPI
# Routes are declared here
from app.api.routes import app_router

# enable cors
from fastapi.middleware.cors import CORSMiddleware
from app.cors_config import CORS_ORIGIN

# Check if running in dev container or Vercel only
if not (os.getenv('IS_DEVCONTAINER') or os.getenv('VERCEL')):
    print("\n⚠️  This application can only run inside a dev container or on Vercel\n")
    sys.exit(1)

app = FastAPI(title="Gita With AI Backend")

# to enable cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=[CORS_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Include the router
app.include_router(app_router)