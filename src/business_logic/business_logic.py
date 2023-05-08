from src.errors.errors import StorageAccessException


SET_AREAS: dict = {
    "россия": 113,
    "москва": 1,
    "санкт-петербург": 2,
    "владивосток": 22,
    "волгоград": 24,
    "воронеж": 26,
    "екатеринбург": 3,
    "казань": 88,
    "калуга": 43,
    "краснодар": 53,
    "красноярск": 54,
    "нижний новгород": 66,
    "новосибирск": 4,
    "ростов-на-дону": 76,
    "самара": 78,
    "саратов": 79,
    "сочи": 237,
    "уфа": 99,
    "ярославль": 112,
    "севастополь": 130,
    "симферополь": 131
    }

DEFAULT_AREA_CODE: int = SET_AREAS["россия"]


def construct_vacancy_request(storage_request: dict) -> tuple:
    """Класс для построения кортежа содержащего ключевое слово и регион"""
    keyword = get_keyword_from_storage_data(storage_request)
    region = get_region_from_storage_data(storage_request)
    vacancy_request = (keyword,
                       region)
    return vacancy_request


def get_region_from_storage_data(storage_request: dict) -> int:
    """Класс для получения данных о регионе из запроса к хранилищу данных"""
    if storage_request["region"] not in SET_AREAS:
        return DEFAULT_AREA_CODE
    return SET_AREAS[storage_request["region"]]


def get_keyword_from_storage_data(storage_request) -> str | None:
    """
    Класс для получения данных о ключевом слове из запроса к хранилищу данных
    """
    if not storage_request["keyword"]:
        raise StorageAccessException
    return storage_request["keyword"]
