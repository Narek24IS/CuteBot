from aiogram import Bot
from aiogram.types import BotCommand
from lexicon import COMMANDS_LEXICON_RU
from environs import Env
from dataclasses import dataclass


@dataclass
class ApiUrl:
    bot: str  # Начало ссылки на бота
    cat: str  # Ссылка на АПИ с котами
    dog: str  # Ссылка на АПИ с собаками
    fox: str  # Ссылка на АПИ с лисами


@dataclass
class BotConfig:
    token: str  # Токен для доступа к телеграм-боту
    admin_id: int  # Список id администраторов бота


@dataclass
class DatabaseConfig:
    database: str  # Название базы данных
    db_host: str  # URL-адрес базы данных
    db_user: str  # Username пользователя базы данных
    db_password: str  # Пароль к базе данных


@dataclass
class Config:
    api: ApiUrl
    bot: BotConfig
    db: DatabaseConfig


# Загрузка переменных окружения из файла .env
def load_config(path:str="") -> Config:
    # Считывание переменных окружения
    if path:
        env = Env()
        env.read_env(path)
    else:
        env = Env()
        env.read_env()

    full_config:Config = Config(
        api=ApiUrl(
            bot="https://api.telegram.org/bot",
            cat="https://api.thecatapi.com/v1/images/search",
            dog="https://random.dog/woof.json",
            fox="https://randomfox.ca/floof/"
        ),
        bot=BotConfig(
            token=env('BOT_TOKEN'),
            admin_id=env.int('ADMIN_ID')
        ),
        db=DatabaseConfig(
            database=env('DATABASE'),
            db_host=env('DB_HOST'),
            db_user=env('DB_USER'),
            db_password=env('DB_PASSWORD')
        )
    )

    return full_config



# Функция для настройки кнопки Menu бота
async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(
            command=command.command,
            description=command.description
        ) for command in vars(COMMANDS_LEXICON_RU).values()
    ]
    await bot.set_my_commands(main_menu_commands)

if __name__ == '__main__':
    config = load_config()