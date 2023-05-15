class InvalidCommandException(Exception):
    """Класс исключений при вводе комманд пользователем"""


class StorageAccessException(Exception):
    """Класс исключений при работе с хранилищем данных"""


class RegionNotDefinedExeption(Exception):
    """
    Класс исключений возникающих при отсутствии данных
    о регионе пользователя
    """


class KeywordNotDefinedExeption(Exception):
    """
    Класс исключений возникающих при отсутствии данных
    о ключевом слове пользователя
    """


class IdNotDefinedExeption(Exception):
    """
    Класс исключений возникающих при отсутствии данных
    об id пользователя
    """
