from game import Game

class CommandLineGame(Game):
    
    def show(self, player):
        print self.board
        print player.hand

    def play(self):
        self.setup()
        for player in self.players: self.show(player)