from game import Game

class CommandLineGame(Game):
    
    def show(self, player):
        print self.board
        print player.hand

    def getCard(self, player):
        try:
            cardNumber = int(raw_input('Which card? '))
            card = next((c for c in player.hand.cards if c.number == cardNumber), None)
        except ValueError:
            card = None

        if card == None: return None, None
        try:
            pileNumber = int(raw_input('Which pile? '))
            pile = next((p for p in self.board.piles if p.currentNumber() == pileNumber), None)
        except ValueError:
            pile = None

        return card, pile

    def getCommand(self):
        command = raw_input('Play or Draw?')
        if(command == 'P' or command == 'p' or command == 'Play'):
            return 'Play'
        elif(command == 'D' or command == 'd' or command == 'Draw'):
            return 'Draw'
        else:
            return 'Invalid'

    def play(self):
        self.setup()
        for player in self.players:
            while True:
                self.show(player)
                command = self.getCommand()
                if command == 'Invalid': continue
                if command == 'Draw':
                    break
                if command == 'Play':
                    card, pile = self.getCard(player)
                    if card == None or pile == None:
                        continue
                    self.playCard(player, card, pile)