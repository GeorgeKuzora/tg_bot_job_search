from src.errors.errors import StorageAccessException
from src.interactors.external_interface import StorageInterface as si
from src.interactors.external_interface import CompilerInterface as ci


class Interactor:
    def set_user_data(self, user_data: tuple):
        try:
            si.write_user_data(user_data)
        except StorageAccessException as er:
            print(f"{er}, {type(er)}, Can't get access to data storage")

    def set_region_data(self, region_data: tuple):
        try:
            si.write_region_data(region_data)
        except StorageAccessException as er:
            print(f"{er}, {type(er)}, Can't get access to data storage")

    def get_vacancy_list(self, keyword_data: tuple) -> list[tuple]:
        vacancy_request_data: tuple = self._get_data_for_vacancies_request(keyword_data)
        return ci.get_vacancy_list(vacancy_request_data)

    def _get_data_for_vacancies_request(self, keyword_data: tuple) -> tuple:
        data_for_keyword: tuple = si.get_data_for_keyword(keyword_data)
        return data_for_keyword
