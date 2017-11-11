from unittest import TestCase, mock
from unittest.mock import call

from blackjack.players.player import Player


class PlayerTest(TestCase):

    @mock.patch('blackjack.players.player.input', return_value='c')
    def test_command_continue(self, input_):
        player = Player()
        self.assertTrue(player.will_continue())

    @mock.patch('blackjack.players.player.input', return_value='s')
    def test_command_stop(self, input_):
        player = Player()
        self.assertFalse(player.will_continue())

    @mock.patch('blackjack.players.player.print')
    @mock.patch('blackjack.players.player.input', side_effect=['haha', 's'])
    def test_command_invalid(self, input_, print_):
        player = Player()
        player.will_continue()
        self.assertEqual(print_.call_args_list[0],
                         call('Comando inválido'))
