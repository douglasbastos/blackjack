from unittest import TestCase, mock
from unittest.mock import call

from blackjack.play import Run


class PlayTest(TestCase):

    @mock.patch.object(Run, 'bust_card', return_value=False)
    @mock.patch('blackjack.play.input', side_effect=['c', 's'])
    def test_command(self, input, bust_card):
        Run()
        self.assertEqual(2, bust_card.call_count)

    def test_bust_card_should_returns_true(self):
        pass

    def test_bust_card_should_returns_false(self):
        pass

    @mock.patch.object(Run, 'bust_card', return_value=True)
    @mock.patch('blackjack.play.print')
    def test_stop_running_when_bust_card_is_true(self, print_, bust_card):
        Run()
        self.assertEqual(print_.call_args_list[0],
                         call('Você passou do limite de 21 pontos'))
