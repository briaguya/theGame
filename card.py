class Card(object):

    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        return self.number == other.number