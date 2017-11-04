from unittest import TestCase, skip

from blackjack.pack import Card
from blackjack.twenty_one import TwentyOne


class TwentyOneTest(TestCase):

    def test_score_21_with_only_numbers(self):
        cards = [Card(rank='10', suit='♠'),
                 Card(rank='5', suit='♠'),
                 Card(rank='6', suit='♠')]
        twenty_one = TwentyOne(cards)

        self.assertEqual(21, twenty_one.score())

    def test_score_21_with_cards_without_numbers(self):
        cards = [Card(rank='J', suit='♠'),
                 Card(rank='5', suit='♠'),
                 Card(rank='6', suit='♠')]
        twenty_one = TwentyOne(cards)

        self.assertEqual(21, twenty_one.score())

    def test_score_21_with_as_worth_1(self):
        cards = [Card(rank='A', suit='♠'),
                 Card(rank='10', suit='♠'),
                 Card(rank='8', suit='♠'),
                 Card(rank='2', suit='♠')]
        twenty_one = TwentyOne(cards)

        self.assertEqual(21, twenty_one.score())

    @skip('Essa regra ainda não foi implementada')
    def test_score_21_with_as_worth_11(self):
        cards = [Card(rank='A', suit='♠'),
                 Card(rank='8', suit='♠'),
                 Card(rank='2', suit='♠')]
        twenty_one = TwentyOne(cards)

        self.assertEqual(21, twenty_one.score())
