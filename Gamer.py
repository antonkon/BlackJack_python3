from Croupier import Croupier


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
            self.balance -= size_ante
            Croupier.write_stat_game_all(self.name, self.balance)
            with open('game_log', 'a') as f:
                f.write('Debit off gamer: {0}, size: {1}, balance: {2}\n'.format(self.name, size_ante, self.balance))


            return size_ante

    def put_gain(self, gain):
        self.balance += gain
        if gain != 0:
            Croupier.write_stat_game_all(self.name, self.balance)
        with open('game_log', 'a') as f:
            f.write('Put gain gamer: {0}, size: {1}, balance: {2}\n'.format(self.name, gain, self.balance))