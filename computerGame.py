from game import Game

class ComputerGame(Game):
    
    def show(self, player):
        print self.board
        print player.hand

    def play(self):
        self.setup()
        while True:
            self.show(self.turn.player)
            move = self.turn.player.getMove(self.board)
            for play in move.plays:
                self.playCard(self.turn.player,play[0],pileIndex=play[1])
            self.endTurn()
