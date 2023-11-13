from dataclasses import dataclass


# ---РЕАЛИЗАЦИЯ КЛАССОВ--- #
@dataclass
class BUTTONS_LEXICON:
    dog_button: str
    cat_button: str
    fox_button: str


@dataclass
class ANSWER_LEXICON:
    no_animal: str
    no_dog: str
    no_cat: str
    no_fox: str
    bot_cant: str


@dataclass
class COMMAND:
    command: str
    description: str
    answer: str


@dataclass
class COMMANDS_LEXICON:
    start: COMMAND
    help: COMMAND
    test: COMMAND


# ---СОЗДАНИЕ ЭКЗЕМПЛЯРОВ--- #
BUTTONS_LEXICON_RU = BUTTONS_LEXICON(
    dog_button='Собаку🦮',
    cat_button='Котика🐈',
    fox_button='Лисичку🦊'
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
