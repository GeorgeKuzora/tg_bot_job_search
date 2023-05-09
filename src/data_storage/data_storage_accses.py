import json

class Vacancy:
    def __init__(self, name, company, solary, link) -> None:
        self.name = name
        self.company = company
        self.solary = solary
        self.link = link

def read_tg_data(user_data: tuple) -> None:
    """Считывание данных пользователя полученные от тг бота"""
    pass


def save_tg_data():
   """Запись данных пользователя в папку data в формате json"""
   pass

def read_list_vacancy(list_company: list):
     """Считывание списка вакансий из парсера"""
     for i in range(len(list_company)):
        new_vacancy = create_vacancy_from_tuple(list_company[i])
        json_str = create_json_str(new_vacancy)
        print(json_str)


def create_vacancy_from_tuple(vacancy_data: tuple) -> str:
     """Создание объекта класса Vacancy из кортежа"""
     return  Vacancy(vacancy_data[0], vacancy_data[1], vacancy_data[2], vacancy_data[3])


def create_json_str(new_vacancy) -> str:
        """Создание json строки из объекта класса Vacancy"""
        json_str = json.dumps(new_vacancy.__dict__,
                              sort_keys=False,
                             indent=4,
                             ensure_ascii=False,
                             separators=(',', ': '))
        return json_str

def save_json_in_file(json_str: str):
     """Сохранение строки json в файл"""
     with open("sample.json", "w") as outfile:
        json.dump(json_str, outfile)


if __name__ == "__main__":

    list_vacancy = [('Java разработчик', 'Sportmaster Lab', '', 'https://career.habr.com/vacancies/1000080748'),
                ('Java-разработчик', 'Okko', '', 'https://career.habr.com/vacancies/1000102160'),
                ('Java Developer', 'Aston (ex. Andersen)', '', 'https://career.habr.com/vacancies/1000119776'),
                ('Java-разработчик', 'Сбер', '', 'https://career.habr.com/vacancies/1000112743'),
                ('Java-разработчик', 'МегаФон', '', 'https://career.habr.com/vacancies/1000123570'),
                ('Разработчик Java', 'TINKOFF', '', 'https://career.habr.com/vacancies/1000121969'),
                ('Java-разработчик', 'Bell Integrator', '', 'https://career.habr.com/vacancies/1000115597')]

    read_list_vacancy(list_vacancy)