import json
import os
import datetime
from pathlib import Path

DATA_DIR = "data"

class Vacancy:
    def __init__(self, name, company, salary, link) -> None:
        self.name = name
        self.company = company
        self.salary = salary
        self.link = link

def write_data(request_data: dict):
    data_dir_path = set_path_to_data_dir()
    address = request_data["id"] + ".json"
    file_path = set_file_path(address, data_dir_path)
    if file_path.exists() and file_path.is_file():
        request_data = merge_with_user_data(request_data, file_path)
    write_data_to_json_file(request_data, file_path)


def set_path_to_data_dir():
    path = Path(".")
    data_dir_path = path / DATA_DIR
    if data_dir_path.exists() and data_dir_path.is_dir():
        return data_dir_path
    data_dir_path.mkdir()
    return data_dir_path


def set_file_path(file_name: str, data_dir_path: Path):
    file_path = data_dir_path / file_name
    return file_path


def merge_with_user_data(request: dict, file_path: Path):
    with open(file_path.as_posix(), "r", encoding="utf-8") as file:
        file_contents = json.load(file)
    for key in request:
        if request[key]:
            file_contents[key] = request[key]
    return file_contents


def write_data_to_json_file(data, file_path):
    with open(file_path.as_posix(), "w", encoding="utf-8") as file:
        json.dump(data, file)


def create_list_vacancies(list_company: tuple) -> list:
     """Создание списка словарей вакансий"""
     list_vacancies = list()
     for i in range(len(list_company[1])):
        list_vacancies.append(create_dict_vacancy(list_company[1][i]))
     return list_vacancies


def create_dict_vacancy(vacancy: tuple) -> dict:
    """Создание словаря вакансии из объекта"""
    new_vacancy = create_vacancy_from_tuple(vacancy)
    return new_vacancy.__dict__


def create_vacancy_from_tuple(vacancy_data: tuple) -> str:
     """Создание объекта класса Vacancy из кортежа"""
     return  Vacancy(vacancy_data[0], vacancy_data[1], vacancy_data[2], vacancy_data[3])


def create_path(list_vacancy: tuple) -> str:
    """Формирование полного названия файла"""
    return PATH + list_vacancy[0] + ".json"


def save_list_vacancies(list_company: list) -> None:
    """Сохранение списка вакансий в файл"""
    list_vacancies = create_list_vacancies(list_company)
    name = create_path(list_company)
    if check_data(PATH):
        with open(name, "w") as jsonfile:
            json.dump(list_vacancies,
                      jsonfile,
                      sort_keys=False,
                      indent=4,
                      ensure_ascii=False,
                      separators=(',', ': '))


def check_data(PATH: str) -> bool:
    """Проверка наличия папки data"""
    if not os.path.exists(PATH):
        create_dir(PATH)
    return True


def create_dir(PATH: str) -> None:
    """Создание папки data"""
    return os.mkdir(PATH)


if __name__ == "__main__":

    list_vacancy = ( "NEW_ID_153621", [('Java разработчик', 'Sportmaster Lab', '', 'https://career.habr.com/vacancies/1000080748'),
                ('Java-разработчик', 'Okko', '', 'https://career.habr.com/vacancies/1000102160'),
                ('Java Developer', 'Aston (ex. Andersen)', '', 'https://career.habr.com/vacancies/1000119776'),
                ('Java-разработчик', 'Сбер', '', 'https://career.habr.com/vacancies/1000112743'),
                ('Java-разработчик', 'МегаФон', '', 'https://career.habr.com/vacancies/1000123570'),
                ('Разработчик Java', 'TINKOFF', '', 'https://career.habr.com/vacancies/1000121969'),
                ('Java-разработчик', 'Bell Integrator', '', 'https://career.habr.com/vacancies/1000115597')])

    save_list_vacancies(list_vacancy)
