from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.database.database import init_db
from src.routers import notes
from src.logger import logger
from starlette.middleware.base import BaseHTTPMiddleware
from src.middleware import log_middleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)
logger.info('Starting API...')

# routes
app.include_router(notes.router)


@app.on_event("startup")
async def startup_event():
    print("INITIALISING DATABASE")
    init_db(app)
