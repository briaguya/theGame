from game import Game

class CommandLineGame(Game):
    
    def show(self, player):
        print self.board
        print player.hand

    def getCommand(self, player):
        cardNumber = input('Which card? ')
        card = next(c for c in player.hand.cards if c.number == cardNumber)
        pileNumber = input('Which pile? ')
        pile = next(p for p in self.board.piles if p.currentNumber() == pileNumber)
        return card, pile

    def play(self):
        self.setup()
        for player in self.players:
            self.show(player)
            card, pile = self.getCommand(player)
            self.playCard(player, card, pile)
            self.show(player)
