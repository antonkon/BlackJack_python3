import GUI


class Croupier:
    """Класс: Крупье.
    Ведёт подсчёт очков и сбор ставок.
    """
    def __init__(self, table):
        self.table = table

    def issue_cards_gamer(self):
        """Выдать карты игроку.

        """
        # Проверить поставлена ли ставка
        if not self.table.user['ante']:
            GUI.show_err(101)
            exit()

        while True:
            # Выдать первую карту и прибавить очки
            self.table.user['card'].append(self.table.shoe.get_card())
            self.table.user['points'] += self.table.user['card'][-1].value

            # Задокументировать выдачу карты и очки
            f = open('game_log', 'a')
            log = 'Issuance of cards gamer: {n}: '.format(n=self.table.user['name'])
            for i in self.table.user['card']:
                log += i.name + ' '
            f.write(log+', points: '+str(self.table.user['points'])+'\n')
            f.close()

            # Показать карты и очки
            GUI.show_card_points(self.table.user['card'], self.table.user['points'])

            if self.table.user['points'] >= 21:
                act = '0'
            else:
                # Узнать дальнейшее действие
                GUI.show_game_dial()
                act = GUI.get_action()

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
        f = open('game_log', 'a')
        log = 'Issuance of cards croupier: '
        for i in self.table.croupier['card']:
            log += i.name + ' '
        f.write(log+', points: '+str(self.table.croupier['points'])+'\n')
        f.close()

    def calculate_points(self):
        """ Подсчитать очки. """
        # пройгрышный вариант - "перебор"
        is_win = 0
        if self.table.user['points'] > 21:
            is_win = 0
        elif self.table.user['points'] == 21 and self.table.croupier['points'] != 21:
            is_win = 1
        elif self.table.user['points'] > self.table.croupier['points']:
            is_win = 1

        # Вскрыться: показать карты крупье, карты игрока и выйграл или проиграл игрок
        GUI.show_part_end(self.table.croupier, self.table.user, is_win)

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
        f = open('game_log', 'a')
        log = 'Clear card and ante '
        f.write(log+'\n')
        f.close()

        return gain
