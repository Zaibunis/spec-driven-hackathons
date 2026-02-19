import os
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import logging

from src.config import settings
from src.models.database import init_db
from src.api.routes.tasks import router as tasks_router
from src.api.routes.auth import router as auth_router
from src.api.routes.chat import router as chat_router

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.log_level.upper()),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Run DB init fast, non-blocking
    try:
        init_db()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.warning(f"Database init skipped or failed: {e}")
    yield
    logger.info("Application shutdown complete")

# Create FastAPI app
app = FastAPI(
    title="Task API",
    description="RESTful API for task management with user isolation",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS for Vercel frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8000", "https://phase-3-six.vercel.app", "http://127.0.0.1:61864"],  # Frontend URLs
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, OPTIONS sab allow
    allow_headers=["*"],  # Content-Type, Authorization etc.
)

# Include routers
app.include_router(tasks_router, prefix="/v1/tasks", tags=["tasks"])
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(chat_router, prefix="/api/v1", tags=["chat"])

# Health check
@app.get("/health", tags=["health"])
@app.get("/", tags=["health"])  # HF ping root for readiness
async def health_check():
    return {"status": "healthy"}

# Exception handlers
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code in (401, 403):
        detail = exc.detail
        if isinstance(detail, dict):
            return JSONResponse(status_code=exc.status_code, content={"error": detail})
        else:
            return JSONResponse(
                status_code=exc.status_code,
                content={"error": {"code": str(exc.status_code), "message": str(detail)}}
            )
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unexpected error: {exc}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"error": {"code": "INTERNAL_ERROR", "message": "An unexpected error occurred", "details": None}}
    )

# === HUGGING FACE ENTRYPOINT ===
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 7860))  # HF requires $PORT
    uvicorn.run(app, host="0.0.0.0", port=port)