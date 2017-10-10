if __name__ != '__main__':
    print('This main programm !\nRun this module !')
    exit()

import json
from GUI import GUI
from Gamer import Gamer
from Table import Table
from Croupier import Croupier


# Выводим приветственное сообщение, главное меню и ждём действий пользователя
GUI.show_start_message()

# Показывает что игра может быть загружена
is_restore_game = 0
_flag = ['', '', '']
__min_stack = 10

# Загрузка части лог файла
with open('game_log', 'r') as f:
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

# Проверка корректности завершения прошлого сеанса игры
if block_log[-1].find('End game') == -1:
    # Завершение игры прошло не корректно, можно восстановить предыдущую игру
    is_restore_game = 1

# log начала игры
with open('game_log', 'a') as f:
    log = '---------------Start game BlackJack---------------'
    f.write(log+'\n')

while True:
    # Проверка на существование созданных игр
    try:
        # Открыть файл и считываем json объект
        with open('stat_log.json', 'r') as fr:
            stat_log = json.loads(fr.read())

        is_exist_games = 1

    except IOError:
        is_exist_games = 0

    # Показать главное меню
    if is_exist_games:
        if is_restore_game:
            GUI.show_main_menu([1, 2, 3, 10])
        else:
            GUI.show_main_menu([1, 2, 10])

    else:
        if is_restore_game:
            GUI.show_main_menu([1, 3, 10])
        else:
            GUI.show_main_menu([1, 10])

    is_exist_games = 0
    act = GUI.get_start_action()

    while True:
        # Если пользователь ввёл: 1
        if act == '1':
            # Создаём пользователя
            # Запрашиваем имя с консоли и считываем значение стартого капиталла из конфига
            if _flag[0] != '/1' and _flag[1] != '/2' and is_exist_games == 0:
                with open("config.json", "r") as f:
                    conf = json.loads(f.read())

                gamer = Gamer(str(GUI.get_name_gamer()), conf['start_capital'])
                Croupier.write_stat_game_all(gamer.name, gamer.balance)

                # log создание пользователя
                with open('game_log', 'a') as f:
                    log = 'Create gamer: {0}, balance: {1}'.format(gamer.name, gamer.balance)
                    f.write(log + '\n')

            # Выводим стартовый капитал
            if is_exist_games == 0:
                # Если не загружали игру
                GUI.show_start_capital(gamer)
            else:
                # Если загружали игру
                if _flag[0] == '/1':
                    GUI.show_name_gamer(gamer)
                    GUI.show_capital(gamer)
                    _flag = ['', '', '']
                elif _flag[1] != '/2':
                    GUI.show_capital(gamer)

            # Показываем следующее меню (игровое меню),
            # ждём действий пользователя и заходим в соответствующий блок условий
            while True:
                if _flag[1] == '/2':
                    GUI.show_name_gamer(gamer)
                    act = '1'
                    _flag = ['', '', '']
                else:
                    GUI.show_game_menu()
                    act = GUI.get_action()

                if act == '1':

                    if 'table' not in locals():
                        # Создаем стол, крупье и начинаем игру
                        table = Table(gamer.name)
                        croupier = Croupier(table)

                    # log начала партии
                    with open('game_log', 'a') as f:
                        log = 'Start_part '
                        f.write(log + '\n')
                    # Спросить размер и поставить ставку
                    try:
                        ante = int(GUI.get_ante(gamer))
                        if gamer.balance - ante < 0:
                            GUI.show_not_enough_money()

                            with open('game_log', 'a') as f:
                                log = 'End_part '
                                f.write(log + '\n')
                            continue

                    except ValueError:
                        # log конца партии
                        with open('game_log', 'a') as f:
                            log = 'End_part '
                            f.write(log + '\n')
                        continue

                    if 0 < ante:
                        table.user['ante'] = gamer.place_ante(ante)
                    else:

                        # log конца партии
                        with open('game_log', 'a') as f:
                            log = 'End_part '
                            f.write(log + '\n')
                        continue
                    # Выдать карты крупье
                    croupier.issue_cards_croupier()
                    # Выдать карты игроку
                    if croupier.issue_cards_gamer() == 1:
                        continue
                    # Узнать исход игры
                    is_win = croupier.calculate_points()
                    # Очистить стол, убрат карты и ставку
                    gain = croupier.clear_card_get_ante(is_win)
                    # При выйгрыше увеличить баланс игрока
                    gamer.put_gain(gain)

                    # log конца партии
                    with open('game_log', 'a') as f:
                        log = 'End_part '
                        f.write(log + '\n')

                elif act == '0':
                    break
                else:
                    # если введён неправельный символ
                    continue
            break

        # Если пользователь ввёл: 0
        elif act == '0':
            # log заверщения игры
            with open('game_log', 'a') as f:
                log = '================End game BlackJack================'
                f.write(log + '\n')

            # Показываем прощальное сообщение и заверщаем программу
            GUI.show_bye()
            exit()

        elif act == '2':
            if _flag[0] == '/1':
                # Случай восстановления после сбоя
                gamer = Gamer(_flag[2], stat_log[_flag[2]][2])

                if _flag[1] == '/2':
                    _flag[0] = ''

                with open('game_log', 'a') as f:
                    log = 'Load_game: ' + _flag[2]
                    f.write(log + '\n')
            else:
                # Загрузить список начитых игр
                names = set(stat_log)
                GUI.show_list_games(names)
                # log загрузки списка игр
                with open('game_log', 'a') as f:
                    log = 'Load_list games'
                    f.write(log + '\n')

                act = GUI.get_action()
                # Загрузить игру
                # log загрузки игры

                try:
                    act = int(act)
                except ValueError:
                    break

                names = list(names)

                if act == 0 or act > len(names):
                    break

                gamer = Gamer(names[act-1], stat_log[names[act-1]][2])

                with open('game_log', 'a') as f:
                    log = 'Load_game: ' + names[act-1]
                    f.write(log + '\n')

            is_exist_games = 1
            act = '1'

        elif act == '3':
            # Восстановить игру после некорректного завершения
            # block_log
            # log восстановления игры
            with open('game_log', 'a') as f:
                log = 'Restore after fail'
                f.write(log + '\n')

            while len(block_log) != 0:
                str_log = block_log.pop()
                stage = str_log[:str_log.find(' ')]

                if stage.startswith('-'):
                    stage = stage.replace('---------------', '')

                if stage == 'Start':
                    act = ''
                    break

                elif stage == 'Start_part':
                    _flag[0] = '/1'
                    _flag[1] = '/2'
                    _flag[2] = str_log[str_log.find(': ') + 2:str_log.find(',')]
                    continue

                elif stage == 'Load_game:' or stage == 'Create':
                    _flag[0] = '/1'
                    _flag[2] = str_log[str_log.find(': ') + 2:str_log.find(',')]
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
                    while stage != 'Debit':
                        str_log = block_log.pop()
                        stage = str_log[:str_log.find(' ')]

                    # Вернуть ставку
                    name_game = str_log[str_log.find(': ')+2:str_log.find(',')]
                    ante = int(str_log[str_log.find('e: ')+3:str_log.find(', b')])
                    balance = int(str_log[str_log.find('balance: ')+9:-1])
                    Croupier.write_stat_game_all(name_game, ante + balance)

                    with open('stat_log.json', 'r') as fr:
                        stat_log = json.loads(fr.read())

                    continue

                elif stage == 'End_part':
                    while stage != 'Load_game:' and stage != 'Create':
                        str_log = block_log.pop()
                        stage = str_log[:str_log.find(' ')]

                    _flag[0] = '/1'
                    _flag[2] = str_log[str_log.find(': ') + 2:str_log.find(',')]
                    act = '2'
                    break

            else:
                GUI.show_restore_fail()
                act = ''

            is_restore_game = 0

        else:
            break
