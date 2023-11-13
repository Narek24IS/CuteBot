import sqlite3
import requests
from aiogram.types import Message
from config import load_config, Config
from lexicon import ANSWER_LEXICON_RU

config: Config = load_config()


def load_users_id() -> list[int]:
    with sqlite3.connect("CuteBotDB.db") as connection:
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY UNIQUE,
                    username TEXT,
                    name TEXT
                )''')

        cursor.execute("SELECT * FROM users")
        users_id_list:list[int] = [row[0] for row in cursor.fetchall()]

    return users_id_list


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
    with sqlite3.connect("CuteBotDB.db") as connection:
        cursor = connection.cursor()
        try:
            # Начинаем транзакцию автоматически
            with connection:
                if sender_id not in users_id:
                    cursor.execute("INSERT INTO users (id, username, name) VALUES (?, ?, ?)",
                                   (sender_id, username, name))
                    print('ИД сохранён')
                    connection.commit()

            return load_users_id()

        except Exception as ex:
            # Ошибки будут приводить к автоматическому откату транзакции
            print(ex)
            print('Ошибка при сохранении ИД')
            return load_users_id()


async def send_animal_photo(message: Message, animal: str) -> None:
    photo_link: str = ''
    animal = animal.lower()
    if "соба" in animal:
        dog_req = requests.get(config.api.dog)
        if dog_req.status_code == 200:
            photo_link = dog_req.json()['url']
        else:
            print('Ошибка получения фото собаки')
            await message.answer(ANSWER_LEXICON_RU.no_dog)
    elif ("кот" in animal) or ("кош" in animal):
        cat_req = requests.get(config.api.cat)
        if cat_req.status_code == 200:
            photo_link = cat_req.json()[0]['url']
        else:
            print('Ошибка получения фото кошки')
            await message.answer(ANSWER_LEXICON_RU.no_cat)
    elif "лис" in animal:
        fox_req = requests.get(config.api.fox)
        if fox_req.status_code == 200:
            photo_link = fox_req.json()['image']
        else:
            print('Ошибка получения фото лисы')
            await message.answer(ANSWER_LEXICON_RU.no_fox)
    else:
        await message.answer(ANSWER_LEXICON_RU.bot_cant)

    if photo_link:
        await message.answer_photo(photo_link)

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

