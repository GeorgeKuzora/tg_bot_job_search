from src.errors.errors import StorageAccessException


class Handler:
    def set_user_data(self, user_data: tuple):
        """Метод для записи данных пользователя в систему хранения"""
        try:
            si.write_user_data(user_data)
        except StorageAccessException as er:
            print(f"{er}, {type(er)}, Can't get access to data storage")
