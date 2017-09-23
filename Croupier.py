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
            # Выдать первую карту
            self.table.user['card'].append(self.table.shoe.get_card())
            # Задокументировать выдачу карты
            f = open('game_log', 'w')
            log = 'Issuance of cards gamer: {n}: '.format(n=self.table.user['name'])
            for i in self.table.user['card']:
                log += i.name + ' '
            f.write(log+'\n')
            f.close()

            # Показать карты
            GUI.show_card(self.table.user['card'])

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
        points = 0
        while True:
            self.table.croupier['card'].append(self.table.shoe.get_card())
            points += self.table.croupier['card'][-1].value
            if points >= 17:
                break

        # Задокументировать выдачу карты
        f = open('game_log', 'a')
        log = 'Issuance of cards croupier: '
        for i in self.table.croupier['card']:
            log += i.name + ' '
            f.write(log+'\n')
        f.close()

    def calculate_points(self):
        """ Подсчитать очки. """
        pass