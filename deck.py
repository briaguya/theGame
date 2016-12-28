from card import Card

class Deck(object):

    def __init__(self):
        self.cards = [Card(n) for n in range(1,100)]


