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
GUI.show_main_menu([1, 10])
act = GUI.get_start_action()

# Если пользователь ввёл: 1
if act == '1':

    f = open("config.json", "r")
    conf = json.loads(f.read())

    # Создаём пользователя
    # Запрашиваем имя с консоли и считываем значение стартого капиталла из конфига
    gamer = Gamer(str(GUI.get_name_gamer()), conf['start_capital'])
    # Выводим стартовый капитал и закрываем файл конфига
    GUI.show_start_capital(gamer)
    f.close()

    # Показываем следующее меню, ждём действий пользователя и заходим в соответствующий блок условий
    GUI.show_game_menu()
    act = GUI.get_action()
    if act == '1':
        # Создаем стол, крупье и начинаем игру
        table = Table(gamer.name)
        croupier = Croupier(table)
        while True:
            # Спросить размер и поставить ставку
            table.user['ante'] = gamer.place_ante(int(GUI.get_ante()))
            croupier.issue_cards_gamer()
            croupier.issue_cards_croupier()

            GUI
            act = GUI.get_action()
            if act:
                break

    else:
        # Показываем прощальное сообщение и заверщаем программу
        GUI.show_bye()
        exit()

# Если пользователь ввёл: 0
elif act == '0':
    # Показываем прощальное сообщение и заверщаем программу
    GUI.show_bye()
    exit()
