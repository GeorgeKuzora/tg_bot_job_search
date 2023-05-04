from src.interactors.interactor import Interactor


class Controller:
    """Класс для задания методов работы контроллера"""

    @staticmethod
    def set_user_data(user_data: tuple) -> None:
        """Метод для записи данных пользователя полученных от Bot API"""
        interface = Interactor()
        interface.set_user_data(user_data)

    @staticmethod
    def set_region_data(region_data: tuple) -> None:
        """Метод для записи данных региона полученных от Bot API"""
        interface = Interactor()
        interface.set_region_data(region_data)

    @staticmethod
    def get_vacancy_list_by_keyword(keyword_data: tuple) -> list[tuple]:
        """
        Метод для получения списка вакансий
        по запрошенному ключевому слову
        """
        return Interactor().get_vacancy_list(keyword_data)
