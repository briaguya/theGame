from player import Player
from board import Board

class Game(object):

    def __init__(self, numOfPlayers):
        self.board = Board()
        self.players = [Player(8 if numOfPlayers == 1 else 7 if numOfPlayers == 2 else 6) for p in range(numOfPlayers)]

    def play(self):
    	self.board.show()
    	for player in self.players:
    		print player.hand.size