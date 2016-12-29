from card import Card
from hand import Hand
from random import shuffle

class Deck(object):

    def __init__(self):
        self.cards = [Card(n) for n in range(1,100)]

    def draw(self):
        return self.cards.pop()

    def deal(self, hands):
        for hand in hands:
            while hand.canAdd():
                hand.add(self.draw())

    def shuffle(self):
        shuffle(self.cards)        