from lexicon import COMMANDS_LEXICON_RU, BUTTONS_LEXICON_RU, ANSWER_LEXICON_RU
from aiogram.filters import Command, CommandStart
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from config import load_config, Config
from services.functions import save_users_id, send_animal_photo, load_users_id
from keyboards import animals_kd, inline_keyboard

config: Config = load_config()
router = Router()
users_id = load_users_id()


@router.message(CommandStart())
async def process_start_command(message: Message) -> None:
    print('process_start_message')
    global users_id
    users_id = await save_users_id(message)
    await message.answer(COMMANDS_LEXICON_RU.start.answer,
                         reply_markup=animals_kd)


@router.message(Command(commands='help'))
async def process_help_command(message: Message) -> None:
    print('process_help_message')
    global users_id
    users_id = await save_users_id(message)
    await message.answer(COMMANDS_LEXICON_RU.help.answer,
                         reply_markup=inline_keyboard)


@router.callback_query(F.data == 'big_button_1_pressed')
async def process_button_1_press(callback: CallbackQuery):
    await callback.message.answer(text='Была нажата БОЛЬШАЯ КНОПКА 1')


@router.callback_query(F.data == 'big_button_2_pressed')
async def process_button_2_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Была нажата БОЛЬШАЯ КНОПКА 2',
        reply_markup=callback.message.reply_markup
    )

@router.callback_query(F.data == 'big_button_3_pressed')
async def process_button_3_press(callback: CallbackQuery):
    await callback.answer(text='Была нажата БОЛЬШАЯ КНОПКА 3')

@router.message(F.text == BUTTONS_LEXICON_RU.dog_button)
async def process_dog_message(message: Message) -> None:
    print('process_dog_message')
    global users_id
    users_id = await save_users_id(message)
    await send_animal_photo(message, BUTTONS_LEXICON_RU.dog_button)


@router.message(F.text == BUTTONS_LEXICON_RU.fox_button)
async def process_fox_message(message: Message) -> None:
    print('process_fox_message')
    global users_id
    users_id = await save_users_id(message)
    await send_animal_photo(message, BUTTONS_LEXICON_RU.fox_button)


@router.message(F.text == BUTTONS_LEXICON_RU.cat_button)
async def process_cat_message(message: Message) -> None:
    print('process_cat_message')
    global users_id
    users_id = await save_users_id(message)
    await send_animal_photo(message, BUTTONS_LEXICON_RU.cat_button)



@router.message(F.text.lower().startswith('хочу'))
async def process_cute_message(message: Message) -> None:
    print('process_cute_message')
    global users_id
    users_id = await save_users_id(message)
    if len(message.text.split()) < 2:
        await message.answer(ANSWER_LEXICON_RU.no_animal)
    else:
        await send_animal_photo(message, message.text.lower())




# @router.message(F.photo[0].as_('photo_min'))
# async def process_photo_send(message: Message, photo_min: PhotoSize):
#     print(photo_min)


@router.message()
async def process_message(message: Message) -> None:
    print('process_message')
    global users_id
    users_id = await save_users_id(message)
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.send_copy(chat_id=message.from_user.id)
    # for chat_id in users_id:
    #     await message.send_copy(chat_id=chat_id)

