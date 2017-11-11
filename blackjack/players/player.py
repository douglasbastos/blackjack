from blackjack import Blackjack


class Player:
    cards = []
    opponent_cards = []

    def __init__(self):
        self.blackjack = Blackjack()

    @property
    def score(self):
        return self.blackjack.score(self.cards)

    @property
    def opponent_score(self):
        return self.blackjack.score(self.opponent_cards)
