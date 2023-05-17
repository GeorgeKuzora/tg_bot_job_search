from src.errors.errors import StorageAccessException


class Handler:
    def set_user_data(self, user_data: tuple):
        """Метод для записи данных пользователя в систему хранения"""
        try:
            si.write_user_data(user_data)
        except StorageAccessException as er:
            print(f"{er}, {type(er)}, Can't get access to data storage")

    def set_region_data(self, region_data: tuple):
        """
        Метод для записи данных о регионе выбранном пользователем
        в систему хранения
        """
        try:
            si.write_region_data(region_data)
        except StorageAccessException as er:
            print(f"{er}, {type(er)}, Can't get access to data storage")

    def set_keyword_data(self, keyword_data: tuple):
        """
        Метод для записи данных о регионе выбранном пользователем
        в систему хранения
        """
        try:
            si.write_keyword_data(keyword_data)
        except StorageAccessException as er:
            print(f"{er}, {type(er)}, Can't get access to data storage")

