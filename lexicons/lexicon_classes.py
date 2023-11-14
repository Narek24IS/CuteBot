from dataclasses import dataclass


# ---РЕАЛИЗАЦИЯ КЛАССОВ--- #
@dataclass
class BUTTONS_LEXICON:
    dog_button: str
    cat_button: str
    fox_button: str

    big_button_1_pressed:str


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