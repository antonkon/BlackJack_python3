from Card import Card


class Deck:
    """ Класс: Колода.
     Создаёт колоду карт.

     """
    @classmethod
    def create_deck(cls):
        """Создаёт и возвращает колоду карт.

        :return: Возвращает множество с картами.
        """
        deck = set()
        for j in range(4):
            for i in range(2, 11):
                deck.add(Card(str(i), i))

        for i in range(4):
            deck.add(Card('V', 10))
            deck.add(Card('D', 10))
            deck.add(Card('K', 10))
            deck.add(Card('T', 11))

        return deck
