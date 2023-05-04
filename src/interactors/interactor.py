# Незавершенный класс, будет завершен или заменен при разработке интерактора
class InteracrorInterface:
    """Класс для передачи данных между контроллером и интерактором"""

    def __init__(self) -> None:
        self.keyword_data: tuple
        self.region_data: tuple

    def set_user_data(self, user_data: tuple) -> tuple:
        return user_data

    def set_region_data(self, region_data: tuple) -> tuple:
        return region_data

    def get_vacancy_list(self, keyword_data: tuple) -> list[tuple]:
        self._set_keyword_data(keyword_data)
        compiled_vacancy_data = [tuple()]
        return compiled_vacancy_data

    def _set_keyword_data(self, keyword_data: tuple) -> None:
        self.keyword_data = keyword_data
