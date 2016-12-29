from card import Card

class Hand(object):

    def __init__(self, size):
        self.size = size
        self.cards = []

    def __str__(self):
        return '--------- HAND ----------\n' +  ' | '.join(map(str,[card.number for card in self.cards]))

    def sort(self):
           self.cards.sort(key=lambda card: card.number)

    def canAdd(self):
           return len(self.cards) != self.size

    def add(self, card):
        if self.canAdd():
            self.cards.append(card)
            self.sort()
            return True
        else:
            return False