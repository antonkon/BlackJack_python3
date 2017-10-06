"""Консольный интерфейс.

"""


def show_start_message():
    """ Вывести приветственное сообщение. """
    print('Здравствуйте, это игра BlackJack.\n')


def show_main_menu(lines_menu):
    """ Показать главное меню. """
    print('---------------------------------')
    menu = {1: '  1. Новая игра.\n', 2: '  2. Загрузить игру.\n', 3: '  3. Восстановить игру.\n', 10: '  0. Выход.\n'}
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
    name = input('Введите название игры: ')
    return name


def show_game_menu():
    """ Показать игровое меню. """
    print('---------------------------------')
    print('  1. Играть.\n  0. Назад.')


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


def get_ante(gamer):
    """ Спросить размер ставки. """
    print('Ваш баланс: {}'.format(str(gamer.balance)))
    return input('Размер вашей ставки ?\n> ')


def show_card_points(cards, points):
    """ Показать карты и очки. """
    s = '{0}\n{1}\n{2}\n{3}'.format(' ___ '*len(cards), '|   |'*len(cards),
                                    '| {.name} |'*len(cards), '|___|'*len(cards))
    print(s.format(*cards).replace('10 ', '10'))
    print('Кол-во очков: '+str(points))


class ErrorCode():
    not_bet = 101

    error_dict = {
        not_bet: 'ERRPR: '
    }


def show_err(err):
    """ Показать ошибку. """
    if err == ErrorCode.not_bet:
        print('ERROR: Ставка не сделана!')


def show_game_dial():
    """ Показать игровой диалог. """
    print('---------------------------------')
    print('  1. Ещё.\n  0. Хватит.')


def show_part_end(player1, player2, is_win):
    print('---------------------------------')
    print('Карты ' + player1['name'] + ':')
    show_card_points(player1['card'], player1['points'])
    print('Карты ' + player2['name'] + ':')
    show_card_points(player2['card'], player2['points'])

    if is_win:
        print('Вы выйграли !')
    else:
        print('Вы проиграли !')


def show_stat_game(win, les):
    """Показать статистику игры

    :param win: Кол-во выйгрышей игрока
    :param les: Кол-во пройгрышей игрока
    :return:
    """
    print('{} : {} (выйгрышей : пройгрышей)'.format(str(win), str(les)))
def show_load_games(users):
    print('---------------------------------')
    print('Выберите игру:')
    i = 0
    for user in users:
        i += 1
        print('  '+str(i)+'. '+user)
