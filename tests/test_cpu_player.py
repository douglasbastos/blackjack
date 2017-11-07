from unittest import TestCase

from blackjack.cpu_player import CpuPlayer


class CpuPlayerTest(TestCase):

    def test_opponent_with_the_game_finalized_and_cpu_losing(self):
        cpu_player = CpuPlayer(player_score=20, cpu_score=19)
        self.assertTrue(cpu_player.will_continue(), 'Continue jogada')

    def test_opponent_with_the_game_finalized_and_cpu_winning(self):
        cpu_player = CpuPlayer(player_score=19, cpu_score=20)
        self.assertFalse(cpu_player.will_continue(), 'Terminar jogada')

    def test_opponent_without_having_played_stopped_when_18_points(self):
        cpu_player = CpuPlayer(player_score=0, cpu_score=18)
        self.assertFalse(cpu_player.will_continue(), 'Terminar jogada')

    def test_opponent_without_having_played_continue_when_17_points(self):
        cpu_player = CpuPlayer(player_score=0, cpu_score=17)
        self.assertTrue(cpu_player.will_continue(), 'Continue jogada')

