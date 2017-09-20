class Gamer:
    """Класс: Игрок.
    Создает игрока с начальным капиталлом переданным конструктору.
    Хранит баланс игрока.
    При печать показывает текущее значение баланса.

    """
    def __init__(self, start_capital):
        """Сохраняет начальноое значение баланса.

        :param start_capital: Значение стартового капиталла.
        """
        self.balance = start_capital

    def __str__(self):
        return 'Текущий балонс: ' + self.balance