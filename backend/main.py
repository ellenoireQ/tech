from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.routers import login

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="technical test api",
)

# CORS Settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(login.router, prefix="/login", tags=["login"])

# Global endpoints
@app.get("/", tags=["root"])
def root():
    return {"message": f"Welcome to {settings.APP_NAME}"}

@app.get("/health", tags=["root"])
def health_check():
    return {"status": "ok"}
