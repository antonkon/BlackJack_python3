if __name__ != '__main__':
    print('This main programm !\nRun this module !')
    exit()

import json
import GUI
from Gamer import Gamer
from Table import Table
from Croupier import Croupier


# Выводим приветственное сообщение, главное меню и ждём действий пользователя
GUI.show_start_message()


is_restore_game = 0
_flag = ['', '']

# Загрузка части лог файла
with open('game_log', 'r') as f:
    block_log = []
    for line in f.readlines():
        if line.find('Start game') != -1:
            block_log = []
        block_log.append(line)

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

    act = GUI.get_start_action()

    while True:
        # Если пользователь ввёл: 1
        if act == '1':
            # Создаём пользователя
            # Запрашиваем имя с консоли и считываем значение стартого капиталла из конфига
            if not 'gamer' in globals():
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
                is_exist_games = 1
                GUI.show_start_capital(gamer)
            else:
                # Если загружали игру
                if _flag[0] != '/1':
                    GUI.show_capital(gamer)

            # Показываем следующее меню (игровое меню), ждём действий пользователя и заходим в соответствующий блок условий
            while True:
                if _flag[0] == '/1':
                    act = '1'
                    _flag = ['']
                else:
                    GUI.show_game_menu()
                    act = GUI.get_action()

                if act == '1':
                    # Создаем стол, крупье и начинаем игру
                    table = Table(gamer.name)
                    croupier = Croupier(table)
                    while True:
                        # log начала партии
                        with open('game_log', 'a') as f:
                            log = 'Start_part '
                            f.write(log + '\n')
                        # Спросить размер и поставить ставку
                        try:
                            ante = int(GUI.get_ante(gamer))

                        except ValueError:
                            act = '/1'
                            break

                        if 0 < ante:
                            table.user['ante'] = gamer.place_ante(ante)
                        else:
                            act = '/1'
                            # log конца партии
                            with open('game_log', 'a') as f:
                                log = 'End_part '
                                f.write(log + '\n')
                            break
                        # Выдать карты крупье
                        croupier.issue_cards_croupier()
                        # Выдать карты игроку
                        croupier.issue_cards_gamer()
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

                        act = '/1'
                        break

                    if act == '/1':
                        continue
                    else:
                        break
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
                gamer = Gamer(_flag[1], stat_log[_flag[1]][2])
                try:
                    _flag.index('/2')
                except Exception:
                    _flag[0] = ''
            else:
                # Загрузить список начитых игр
                names = set(stat_log)
                GUI.show_load_games(names)
                # log загрузки списка игр
                with open('game_log', 'a') as f:
                    log = 'Load_list games'
                    f.write(log + '\n')

                act = GUI.get_action()
                # Загрузить игру
                # log загрузки игры
                try:
                    act = int(act)
                except Exception:
                    break
                names = list(names)
                gamer = Gamer(names[act-1], stat_log[names[act-1]][2])

                with open('game_log', 'a') as f:
                    log = 'Load_game: ' + names[act-1]
                    f.write(log + '\n')

            act = '1'

        elif act == '3':
            # Восстановить игру после некорректного завершения
            # block_log
            # log восстановления игры
            with open('game_log', 'a') as f:
                log = 'Restore after fail'
                f.write(log + '\n')

            while block_log != []:
                str_log = block_log.pop()
                stage = str_log[:str_log.find(' ')]

                # if stage == 'Start' or
                if stage == 'Create':
                    _flag = ['/1', str_log[str_log.find(': ')+2:str_log.find(',')]]
                    act = '2'
                    break

                elif stage == 'Start_part':
                    str_log = block_log.pop()
                    stage = str_log[:str_log.find(' ')]

                    if stage == 'Load_game:' or stage == 'Create':
                        _flag = ['/1', str_log[str_log.find(': ') + 2:str_log.find(',')], '/2']

                    act = '2'
                    break

            is_restore_game = 0

        else:
            break
