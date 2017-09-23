"""Консольный интерфейс.

"""


def show_start_message():
    """ Вывести приветственное сообщение. """
    print('Здравствуйте, это игра BlackJack.\n')


def show_main_menu(lines_menu):
    """ Показать главное меню. """
    menu = {1: '  1. Новая игра.\n', 2: '  2. Загрузить игру.\n', 10: '  0. Выход.\n'}
    mes = ''
    for line in sorted(lines_menu):
        mes += menu[line]

    print(mes)


def get_start_action():
    """ Узнать первоначальное действие игрока. """
    return input("Введите соответствующую цифру: ")


def get_action():
    """ Узнать действие игрока. """
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
    """ Показать игровое меню. """
    print('---------------------------------')
    print('  1. Играть.\n  0. Выйти.')


def show_start_capital(gamer):
    """ Показать начальный баланс. """
    print('Начальный баланс: ' + str(gamer.balance))


def show_capital(gamer):
    """ Показать баланс. """
    print(gamer)


def show_bye():
    """ Показать прощальное сообщение. """
    print('---------------------------------')
    print('До свидания!')


def get_ante():
    """ Спросить размер ставки. """
    return input('Размер вашей ставки ?\n> ')


def show_card(cards):
    """ Показать карты. """
    s = '{0}\n{1}\n{2}\n{3}'.format(' ___ '*len(cards), '|   |'*len(cards), '| {.name} |'*len(cards), '|___|'*len(cards))
    print(s.format(*cards).replace('10 ', '10'))


def show_err(err):
    """ Показать ошибку. """
    if err == 101:
        print('ERROR: Ставка не сделана!')


def show_game_dial():
    """ Показать игровой диалог. """
    print('---------------------------------')
    print('  1. Ещё.\n  0. Хватит.')
