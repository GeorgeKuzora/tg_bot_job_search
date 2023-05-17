from src.errors.errors import (
    IdNotDefinedExeption,
    KeywordNotDefinedExeption,
)
from collections import namedtuple


SET_AREAS: dict = {
    "россия": "113",
    "москва": "1",
    "санкт-петербург": "2",
    "владивосток": "22",
    "волгоград": "24",
    "воронеж": "26",
    "екатеринбург": "3",
    "казань": "88",
    "калуга": "43",
    "краснодар": "53",
    "красноярск": "54",
    "нижний новгород": "66",
    "новосибирск": "4",
    "ростов-на-дону": "76",
    "самара": "78",
    "саратов": "79",
    "сочи": "237",
    "уфа": "99",
    "ярославль": "112",
    "севастополь": "130",
    "симферополь": "131",
}

DEFAULT_AREA_CODE: str = SET_AREAS["россия"]


class VacancyRequestHandler:
    """Класс для построения запроса для получения списка вакансий"""

    SerializedRequest = namedtuple("SerializedRequest", "region keyword")

    def __init__(self, user_id: str, region: str, keyword: str) -> None:
        """Конструктор объекта"""
        self.user_id: str = self._set_user_id(user_id)
        self.region: str = self._set_region(region)
        self.keyword: str = self._set_keyword(keyword)

    def _set_region(self, region: str) -> str:
        """
        Функция для установки атрибута region
        """
        if region not in SET_AREAS:
            return DEFAULT_AREA_CODE
        return SET_AREAS[region]

    def _set_keyword(self, keyword: str) -> str:
        """
        Функция для установки атрибута keyword
        """
        if not keyword:
            raise KeywordNotDefinedExeption
        return keyword

    def _set_user_id(self, user_id: str) -> str:
        """
        Функция для установки атрибута id
        """
        if not user_id:
            raise IdNotDefinedExeption
        return user_id

    @property
    def request(self) -> SerializedRequest:
        """
        Функция для построения кортежа содержащего регион и ключевое слово
        """
        return self.SerializedRequest(region=self.region, keyword=self.keyword)

    def get_full_results(self, raw_results: list[list[tuple]]) -> list[tuple]:
        full: list = []
        for part in raw_results:
            full += part
        return full

