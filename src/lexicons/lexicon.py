class LexiconRu:
    def get_start_command_answer(self) -> str:
        """Метод возвращает ответ на комманду /start"""
        return (
            "Привет!\nДоступны следующие комманды:\n"
            "/region - установить свой регион\n"
            "/keyword - получить вакансии по ключевому слову"
        )

    def get_region_command_answer(self, region: str) -> str:
        """Метод возвращает ответ на комманду /region"""
        return f"Вы задали регион: {region}"

    def get_invalid_region_command_answer(self) -> str:
        """Метод возвращает ответ на неверную комманду /region"""
        return "Вы не указали название региона"

    def get_keyword_command_answer(self, keyword: str) -> str:
        """Метод возвращает ответ на комманду /keyword"""
        return f"Вы задали ключевое слово: {keyword}"

    def get_invalid_keyword_command_answer(self) -> str:
        """Метод возвращает ответ на неверную комманду /keyword"""
        return "Вы не указали ключевое слово"

    def get_invalid_command_answer(self) -> str:
        """Метод возвращает ответ на неверную комманду"""
        return "Команда не распознана"

    def get_keyword_command_results(self, vacancy_data: list[tuple]) -> str:
        """Метод возвращает строку с информацией о вакансиях
        по запрошенному ключевому слову"""
        get_messages = list(map(self.concat_vacancy_results, vacancy_data))
        get_messages = "\n".join(get_messages)
        return get_messages

    def concat_vacancy_results(self, vacancy: tuple) -> str:
        """Метод соединяет информацию о вакансии в строку"""
        answer_message: str = ""
        answer_message += (
            f"{vacancy[1]}\n{vacancy[2]}\n{vacancy[3]}\n{vacancy[4]}\n{vacancy[5]}\n\n"
        )
        return answer_message
