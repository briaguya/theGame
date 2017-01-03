from card import Card

class Pile(object):

    def __init__(self, direction, index):
        self.direction = direction
        self.index = index
        self.cards = []
        self.cards.append(Card(1) if self.direction == "Increasing" else Card(100))

    def scoreWithPlays(self, plays):
        cards = [play[0] for play in plays if play[1] == self.index]
        if not cards:
            return self.currentScore()

        return self.scoreWithCards(cards)

    def scoreWithCards(self, cards):
        # Make sure we can play all these cards on the pile
        for n in range(len(cards)):
            if n == 0:
                if not self.canPlay(cards[n]):
                    return None
            elif not self.canPlay(cards[n], cards[n-1].number):
                return None

        # We can play them all, get the score from the last one
        if self.direction == "Increasing":
            return cards[-1].number - self.cards[0].number
        elif self.direction == "Decreasing":
            return self.cards[0].number - cards[-1].number      

    def currentScore(self):
        if self.direction == "Increasing":
            return self.currentNumber() - self.cards[0].number
        elif self.direction == "Decreasing":
            return self.cards[0].number - self.currentNumber()

    def currentNumber(self):
        return self.cards[-1].number

    def canPlay(self, card, playingOnNumber = -1):
        if(playingOnNumber == -1):
            playingOnNumber = self.currentNumber()
        if self.direction == "Increasing":
            return playingOnNumber < card.number or card.number == (playingOnNumber - 10)
        elif self.direction == "Decreasing":
            return playingOnNumber > card.number or card.number == (playingOnNumber + 10)
        else: return False

    def putCardOnPile(self, card):
        if self.canPlay(card):
            self.cards.append(card)