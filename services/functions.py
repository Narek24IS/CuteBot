import sqlite3
import requests
from aiogram.types import Message
from config.config import config
from lexicons.lexicon import ANSWER_LEXICON_RU
from services.db_connection import bot_database

# config: Config = load_config()


def load_users_id() -> list[int]:
    return bot_database.get_table_data_as_dict('users').keys()

# users_id = load_users_id()
users_id = load_users_id()


# Восстановление ИД пользователей
# Сохранение ИД пользователей в файл
async def save_users_id(message: Message) -> list[int]:
    name = message.from_user.first_name
    sender_id = message.from_user.id
    username = message.from_user.username
    global users_id

    print(f'{message.from_user.first_name}: {message.text}')

    bot_database.user_interface.create_if_not_exists(sender_id, username, name)

    return load_users_id()


async def send_animal_photo(message: Message, animal: str) -> None:
    print('Отправление фото', end=" ")
    photo_link: str = ''
    animal = animal.lower()
    if "соба" in animal:
        print('собаки', end='. ')
        try:
            dog_req = requests.get(config.api.dog, timeout=3)
            if dog_req.status_code == 200:
                print('Фото получено', end=' ')
                photo_link = dog_req.json()['url']
            else:
                print('Ошибка получения фото собаки')
                await message.answer(ANSWER_LEXICON_RU.no_dog)
        except:
            print('Ошибка получения фото собаки')
            await message.answer(ANSWER_LEXICON_RU.no_dog)
    elif ("кот" in animal) or ("кош" in animal):
        print('кота', end='. ')
        cat_req = requests.get(config.api.cat)
        if cat_req.status_code == 200:
            print('Фото получено', end=' ')
            photo_link = cat_req.json()[0]['url']
        else:
            print('Ошибка получения фото кошки')
            await message.answer(ANSWER_LEXICON_RU.no_cat)
    elif "лис" in animal:
        print('лисы', end='. ')
        fox_req = requests.get(config.api.fox)
        if fox_req.status_code == 200:
            print('Фото получено', end=' ')
            photo_link = fox_req.json()['image']
        else:
            print('Ошибка получения фото лисы')
            await message.answer(ANSWER_LEXICON_RU.no_fox)
    else:
        await message.answer(ANSWER_LEXICON_RU.bot_cant)

    if photo_link:
        await message.answer_photo(photo_link)
        print('и отправлено!')

# Создаем список с командами и их описанием для кнопки menu
# async def set_main_menu(bot: Bot):
#     main_menu_commands = [
#         BotCommand(command='/start',
#                    description='Начать общение'),
#         BotCommand(command='/help',
#                    description='Справка по работе бота')
#     ]
#
#     await bot.set_my_commands(main_menu_commands)

