from player import Player
from possibleMove import PossibleMove

class ComputerPlayer(Player):

    def getMove(self, board):
        self.move = PossibleMove(board, self.hand)
        self.move = self.move.bestMove
        print self.move