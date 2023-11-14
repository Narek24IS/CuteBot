from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType,
                           WebAppInfo, InlineKeyboardButton)
from keyboards.keyboard_builders import Keyboard, InlineKeyboard
from lexicons.lexicon import BUTTONS_LEXICON_RU




animals_kb: ReplyKeyboardMarkup = Keyboard(BUTTONS_LEXICON_RU.dog_button,
                                           BUTTONS_LEXICON_RU.fox_button,
                                           BUTTONS_LEXICON_RU.cat_button)(2)

# Создаем кнопки
contact_btn = KeyboardButton(
    text='Отправить телефон',
    request_contact=True
)
geo_btn = KeyboardButton(
    text='Отправить геолокацию',
    request_location=True
)
poll_btn = KeyboardButton(
    text='Создать опрос/викторину',
    request_poll=KeyboardButtonPollType()
)
web_app_btn = KeyboardButton(
    text='Start Web App',
    web_app=WebAppInfo(url="https://stepik.org/")
)

# Создаем объект клавиатуры
test_keyboard: ReplyKeyboardMarkup = Keyboard(contact_btn, geo_btn, poll_btn, web_app_btn,
                                              is_persistent=True)(1)

# Создаем объекты инлайн-кнопок
big_button_1 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 1',
    callback_data='big_button_1_pressed'
)

big_button_2 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 2',
    callback_data='big_button_2_pressed'
)

big_button_3 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 3',
    callback_data='big_button_3_pressed'
)

# Создаем объект инлайн-клавиатуры
# inline_kb = InlineKeyboardMarkup(
#     inline_keyboard=[[big_button_1],
#                      [big_button_2],
#                      [big_button_3]]
# )

inline_kb = InlineKeyboard('big_button_1_pressed', big_button_2, big_button_3_pressed='БОЛЬШАЯ КНОПКА 3')(2)
