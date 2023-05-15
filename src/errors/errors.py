class InvalidCommandException(Exception):
    """Класс исключений при вводе комманд пользователем"""


class StorageAccessException(Exception):
    """Класс исключений при работе с хранилищем данных"""


class RegionNotDefinedExeption(Exception):
    """
    Класс исключений возникающих при отсутствии данных
    о регионе пользователя
    """
