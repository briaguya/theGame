from board import Board
from card import Card
import copy

class PossibleMove(object):
    def __init__(self, board, hand, plays = [], threshold = 200, playsLeft = 2):
        self.board = board
        self.hand = hand
        self.plays = plays
        self.threshold = threshold
        self.playsLeft = playsLeft
        if self.plays:
            self.score = self.board.scoreWithPlays(plays)
        else:
            self.score = self.board.currentScore()
        self.spots = self.getPlayableSpots(plays)
        self.getNextMoves()
        self.bestMove = self.getBest(self)

    def listRightIndex(self, alist, value):
        return len(alist) - alist[-1::-1].index(value) -1

    def getNextMoves(self):
        self.nextMoves = []
        if (self.getPlayableSpots([]) - self.spots) > self.threshold:
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

                self.nextMoves.append(PossibleMove(self.board, self.hand, self.playCard(card, pileIndex), self.threshold, self.playsLeft))

    def playCard(self, card, pileIndex):
        plays = copy.deepcopy(self.plays)
        plays.append([card,pileIndex])
        return plays

    def getBest(self, thisMove):
        bestMove = None
        bestSpots = 0
        # We need to play at least 2 cards
        if len(thisMove.plays) >= self.playsLeft:
            bestMove = thisMove
            bestSpots = bestMove.spots
        if thisMove.nextMoves:
            for move in thisMove.nextMoves:
                nextMove = self.getBest(move)
                nextSpots = 0
                if nextMove:
                    nextSpots = nextMove.spots
                if nextSpots > bestSpots:
                    bestMove = nextMove
                    bestSpots = nextSpots
        return bestMove

    def getPlayableSpots(self, plays):
        # Get the numbers of all the played cards
        playedNumbers = [card.number for pile in self.board.piles for card in pile.cards[1:]]
        # Add the cards from plays
        playedNumbers.extend([play[0].number for play in plays])

        # All the other numbers are the ones that need to be played still
        numbersLeft = [number for number in range(2,100) if number not in playedNumbers]
        # Then we need to see how many are playable
        return sum([self.board.numberOfPlacesCardCanBePlayed(Card(number),plays) for number in numbersLeft])