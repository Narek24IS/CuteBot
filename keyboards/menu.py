# Функция для настройки кнопки Menu бота
from aiogram import Bot
from aiogram.types import BotCommand

from lexicons.lexicon import COMMANDS_LEXICON_RU


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(
            command="/"+command.command,
            description=command.description
        ) for command in vars(COMMANDS_LEXICON_RU).values()
    ]
    await bot.set_my_commands(main_menu_commands)