from board import Board
import copy

class PossibleMove(object):
    def __init__(self, board, hand, plays = [], threshold = 20):
        self.board = board
        self.hand = hand
        self.plays = plays
        self.threshold = threshold
        if self.plays:
            self.score = self.board.scoreWithPlays(plays)
        else: self.score = self.board.currentScore()
        self.getNextMoves()
        self.bestMove = self.getBest(self)

    def listRightIndex(self, alist, value):
        return len(alist) - alist[-1::-1].index(value) -1

    def getNextMoves(self):
        self.nextMoves = []
        print self.score - self.board.currentScore()
        if (self.score - self.board.currentScore()) > self.threshold:
            return
        
        for card in self.hand.cards:
            # If we already played this card we can't play it again
            if card.number in [play[0].number for play in self.plays]:
                continue
            for pile in self.board.piles:
                # If we already played on this pile we need to check that play instead
                if pile in [play[1] for play in self.plays]:
                    playIndex = self.listRightIndex([play[1] for play in self.plays], pile)
                    pileCard = self.plays[playIndex][0]
                    if not pile.canPlay(card,pileCard.number):
                        continue
                else:
                    if not pile.canPlay(card):
                        continue

                self.nextMoves.append(PossibleMove(self.board, self.hand, self.playCard(card, pile)))

    def playCard(self, card, pile):
        plays = copy.deepcopy(self.plays)
        plays.append([card,pile])
        return plays

    def getBest(self, thisMove):
        bestMove = thisMove
        if self.nextMoves:
            for move in self.nextMoves:
                nextMove = self.getBest(move)
                if nextMove.score < bestMove.score: bestMove = nextMove
        return bestMove
