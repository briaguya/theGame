from unittest import TestCase
from computerPlayer import ComputerPlayer
from card import Card
from board import Board

class TestComputerPlayer(TestCase):
    def setUp(self):
        self.board = Board()

    def test_play_90_85_95(self):
        player = ComputerPlayer(3,1)
        player.hand.cards = [Card(n) for n in [90,85,95]]
        move = player.getMove(self.board,2)

        # It should play all 3 cards
        self.assertTrue(len(move.plays) == 3)

        # The last card in the move should be 95
        self.assertEqual(move.plays[-1][0],Card(95))

        # They should all play on the same pile
        self.assertTrue(all(play[1] == move.plays[-1][1] for play in move.plays))

    def test_play_2_10_12(self):
        player = ComputerPlayer(3,1)
        player.hand.cards = [Card(n) for n in [2,10,12]]
        move = player.getMove(self.board,2)

        # It should play all 3 cards
        self.assertTrue(len(move.plays) == 3)

        # The last card in the move should be 2
        self.assertEqual(move.plays[-1][0],Card(2))

        # They should all play on the same pile
        self.assertTrue(all(play[1] == move.plays[-1][1] for play in move.plays))
