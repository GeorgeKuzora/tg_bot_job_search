import re
from unittest import TestCase
import src.handlers.user_handlers as user_handlers
import src.config.config as config


class TestEnviromentAccess(TestCase):
    def test_tg_bot_token(self) -> None:
        token_pattern: str = "^\d.*"
