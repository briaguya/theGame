from computerGame import ComputerGame
from computerPlayer import ComputerPlayer

print 'The Game'
players = [ComputerPlayer(8)]
game = ComputerGame(1,players)
game.play()