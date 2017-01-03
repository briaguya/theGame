from game import Game

class ComputerGame(Game):
    
    def show(self, player):
        print self.board
        print player.hand

    def play(self):
        self.setup()
        while True:
            self.show(self.turn.player)
            self.turn.player.getMove(self.board)