from src.interactors.interactor import InteracrorInterface


class Controller:
    """Класс для задания методов работы контроллера"""

    @staticmethod
    def set_user_data(user_data: tuple) -> None:
        """Метод для записи данных пользователя полученных от Bot API"""
        interface = InteracrorInterface()
        interface.set_user_data(user_data)

    @staticmethod
    def set_region_data(region_data: tuple) -> None:
        """Метод для записи данных региона полученных от Bot API"""
        interface = InteracrorInterface()
        interface.set_region_data(region_data)

    @staticmethod
    def get_vacancy_list_by_keyword(keyword_data: tuple) -> list[tuple]:
        """
        Метод для получения списка вакансий
        по запрошенному ключевому слову
        """
        interface = InteracrorInterface()
        return interface.get_vacancy_list(keyword_data)
