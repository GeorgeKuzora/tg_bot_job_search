import requests
from bs4 import BeautifulSoup as bs
import fake_useragent
import time
import logging
from typing import Union
from typing import Generator


URL = "https://hh.ru/search/vacancy"
FIRST_PAGE = 0

AREA = {
    "Россия": 113,
    "Москва": 1,
    "Санкт-Петербург": 2,
    "Владивосток": 22,
    "Волгоград": 24,
    "Воронеж": 26,
    "Екатеринбург": 3,
    "Казань": 88,
    "Калуга": 43,
    "Краснодар": 53,
    "Красноярск": 54,
    "Нижний Новгород": 66,
    "Новосибирск": 4,
    "Ростов-на-Дону": 76,
    "Самара": 78,
    "Саратов": 79,
    "Сочи": 237,
    "Уфа": 99,
    "Ярославль": 112,
    "Севастополь": 130,
    "Симферополь": 131
    }

IN_PARAMS = {
    "text": None,
    "area": AREA["Россия"],
    "page": FIRST_PAGE
    }


def main():
    print(get_vacancies_data("python", "Москва"))


def get_vacancies_data(keyword: str, region: str) -> list:
    '''Приём поисковых данных, парсинг и возврат 
    списка картежей с результатами поиска вакансий'''
    IN_PARAMS["text"] = keyword
    IN_PARAMS["area"] = AREA[region]
    result = list()
    for a in get_links(URL, IN_PARAMS):
        result.append(get_vacancy(a))
        time.sleep(1)
    return result


def get_links(link: str, in_params: dict[str, Union[str, int]]) -> Generator[str, None, None]:
    '''Находим и передаём через генератор ссылки на все вакансии по запросу'''
    try:
        soup = bs(get_response_data(link, in_params).content, "lxml")
        page_count = get_number_pages(soup)
        for page in range(FIRST_PAGE, page_count + 1):
            in_params["page"] = page
            soup = bs(get_response_data(link, in_params).content, "lxml")
            yield from get_vacancy_ref(soup)
            time.sleep(1)
    except:
        return []
    

def cheack_server_response(func):
    '''Проверка отвтета от серваера и его содержания 
        по номеру кода ответа'''
    def wrapper(*args):
        response = func(*args)
        logging.basicConfig(
            level=logging.DEBUG,
            filename = "mylog.log",
            format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
            datefmt='%d.%m.%Y [%H:%M:%S]',
            )
        if response.status_code == 200:
            return response
        logging.info(f' - {response.status_code}')
        raise ConnectionError("response content isn`t correct, status code isn`t 200")
    return wrapper


@cheack_server_response
def get_response_data(link: str, in_params: dict[str, Union[str, int]]) -> requests.Response:
    '''Формирование и отправка GET запроса на сервер'''
    ua = fake_useragent.UserAgent()
    data = requests.get(
        url = link,
        params = in_params,
        headers = {"user-agent": ua.random}
    )
    return data


def get_number_pages(soup: bs) -> int:
    '''Парсинг номера последней страницы из полученного списка 
    страниц с результатами поиска'''
    try:
        page_count = int(soup.find("div", attrs={"class": "pager"}).find_all(
                "span", recursive=False)[-1].find("a", attrs={"class": "bloko-button"}).find("span").text)
        return page_count
    except:
        raise RuntimeError("number of pages wasn`t find")


def get_vacancy_ref(soup: bs) -> Generator[str, None, None]:
    '''Парсинг ссылки на каждую вакансию из списка вакансий одной страницы результатов поиска'''
    try:
        for a in soup.find_all("a", attrs={"class": "serp-item__title"}):
            yield f"{a.attrs['href'].split('?')[0]}"
    except:
        raise RuntimeError("vacancy reference not found")
    

def get_vacancy(link: str) -> tuple[tuple[str, str, str, str, str], ...]:
    '''Парсим карточку вакансии по полученной ссылке'''
    try:
        soup = bs(get_response_data(link).content, "lxml")
        vacancy = (
            ("name", find_vacancy_name(soup)),
            ("company_name", find_vacancy_company_name(soup)),
            ("salary", find_vacancy_salary(soup)),
            ("location", find_vacancy_location(soup)),
            ("reference", link)
        )
        return vacancy
    except:
        return ()


def find_vacancy_name(soup: bs) -> str:
    '''Парсим навание вакансии'''
    name = soup.find(
        "div", attrs={"class": "vacancy-title"}).find("h1").text.replace(u'\xa0', u' ')
    if not name:
        name = ""
    return name


def find_vacancy_salary(soup: bs) -> str:
    '''Парсим зарплату вакансии'''
    salary = soup.find("div", attrs={"class": "vacancy-title"}).find(
        "div", attrs={"data-qa": "vacancy-salary"}).text.replace(u'\xa0', u'')
    if not salary:
        salary = ""
    return salary


def find_vacancy_company_name(soup: bs) -> str:
    '''Парсим навание компании разместившей вакансию'''
    company_name = soup.find(
        "span", attrs={"class": "vacancy-company-name"}).text.replace(
        u'\xa0', u' ')
    if not company_name:
        company_name = ""
    return company_name


def find_vacancy_location(soup: bs) -> str:
    '''Парсим место нахождение компании разместившей вакансию'''
    if soup.find(
        "p", attrs={"data-qa": "vacancy-view-location"}):
        location = soup.find(
            "p", attrs={"data-qa": "vacancy-view-location"}).text.replace(
            u'\xa0', u' ')
    elif soup.find(
        "a", attrs={"class": "bloko-link bloko-link_kind-tertiary bloko-link_disable-visited"}):
        location = soup.find(
            "a", attrs={"class": "bloko-link bloko-link_kind-tertiary bloko-link_disable-visited"}).text.replace(u'\xa0', u' ')
    elif soup.find(
        "span", attrs={"data-qa": "vacancy-view-raw-address"}):
        location = soup.find(
            "span", attrs={"data-qa": "vacancy-view-raw-address"}).text.replace(u'\xa0', u' ')
    else:
        location = ""
    return location
    

if __name__ == "__main__":
    main()