import json
from Deck import Deck
from Shoe import Shoe


class Table:
    """Класс: Стол.
     Содержит карты Игрока и Компьютера.
     Раздаёт карты.

    """
    user = {'name': '', 'card': [], 'points': 0, 'ante': 0}
    croupier = {'name': 'Крупье', 'card': [], 'points': 0}

    def __init__(self, user_name):
        """Создаёт стол.
        Создание стола заключается в добавлении пользователя в стол.

        :param user_name: имя игрока
        :param get_card: Функция выдачи карт.
        """
        self.user['name'] = user_name

        # Создать карты и шуз
        # открыть файл config и взять из него параметр: количество колод
        f = open("config.json", "r")
        conf = json.loads(f.read())

        # Создаём шуз: передаём функцию которая возвращает карты и количество колод участвующих в игре
        self.shoe = Shoe(Deck.create_deck, conf['number_deck'])

        f.close()
