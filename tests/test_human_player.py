from unittest import TestCase, mock
from unittest.mock import call

from blackjack.players.human_player import HumanPlayer


class HumanPlayerTest(TestCase):

    @mock.patch('blackjack.players.human_player.input', return_value='c')
    def test_command_continue(self, input_):
        player = HumanPlayer()
        self.assertTrue(player.will_continue())

    @mock.patch('blackjack.players.human_player.input', return_value='s')
    def test_command_stop(self, input_):
        player = HumanPlayer()
        self.assertFalse(player.will_continue())

    @mock.patch('blackjack.players.human_player.print')
    @mock.patch('blackjack.players.human_player.input', side_effect=['haha', 's'])
    def test_command_invalid(self, input_, print_):
        player = HumanPlayer()
        player.will_continue()
        self.assertEqual(print_.call_args_list[0],
                         call('Opção inválida'))
