#import player
from board import Board

class Game(object):

    def __init__(self):
        self.board = Board()

    def play(self):
    	for card in self.board.deck.cards:
    		print card.number