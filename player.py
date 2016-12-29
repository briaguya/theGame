from hand import Hand

class Player(object):

    def __init__(self, handSize):
        self.hand = Hand(handSize)