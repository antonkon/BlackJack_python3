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

# log начала игры
f = open('game_log', 'a')
log = '---------------Start game BlackJack---------------'
f.write(log+'\n')
f.close()

# ! убрать
is_exist_games = 0

while True:
    # Загрузка игр
    # ! реализовать


    if is_exist_games:
        GUI.show_main_menu([1, 2, 10])
    else:
        GUI.show_main_menu([1, 10])
    act = GUI.get_start_action()
    # Если пользователь ввёл: 1
    while True:
        if act == '1':
            f = open("config.json", "r")
            conf = json.loads(f.read())
            f.close()
            # Создаём пользователя
            # Запрашиваем имя с консоли и считываем значение стартого капиталла из конфига
            gamer = Gamer(str(GUI.get_name_gamer()), conf['start_capital'])

            # log создание пользователя
            f = open('game_log', 'a')
            log = 'Create gamer: {0}, balance: {1}'.format(gamer.name, gamer.balance)
            f.write(log + '\n')
            f.close()

            # создали игру => есть игра
            # ! потом убрать
            is_exist_games = 1

            # Выводим стартовый капитал
            GUI.show_start_capital(gamer)

            # Показываем следующее меню (игровое меню), ждём действий пользователя и заходим в соответствующий блок условий
            while True:
                if act != 1:
                    GUI.show_game_menu()
                    act = GUI.get_action()

                if act == '1':
                    # Создаем стол, крупье и начинаем игру
                    table = Table(gamer.name)
                    croupier = Croupier(table)
                    while True:
                        # Спросить размер и поставить ставку
                        # ! Обработать неправильное значение ставки
                        table.user['ante'] = gamer.place_ante(int(GUI.get_ante()))
                        croupier.issue_cards_croupier()
                        croupier.issue_cards_gamer()
                        is_win = croupier.calculate_points()
                        gain = croupier.clear_card_get_ante(is_win)
                        gamer.put_gain(gain)

                        GUI.show_game_menu()
                        act = GUI.get_action()
                        if act == '1':
                            continue
                        else:
                            break

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
            f = open('game_log', 'a')
            log = '================End game BlackJack================'
            f.write(log + '\n')
            f.close()

            # Показываем прощальное сообщение и заверщаем программу
            GUI.show_bye()
            exit()
        else:
            break
