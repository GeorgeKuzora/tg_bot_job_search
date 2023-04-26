from unittest import TestCase
from unittest.mock import Mock
import src.handlers.user_handlers as user_handlers
from src.errors.errors import InvalidCommandExeption


class TestEnviromentAccess(TestCase):
    
    def test_tg_bot_token(self) -> None:
        token_pattern: str = r"^\d.*"
        self.assertTrue(type(user_handlers.bot_token), type("string"))
    
    def test_set_message_text(self) -> None: 
        message = Mock()
        message.text = "first second"
        message_text = user_handlers.set_message_text(message)
        self.assertEqual(message_text, "second")
        
    def test_set_message_text_raises(self) -> None: 
        message = Mock()
        message.text = "first"
        with self.assertRaises(InvalidCommandExeption):
            _ = user_handlers.set_message_text(message)
