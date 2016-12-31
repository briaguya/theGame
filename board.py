from pile import Pile
from deck import Deck

class Board(object):

    def __init__(self):
        self.deck = Deck()
        self.piles = [Pile(d) for d in ["Increasing","Increasing","Decreasing","Decreasing"]]

    def __str__(self):
        output = ''
        for i in range(max([len(p.cards) for p in self.piles])):
            # print len(pile.cards)
            output += '| {:>3} | {:>3} | {:>3} | {:>3} |\n'.format(*[pile.cards[i].number if len(pile.cards) > i else ' ' for pile in self.piles])
        return output[:-1]