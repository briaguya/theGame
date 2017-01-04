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

    def test_play_2_on_called_12(self):
        player = ComputerPlayer(2,1)
        player.hand.cards = [Card(n) for n in [2,12]]

        # Get the next moves, it should be play 12 then 2
        move = player.getMove(self.board,2)

        # The last card in the move should be 2
        self.assertEqual(move.plays[-1][0], Card(2))

        # Now we play the 12
        self.board.piles[move.plays[0][1]].putCardOnPile(move.plays[0][0])
        player.hand.takeCardFromHand(move.plays[0][0])

        self.assertEqual(self.board.piles[move.plays[0][1]].currentNumber(),12)

        # And since we have the 2, we call the 12
        self.board.piles[move.plays[0][1]].called = True

        # Since it's been called, we need to get the next move
        move = player.getMove(self.board,1)

        # It should play the 2
        self.assertEqual(move.plays[0][0],Card(2))

    def test_play_45_35_on_8(self):
        # todo fix this
        # Player - 2
        # | | | | |
        # | 1 | 1 | 100 | 100 |
        # | 8 | 7 | 89 | 92 |
        # --------- HAND - ---------
        # 3 | 6 | 35 | 45 | 52 | 93
        # Out of moves, game over.
        # 70 cards left in deck.
        self.assertTrue(False)