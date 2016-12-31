from card import Card

class Pile(object):

    def __init__(self, direction):
        self.direction = direction
        self.cards = []
        self.cards.append(Card(1) if self.direction == "Increasing" else Card(100))

    def currentNumber(self):
        return self.cards[0].number

    def putCardOnPile(self, card):
        # TODO validation logic
        self.cards.append(card)