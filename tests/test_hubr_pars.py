import unittest
from habr import *


class TestHabr(unittest.TestCase):

   def test_get_useragent(self):
      self.assertIsInstance(get_useragent(), fake_useragent.fake.FakeUserAgent)

   def test_make_response(self):
      self.assertIsNot(make_response("https://career.habr.com/vacancies?locations[]=c_679&page=1&q=java&type=all"),
                       None,
                        "Запрос вернулся пустым")
      self.assertIsInstance(make_response("https://career.habr.com/vacancies?locations[]=c_679&page=1&q=java&type=all"),
                            requests.models.Response,
                            "Запрос вернулся в странном формате")

   def test_make_link_career(self):
      self.assertEqual(make_link_career(1),
                       "https://career.habr.com/vacancies?locations[]=c_679&page=1&q=java&type=all",
                        "Ссылка формируется не верно" )

   def test_find_vacancy_card(self):
      self.assertIsNot(make_response("https://career.habr.com/vacancies?locations[]=c_679&page=1&q=java&type=all"),
                       None,
                        "Нет карточек с вакансиями")

   def test_get_links(self):
      pass

   def test_check_connection(self):
      self.assertTrue(
           check_connection(make_response("https://career.habr.com/vacancies?locations[]=c_679&page=1&q=java&type=all")),
            "Проблемы с соединением"
          )

   def test_create_beautiful_soup(self):
      pass


if __name__ == '__main__':
    unittest.main()