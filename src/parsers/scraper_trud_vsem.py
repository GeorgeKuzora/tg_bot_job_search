import requests
from list_region import get_region_code
from typing import Any

BASE_URL = 'http://opendata.trudvsem.ru/api/v1/vacancies'


def create_link(link_api: str, data: tuple) -> str:
    """формирование url с данными от пользователя"""
    base_vacancy, region = data
    limit_count = 10
    return f"{link_api}/region/{get_region_code(region)}/?text={base_vacancy}&limit={limit_count}"


def check_connection(response: Any) -> bool:
    """Проверка соединения"""
    if response.status_code == 200:
        return True
    else:
        return False


def make_response(url: str) -> Any:
    response = requests.get(url)
    return response


def search_vacancy(url: str) -> list:
    """функция поиска вакансий на сайте trudvsem.ru"""
    response = make_response(url)
    json_data = response.json()
    list_jobs = []
    try:
        for item in json_data["results"]["vacancies"]:
            vacancy = item["vacancy"]
            list_jobs.append((vacancy["job-name"], vacancy["company"]["name"],
                              vacancy["salary_min"], vacancy["region"]["name"],
                              vacancy["vac_url"]))
    except KeyError:
        return [False]
    else:
        return list_jobs


print(search_vacancy(create_link(BASE_URL, ("Frontend", "Москва"))))
