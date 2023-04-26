from unittest import TestCase
from unittest.mock import Mock
import src.handlers.user_handlers as user_handlers
from src.errors.errors import InvalidCommandException


class TestUserHandlers(TestCase):
    
    def test_set_message_text(self) -> None: 
        message = Mock()
        message.text = "first second"
        message_text = user_handlers.set_message_text(message)
        self.assertEqual(message_text, "second")
        
    def test_set_message_text_raises(self) -> None: 
        message = Mock()
        message.text = "first"
        with self.assertRaises(InvalidCommandException):
            _ = user_handlers.set_message_text(message)
