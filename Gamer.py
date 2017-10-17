class Gamer:
    """Класс: Игрок.
    Создает игрока с именем и начальным капиталлом переданным конструктору.
    Хранит баланс игрока.
    При печати показывает текущее значение баланса.

    """

    def __init__(self, name, start_capital, view_file):
        """Сохраняет начальноое значение баланса.

        :param start_capital: Значение стартового капиталла.
        """
        self.name = name
        self.balance = start_capital
        self.view_file = view_file

    def __str__(self):
        return 'Текущий баланс: ' + str(self.balance)

    def place_ante(self, size_ante):
        """Сделать ставку.
        Вычитает и возвращает желаемую сумму ставки из баланса игрока.

        :return: Возвращает сумму ставки, если есть необходимая сумма на балансе.
        """
        if size_ante <= self.balance:
            # Сделать запись о списывании средств
            self.balance -= size_ante
            self.view_file.write_stat_game_all(self.name, self.balance)

            self.view_file.write_game_log('Debit off gamer: {0}, size: {1}, balance: {2}'.format(self.name, size_ante,
                                                                                                 self.balance))

            return size_ante

    def put_gain(self, gain):
        self.balance += gain

        if gain != 0:
            self.view_file.write_stat_game_all(self.name, self.balance)

        self.view_file.write_game_log('Put gain gamer: {0}, size: {1}, balance: {2}'.format(self.name, gain,
                                                                                            self.balance))
