@dataclass
class Compiler:
    """Класс данных для вызова модулей пауков и объединения 
    полученных данных в единый лист кортежей"""
    

    def crawlers_init(keyward: str, region: str) -> list:
        '''Инициируем запуск модулей-пауков'''
        hh_crawler.get_vacancys_data(keyward, region)
        scraper_trud_vsem.get_vacancys_data(keyward, region)
        parser_habr.get_vacancys_data(keyward, region)
        pass #common_list
    

    def check_income_data(keyward, region):
        '''Проверка принятых от пользователя слов на количество символов в запросе'''
        in_data = [keyward, region]
        list_vars = ["keyward", "region"]
        for i in range(len(in_data)):
            if len(in_data[i]) < 1:
                raise Exception(f'недостаточно символов в {list_vars[i]}')
            else:
                pass


    def check_parser_result():
        '''Проверка полученных от модулей-пауков списков на наличие элементнов'''
        if len(in_list) > 0:
            pass
        else:
            raise Exception('list is empty, error in crawler method')
    

    def merge_lists():
        '''Объединение полученных от модулей-пауков списков в один общий список'''
        pass

    def main():
        pass

    if __name__ == "__main__":
        main()