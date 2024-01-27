import os

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from dotenv import load_dotenv

load_dotenv()

TORTOISE_ORM = {
    "connections": {"default": os.getenv("DATABASE_URL")},
    "apps": {
        "models": {
            "models": ["src.database.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=os.getenv("DATABASE_URL"),
        modules={"models": ["src.database.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
