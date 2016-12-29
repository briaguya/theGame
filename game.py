from player import Player
from board import Board
from deck import Deck

class Game(object):

    def __init__(self, numOfPlayers):
        self.board = Board()
        self.deck = Deck()
        self.players = [Player(8 if numOfPlayers == 1 else 7 if numOfPlayers == 2 else 6) for p in range(numOfPlayers)]

    def show(self, player):
        print self.board
        print player.hand

    def setup(self):
        self.deck.shuffle()
        self.deck.deal([player.hand for player in self.players])        

    def play(self):
        self.setup()
        for player in self.players: self.show(player)