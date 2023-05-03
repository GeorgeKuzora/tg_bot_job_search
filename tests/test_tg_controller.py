from unittest import TestCase
from unittest.mock import MagicMock, patch
from src.controllers.tg_controller import Controller
from datetime import date


class TestTgController(TestCase):
    """Класс для тестирования модуля tg_controller"""

    def setUp(self) -> None:
        """Метод для задания тестовых данных"""
        self.test_user_data: tuple = (
            date(2023, 1, 1),
            "test_id",
            "test_username",
            "test_first_name",
            "test_last_name",
        )
        self.test_keyword_data: tuple = (
            date(2023, 1, 1),
            "test_id",
            "test_username",
            "test_keyword",
        )
        self.test_region_data: tuple = (
            date(2023, 1, 1),
            "test_id",
            "test_username",
            "test_region",
        )
        return super().setUp()

    def test_set_user_data(self) -> None:
        """Метод для тестирования метода Controller.set_user_data"""
        with patch("src.controllers.tg_controller.InteracrorInterface") as mock:
            interactor_interface = mock.return_value
            interface_method: MagicMock = interactor_interface.set_user_data
            Controller.set_user_data(self.test_user_data)
            interface_method.assert_called_once_with(self.test_user_data)

    def test_set_region_data(self) -> None:
        """Метод для тестирования метода Controller.set_region_data"""
        with patch("src.controllers.tg_controller.InteracrorInterface") as mock:
            interactor_interface = mock.return_value
            interface_method: MagicMock = interactor_interface.set_region_data
            Controller.set_region_data(self.test_region_data)
            interface_method.assert_called_once_with(self.test_region_data)

    def test_get_vacancy_list_by_keyword(self) -> None:
        """
        Метод для тестирования метода Controller.get_vacancy_list_by_keyword
        """
        with patch("src.controllers.tg_controller.InteracrorInterface") as mock:
            interactor_interface = mock.return_value
            interface_method = interactor_interface.get_vacancy_list
            interface_method.return_value = self.test_keyword_data
            vacancy_list = Controller.get_vacancy_list_by_keyword(
                self.test_keyword_data
            )
            self.assertEqual(vacancy_list, self.test_keyword_data)
            interface_method.assert_called_once_with(self.test_keyword_data)
