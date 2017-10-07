class GUI:
    """Консольный интерфейс.

    """

    @staticmethod
    def show_start_message():
        """ Вывести приветственное сообщение. """
        print('Здравствуйте, это игра BlackJack.\n')

    @staticmethod
    def show_main_menu(lines_menu):
        """ Показать главное меню. """
        print('---------------------------------')
        menu = {1: '  1. Новая игра.\n',
                2: '  2. Загрузить игру.\n',
                3: '  3. Восстановить игру.\n',
                10: '  0. Выход.\n'}
        mes = ''
        for line in sorted(lines_menu):
            mes += menu[line]

        print(mes)

    @staticmethod
    def get_start_action():
        """ Узнать первоначальное действие игрока. """
        return input("Введите соответствующую цифру: ")

    @staticmethod
    def get_action():
        """ Узнать действие игрока. """
        return input("> ")

    @staticmethod
    def get_name_gamer():
        """Спрашивает у пользователя желаемое имя игрока

        :return: Возвращает введёное имя игрока
        """
        print('---------------------------------')
        print('           Новая игра:')
        name = input('Введите название игры: ')
        return name

    @staticmethod
    def show_game_menu():
        """ Показать игровое меню. """
        print('---------------------------------')
        print('  1. Играть.\n  0. Назад.')

    @staticmethod
    def show_start_capital(gamer):
        """ Показать начальный баланс. """
        print('Начальный баланс: ' + str(gamer.balance))

    @staticmethod
    def show_capital(gamer):
        """ Показать баланс. """
        print(gamer)

    @staticmethod
    def show_not_ante():
        print('Сделайте ставку!')

    @staticmethod
    def show_bye():
        """ Показать прощальное сообщение. """
        print('---------------------------------')
        print('До свидания!')

    @staticmethod
    def get_ante(gamer):
        """ Спросить размер ставки. """
        print('Ваш баланс: {}'.format(str(gamer.balance)))
        return input('Размер вашей ставки ?\n> ')

    @staticmethod
    def show_card_points(cards, points):
        """ Показать карты и очки. """
        s = '{0}\n{1}\n{2}\n{3}'.format(' ___ '*len(cards), '|   |'*len(cards),
                                        '| {.name} |'*len(cards), '|___|'*len(cards))
        print(s.format(*cards).replace('10 ', '10'))
        print('Кол-во очков: '+str(points))

    @staticmethod
    def show_game_dial():
        """ Показать игровой диалог. """
        print('---------------------------------')
        print('  1. Ещё.\n  0. Хватит.')

    @classmethod
    def show_part_end(cls, player1, player2, is_win):
        print('---------------------------------')
        print('Карты ' + player1['name'] + ':')
        cls.show_card_points(player1['card'], player1['points'])
        print('Карты ' + player2['name'] + ':')
        cls.show_card_points(player2['card'], player2['points'])

        if is_win:
            print('Вы выйграли !')
        else:
            print('Вы проиграли !')

    @staticmethod
    def show_stat_game(win, les):
        """Показать статистику игры

        :param win: Кол-во выйгрышей игрока
        :param les: Кол-во пройгрышей игрока
        :return:
        """
        print('{} : {} (выйгрышей : пройгрышей)'.format(str(win), str(les)))

    @staticmethod
    def show_list_games(users):
        print('---------------------------------')
        print('Выберите игру:')
        i = 0
        for user in users:
            i += 1
            print('  '+str(i)+'. '+user)

        print('\n  0. Назад')

    @staticmethod
    def show_restore_fail():
        print('---------------------------------')
        print('Восстановить не удалось!')

    @staticmethod
    def show_name_gamer(gamer):
        print('---------------------------------')
        print('Name game: '+gamer.name)

    @staticmethod
    def show_not_enough_money():
        print('Ошибка, низкий баланс!')
