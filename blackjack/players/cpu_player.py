from time import sleep
from blackjack.players.player import Player


class CpuPlayer(Player):

    def _opponent_played_already(self):
        if len(self.opponent_cards) > 2:
           return True
        return False

    def _opponent_ahead(self):
        if self.opponent_score > self.score:
            return True
        return False

    def _opponent_bust_card(self):
        if self.opponent_score > 21:
            return True
        return False

    def _is_max_limit_to_continue(self):
        max_limit_continue = 17
        if self.score > max_limit_continue:
            return False
        return True

    def will_continue(self):
        sleep(1)
        if self._opponent_played_already():
            if self._opponent_ahead() and not self._opponent_bust_card():
                return True
            return False
        else:
            return self._is_max_limit_to_continue()
