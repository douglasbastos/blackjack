import random
from collections import namedtuple, deque

Card = namedtuple('Card', ['rank', 'suit'])


class Pack:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ('♠', '♥', '♦', '♣')

    def __init__(self):
        self._cards = [
            Card(rank, suit)
            for suit in self.suits
            for rank in self.ranks
        ]
        self.shuffle()
        self._cards = deque(self)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, position, card):
        self._cards[position] = card

    def shuffle(self):
        return random.shuffle(self)

    def next(self):
        return self._cards.popleft()
