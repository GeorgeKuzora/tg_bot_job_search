from unittest import TestCase
from src.lexicons.lexicon import LexiconRu


class TestLexiconRu(TestCase):
    def test_get_keyword_command_results(self) -> None:
        vacancy_data = [("1", "2", "3", "4", "5", "6") for _ in range(3)]
        results = LexiconRu().get_keyword_command_results(vacancy_data)
        self.assertEqual(type(results), type("string"))

