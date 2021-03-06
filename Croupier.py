class Croupier:
    """Класс: Крупье.
    Ведёт подсчёт очков и сбор ставок.

    """
    def __init__(self, table, view, view_file):
        self.table = table
        self.view = view
        self.view_file = view_file

    def issue_cards_gamer(self, _flag = 0):
        """Выдать карты игроку.

        """
        # Проверить поставлена ли ставка
        if not self.table.user['ante']:
            self.view.show_not_ante()
            return 1

        while True:

            if not _flag:
                # Выдать первую карту и прибавить очки
                self.table.user['card'].append(self.table.shoe.get_card())
                self.table.user['points'] += self.table.user['card'][-1].value

                # Задокументировать выдачу карты и очки
                log = 'Issuance of cards gamer: {n}; '.format(n=self.table.user['name'])
                for i in self.table.user['card']:
                    log += i.name + ' '
                self.view_file.write_game_log(log+', points: '+str(self.table.user['points']))
            else:
                _flag = 0
            # Показать карты и очки
            self.view.show_card_points(self.table.user['card'], self.table.user['points'])

            if self.table.user['points'] >= 21:
                act = '0'
            else:
                # Узнать дальнейшее действие
                self.view.show_game_dial()
                act = self.view.get_action()

            if act == '1':
                # Продолжить выдавать карты
                continue
            elif act == '0':
                # Перестать выдавать карты
                break

    def issue_cards_croupier(self):
        """Выдать карты крупье

        """
        while True:
            self.table.croupier['card'].append(self.table.shoe.get_card())
            self.table.croupier['points'] += self.table.croupier['card'][-1].value
            if self.table.croupier['points'] >= 17:
                break

        # Задокументировать выдачу карты
        log = 'Issuance of cards croupier: '
        for i in self.table.croupier['card']:
            log += i.name + ' '
        self.view_file.write_game_log(log+', points: '+str(self.table.croupier['points']))

    def calculate_points(self):
        """ Подсчитать очки. """
        # пройгрышный вариант - "перебор"
        is_win = 0
        if self.table.user['points'] > 21:
            is_win = 0

        elif self.table.user['points'] == 21:
            if self.table.croupier['points'] == 21:
                is_win = 1

            else:
                is_win = 1
                self.table.user['ante'] *= 3

        elif self.table.croupier['points'] > 21:
            is_win = 1
            self.table.user['ante'] *= 2

        elif self.table.croupier['points'] == 21:
            is_win = 0

        elif self.table.user['points'] > self.table.croupier['points']:
            is_win = 1
            self.table.user['ante'] *= 2

        # log результата игры

        if is_win:
            log = 'Result of the game: {}, Win'.format(self.table.user['name'])
        else:
            log = 'Result of the game: {}, Lesion'.format(self.table.user['name'])
        self.view_file.write_game_log(log)

        # Вскрыться: показать карты крупье, карты игрока и выйграл или проиграл игрок
        self.view.show_part_end(self.table.croupier, self.table.user, is_win)

        # Показать и записать статистику игры
        line = self.view_file.write_stat_game(self.table.user['name'], is_win)
        self.view.show_stat_game(line[0], line[1])

        return is_win

    def clear_card_get_ante(self, is_win):
        """Очищает поля с картами и поле ставки относительно результата игры

        :return:
        """
        if is_win:
            # Если выйгрышь возвращаем увеличенную ставку
            gain = self.table.user['ante']
        else:
            # Если проигрышь возвращаем 0
            gain = 0

        self.table.user['card'] = []
        self.table.user['ante'] = 0
        self.table.user['points'] = 0

        self.table.croupier['card'] = []
        self.table.croupier['points'] = 0

        # log очистки карт и ставки

        self.view_file.write_game_log('Clear card and ante ')

        return gain
