if __name__ != '__main__':
    print('This main programm !\nRun this module !')
    exit()

import json
from GUI import View, ViewFile
from Gamer import Gamer
from Table import Table
from Croupier import Croupier

view = View()
view_file = ViewFile()

# Выводим приветственное сообщение, главное меню и ждём действий пользователя
view.show_start_message()

# Показывает что игра может быть загружена
is_restore_game = 0
_flag = ['', '', '', {}]

# Загрузка части лог файла
block_log = view_file.read_part_log(10)

if block_log:
    # Проверка корректности завершения прошлого сеанса игры
    if block_log[-1].find('End game') == -1:
        # Завершение игры прошло не корректно, можно восстановить предыдущую игру
        is_restore_game = 1

# log начала игры
view_file.write_game_log('---------------Start game BlackJack---------------')

while True:
    # Проверка на существование созданных игр
    is_exist_games = view_file.check_exist_game()

    # Показать главное меню
    if is_exist_games:
        if is_restore_game:
            view.show_main_menu([1, 2, 3, 10])
        else:
            view.show_main_menu([1, 2, 10])

        stat_log = view_file.read_stat()

    else:
        if is_restore_game:
            view.show_main_menu([1, 3, 10])
        else:
            view.show_main_menu([1, 10])
    view_file.write_game_log('Load_menu')
    is_exist_games = 0
    act = view.get_start_action()

    while True:
        # Если пользователь ввёл: 1
        if act == '1':
            # Создаём пользователя
            # Запрашиваем имя с консоли и считываем значение стартого капиталла из конфига
            if _flag[0] != '/1' and _flag[1] != '/2' and is_exist_games == 0:

                conf = view_file.read_conf()

                gamer = Gamer(str(view.get_name_gamer()), conf['start_capital'], view_file)
                view_file.write_stat_game_all(gamer.name, gamer.balance)

                # log создание пользователя
                view_file.write_game_log('Create gamer: {0}, balance: {1}'.format(gamer.name, gamer.balance))

            # Выводим стартовый капитал
            if is_exist_games == 0:
                # Если не загружали игру
                view.show_start_capital(gamer)
            else:
                # Если загружали игру
                if _flag[0] == '/1':
                    view.show_name_gamer(gamer)
                    view.show_capital(gamer)
                    if _flag[2] != '/3':
                        _flag = ['', '', '', {}]
                elif _flag[1] != '/2':
                    view.show_capital(gamer)

            # Показываем следующее меню (игровое меню),
            # ждём действий пользователя и заходим в соответствующий блок условий
            while True:
                if _flag[1] == '/2':
                    view.show_name_gamer(gamer)
                    act = '1'
                    _flag = ['', '', '', {}]
                elif _flag[2] != '/3':
                    view.show_game_menu()
                    act = view.get_action()

                if act == '1':

                    if 'table' not in locals():
                        # Создаем стол, крупье и начинаем игру
                        table = Table(gamer.name, view_file)
                        croupier = Croupier(table, view, view_file)

                    if _flag[2] == '/3':
                        from Card import Card

                        # Восстановить очки и карты крупье
                        table.croupier['points'] = _flag[3]['points_croup']
                        for c in _flag[3]['card_croup']:
                            if c.isdigit():
                                table.croupier['card'].append(Card(c, int(c)))
                            else:
                                table.croupier['card'].append(Card(c, 10))

                        # Восстановить очки, карты и ставку игрока
                        table.user['points'] = _flag[3]['points_user']
                        table.user['ante'] = _flag[3]['ante']
                        for c in _flag[3]['card_user']:
                            if c.isdigit():
                                table.user['card'].append(Card(c, int(c)))
                            else:
                                table.user['card'].append(Card(c, 10))

                        # log восстановления карт
                        view_file.write_game_log('Restored_card')

                        # Выдать карты игроку
                        if croupier.issue_cards_gamer(1) == 1:
                            continue

                        _flag = ['', '', '', {}]

                    else:

                        # log начала партии
                        view_file.write_game_log('Start_part ')

                        # Спросить размер и поставить ставку
                        try:
                            ante = int(view.get_ante(gamer))
                            if gamer.balance - ante < 0:
                                view.show_not_enough_money()

                                # log окончания партии
                                view_file.write_game_log('End_part ')

                                continue

                        except ValueError:
                            # log конца партии
                            view_file.write_game_log('End_part ')

                            continue

                        if 0 < ante:
                            table.user['ante'] = gamer.place_ante(ante)
                        else:

                            # log конца партии
                            view_file.write_game_log('End_part ')

                            continue
                        # Выдать карты крупье
                        croupier.issue_cards_croupier()

                        # Выдать карты игроку
                        if croupier.issue_cards_gamer() == 1:
                            continue

                    # Узнать исход игры
                    is_win = croupier.calculate_points()

                    stat_log = view_file.read_stat()
                    # Очистить стол, убрат карты и ставку
                    gain = croupier.clear_card_get_ante(is_win)
                    # При выйгрыше увеличить баланс игрока
                    gamer.put_gain(gain)

                    # log конца партии
                    view_file.write_game_log('End_part ')

                elif act == '0':
                    break
                else:
                    # если введён неправельный символ
                    continue
            break

        # Если пользователь ввёл: 0
        elif act == '0':
            # log заверщения игры
            view_file.write_game_log('================End game BlackJack================')

            # Показываем прощальное сообщение и заверщаем программу
            view.show_bye()
            exit()

        elif act == '2':
            if _flag[0] == '/1':

                stat_log = view_file.read_stat()

                # Случай восстановления после сбоя
                gamer = Gamer(_flag[3]['name_game'], stat_log[_flag[3]['name_game']][2], view_file)

                if _flag[1] == '/2':
                    _flag[0] = ''

                # log загрузки игры
                view_file.write_game_log('Load_game: ' + _flag[3]['name_game'])

            else:

                stat_log = view_file.read_stat()

                # Загрузить список начитых игр
                names = set(stat_log)
                view.show_list_games(names)

                # log загрузки списка игр
                view_file.write_game_log('Load_list games')

                act = view.get_action()

                # Загрузить игру
                try:
                    act = int(act)
                except ValueError:
                    break

                names = list(names)

                if act == 0 or act > len(names):
                    break

                gamer = Gamer(names[act-1], stat_log[names[act-1]][2], view_file)

                # log загрузки игры
                view_file.write_game_log('Load_game: ' + names[act-1])

            is_exist_games = 1
            act = '1'

        elif act == '3':
            # Восстановить игру после некорректного завершения

            # log восстановления игры
            view_file.write_game_log('Restore after fail')
            fifty = 0

            while len(block_log) != 0:
                str_log = block_log.pop()
                stage = str_log[:str_log.find(' ')]

                if stage.startswith('-'):
                    stage = stage.replace('---------------', '')

                if stage == 'Start' or stage == 'Load_menu':
                    act = ''
                    break

                elif stage == 'Start_part':
                    _flag[0] = '/1'
                    _flag[1] = '/2'
                    _flag[3] = {'name_game': str_log[str_log.find(': ') + 2:str_log.find(',')]}
                    continue

                elif stage == 'Load_game:' or stage == 'Create':
                    _flag[0] = '/1'
                    _flag[3] = {'name_game': str_log[str_log.find(': ') + 2:str_log.find(',')]}
                    act = '2'
                    break

                elif stage == 'Restore':
                    while stage != 'Start':
                        str_log = block_log.pop()
                        stage = str_log[:str_log.find(' ')]

                        if stage.startswith('-'):
                            stage = stage.replace('---------------', '')

                elif stage == 'Load_list':
                    act = '2'
                    break

                elif stage == 'Issuance':
                    name_game = str_log[str_log.find(': ') + 2:str_log.find(';')]
                    card_user = str_log[str_log.find('; ') + 2:str_log.find(' ,')].split(' ')
                    points_user = int(str_log[str_log.find('s: ') + 3:-1])

                    while str_log.find('croupier') == -1:
                        str_log = block_log.pop()

                    card_croup = str_log[str_log.find(': ') + 2:str_log.find(' ,')].split(' ')
                    points_croup = int(str_log[str_log.find('s: ') + 3:-1])

                    while stage != 'Debit':
                        str_log = block_log.pop()
                        stage = str_log[:str_log.find(' ')]

                    ante = int(str_log[str_log.find('e: ') + 3:str_log.find(', b')])

                    _flag[0] = '/1'
                    _flag[1] = ''
                    _flag[2] = '/3'
                    _flag[3] = {'name_game': name_game, 'card_user': card_user, 'points_user': points_user,
                                'card_croup': card_croup, 'points_croup': points_croup, 'ante': ante}

                    act = '2'
                    break

                elif stage == 'End_part':
                    while stage != 'Load_game:' and stage != 'Create':
                        str_log = block_log.pop()
                        stage = str_log[:str_log.find(' ')]

                    _flag[0] = '/1'
                    _flag[3] = {'name_game': str_log[str_log.find(': ') + 2:str_log.find(',')]}
                    act = '2'
                    break

                if len(block_log) <= 0:
                    if fifty:
                        view.show_restore_fail()
                        break

                    block_log = view_file.read_part_log(50)
                    fifty = 1

            else:
                view.show_restore_fail()
                act = ''

            is_restore_game = 0

        else:
            break
