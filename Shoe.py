import random

class Shoe:
    """Класс: Шуз.
    Создает и инициализирует устройство выдачи карт.
    Хранит и выдаёт карты.
    Преремешивает карты.

    """
    # Хранит все карты в шузе
    shoe = []

    def __init__(self, func_deck, num_deck):
        """Создает шуз.

        :param func_deck: Функция возвращающая множество карт. Каждые элемент множества есть карта.
        :param num_deck: Количество колод участвующих в игре.
        """
        # Проверяем возвращает ли переданная функция множество
        deck = func_deck()
        if type(deck) != set:
            print('Error: deck не является множеством !')
            return

        # Складываем все карты в одно место, в шуз
        for i in range(num_deck):
            self.shoe.extend(deck)
            deck = func_deck()

        # вычисляется кол-во карт, чтобы определять когда перетасовывать
        self.num_cards = len(self.shoe)

        # Перетасовываем карты
        self.shuffle()

    def shuffle(self):
        """Перетасовать карты в шузе.

        """
        random.shuffle(self.shoe)

    def get_card(self):
        """Выдать карту.

        :return: Возвращает объект Card, экземпляр карты.
        """
        return self.shoe.pop(0)
