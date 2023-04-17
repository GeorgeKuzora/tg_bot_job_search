import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, Text
from aiogram.types import Message, ContentType
from exceptions import InvalidCommandExeption

TG_BOT_TOKEN: str = os.getenvb(b"TG_BOT_TOKEN", default=b"can't access token").decode(
    "utf-8"
)
bot: Bot = Bot(token=TG_BOT_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message) -> None:
    """Функция для обработки команды пользователя: /start"""
    await message.answer(
        "Привет!\nДоступны следующие комманды:\n"
        "/region - установить свой регион\n"
        "/keyword - получить вакансии по ключевому слову"
    )
    user_data: tuple = (
        message.date,
        message.chat.id,
        message.chat.username,
        message.chat.first_name,
        message.chat.last_name,
    )
    # controller = Controller()
    # controller.set_user_data(user_data)


@dp.message(Command(commands=["region"]))
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
        await message.answer(f"Вы задали регион: {region}")
        # controller = Controller()
        # controller.set_region_data(region_data)
    except InvalidCommandExeption:
        await message.answer(f"Вы не указали название региона")


@dp.message(Command(commands=["keyword"]))
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
        await message.answer(f"Вы задали ключевое слово: {keyword}")
        # controller = Controller()
        # controller.set_keyword_data(keyword_data)
    except InvalidCommandExeption:
        await message.answer(f"Вы не указали ключевое слово")


@dp.message()
async def process_other_input(message: Message) -> None:
    """Функция для сообщения о том что ввод не распознан"""
    await message.answer("Команда не распознана")


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


if __name__ == "__main__":
    dp.run_polling(bot)
