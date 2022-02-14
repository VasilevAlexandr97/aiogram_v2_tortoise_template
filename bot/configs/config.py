import configparser
from dataclasses import dataclass
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE_PATH = BASE_DIR.joinpath("configs/config.ini")

print(BASE_DIR)


@dataclass
class DbConfig:
    host: str
    port: str
    user: str
    password: str
    name: str


@dataclass
class MongoDbConfig:
    name: str


@dataclass
class TgBot:
    token: str
    admin_id: str
    bot_username: str


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    mongodb: MongoDbConfig


def load_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)

    tg_bot = config["tg_bot"]

    return Config(
        tg_bot=TgBot(
            token=tg_bot["token"],
            admin_id=int(tg_bot["admin_id"]),
            bot_username=tg_bot["bot_username"]
        ),
        db=DbConfig(**config["db"]),
        mongodb=MongoDbConfig(
            config["mongodb"]["name"]
        )
    )


config = load_config(str(CONFIG_FILE_PATH))


# Postgresql settings

DATABASE_PATH = (
    f"postgres://{config.db.user}:{config.db.password}"
    f"@{config.db.host}:{config.db.port}/{config.db.name}"
)
