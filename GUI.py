from View import AbcView
from View import AbcViewFile


class View(AbcView):
    """Консольный интерфейс.

    """

    def show_start_message(self):
        """ Вывести приветственное сообщение. """
        print('Здравствуйте, это игра BlackJack.\n')

    def show_main_menu(self, lines_menu):
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

    def get_start_action(self):
        """ Узнать первоначальное действие игрока. """
        return input("Введите соответствующую цифру: ")

    def get_action(self):
        """ Узнать действие игрока. """
        return input("> ")

    def get_name_gamer(self):
        """Спрашивает у пользователя желаемое имя игрока

        :return: Возвращает введёное имя игрока
        """
        print('---------------------------------')
        print('           Новая игра:')
        name = input('Введите название игры: ')
        return name

    def show_game_menu(self):
        """ Показать игровое меню. """
        print('---------------------------------')
        print('  1. Играть.\n  0. Назад.')

    def show_start_capital(self, gamer):
        """ Показать начальный баланс. """
        print('Начальный баланс: ' + str(gamer.balance))

    def show_capital(self, gamer):
        """ Показать баланс. """
        print(gamer)

    def show_not_ante(self):
        """ Сообщить что ставка не сделана. """
        print('Сделайте ставку!')

    def show_bye(self):
        """ Показать завершающее сообщение. """
        print('---------------------------------')
        print('До свидания!')

    def get_ante(self, gamer):
        """ Спросить размер ставки. """
        print('Ваш баланс: {}'.format(str(gamer.balance)))
        return input('Размер вашей ставки ?\n> ')

    def show_card_points(self, cards, points):
        """ Показать карты и очки. """
        s = '{0}\n{1}\n{2}\n{3}'.format(' ___ '*len(cards), '|   |'*len(cards),
                                        '| {.name} |'*len(cards), '|___|'*len(cards))
        print(s.format(*cards).replace('10 ', '10'))
        print('Кол-во очков: '+str(points))

    def show_game_dial(self):
        """ Показать игровой диалог. """
        print('---------------------------------')
        print('  1. Ещё.\n  0. Хватит.')

    def show_part_end(self, player1, player2, is_win):
        """ Вывести результат партии. """
        print('---------------------------------')
        print('Карты ' + player1['name'] + ':')
        self.show_card_points(player1['card'], player1['points'])
        print('Карты ' + player2['name'] + ':')
        self.show_card_points(player2['card'], player2['points'])

        if is_win:
            print('Вы выйграли !')
        else:
            print('Вы проиграли !')

    def show_stat_game(self, win, les):
        """Показать статистику игры

        :param win: Кол-во выйгрышей игрока
        :param les: Кол-во пройгрышей игрока
        :return:
        """
        print('{} : {} (выйгрышей : пройгрышей)'.format(str(win), str(les)))

    def show_list_games(self, games):
        """Вывести список доступных игр.

        :param games: Список доступных игр
        """
        print('---------------------------------')
        print('Выберите игру:')
        i = 0
        for game in games:
            i += 1
            print('  '+str(i)+'. '+game)

        print('\n  0. Назад')

    def show_restore_fail(self):
        """ Вывести сообщение о неудачном восстановлении. """
        print('---------------------------------')
        print('Восстановить не удалось!')

    def show_name_gamer(self, gamer):
        """ Вывести назване игры (имя игрока). """
        print('---------------------------------')
        print('Название игры: '+gamer.name)

    def show_not_enough_money(self):
        """ Вывести сообщение о низком балансе. """
        print('Ошибка, низкий баланс!')


class ViewFile(AbcViewFile):
    """Интерфейс для записи в файл

    """

    def write_game_log(self, log):
        """Записать лог игры.

        :param log: Сообщение.
        """
        with open('game_log', 'a') as f:
            f.write(log+'\n')

    def write_stat_game(self, game_name, is_win):
        """Записать статистику игры.

        :param game_name: Название игры (имя игрока)
        :param is_win: если подедил - 1, иначе - 0
        """
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

    def write_stat_game_all(self, name_game, balance, win=0, les=0):
        """Запись статистики игр.

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

    def read_conf(self):
        """Возвращает содержимое конфиг файла

        :return: Словарь с конфигурациями
        """
        import json

        with open("config.json", "r") as f:
            conf = json.loads(f.read())

        return conf

    def read_part_log(self, min_stack):
        """ Возвращает часть лог файла

        :min_stack: Минимальное кол-во строк которое вернет функция
        :return: Список строк лог файла
        """
        try:
            f = open('game_log', 'r')
        except IOError:
            return 0

        block_log = []
        i = 0
        for line in f.readlines():
            if line.find('Start game') != -1:
                i = 0

            i += 1
            block_log.append(line)
            if (len(block_log) >= min_stack) and (i < min_stack):
                while len(block_log) > min_stack:
                    block_log.pop(0)

        return block_log

    def check_exist_game(self):
        """ Проверить существует ли файл статистики игры. """
        import json

        try:
            # Открыть файл и считываем json объект
            with open('stat_log.json', 'r') as fr:
                json.loads(fr.read())

            return 1

        except IOError:
            return 0

    def read_stat(self):
        """ Возвращает словарь со статистикой игры.

        :return:
        """
        import json

        with open('stat_log.json', 'r') as fr:
            stat_log = json.loads(fr.read())

        return stat_log
