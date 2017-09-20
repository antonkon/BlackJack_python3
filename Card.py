class Card:
    """ Класс: Карта.
     Хранит имя и значение карты.

     """
    def __init__(self, name, value):
        """ Конструктор.
        Создает объект карты.

        :param name: Название карты.
        :param value: Количество очков карты.
        """
        self.name = name
        self.value = value

    def __str__(self):
        """ Красиво выводит карту на экран.

        """
        return ' ___\n|   |\n| {} |\n|___|'.format(self.name)
