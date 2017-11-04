from unittest import TestCase

from blackjack.pack import Pack, Card


class PackTest(TestCase):

    def test_total_cards(self):
        pack = Pack()
        self.assertEqual(52, len(pack))

    def test_get_card_of_pack(self):
        pack = Pack()
        card = pack.next()
        self.assertEqual(51, len(pack))
        self.assertIsInstance(card, Card)