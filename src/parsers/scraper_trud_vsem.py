import requests
from list_region import get_region_code

BASE_URL = 'http://opendata.trudvsem.ru/api/v1/vacancies'


def create_link(link_api: str, data: tuple) -> str:
    """формирование url с данными от пользователя"""
    base_vacancy, region = data
    limit_count = 10
    return f"{link_api}/region/{get_region_code(region)}/?text={base_vacancy}&limit={limit_count}"


def make_response(url: str) -> requests.Response:
    """Соедиенение с сервером"""
    response = requests.get(url)

    return response


def check_connection(response: requests.Response) -> bool:
    """Проверка соединения"""
    if response.status_code == 200:
        return True
    else:
        return False


def search_vacancy(url: str) -> list:
    """функция поиска вакансий на сайте trudvsem.ru"""
    response = make_response(url=url)
    if check_connection(response):
        json_data = response.json()
        list_jobs = []
        try:
            vacancies = json_data["results"]["vacancies"]
        except KeyError:
            return []
        else:
            for item in vacancies:
                vacancy = item["vacancy"]
                job_name = vacancy["job-name"]
                company_name = vacancy["company"]["name"]
                salary_min = vacancy["salary_min"]
                salary_max = vacancy["salary_max"]
                salary = vacancy["salary"]
                region_name = vacancy["region"]["name"]
                vacancy_url = vacancy["vac_url"]
                list_jobs.append((job_name, company_name, salary, region_name, vacancy_url))
            return list_jobs
    else:
        raise ConnectionError


def main():
    print(search_vacancy(create_link(BASE_URL, ("строитель", "Кемерово"))))


if __name__ == "__main__":
    main()
