from time import sleep


class CpuPlayer():
    score = 0
    opponent_score = 0

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
