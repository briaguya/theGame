from pile import Pile
from deck import Deck

class Board(object):

    def __init__(self):
    	self.deck = Deck()
        self.piles = [Pile(d) for d in ["Increasing","Increasing","Decreasing","Decreasing"]]

    def show(self):
    	print '{} {}'.format('one', 'two')

