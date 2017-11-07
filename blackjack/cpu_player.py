class CpuPlayer():

    def __init__(self, cpu_score, player_score):
        self.cpu_score = cpu_score
        self.player_score = player_score
        self.will_continue()

    def will_continue(self):
        if self.player_score:
            if self.player_score > self.cpu_score:
                return True
            return False
        else:
            max_limit_continue = 17
            if self.cpu_score > max_limit_continue:
                return False
            return True
