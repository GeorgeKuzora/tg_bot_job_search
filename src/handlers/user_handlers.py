from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from src.errors.errors import InvalidCommandExeption
from src.lexicons.lexicon import LexiconRu


lexicon_ru: LexiconRu = LexiconRu()
router: Router = Router()

@router.message(Command(commands=["start"]))
async def process_start_command(message: Message) -> None:
    """Функция для обработки команды пользователя: /start"""
    await message.answer(lexicon_ru.get_start_command_answer())
    user_data: tuple = (
        message.date,
        message.chat.id,
        message.chat.username,
        message.chat.first_name,
        message.chat.last_name,
    )
    # controller = Controller()
    # controller.set_user_data(user_data)


@router.message(Command(commands=["region"]))
async def process_region_command(message: Message) -> None:
    """Функция для обработки команды пользователя: /region"""
    try:
        region = set_message_text(message)
        region_data: tuple = (
            message.date,
            message.chat.id,
            message.chat.username,
            region.lower(),
        )
        await message.answer(lexicon_ru.get_region_command_answer(region))
        # controller = Controller()
        # controller.set_region_data(region_data)
    except InvalidCommandExeption:
        await message.answer(lexicon_ru.get_invalid_region_command_answer())


@router.message(Command(commands=["keyword"]))
async def process_keyword_command(message: Message) -> None:
    """Функция для обработки команды пользователя: /keyword"""
    try:
        keyword: str = set_message_text(message)
        keyword_data: tuple = (
            message.date,
            message.chat.id,
            message.chat.username,
            keyword.lower(),
        )
        await message.answer(lexicon_ru.get_keyword_command_answer(keyword))
        # controller = Controller()
        # controller.set_keyword_data(keyword_data)
        # vacancy_list = controller.get_vacancy_list()
        # await message.answer(lexicon_ru.get_keyword_command_results(vacancies_data))
    except InvalidCommandExeption:
        await message.answer(lexicon_ru.get_invalid_keyword_command_answer())


@router.message()
async def process_other_input(message: Message) -> None:
    """Функция для сообщения о том что ввод не распознан"""
    await message.answer(lexicon_ru.get_invalid_command_answer())


def set_message_text(message: Message) -> str:
    """
    Функция для извлечение текста пользователя из введенной комманды.
    Если возникает IndexError вызвается InvalidCommandExeption"""
    try:
        message_text = message.text.split(maxsplit=1)[1]
        validate_message_text(message_text)
        return message_text
    except IndexError:
        raise InvalidCommandExeption


def validate_message_text(message_text: str) -> None:
    """
    Функция для проверки был ли введн пользователем валидный текст команды.
    Если текст на валиден вызвает исключение InvalidCommandExeption.
    """
    if not message_text:
        raise InvalidCommandExeption
