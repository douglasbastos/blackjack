from time import sleep
from blackjack.players.player import Player


class CpuPlayer(Player):
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
