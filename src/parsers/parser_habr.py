import requests
from bs4 import BeautifulSoup
import fake_useragent


region = {"Москва": "c_678",
          "Питер": "c_679"
}


URL = "https://career.habr.com"
JOB = "java"
CURRENT_REGION = region["Питер"]


def get_useragent() -> fake_useragent.fake.FakeUserAgent:
    """Генерирует фейковый заголовок"""
    return fake_useragent.UserAgent()


def make_response(current_url: str) -> requests.models.Response:
    """Создает запрос веб странице"""
    ua = get_useragent()
    response = requests.get(
        url=current_url,
        headers={"user-agent":ua.random}
    )
    return response


def make_link_career(page: int) -> str:
    """Формирует url списка вакансий"""
    return f"{URL}/vacancies?locations[]={CURRENT_REGION}&page={page}&q={JOB}&type=all"


def find_vacancy_card(response) -> list:
    """Создает список ссылок на вакансии по одной странице, вызывается после проверки связи"""
    link_list = []
    soup = create_beautiful_soup(response)
    if not soup.find('a', attrs={"class":"vacancy-card__title-link"}):
        return link_list
    for link in soup.find_all('a', attrs={"class":"vacancy-card__title-link"}):
        link_list.append(f"{URL}{link.get('href')}")
    return link_list


def check_connection(response) -> bool:
    """Проверка связи"""
    if response.status_code == 200:
        return True
    else:
        return False


def create_beautiful_soup(response) ->BeautifulSoup:
    """Создание объекта BeautifulSoup"""
    return BeautifulSoup(response.content, "lxml")


def get_links() -> list:
    """Соединяет списки ваканский по всем страницам"""
    all_link_list = []
    i = 1
    response = make_response(make_link_career(i))
    if check_connection(response) == False:
        return all_link_list
    while find_vacancy_card(response) != []:
        response = make_response(make_link_career(i))
        if check_connection(response):
           if find_vacancy_card(response) != []:
             all_link_list.extend(find_vacancy_card(response))
        else:
            pass
        i += 1

    return all_link_list


def get_company(link: str) -> tuple:
    """Создание кортежа данных по вакансии"""
    response = make_response(link)
    if not check_connection(response):
        return ()
    soup = create_beautiful_soup(response)

    if not soup.find('div', attrs={"class":"basic-salary basic-salary--appearance-vacancy-header"}):
         salary = ""
    else:
        salary = soup.find('div', attrs={"class":"basic-salary basic-salary--appearance-vacancy-header"}).text
    tuple_job =(
                   soup.find('h1', attrs={"class":"page-title__title"}).text,
                   soup.find('div', attrs={"class":"company_name"}).text,
                   salary,
                   #CURRENT_REGION, - здесь будет прописан регион поиска, вводимый пользователем
                   link
    )
    return tuple_job


def get_list_company(all_link_list: list) -> list:
    """Получение списка кортежей вакансии"""
    list_company = []
    for i in all_link_list:
        list_company.append(get_company(i))
    return list_company


# def save_in_json(list_company):
#    """Сохранение резултьатов в json"""
#     with open("mydata.json", "w") as file:
#         json.dump(list_company, file)


if __name__=="__main__":

    print(get_list_company(get_links()))
