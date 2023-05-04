class StorageInterface:
    @staticmethod
    def write_user_data(user_data: tuple) -> None:
        pass

    @staticmethod
    def write_region_data(region_data: tuple) -> None:
        pass

    @staticmethod
    def get_data_for_keyword(keyword_data: tuple) -> tuple:
        return ()


class CompilerInterface:
    @staticmethod
    def get_vacancy_list(vacancy_request_data: tuple) -> list[tuple]:
        return [tuple()]
