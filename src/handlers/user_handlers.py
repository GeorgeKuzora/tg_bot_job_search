from datetime import datetime
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from src.errors.errors import InvalidCommandException
from src.lexicons.lexicon import LexiconRu
import src.controllers.tg_controller as ctrl


lexicon_ru: LexiconRu = LexiconRu()
router: Router = Router()
UNDEFINED_STR: str = "undefined"
UNDEFINED_DATE: datetime = datetime.now()


@router.message(Command(commands=["start"]))
async def process_start_command(message: Message) -> None:
    """Функция для обработки команды пользователя: /start"""
    await message.answer(lexicon_ru.get_start_command_answer())
    user: ctrl.User = ctrl.User(
        str(message.chat.id),
        message.chat.username,
    )
    fullname: ctrl.Fullname = ctrl.Fullname(
        message.date,
        user,
        f"{message.chat.first_name} _ {message.chat.last_name}",
    )
    controler = ctrl.Controler(fullname)
    controler.send_request()


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
        Controller.set_region_data(region_data)
    except InvalidCommandException:
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
        vacancies: list[tuple] = Controller.get_vacancy_list_by_keyword(keyword_data)
        await message.answer(lexicon_ru.get_keyword_command_results(vacancies))
    except InvalidCommandException:
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
        raise InvalidCommandException


def validate_message_text(message_text: str) -> None:
    """
    Функция для проверки был ли введн пользователем валидный текст команды.
    Если текст на валиден вызвает исключение InvalidCommandExeption.
    """
    if not message_text:
        raise InvalidCommandException
