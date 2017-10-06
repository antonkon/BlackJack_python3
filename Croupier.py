import GUI
import json


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

        elif self.table.croupier['points'] > 21:
            is_win = 1
            self.table.user['ante'] = self.table.user['ante'] * 2

        elif self.table.user['points'] == 21:
            if self.table.croupier['points'] == 21:
                is_win = 1

            else:
                is_win = 1
                self.table.user['ante'] *= 3

        elif self.table.croupier['points'] == 21:
            is_win = 0

        elif self.table.user['points'] > self.table.croupier['points']:
            is_win = 1

        # log результата игры
        with open('game_log', 'a') as f:
            if is_win:
                log = 'Result of the game: {}, Win'.format(self.table.user['name'])
            else:
                log = 'Result of the game: {}, Lesion'.format(self.table.user['name'])
            f.write(log + '\n')

        # Вскрыться: показать карты крупье, карты игрока и выйграл или проиграл игрок
        GUI.show_part_end(self.table.croupier, self.table.user, is_win)


        # Показать и записать статистику игры
        line = self.write_stat_game(is_win)
        GUI.show_stat_game(line[0], line[1])

        return is_win

    def write_stat_game(self, is_win):
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
            stat_log = {}
            stat_log[self.table.user['name']] = line

            with open('stat_log.json', 'w') as fw:
                json.dump(stat_log, fw)

            return line

        try:
            # Если файл существует и в нём есть нужная запись
            # Достаем из него значения и увеличиваем одно из них
            line = stat_log[self.table.user['name']]

        except KeyError:
            # Если файл существует, но в нём нет нужной записи
            line = [0, 0, 0]

        if is_win:
            line[0] += 1
        else:
            line[1] += 1

        stat_log[self.table.user['name']] = line

        with open('stat_log.json', 'w') as fw:
            json.dump(stat_log, fw)

        return line

    @classmethod
    def write_stat_game_all(cls, name_game, balance, win=0, les=0):
        line = [win, les, balance]
        try:
            # Открыть файл и считываем json объект
            with open('stat_log.json', 'r') as fr:
                stat_log = json.loads(fr.read())

        except IOError:
            # Если файл не существует
            # Формируем словарь и записываем в json файл
            stat_log = {}
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
        with open('game_log', 'a')as f:
            log = 'Clear card and ante '
            f.write(log+'\n')

        return gain
