from computerGame import ComputerGame
from computerPlayer import ComputerPlayer

print 'The Game'
players = [ComputerPlayer(6,x) for x in range(4)]
game = ComputerGame(4,players)
game.play()