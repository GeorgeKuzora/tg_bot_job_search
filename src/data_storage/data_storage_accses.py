import json
import os
import datetime

PATH = os.getcwd () +"/src/data_storage/data//"

class Vacancy:
    def __init__(self, name, company, salary, link) -> None:
        self.name = name
        self.company = company
        self.salary = salary
        self.link = link

class User:
    """Класс для работы с данными пользователя"""
    def __init__(self, user_id, region, keyword) -> None:
        self.user_id = user_id
        self.region = region
        self.keyword = keyword


def create_user_data(user_data: tuple) -> str:
    """Создание объекта класса User"""
    return User(user_data[0], user_data[1], user_data[2])


def create_list_vacancies(list_company: list) -> list:
     """Создание списка словарей вакансий"""
     list_vacancies = list()
     for i in range(len(list_company)):
        list_vacancies.append(create_dict_vacancy(list_company[i]))
     return list_vacancies


def create_dict_vacancy(vacancy: tuple) -> dict:
    """Создание словаря вакансии из объекта"""
    new_vacancy = create_vacancy_from_tuple(vacancy)
    return new_vacancy.__dict__


def create_vacancy_from_tuple(vacancy_data: tuple) -> str:
     """Создание объекта класса Vacancy из кортежа"""
     return  Vacancy(vacancy_data[0], vacancy_data[1], vacancy_data[2], vacancy_data[3])


def name_file(user_data: tuple) -> str:
    """Формирование имени файла"""
    new_user = create_user_data(user_data)
    now = str(datetime.datetime.now())
    return getattr(new_user, "user_id") + "_" + getattr(new_user, "region") + "_" +getattr(new_user, "keyword") + " " + now[:10]


def create_path(user_data: tuple) -> str:
    """Формирование полного названия файла"""
    return PATH + name_file(user_data) + ".json"


def save_list_vacancies(list_company: list) -> None:
    """Сохранение списка вакансий в файл"""
    list_vacancies = create_list_vacancies(list_company)
    name = create_path(user_data)
    if check_data(PATH):
        with open(name, "w") as jsonfile:
            json.dump(list_vacancies,
                      jsonfile,
                      sort_keys=False,
                      indent=4,
                      ensure_ascii=False,
                      separators=(',', ': '))

def read_list_vacancy(list_company: list):
     """Считывание списка вакансий из парсера"""
     for i in range(len(list_company)):
        new_vacancy = create_vacancy_from_tuple(list_company[i])
        json_str = create_json_str(new_vacancy)
        print(json_str)


def check_data(PATH: str) -> bool:
    """Проверка наличия папки data"""
    if not os.path.exists(PATH):
        create_dir(PATH)
    return True


def create_dir(PATH: str) -> None:
    """Создание папки data"""
    return os.mkdir(PATH)


if __name__ == "__main__":

    list_vacancy = [('Java разработчик', 'Sportmaster Lab', '', 'https://career.habr.com/vacancies/1000080748'),
                ('Java-разработчик', 'Okko', '', 'https://career.habr.com/vacancies/1000102160'),
                ('Java Developer', 'Aston (ex. Andersen)', '', 'https://career.habr.com/vacancies/1000119776'),
                ('Java-разработчик', 'Сбер', '', 'https://career.habr.com/vacancies/1000112743'),
                ('Java-разработчик', 'МегаФон', '', 'https://career.habr.com/vacancies/1000123570'),
                ('Разработчик Java', 'TINKOFF', '', 'https://career.habr.com/vacancies/1000121969'),
                ('Java-разработчик', 'Bell Integrator', '', 'https://career.habr.com/vacancies/1000115597')]

    user_data = ( "001" , "Москва", "Python")

    save_list_vacancies(list_vacancy)
