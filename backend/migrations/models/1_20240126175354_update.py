from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "notes" ADD "message" VARCHAR(50) NOT NULL;
        ALTER TABLE "notes" ADD "description" VARCHAR(300) NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "notes" DROP COLUMN "message";
        ALTER TABLE "notes" DROP COLUMN "description";"""
