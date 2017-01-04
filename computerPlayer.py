from player import Player
from possibleMove import PossibleMove

class ComputerPlayer(Player):

    def getMove(self, board, playsLeft):
        for threshold in range(40,100,5):
            move = PossibleMove(board, self.hand, threshold=threshold, playsLeft=playsLeft)
            if move.bestMove: return move.bestMove

    def callPiles(self, board):
        calledSomething = False
        for pile in board.piles:
            for card in self.hand.cards:
                if pile.canJumpBack(card):
                    pile.called = True
                    calledSomething = True
        return calledSomething