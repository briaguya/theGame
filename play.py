from commandLineGame import CommandLineGame

print 'The Game'
players = input('How many players? ')
game = CommandLineGame(players)
game.play()