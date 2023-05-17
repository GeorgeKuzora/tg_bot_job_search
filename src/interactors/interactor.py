from src.errors.errors import StorageAccessException
from src.interactors.external_interface import StorageInterface as si
from src.interactors.external_interface import CompilerInterface as ci


class Interactor:
    """Класс для управления взаимодействием модулями программы"""

    def get_vacancy_list(self, keyword_data: tuple) -> list[tuple]:
        """
        Метод для получения списка с вакансиями и передачи его пользователю
        """
        try:
            vacancy_request_data: tuple = self._get_data_for_vacancies_request(
                keyword_data
            )
            return ci.get_vacancy_list(vacancy_request_data)
        except StorageAccessException:
            return [("Can't access data storage",)]
        except RuntimeError:
            return [("Can't access job servicies",)]

    def _get_data_for_vacancies_request(self, keyword_data: tuple) -> tuple:
        """Метод для получения информации к ключевому слову,
        для создания запроса вакансий"""
        data_for_keyword: tuple = si.get_data_for_keyword(keyword_data)
        return data_for_keyword
