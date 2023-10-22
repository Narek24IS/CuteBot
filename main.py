import asyncio
import json
import requests
import os
from environs import Env
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, PhotoSize
from pprint import pprint

# Загрузка переменных окружения из файла .env
env = Env()
env.read_env()

# Создание констант
BOT_API_URL = "https://api.telegram.org/bot"
CAT_API_URL = "https://api.thecatapi.com/v1/images/search"
DOG_API_URL = "https://random.dog/woof.json"
FOX_API_URL = "https://randomfox.ca/floof/"
bot_token = env('BOT_TOKEN')
admin_id = env.int('ADMIN_ID')

bot = Bot(token=bot_token)
dp = Dispatcher()


# Сохранение ИД пользователей в файл
def save_users_id(message: Message) -> None:
    sender = message.from_user.first_name
    sender_id = message.from_user.id

    if sender not in users_id:
        users_id[sender] = sender_id
        with open("users_id.json", "w") as file:
            json.dump(users_id, file)
            print('ИД сохранён')


# Восстановление ИД пользователей
def load_users_id() -> dict:
    try:
        with open("users_id.json", "r") as file:
            users_id_dict: dict = json.load(file)
            print('ИД загружены:', end=' ')
            print(*users_id_dict.keys(), sep=', ')
            return users_id_dict
    except FileNotFoundError:
        print('Не удалось найти файл')
        return {}
    except:
        print('Не удалось загрузить ИД пользователей')
        return {}


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message) -> None:
    await message.answer("Добро пожаловать в обиталище милашек и из любителей!^_^")


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message) -> None:
    await message.answer("Заклинания для вызова милашек:"
                         "1. Хочу котика!"
                         "2. Хочу лисичку!"
                         "3. Хочу собачку!")


# @dp.message(F.photo)
# async def process_images(message: Message) -> None:
#     await message.answer('Вот ваше сжатое изображение:')
#     await message.answer_photo(message.photo[1].file_id)


@dp.message(F.text.lower().startswith('хочу'))
async def process_cute_message(message: Message) -> None:
    print(f'{message.from_user.first_name}: {message.text}')
    photo_link: str | None = None
    match message.text.lower():
        case _ if "кот" in message.text.lower():
            cat_req = requests.get(CAT_API_URL)
            if cat_req.status_code == 200:
                photo_link = cat_req.json()[0]['url']
                # for chat_id in users_id.values():
        case _ if "соба" in message.text.lower():
            dog_req = requests.get(DOG_API_URL)
            if dog_req.status_code == 200:
                photo_link = dog_req.json()['url']
        case _ if "лис" in message.text.lower():
            fox_req = requests.get(FOX_API_URL)
            if fox_req.status_code == 200:
                photo_link = fox_req.json()['image']
        case _ if len(message.text.split()) < 2:
            await message.answer('Что именно ты хочешь? Лисичку? Котика? Или собачку?')
        case _:
            await message.answer('Я такого пока не умею(')

    if photo_link:
        await message.answer_photo(photo_link)

@dp.message(F.photo[0].as_('photo_min'))
async def process_photo_send(message: Message, photo_min: PhotoSize):
    print(photo_min)

@dp.message()
async def process_message(message: Message) -> None:
    print(f'{message.from_user.first_name}: {message.text}')
    save_users_id(message)
    for chat_id in users_id.values():
        print(message.model_dump_json(indent=4, exclude_none=True))
        await message.send_copy(chat_id=chat_id, )


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == '__main__':
    users_id = load_users_id()
    asyncio.run(main())
