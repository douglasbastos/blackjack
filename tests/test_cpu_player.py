from unittest import TestCase

from blackjack.pack import Card
from blackjack.players.cpu_player import CpuPlayer


class CpuPlayerTest(TestCase):

    def test_opponent_with_the_game_finalized_and_cpu_losing(self):
        cpu_player = CpuPlayer()
        cpu_player.cards = [Card(rank='10', suit='♠'),
                            Card(rank='9', suit='♠')]
        cpu_player.opponent_cards = [Card(rank='10', suit='♠'),
                                     Card(rank='8', suit='♠'),
                                     Card(rank='2', suit='♠')]

        self.assertTrue(cpu_player.will_continue(), 'Continue jogando')

    def test_opponent_with_the_game_finalized_and_cpu_winning(self):
        cpu_player = CpuPlayer()
        cpu_player.cards = [Card(rank='10', suit='♠'),
                            Card(rank='8', suit='♠'),
                            Card(rank='2', suit='♠')]
        cpu_player.opponent_cards = [Card(rank='10', suit='♠'),
                                     Card(rank='9', suit='♠')]

        self.assertFalse(cpu_player.will_continue(), 'Terminar jogada')


    def test_opponent_bust_card(self):
        cpu_player = CpuPlayer()
        cpu_player.cards = [Card(rank='3', suit='♠'),
                            Card(rank='4', suit='♠')]
        cpu_player.opponent_cards = [Card(rank='10', suit='♠'),
                                     Card(rank='K', suit='♠'),
                                     Card(rank='2', suit='♠')]

        self.assertFalse(cpu_player.will_continue(), 'Terminar jogada')

    def test_opponent_without_having_played_and_score_bigger_or_equal_then_18(self):
        cpu_player = CpuPlayer()
        cpu_player.cards = [Card(rank='10', suit='♥'),
                            Card(rank='8', suit='♥')]
        cpu_player.opponent_cards = [Card(rank='10', suit='♠'),
                                     Card(rank='8', suit='♠')]

        self.assertFalse(cpu_player.will_continue(), 'Terminar jogada')

    def test_opponent_without_having_played_and_score_less_then_17(self):
        cpu_player = CpuPlayer()
        cpu_player.cards = [Card(rank='10', suit='♥'),
                            Card(rank='7', suit='♥')]
        cpu_player.opponent_cards = [Card(rank='10', suit='♠'),
                                     Card(rank='7', suit='♠')]

        self.assertTrue(cpu_player.will_continue(), 'Continar jogadando')
