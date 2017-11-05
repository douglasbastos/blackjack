from unittest import TestCase, mock
from unittest.mock import call

from blackjack.pack import Card
from blackjack.play import Run


class PlayTest(TestCase):

    @mock.patch.object(Run, 'bust_card', return_value=False)
    @mock.patch('blackjack.play.input', side_effect=['c', 's'])
    def test_command(self, input, bust_card):
        Run()
        self.assertEqual(2, bust_card.call_count)

    @mock.patch.object(Run, 'main')
    def test_bust_card_should_returns_true(self, main):
        cards = [Card(rank='10', suit='♠'),
                 Card(rank='5', suit='♠'),
                 Card(rank='7', suit='♠')]
        run = Run()
        self.assertTrue(run.bust_card(cards))

    @mock.patch.object(Run, 'main')
    def test_bust_card_should_returns_false(self, main):
        cards = [Card(rank='10', suit='♠'),
                 Card(rank='4', suit='♠'),
                 Card(rank='7', suit='♠')]
        run = Run()
        self.assertFalse(run.bust_card(cards))

    @mock.patch.object(Run, 'bust_card', return_value=True)
    @mock.patch('blackjack.play.print')
    def test_stop_running_when_bust_card_is_true(self, print_, bust_card):
        Run()
        self.assertEqual(print_.call_args_list[0],
                         call('Você passou do limite de 21 pontos'))
