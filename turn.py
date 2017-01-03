class Turn(object):

    def __init__(self, player):
        self.player = player
        self.cardsPlayed = 0

    def canEnd(self):
        return self.cardsPlayed >= 2