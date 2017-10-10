class ViewConsole:
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


class ViewFile:
    """Интерфейс для записи в файл

    """

    @staticmethod
    def write_game_log(log):
        with open('game_log', 'a') as f:
            f.write(log+'\n')

    @staticmethod
    def write_stat_game(game_name, is_win):
        import json

        line = [0, 0, 0]
        try:
            # Открыть файл и считываем json объект
            with open('stat_log.json', 'r') as fr:
                stat_log = json.loads(fr.read())

        except IOError:
            # Если файл не существует
            if is_win:
                line[0] += 1
            else:
                line[1] += 1

            # Формируем словарь и записываем в json файл
            stat_log = dict()
            stat_log[game_name] = line

            with open('stat_log.json', 'w') as fw:
                json.dump(stat_log, fw)

            return line

        try:
            # Если файл существует и в нём есть нужная запись
            # Достаем из него значения и увеличиваем одно из них
            line = stat_log[game_name]

        except KeyError:
            # Если файл существует, но в нём нет нужной записи
            line = [0, 0, 0]

        if is_win:
            line[0] += 1
        else:
            line[1] += 1

        stat_log[game_name] = line

        with open('stat_log.json', 'w') as fw:
            json.dump(stat_log, fw)

        return line

    @staticmethod
    def write_stat_game_all(name_game, balance, win=0, les=0):
        """Запись статистики игр.
        Этот метод должен быть в классе Gamer
        :param name_game: Название игры
        :param balance: Баланс
        :param win: Кол-во выйгрышей
        :param les: Кол-во пройгрышей
        :return:
        """
        import json

        line = [win, les, balance]
        try:
            # Открыть файл и считываем json объект
            with open('stat_log.json', 'r') as fr:
                stat_log = json.loads(fr.read())

        except IOError:
            # Если файл не существует
            # Формируем словарь и записываем в json файл
            stat_log = dict()
            stat_log[name_game] = line

            with open('stat_log.json', 'w') as fw:
                json.dump(stat_log, fw)

            return

        try:
            # Если файл существует и в нём есть нужная запись
            # Достаем из него значения
            line = stat_log[name_game]
            line[2] = balance

        except KeyError:
            # Если файл существует, но в нём нет нужной записи
            line = [win, les, balance]

        stat_log[name_game] = line

        with open('stat_log.json', 'w') as fw:
            json.dump(stat_log, fw)

        return

    @staticmethod
    def read_conf():
        """Возвращает содержимое конфиг файла

        :return:
        """
        import json

        with open("config.json", "r") as f:
            conf = json.loads(f.read())

        return conf

    @staticmethod
    def read_part_log():
        """ Возвращает часть лог файла

        :return:
        """
        with open('game_log', 'r') as f:
            __min_stack = 10
            block_log = []
            i = 0
            for line in f.readlines():
                if line.find('Start game') != -1:
                    i = 0

                i += 1
                block_log.append(line)
                if (len(block_log) >= __min_stack) and (i < __min_stack):
                    while len(block_log) > __min_stack:
                        block_log.pop(0)

        return block_log

    @staticmethod
    def check_exist_game():
        import json

        try:
            # Открыть файл и считываем json объект
            with open('stat_log.json', 'r') as fr:
                json.loads(fr.read())

            return 1

        except IOError:
            return 0
