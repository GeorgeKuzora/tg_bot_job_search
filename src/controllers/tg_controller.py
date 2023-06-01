from dataclasses import dataclass
from datetime import datetime
from typing import Any, Protocol
from src.interactors.interactor import Interactor


@dataclass
class User:
    id: str
    username: str | None


@dataclass
class Request(Protocol):

    @property
    def date(self) -> datetime: ...

    @property
    def user(self) -> User: ...

    @property
    def value(self) -> Any: ...

    def parse_request(self) -> dict: ...


@dataclass
class Fullname:
    date: datetime
    user: User
    value: str | None

    def parse_request(self) -> dict:
        return {
            "date": self.date,
            "id": self.user.id,
            "fullname": self.value,
        }


@dataclass
class Region:
    date: datetime
    user: User
    value: str | None

    def parse_request(self) -> dict:
        return {
            "date": self.date,
            "id": self.user.id,
            "region": self.value,
        }


@dataclass
class Keyword:
    date: datetime
    user: User
    value: str | None

    def parse_request(self) -> dict:
        return {
            "date": self.date,
            "id": self.user.id,
            "keyword": self.value,
        }


    """Класс для задания методов работы контроллера"""

    @staticmethod
    def set_user_data(user_data: tuple) -> None:
        """Метод для записи данных пользователя полученных от Bot API"""
        interface = Interactor()
        interface.set_user_data(user_data)

    @staticmethod
    def set_region_data(region_data: tuple) -> None:
        """Метод для записи данных региона полученных от Bot API"""
        interface = Interactor()
        interface.set_region_data(region_data)

    @staticmethod
    def get_vacancy_list_by_keyword(keyword_data: tuple) -> list[tuple]:
        """
        Метод для получения списка вакансий
        по запрошенному ключевому слову
        """
        return Interactor().get_vacancy_list(keyword_data)
