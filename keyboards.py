from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType, WebAppInfo, InlineKeyboardButton, \
    InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon import BUTTONS_LEXICON_RU


class Keyboard:
    def __init__(self, *buttons: str | KeyboardButton, resize_keyboard: bool = True,
                 is_persistent: bool = False, one_time_keyboard: bool = False):
        if isinstance(buttons[0], str):
            self.__buttons = [KeyboardButton(text=f'{button}') for button in buttons]
        else:
            self.__buttons = buttons
        self.resize_keyboard = resize_keyboard
        self.is_persistent = is_persistent
        self.one_time_keyboard = one_time_keyboard

    def __call__(self, width: int) -> ReplyKeyboardMarkup:
        kb_builder = ReplyKeyboardBuilder()
        kb_builder.row(*self.__buttons, width=width)
        keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=self.resize_keyboard,
                                                             is_persistent=self.is_persistent,
                                                             one_time_keyboard=self.one_time_keyboard)
        return keyboard


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
inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_1],
                     [big_button_2],
                     [big_button_3]]
)
