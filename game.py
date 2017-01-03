from player import Player
from board import Board
from deck import Deck
from turn import Turn

class Game(object):

    def __init__(self, numOfPlayers):
        self.board = Board()
        self.deck = Deck()
        self.numOfPlayers = numOfPlayers
        self.players = [Player(8 if numOfPlayers == 1 else 7 if numOfPlayers == 2 else 6) for p in range(numOfPlayers)]
        self.turn = None
        self.turnsPlayed = 0

    def setup(self):
        self.deck.shuffle()
        self.deck.deal([player.hand for player in self.players])
        self.startTurn(self.players[0])

    def playCard(self, player, card, pile):
        cardFromHand = player.hand.takeCardFromHand(card)
        pile.putCardOnPile(cardFromHand)
        self.turn.cardsPlayed += 1

    def startTurn(self, player):
        self.turn = Turn(player)

    def endTurn(self):
        if self.turn.canEnd():
            self.turnsPlayed += 1
            self.startTurn(self.players[self.turnsPlayed%self.numOfPlayers])
