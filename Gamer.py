class Gamer:
    """Класс: Игрок.
    Создает игрока с именем и начальным капиталлом переданным конструктору.
    Хранит баланс игрока.
    При печати показывает текущее значение баланса.

    """

    def __init__(self, name, start_capital):
        """Сохраняет начальноое значение баланса.

        :param start_capital: Значение стартового капиталла.
        """
        self.name = name
        self.balance = start_capital

    def __str__(self):
        return 'Текущий баланс: ' + str(self.balance)

    def place_ante(self, size_ante):
        """Сделать ставку.
        Вычитает и возвращает желаемую сумму ставки из баланса игрока.

        :return: Возвращает сумму ставки, если есть необходимая сумма на балансе.
        """
        if size_ante <= self.balance:
            # Сделать запись о списывании средств
            f = open('game_log', 'w')
            f.write('Debit gamer: {0} at the rate of: {1}, it was: {2}'.format(self.name, size_ante, self.balance))
            f.close()
            self.balance -= size_ante
            return size_ante
