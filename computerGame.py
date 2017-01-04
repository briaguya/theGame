from game import Game

class ComputerGame(Game):
    
    def show(self, player):
        print 'Player - {}'.format(player.name)
        print self.board
        print player.hand

    def play(self):
        self.setup()
        while True:
            self.show(self.turn.player)
            playsPerTurn = 2 if len(self.deck.cards) else 1
            move = self.turn.player.getMove(self.board, playsPerTurn - self.turn.cardsPlayed)
            if move:
                for play in move.plays:
                    self.playCard(self.turn.player,play[0],pileIndex=play[1])
                    calledSomething = False
                    for player in self.players:
                        calledSomething = calledSomething or player.callPiles(self.board)
                    if calledSomething: break
                self.endTurn()
            else:
                print 'Out of moves, game over.'
                print '{} cards left in deck.'.format(len(self.deck.cards))
                break