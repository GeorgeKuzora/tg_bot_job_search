from src.business_logic.business_logic import VacancyRequestHandler
from src.compilers.compiler import Compiler
from src.configs.config import request_quantity
from src.errors.errors import StorageAccessException
from ..data_storage.storage_access_handler import Handler
from ..controllers.tg_controller import Fullname, Region, Keyword


class Interactor:
    """Класс для управления взаимодействием модулями программы"""

    @staticmethod
    def get_vacancy_list(keyword_data: tuple) -> list[tuple]:
        """
        Метод для получения списка с вакансиями и передачи его пользователю
        """
        handler = Handler()
        handler.set_keyword_data(keyword_data)
        request_data = self.handler.get_request_data(keyword_data.user_id)
        request_handler = VacancyRequestHandler(*request_data)
        compiler = Compiler()
        vacancies = compiler.get_response(request_handler.request)
        handler.save_vacancies(request_handler.get_full_results(vacancies))
        return request_handler.get_part_results(vacancies, request_quantity)

    @staticmethod
    def write_request(request: dict):
        handler = Handler()
        handler.set_data(request)
