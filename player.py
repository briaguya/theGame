from hand import Hand

class Player(object):

    def __init__(self, handSize, name):
        self.name = name
        self.hand = Hand(handSize)