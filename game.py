#import board
#import player
from deck import Deck

class Game(object):

    def __init__(self):
        self.deck = Deck();

    def play(self):
    	for card in self.deck.cards:
    		print card.number