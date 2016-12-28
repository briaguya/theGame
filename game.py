#import board
#import player
from deck import Deck

class Game(object):

    def __init__(self):
        self.deck = Deck();
        print self.deck