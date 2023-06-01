from src.errors.errors import StorageAccessException
from . import data_storage_accses as si


class Handler:
    def set_data(self, user_data: dict):
        """Метод для записи данных пользователя в систему хранения"""
        try:
            si.write_data(user_data)
        except StorageAccessException as er:
            print(f"{er}, {type(er)}, Can't get access to data storage")
