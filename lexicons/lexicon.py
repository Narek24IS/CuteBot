from lexicons.lexicon_classes import BUTTONS_LEXICON, ANSWER_LEXICON, COMMAND, COMMANDS_LEXICON

# ---СОЗДАНИЕ ЭКЗЕМПЛЯРОВ--- #
BUTTONS_LEXICON_RU = BUTTONS_LEXICON(
    dog_button='Собаку🦮',
    cat_button='Котика🐈',
    fox_button='Лисичку🦊',

    big_button_1_pressed='БОЛЬШАЯ КНОПКА 1'
)


ANSWER_LEXICON_RU = ANSWER_LEXICON(
    no_animal='Что именно ты хочешь? Лисичку? Котика? Или собачку?',
    no_dog='Не нашли собачку',
    no_cat='Не нашли кошку',
    no_fox='Не нашли лисичку',
    bot_cant='Я такого пока не умею('
)

HELP_COMMAND_RU = COMMAND(
    command="help",
    description="Получить помощь",
    answer="Заклинания для вызова милашек:\n"
           "1. Хочу котика!\n"
           "2. Хочу лисичку!\n"
           "3. Хочу собачку!"
)

START_COMMAND_RU = COMMAND(
    command="start",
    description="Начать общение",
    answer="Добро пожаловать в обиталище милашек и из любителей!^_^\n"
           "Кого бы вы хотели увидеть?"
)

TEST_COMMAND_RU = COMMAND(
    command="test",
    description="Команда для тестов",
    answer="Пока ничего нет"
)

COMMANDS_LEXICON_RU = COMMANDS_LEXICON(
    start=START_COMMAND_RU,
    help=HELP_COMMAND_RU,
    test=TEST_COMMAND_RU
)
