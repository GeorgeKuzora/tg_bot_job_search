import json

class Vacancy:
    def __init__(self, name, company, solary, link) -> None:
        self.name = name
        self.company = company
        self.solary = solary
        self.link = link

# def read_tg_data(user_data: tuple) -> None:
#     """Считывание данных пользователя полученные от тг бота"""
#     pass


# def save_tg_data():
#     """Запись данных пользователя в папку data в формате json"""
#     pass


# def read_parser_data(parser_data: list) -> tuple:
#     """Считывание списка кортежей парсера"""


# def tuple_from_list():
#     #json_obj = json.dumps(tup)
#     pass

# def save_tg_data():
#     """Запись данных парсера в папку data в формате json"""
#     pass

if __name__ == "__main__":

    list_vacancy = [('Java разработчик', 'Sportmaster Lab', '', 'https://career.habr.com/vacancies/1000080748'),
                ('Java-разработчик', 'Okko', '', 'https://career.habr.com/vacancies/1000102160'),
                ('Java Developer', 'Aston (ex. Andersen)', '', 'https://career.habr.com/vacancies/1000119776'),
                ('Java-разработчик', 'Сбер', '', 'https://career.habr.com/vacancies/1000112743'),
                ('Java-разработчик', 'МегаФон', '', 'https://career.habr.com/vacancies/1000123570'),
                ('Разработчик Java', 'TINKOFF', '', 'https://career.habr.com/vacancies/1000121969'),
                ('Java-разработчик', 'Bell Integrator', '', 'https://career.habr.com/vacancies/1000115597')]

    for i in range(len(list_vacancy)):
        json_obj = json.dumps(list_vacancy[i])

    with open("mydata.json", "w") as file:
        json.dump(list_company, file)