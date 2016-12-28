#import player
from board import Board

class Game(object):

    def __init__(self):
        self.board = Board()

    def play(self):
    	self.board.show()