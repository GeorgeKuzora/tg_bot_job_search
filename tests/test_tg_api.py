import re
from unittest import TestCase
import src.tg_api


class TestEnviromentAccess(TestCase):
    def test_tg_bot_token(self) -> None:
        token_pattern: str = "^\d.*"
        self.assertTrue(re.fullmatch(token_pattern, src.tg_api.TG_BOT_TOKEN))
