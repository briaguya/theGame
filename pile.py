from card import Card

class Pile(object):

    def __init__(self, direction):
        self.direction = direction
        self.cards = []
        self.cards.append(Card(1) if self.direction == "Increasing" else Card(100))