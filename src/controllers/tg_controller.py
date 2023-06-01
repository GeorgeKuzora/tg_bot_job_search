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


class Controler:
    """Класс для задания методов работы контроллера"""

    def __init__(self, request: Request) -> None:
        self.request: Request = request

    def send_request(self):
        Interactor.write_request(self.request.parse_request())

    def get_response(self):
        pass

    def _convert_none_to_undefined_value(self):
        pass
