class LexiconRu:
    def get_start_command_answer(self) -> str:
        """Метод возвращает ответ на комманду /start"""
        return ("Привет!\nДоступны следующие комманды:\n"
                "/region - установить свой регион\n"
                "/keyword - получить вакансии по ключевому слову")

    def get_region_command_answer(self, region: str) -> str:
        """Метод возвращает ответ на комманду /region"""
        return (f"Вы задали регион: {region}")

    def get_invalid_region_command_answer(self) -> str:
        """Метод возвращает ответ на неверную комманду /region"""
        return ("Вы не указали название региона")

    def get_keyword_command_answer(self, keyword: str) -> str:
        """Метод возвращает ответ на комманду /keyword"""
        return (f"Вы задали ключевое слово: {keyword}")

    def get_invalid_keyword_command_answer(self) -> str:
        """Метод возвращает ответ на неверную комманду /keyword"""
        return ("Вы не указали ключевое слово")

    def get_invalid_command_answer(self) -> str:
        """Метод возвращает ответ на неверную комманду"""
        return ("Команда не распознана")
