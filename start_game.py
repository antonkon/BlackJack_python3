if __name__ != '__main__':
    print('This main programm !\nRun this module !')
    exit()

import json
from Deck import Deck
from Shoe import Shoe


# открыть файл config и взять из него параметр: количество колод
f = open("config.json", "r")
conf = json.loads(f.read())

# Создаём шуз: передаём функцию которая возвращает карты и количество колод участвующих в игре
shoe = Shoe(Deck.create_deck, conf['number_deck'])


print(shoe.get_card())
print(shoe.get_card())
print(shoe.get_card())
print(shoe.get_card())
print(shoe.num_cards)
