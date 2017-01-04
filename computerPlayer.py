from player import Player
from possibleMove import PossibleMove

class ComputerPlayer(Player):

    def getMove(self, board):
        for threshold in range(40,100,5):
            move = PossibleMove(board, self.hand, threshold=threshold)
            if move.bestMove: return move.bestMove