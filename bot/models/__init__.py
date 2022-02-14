from bot.configs.config import DATABASE_PATH
from tortoise import Tortoise


async def connect_db() -> None:
    print("connect to database")
    await Tortoise.init(
        db_url=DATABASE_PATH,
        modules={'models': ['bot.models.user']}
    )
    await Tortoise.generate_schemas()
    print("connection established")


async def disconnect_db() -> None:
    await Tortoise.close_connections()
    print("disconnect from the database")