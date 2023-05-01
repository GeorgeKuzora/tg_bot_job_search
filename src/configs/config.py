from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    """Класс данных для хранения информации о боте"""
    token: str

@dataclass
class Config:
    """Класс данных для хранения конфигурации приложения"""
    tg_bot: TgBot
    
def load_config(path: str | None):
    """Функция для загрузки конфигурации приложения"""
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env("BOT_TOKEN")))
