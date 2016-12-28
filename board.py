from pile import Pile
from deck import Deck

class Board(object):

    def __init__(self):
    	self.deck = Deck()
        self.piles = [Pile(d) for d in ["Increasing","Increasing","Decreasing","Decreasing"]]

    def show(self):
    	for i in range(max([len(p.cards) for p in self.piles])):
    		print '| {:>3} | {:>3} | {:>3} | {:>3} |'.format(*[pile.cards[i].number for pile in self.piles])

