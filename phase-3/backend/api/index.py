# Vercel serverless entrypoint for the FastAPI app.
# Vercel's Python runtime imports `app` (ASGI) from this file.
import os
import sys

# Ensure the backend root (parent of api/) is on sys.path so `src.*` imports resolve.
BACKEND_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BACKEND_ROOT not in sys.path:
    sys.path.insert(0, BACKEND_ROOT)

from src.main import app  # noqa: E402
