from time import sleep

from blackjack import Blackjack


class CpuPlayer():
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

    def will_continue(self):
        sleep(1)
        if self.opponent_score:
            if self.opponent_score > self.score:
                return True
            return False
        else:
            max_limit_continue = 17
            if self.score > max_limit_continue:
                return False
            return True
