from board import Board
import copy

class PossibleMove(object):
    def __init__(self, board, hand, plays = [], threshold = 20, playsLeft = 2):
        self.board = board
        self.hand = hand
        self.plays = plays
        self.threshold = threshold
        self.playsLeft = playsLeft
        if self.plays:
            self.score = self.board.scoreWithPlays(plays)
        else: self.score = self.board.currentScore()
        self.getNextMoves()
        self.bestMove = self.getBest(self)

    def listRightIndex(self, alist, value):
        return len(alist) - alist[-1::-1].index(value) -1

    def getNextMoves(self):
        self.nextMoves = []
        if (self.score - self.board.currentScore()) > self.threshold:
            return
        
        for card in self.hand.cards:
            # If we already played this card we can't play it again
            if card.number in [play[0].number for play in self.plays]:
                continue
            for pileIndex in range(len(self.board.piles)):
                # If we already played on this pile we need to check that play instead
                if pileIndex in [play[1] for play in self.plays]:
                    playIndex = self.listRightIndex([play[1] for play in self.plays], pileIndex)
                    pileCard = self.plays[playIndex][0]
                    if not self.board.piles[pileIndex].canPlay(card,pileCard.number):
                        continue
                else:
                    if not self.board.piles[pileIndex].canPlay(card):
                        continue

                self.nextMoves.append(PossibleMove(self.board, self.hand, self.playCard(card, pileIndex)))

    def playCard(self, card, pileIndex):
        plays = copy.deepcopy(self.plays)
        plays.append([card,pileIndex])
        return plays

    def getBest(self, thisMove):
        bestMove = None
        bestScore = 1000
        # We need to play at least 2 cards
        if len(thisMove.plays) >= self.playsLeft:
            bestMove = thisMove
            bestScore = bestMove.score
        if thisMove.nextMoves:
            for move in thisMove.nextMoves:
                nextMove = self.getBest(move)
                nextScore = 1000
                if nextMove:
                    nextScore = nextMove.score
                if nextScore < bestScore:
                    bestMove = nextMove
                    bestScore = nextScore
        return bestMove
