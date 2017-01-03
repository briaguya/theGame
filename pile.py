from card import Card

class Pile(object):

    def __init__(self, direction):
        self.direction = direction
        self.cards = []
        self.cards.append(Card(1) if self.direction == "Increasing" else Card(100))

    def currentNumber(self):
        return self.cards[-1].number

    def canPlay(self, card):
        if self.direction == "Increasing":
            return self.currentNumber() < card.number or card.number == (self.currentNumber() - 10)
        elif self.direction == "Decreasing":
            return self.currentNumber() > card.number or card.number == (self.currentNumber() + 10)
        else: return False

    def putCardOnPile(self, card):
        if self.canPlay(card):
            self.cards.append(card)