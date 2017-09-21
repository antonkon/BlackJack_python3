"""Консольный интерфейс.

"""


def show_start_message():
    print('Здравствуйте, это игра BlackJack.\n')


def show_main_menu(lines_menu):
    menu = {1: '  1. Новая игра.\n', 2: '  2. Загрузить игру.\n', 10: '  0. Выход.\n'}
    mes = ''
    for line in sorted(lines_menu):
        mes += menu[line]

    print(mes)


def get_start_action():
    return input("Введите соответствующую цифру: ")


def get_action():
    return input("> ")


def get_name_gamer():
    """Спрашивает у пользователя желаемое имя игрока

    :return: Возвращает введёное имя игрока
    """
    print('---------------------------------')
    print('           Новая игра:')
    name = input('Введите имя игрока: ')
    return name


def show_game_menu():
    print('---------------------------------')
    print('  1. Играть.\n  0. Выйти.')


def show_start_capital(gamer):
    print('Начальный баланс: ' + str(gamer.balance))


def show_capital(gamer):
    print(gamer)


def show_bye():
    print('---------------------------------')
    print('Досвидания!')
