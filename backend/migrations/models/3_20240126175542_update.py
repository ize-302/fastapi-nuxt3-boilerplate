from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "notes" DROP COLUMN "description";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "notes" ADD "description" VARCHAR(300) NOT NULL;"""
