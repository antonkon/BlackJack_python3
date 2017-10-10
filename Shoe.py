import random


class Shoe:
    """Класс: Шуз.
    Создает и инициализирует устройство выдачи карт.
    Хранит и выдаёт карты.
    Преремешивает карты.

    """
    # Хранит все карты в шузе
    shoe = []
    # Счётчик выданных карт
    num_card_iss = 0

    def __init__(self, func_deck, num_deck):
        """Создает шуз.

        :param func_deck: Функция возвращающая колоду карт. Каждые элемент множества есть карта.
        :param num_deck: Количество колод участвующих в игре.
        """
        # Проверяем возвращает ли переданная функция множество
        self.deck = func_deck()
        if type(self.deck) != set:
            print('Error: deck не является множеством !')
            return

        # Складываем все карты в одно место, в шуз
        for i in range(num_deck):
            self.shoe.extend(self.deck)

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
        # Берём с начала списка карту, помещаем в конец списка и возвращаем из функции
        card = self.shoe.pop(0)
        self.shoe.append(card)
        # Увеличиваем счётчик выданных карт
        self.num_card_iss += 1

        # Проверяем не выдано ли более одной трети всех карт и если так, перемешиваем их
        if self.num_card_iss > self.num_cards/3:
            self.shuffle()
            self.num_card_iss = 0

        return card
