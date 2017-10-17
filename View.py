from abc import abstractmethod


class AbcView:
    """Интерфейс диалога с пользователем

    """

    @abstractmethod
    def show_start_message(self):
        """ Вывести приветственное сообщение. """

    @abstractmethod
    def show_main_menu(self, lines_menu):
        """ Вывести главное меню. """

    @abstractmethod
    def get_start_action(self):
        """ Узнать первое действие игрока.
            Сообщить как осуществляется взаимодействие.
        """

    @abstractmethod
    def get_action(self):
        """ Узнать действие игрока. Что выбрал пользаватель. """

    @abstractmethod
    def get_name_gamer(self):
        """Спрашивает у пользователя желаемое имя игрока

        :return: Возвращает введёное имя игрока
        """

    @abstractmethod
    def show_game_menu(self):
        """ Вывести игровое меню. """

    @abstractmethod
    def show_start_capital(self, gamer):
        """ Вывести начальный баланс. """

    @abstractmethod
    def show_capital(self, gamer):
        """ Вывети текущий баланс. """

    @abstractmethod
    def show_not_ante(self):
        """ Сообщить что ставка не сделана. """

    @abstractmethod
    def show_bye(self):
        """ Вывести завершающее сообщение. """

    @abstractmethod
    def get_ante(self, gamer):
        """ Спросить размер ставки. """

    @abstractmethod
    def show_card_points(self, cards, points):
        """ Показать карты и очки. """

    @abstractmethod
    def show_game_dial(self):
        """ Показать игровой диалог. """

    @abstractmethod
    def show_part_end(self, player1, player2, is_win):
        """ Вывести результат партии. """

    @abstractmethod
    def show_stat_game(self, win, les):
        """Показать статистику игры

        :param win: Кол-во выйгрышей игрока
        :param les: Кол-во пройгрышей игрока
        :return:
        """

    @abstractmethod
    def show_list_games(self, games):
        """Вывести список доступных игр.

        :param games: Список доступных игр
        """

    @abstractmethod
    def show_restore_fail(self):
        """ Вывести сообщение о неудачном восстановлении игры. """

    @abstractmethod
    def show_name_gamer(self, gamer):
        """ Вывести назване игры (имя игрока). """

    @abstractmethod
    def show_not_enough_money(self):
        """ Вывести сообщение о низком балансе. """


class AbcViewFile:

    @abstractmethod
    def write_game_log(self, log):
        """Записать лог игры.

        :param log: Сообщение.
        """

    @abstractmethod
    def write_stat_game(self, game_name, is_win):
        """Записать статистику игры.

        :param game_name: Название игры (имя игрока)
        :param is_win: если подедил - 1, иначе - 0
        """

    @abstractmethod
    def write_stat_game_all(self, name_game, balance, win=0, les=0):
        """Запись статистики игр.

        :param name_game: Название игры
        :param balance: Баланс
        :param win: Кол-во выйгрышей
        :param les: Кол-во пройгрышей
        """

    @abstractmethod
    def read_conf(self):
        """Возвращает содержимое конфиг файла

        :return: Словарь с конфигурациями
        """

    @abstractmethod
    def read_part_log(self, min_stack):
        """ Возвращает часть лог файла

        :return: Список строк лог файла
        """

    @abstractmethod
    def check_exist_game(self):
        """ Проверить существует ли файл статистики игры. """

    @abstractmethod
    def read_stat(self):
        """ Возвращает словарь со статистикой игры.

        :return:
        """
