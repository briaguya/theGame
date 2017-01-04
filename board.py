from pile import Pile
from deck import Deck

class Board(object):

    def __init__(self):
        self.deck = Deck()
        self.piles = [Pile(d, i) for d, i in [("Increasing",0),("Increasing",1),("Decreasing",2),("Decreasing",3)]]

    def __str__(self):
        output = ''
        output += '| {:>3} | {:>3} | {:>3} | {:>3} |\n'.format(*['x' if pile.called else ' ' for pile in self.piles])
        for i in range(max([len(p.cards) for p in self.piles])):
            output += '| {:>3} | {:>3} | {:>3} | {:>3} |\n'.format(*[pile.cards[i].number if len(pile.cards) > i else ' ' for pile in self.piles])
        return output[:-1]

    def currentScore(self):
        return sum([pile.currentScore() for pile in self.piles])

    def scoreWithPlays(self, plays):
        return sum([pile.scoreWithPlays(plays) for pile in self.piles])

    def numberOfPlacesCardCanBePlayed(self, card, plays):
        return len([pile for pile in self.piles if pile.canPlayOnPlays(card, plays)])