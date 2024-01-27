from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "notes" DROP COLUMN "message";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "notes" ADD "message" VARCHAR(50) NOT NULL;"""
