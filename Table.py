import json
from Deck import Deck
from Shoe import Shoe


class Table:
    """Класс: Стол.
     Содержит карты Игрока и Компьютера.
     Раздаёт карты.

    """
    user = ''
    ante = 0

    def __init__(self, user, get_card):
        """Создаёт стол.
        Создание стола заключается в добавлении пользователя в стол.

        :param user: Игрок. Gamer
        :param get_card: Функция выдачи карт.
        """
        self.user = user
        self.get_card = get_card

        # Создать карты, шуз
        # открыть файл config и взять из него параметр: количество колод
        f = open("config.json", "r")
        conf = json.loads(f.read())

        # Создаём шуз: передаём функцию которая возвращает карты и количество колод участвующих в игре
        self.shoe = Shoe(Deck.create_deck, conf['number_deck'])

        f.close()
